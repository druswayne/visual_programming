"""Регистрация, вход и выход."""

import re
import time
from collections import defaultdict

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from config import Config
from extensions import db
from models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

_login_attempts: dict[str, list[float]] = defaultdict(list)
_MAX_LOGIN_ATTEMPTS = 5
_LOGIN_WINDOW_SEC = 300


def _client_key() -> str:
    return request.remote_addr or "unknown"


def _check_rate_limit() -> None:
    key = _client_key()
    now = time.time()
    recent = [t for t in _login_attempts[key] if now - t < _LOGIN_WINDOW_SEC]
    _login_attempts[key] = recent
    if len(recent) >= _MAX_LOGIN_ATTEMPTS:
        raise ValidationError("Слишком много попыток входа. Подождите 5 минут.")


def _record_failed_login() -> None:
    _login_attempts[_client_key()].append(time.time())


def _validate_username(form, field):
    value = field.data.strip()
    if not re.fullmatch(r"[A-Za-z0-9_]+", value):
        raise ValidationError("Имя пользователя: только буквы, цифры и _")


def _validate_password_strength(form, field):
    password = field.data
    if not re.search(r"[A-Za-z]", password):
        raise ValidationError("Пароль должен содержать хотя бы одну букву")
    if not re.search(r"\d", password):
        raise ValidationError("Пароль должен содержать хотя бы одну цифру")


class RegisterForm(FlaskForm):
    username = StringField(
        "Имя пользователя",
        validators=[
            DataRequired(message="Укажите имя пользователя"),
            Length(
                min=Config.USERNAME_MIN_LENGTH,
                max=Config.USERNAME_MAX_LENGTH,
                message=f"От {Config.USERNAME_MIN_LENGTH} до {Config.USERNAME_MAX_LENGTH} символов",
            ),
            _validate_username,
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Укажите email"),
            Email(message="Некорректный email"),
            Length(max=255),
        ],
    )
    password = PasswordField(
        "Пароль",
        validators=[
            DataRequired(message="Укажите пароль"),
            Length(
                min=Config.PASSWORD_MIN_LENGTH,
                message=f"Минимум {Config.PASSWORD_MIN_LENGTH} символов",
            ),
            _validate_password_strength,
        ],
    )
    password_confirm = PasswordField(
        "Подтверждение пароля",
        validators=[
            DataRequired(message="Подтвердите пароль"),
            EqualTo("password", message="Пароли не совпадают"),
        ],
    )
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    login = StringField(
        "Email или имя пользователя",
        validators=[DataRequired(message="Введите email или имя пользователя")],
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired(message="Введите пароль")],
    )
    remember = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("profile.dashboard"))

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        email = form.email.data.strip().lower()

        if User.query.filter_by(username=username).first():
            flash("Это имя пользователя уже занято.", "error")
        elif User.query.filter_by(email=email).first():
            flash("Этот email уже зарегистрирован.", "error")
        else:
            user = User(username=username, email=email)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Добро пожаловать в PyBlocks!", "success")
            return redirect(url_for("learn"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("profile.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            _check_rate_limit()
        except ValidationError as exc:
            flash(str(exc), "error")
            return render_template("auth/login.html", form=form)

        login_value = form.login.data.strip()
        user = User.query.filter(
            (User.email == login_value.lower()) | (User.username == login_value)
        ).first()

        if user is None or not user.check_password(form.password.data):
            _record_failed_login()
            flash("Неверный email/имя пользователя или пароль.", "error")
        else:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if next_page and next_page.startswith("/"):
                return redirect(next_page)
            flash(f"С возвращением, {user.username}!", "success")
            return redirect(url_for("learn"))

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта.", "info")
    return redirect(url_for("landing"))
