"""Модели данных PyBlocks."""

from datetime import datetime, timezone

from flask_login import UserMixin
from sqlalchemy.orm import validates
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


def _utcnow():
    return datetime.now(timezone.utc)


def normalize_username(value: str) -> str:
    return value.strip().lower()


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=_utcnow, nullable=False)

    attempts = db.relationship(
        "TaskAttempt",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    progress = db.relationship(
        "TaskProgress",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    skill_branch_xp = db.relationship(
        "SkillBranchXp",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    skill_medals = db.relationship(
        "SkillMedalPoints",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )
    skill_xp_awards = db.relationship(
        "SkillXpAward",
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="dynamic",
    )

    @validates("username")
    def _set_username(self, key, value: str) -> str:
        return normalize_username(value)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password, method="scrypt")

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User {self.username}>"


class TaskProgress(db.Model):
    __tablename__ = "task_progress"
    __table_args__ = (
        db.UniqueConstraint("user_id", "topic_id", "task_id", name="uq_user_task"),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    topic_id = db.Column(db.String(32), nullable=False, index=True)
    task_id = db.Column(db.String(64), nullable=False, index=True)
    attempts_count = db.Column(db.Integer, default=0, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    solution_code = db.Column(db.Text, nullable=True)
    solution_xml = db.Column(db.Text, nullable=True)
    completed_at = db.Column(db.DateTime(timezone=True), nullable=True)
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=_utcnow,
        onupdate=_utcnow,
        nullable=False,
    )

    user = db.relationship("User", back_populates="progress")

    def record_attempt(self, success: bool, code: str, blocks_xml: str | None = None) -> None:
        self.attempts_count += 1
        if success and not self.completed:
            self.completed = True
            self.completed_at = _utcnow()
            self.solution_code = code.strip() if code else code
            if blocks_xml:
                self.solution_xml = blocks_xml
        elif success:
            self.solution_code = code.strip() if code else code
            if blocks_xml:
                self.solution_xml = blocks_xml


class TaskAttempt(db.Model):
    __tablename__ = "task_attempts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    topic_id = db.Column(db.String(32), nullable=False, index=True)
    task_id = db.Column(db.String(64), nullable=False, index=True)
    code = db.Column(db.Text, nullable=False)
    success = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=_utcnow, nullable=False)

    user = db.relationship("User", back_populates="attempts")


class SkillBranchXp(db.Model):
    """Накопленный XP пользователя в ветке навыка."""

    __tablename__ = "skill_branch_xp"
    __table_args__ = (
        db.UniqueConstraint("user_id", "branch_id", name="uq_user_skill_branch"),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    branch_id = db.Column(db.String(32), nullable=False, index=True)
    xp = db.Column(db.Integer, default=0, nullable=False)

    user = db.relationship("User", back_populates="skill_branch_xp")


class SkillMedalPoints(db.Model):
    """Специализированные очки (медали) пользователя."""

    __tablename__ = "skill_medal_points"
    __table_args__ = (
        db.UniqueConstraint("user_id", "medal_id", name="uq_user_skill_medal"),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    medal_id = db.Column(db.String(32), nullable=False, index=True)
    points = db.Column(db.Integer, default=0, nullable=False)

    user = db.relationship("User", back_populates="skill_medals")


class SkillXpAward(db.Model):
    """Журнал начисления XP за задачу (идемпотентность и лента активности)."""

    __tablename__ = "skill_xp_awards"
    __table_args__ = (
        db.UniqueConstraint("user_id", "topic_id", "task_id", name="uq_skill_xp_award"),
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    topic_id = db.Column(db.String(32), nullable=False, index=True)
    task_id = db.Column(db.String(64), nullable=False, index=True)
    xp_total = db.Column(db.Integer, nullable=False)
    primary_branch = db.Column(db.String(32), nullable=False)
    xp_breakdown = db.Column(db.Text, nullable=False)
    medals_breakdown = db.Column(db.Text, nullable=True)
    awarded_at = db.Column(db.DateTime(timezone=True), default=_utcnow, nullable=False)

    user = db.relationship("User", back_populates="skill_xp_awards")
