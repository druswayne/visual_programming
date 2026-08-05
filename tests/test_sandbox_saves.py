"""Тесты API сохранений песочницы."""

from app import create_app
from extensions import db
from models import SandboxSave, User


def _make_user(suffix: str = "sbx") -> User:
    username = f"__sandbox_{suffix}__"
    email = f"sandbox_{suffix}@test.local"
    u = User.query.filter_by(username=username).first()
    if not u:
        u = User(username=username, email=email)
        u.set_password("test-password")
        db.session.add(u)
        db.session.commit()
    SandboxSave.query.filter_by(user_id=u.id).delete()
    db.session.commit()
    return u


def test_sandbox_saves_crud():
    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        db.create_all()
        user = _make_user("crud")

        client = app.test_client()
        with client.session_transaction() as sess:
            sess["_user_id"] = str(user.id)
            sess["_fresh"] = True

        sample_xml = '<xml xmlns="https://developers.google.com/blockly/xml"><block type="text_print"/></xml>'

        create_resp = client.post(
            "/api/sandbox/saves",
            json={"title": "  Hello world  ", "blocks_xml": sample_xml, "code": 'print("hi")'},
        )
        assert create_resp.status_code == 201, create_resp.get_data(as_text=True)
        created = create_resp.get_json()
        assert created["success"] is True
        assert created["save"]["title"] == "Hello world"
        save_id = created["save"]["id"]

        list_resp = client.get("/api/sandbox/saves")
        assert list_resp.status_code == 200
        listed = list_resp.get_json()
        assert listed["count"] == 1
        assert listed["saves"][0]["id"] == save_id
        assert "blocks_xml" not in listed["saves"][0]

        get_resp = client.get(f"/api/sandbox/saves/{save_id}")
        assert get_resp.status_code == 200
        detail = get_resp.get_json()["save"]
        assert detail["blocks_xml"] == sample_xml

        update_resp = client.put(
            f"/api/sandbox/saves/{save_id}",
            json={"title": "Updated", "blocks_xml": sample_xml, "code": "print(1)"},
        )
        assert update_resp.status_code == 200
        assert update_resp.get_json()["save"]["title"] == "Updated"

        delete_resp = client.delete(f"/api/sandbox/saves/{save_id}")
        assert delete_resp.status_code == 200
        assert client.get(f"/api/sandbox/saves/{save_id}").status_code == 404


def test_sandbox_saves_require_auth():
    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False
    client = app.test_client()
    resp = client.get("/api/sandbox/saves")
    assert resp.status_code in (302, 401)


if __name__ == "__main__":
    test_sandbox_saves_crud()
    test_sandbox_saves_require_auth()
    print("OK")
