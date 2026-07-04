"""Расширения Flask (БД, авторизация, CSRF)."""

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = "auth.login"
login_manager.login_message = "Войдите в аккаунт, чтобы продолжить."
login_manager.login_message_category = "info"
