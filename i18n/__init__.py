"""Локализация PyBlocks (ru / en)."""

from __future__ import annotations

import re
from functools import lru_cache

from flask import g, request, session

SUPPORTED_LOCALES = ("ru", "en")
DEFAULT_LOCALE = "ru"
LOCALE_COOKIE = "lang"
LOCALE_COOKIE_MAX_AGE = 365 * 24 * 3600


def _normalize_locale(value: str | None) -> str:
    if not value:
        return DEFAULT_LOCALE
    code = value.strip().lower().replace("_", "-").split("-")[0]
    return code if code in SUPPORTED_LOCALES else DEFAULT_LOCALE


def get_locale() -> str:
    if hasattr(g, "locale"):
        return g.locale

    query_lang = request.args.get("lang")
    if query_lang:
        return _normalize_locale(query_lang)

    cookie_lang = request.cookies.get(LOCALE_COOKIE)
    if cookie_lang:
        return _normalize_locale(cookie_lang)

    session_lang = session.get("lang")
    if session_lang:
        return _normalize_locale(session_lang)

    accept = request.accept_languages.best_match(SUPPORTED_LOCALES)
    return _normalize_locale(accept)


def set_request_locale() -> None:
    g.locale = get_locale()


@lru_cache(maxsize=2)
def _load_messages(locale: str) -> dict[str, str]:
    if locale == "en":
        from i18n.messages.en import MESSAGES
    else:
        from i18n.messages.ru import MESSAGES
    return MESSAGES


def _(key: str, **kwargs) -> str:
    locale = get_locale()
    messages = _load_messages(locale)
    text = messages.get(key, key)
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text
    return text


def ngettext(singular: str, plural: str, count: int, **kwargs) -> str:
    locale = get_locale()
    if locale == "en":
        template = singular if count == 1 else plural
    else:
        n = abs(int(count))
        if n % 10 == 1 and n % 100 != 11:
            template = singular
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            template = plural
        else:
            from i18n.messages.ru import PLURAL_MANY

            template = PLURAL_MANY.get(singular, plural)
    return _(template, count=count, **kwargs)


@lru_cache(maxsize=2)
def get_js_messages(locale: str | None = None) -> dict:
    loc = locale or get_locale()
    if loc == "en":
        from i18n.messages.js_en import JS_MESSAGES
    else:
        from i18n.messages.js_ru import JS_MESSAGES
    return {
        "locale": JS_MESSAGES.get("locale", loc),
        "messages": {key: value for key, value in JS_MESSAGES.items() if key != "locale"},
    }


@lru_cache(maxsize=2)
def get_block_messages(locale: str | None = None) -> dict:
    loc = locale or get_locale()
    if loc == "en":
        from i18n.messages.blocks_en import BLOCK_MESSAGES
    else:
        from i18n.messages.blocks_ru import BLOCK_MESSAGES
    return BLOCK_MESSAGES


def normalize_locale(value: str | None) -> str:
    return _normalize_locale(value)


def get_blockly_msg_file(locale: str | None = None) -> str:
    loc = locale or get_locale()
    return "en.js" if loc == "en" else "ru.js"


def get_pyblocks_locale_file(locale: str | None = None) -> str:
    loc = locale or get_locale()
    return "pyblocks-locale-en.js" if loc == "en" else "pyblocks-locale.js"
