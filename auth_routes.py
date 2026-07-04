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
from i18n import _
from models import User, normalize_username

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
        raise ValidationError(_("flash.login_rate_limit"))


def _record_failed_login() -> None:
    _login_attempts[_client_key()].append(time.time())


def _validate_username(form, field):
    value = normalize_username(field.data)
    if not re.fullmatch(r"[a-z0-9_]+", value):
        raise ValidationError(_("val.username_format"))


def _validate_password_strength(form, field):
    password = field.data
    if not re.search(r"[A-Za-z]", password):
        raise ValidationError(_("val.password_letter"))
    if not re.search(r"\d", password):
        raise ValidationError(_("val.password_digit"))


class RegisterForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username.label.text = _("auth.username_label")
        self.email.label.text = _("auth.email_label")
        self.password.label.text = _("auth.password_label")
        self.password_confirm.label.text = _("auth.password_confirm_label")
        self.submit.label.text = _("auth.submit_register")

    username = StringField(
        validators=[
            DataRequired(message="val.username_required"),
            Length(
                min=Config.USERNAME_MIN_LENGTH,
                max=Config.USERNAME_MAX_LENGTH,
                message="val.username_length",
            ),
            _validate_username,
        ],
    )
    email = StringField(
        validators=[
            DataRequired(message="val.email_required"),
            Email(message="val.email_invalid"),
            Length(max=255),
        ],
    )
    password = PasswordField(
        validators=[
            DataRequired(message="val.password_required"),
            Length(min=Config.PASSWORD_MIN_LENGTH, message="val.password_min"),
            _validate_password_strength,
        ],
    )
    password_confirm = PasswordField(
        validators=[
            DataRequired(message="val.password_confirm_required"),
            EqualTo("password", message="val.password_mismatch"),
        ],
    )
    submit = SubmitField()


class LoginForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login.label.text = _("auth.login_field_label")
        self.password.label.text = _("auth.password_label")
        self.remember.label.text = _("auth.remember_label")
        self.submit.label.text = _("auth.submit_login")

    login = StringField(
        validators=[DataRequired(message="val.login_required")],
    )
    password = PasswordField(
        validators=[DataRequired(message="val.login_password_required")],
    )
    remember = BooleanField()
    submit = SubmitField()


def _localize_form_errors(form):
    for field in form:
        field.errors = [
            _(msg, min=Config.PASSWORD_MIN_LENGTH, max=Config.USERNAME_MAX_LENGTH)
            for msg in field.errors
        ]


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("profile.dashboard"))

    form = RegisterForm()
    if form.validate_on_submit():
        username = normalize_username(form.username.data)
        email = form.email.data.strip().lower()

        if User.query.filter_by(username=username).first():
            flash(_("flash.username_taken"), "error")
        elif User.query.filter_by(email=email).first():
            flash(_("flash.email_taken"), "error")
        else:
            user = User(username=username, email=email)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash(_("flash.welcome"), "success")
            return redirect(url_for("learn"))

    _localize_form_errors(form)
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

        login_value = form.login.data.strip().lower()
        user = User.query.filter(
            (User.email == login_value) | (User.username == login_value)
        ).first()

        if user is None or not user.check_password(form.password.data):
            _record_failed_login()
            flash(_("flash.bad_credentials"), "error")
        else:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if next_page and next_page.startswith("/"):
                return redirect(next_page)
            flash(_("flash.welcome_back", username=user.username), "success")
            return redirect(url_for("learn"))

    _localize_form_errors(form)
    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash(_("flash.logged_out"), "info")
    return redirect(url_for("landing"))
