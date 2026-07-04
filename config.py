"""Конфигурация приложения PyBlocks."""

import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "pyblocks-dev-secret-change-in-production")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "pyblocks.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = os.environ.get("FLASK_ENV") == "production"
    PERMANENT_SESSION_LIFETIME = timedelta(days=14)

    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = os.environ.get("FLASK_ENV") == "production"
    REMEMBER_COOKIE_DURATION = timedelta(days=30)

    PASSWORD_MIN_LENGTH = 8
    USERNAME_MIN_LENGTH = 3
    USERNAME_MAX_LENGTH = 32

    # Лимиты выполнения кода
    MAX_CONCURRENT_EXECUTIONS = int(os.environ.get("MAX_CONCURRENT_EXECUTIONS", "8"))
    EXECUTION_QUEUE_TIMEOUT = float(os.environ.get("EXECUTION_QUEUE_TIMEOUT", "10"))
    EXECUTION_RATE_LIMIT = int(os.environ.get("EXECUTION_RATE_LIMIT", "30"))
    EXECUTION_RATE_WINDOW = int(os.environ.get("EXECUTION_RATE_WINDOW", "60"))
