"""Сервис сохранений программ в режиме песочницы."""

from datetime import datetime, timezone

from extensions import db
from models import SandboxSave

MAX_SAVES_PER_USER = 20
TITLE_MAX_LEN = 80
BLOCKS_XML_MAX_LEN = 500_000
CODE_MAX_LEN = 200_000


def _utcnow():
    return datetime.now(timezone.utc)


def _normalize_title(title: str | None) -> str | None:
    if title is None:
        return None
    cleaned = " ".join(str(title).strip().split())
    if not cleaned:
        return None
    return cleaned[:TITLE_MAX_LEN]


def list_user_saves(user) -> list[SandboxSave]:
    return (
        SandboxSave.query.filter_by(user_id=user.id)
        .order_by(SandboxSave.updated_at.desc(), SandboxSave.id.desc())
        .all()
    )


def get_user_save(user, save_id: int) -> SandboxSave | None:
    return SandboxSave.query.filter_by(user_id=user.id, id=save_id).first()


def create_user_save(user, title: str, blocks_xml: str, code: str | None = None):
    normalized_title = _normalize_title(title)
    if not normalized_title:
        return None, ["title_required"]

    xml = blocks_xml.strip() if isinstance(blocks_xml, str) else ""
    if not xml:
        return None, ["blocks_required"]
    if len(xml) > BLOCKS_XML_MAX_LEN:
        return None, ["blocks_too_large"]

    code_value = None
    if isinstance(code, str):
        code_value = code.strip() or None
        if code_value and len(code_value) > CODE_MAX_LEN:
            return None, ["code_too_large"]

    count = SandboxSave.query.filter_by(user_id=user.id).count()
    if count >= MAX_SAVES_PER_USER:
        return None, ["limit_reached"]

    save = SandboxSave(
        user_id=user.id,
        title=normalized_title,
        blocks_xml=xml,
        code=code_value,
    )
    db.session.add(save)
    db.session.commit()
    return save, []


def update_user_save(
    user,
    save_id: int,
    *,
    title: str | None = None,
    blocks_xml: str | None = None,
    code: str | None = None,
):
    save = get_user_save(user, save_id)
    if not save:
        return None, ["not_found"]

    if title is not None:
        normalized_title = _normalize_title(title)
        if not normalized_title:
            return None, ["title_required"]
        save.title = normalized_title

    if blocks_xml is not None:
        xml = blocks_xml.strip() if isinstance(blocks_xml, str) else ""
        if not xml:
            return None, ["blocks_required"]
        if len(xml) > BLOCKS_XML_MAX_LEN:
            return None, ["blocks_too_large"]
        save.blocks_xml = xml

    if code is not None:
        code_value = code.strip() if isinstance(code, str) else ""
        code_value = code_value or None
        if code_value and len(code_value) > CODE_MAX_LEN:
            return None, ["code_too_large"]
        save.code = code_value

    save.updated_at = _utcnow()
    db.session.commit()
    return save, []


def delete_user_save(user, save_id: int) -> bool:
    save = get_user_save(user, save_id)
    if not save:
        return False
    db.session.delete(save)
    db.session.commit()
    return True
