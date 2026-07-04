"""Ограничение параллельных запусков Python (subprocess)."""

import threading
from contextlib import contextmanager

from i18n import _

_pool: threading.BoundedSemaphore | None = None
_queue_timeout = 10.0


class ExecutionPoolBusy(Exception):
    """Не удалось получить слот для выполнения за отведённое время."""


def init_execution_pool(max_concurrent: int, queue_timeout: float) -> None:
    global _pool, _queue_timeout
    _pool = threading.BoundedSemaphore(max_concurrent)
    _queue_timeout = queue_timeout


@contextmanager
def execution_slot():
    if _pool is None:
        yield
        return

    acquired = _pool.acquire(blocking=True, timeout=_queue_timeout)
    if not acquired:
        raise ExecutionPoolBusy(_("runner.pool_busy"))
    try:
        yield
    finally:
        _pool.release()
