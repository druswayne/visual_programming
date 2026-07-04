"""Rate limiting для API запуска и проверки кода."""

import threading
import time
from collections import defaultdict
from functools import wraps

from flask import jsonify, request
from flask_login import current_user


class RateLimitExceeded(Exception):
    def __init__(self, retry_after: int):
        self.retry_after = retry_after
        super().__init__(
            f"Слишком много запросов. Подождите {retry_after} сек. и попробуйте снова."
        )


class ExecutionRateLimiter:
    def __init__(self, limit: int, window_sec: int):
        self.limit = limit
        self.window_sec = window_sec
        self._hits: dict[str, list[float]] = defaultdict(list)
        self._lock = threading.Lock()

    def _client_key(self) -> str:
        if current_user.is_authenticated:
            return f"user:{current_user.id}"
        return f"ip:{request.remote_addr or 'unknown'}"

    def check(self) -> None:
        key = self._client_key()
        now = time.time()
        with self._lock:
            recent = [t for t in self._hits[key] if now - t < self.window_sec]
            if len(recent) >= self.limit:
                oldest = min(recent)
                retry_after = max(1, int(self.window_sec - (now - oldest)) + 1)
                raise RateLimitExceeded(retry_after)
            recent.append(now)
            self._hits[key] = recent


_limiter: ExecutionRateLimiter | None = None


def init_rate_limiter(limit: int, window_sec: int) -> None:
    global _limiter
    _limiter = ExecutionRateLimiter(limit, window_sec)


def rate_limit_execution():
    """Декоратор: лимит запросов к /api/run, /api/debug, /api/check."""
    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if _limiter is not None:
                try:
                    _limiter.check()
                except RateLimitExceeded as exc:
                    response = jsonify(
                        {
                            "success": False,
                            "error": str(exc),
                            "retry_after": exc.retry_after,
                        }
                    )
                    response.headers["Retry-After"] = str(exc.retry_after)
                    return response, 429
            return view(*args, **kwargs)

        return wrapped

    return decorator
