# Kunci Modul 2 & 4: tes aturan bisnis, autentikasi, otorisasi, dan keamanan.
import sqlite3

import pytest
from booking_api import add_user, create_app

PASSWORD = "rahasia-uji-123"  # kata sandi palsu khusus tes


@pytest.fixture
def db_path(tmp_path):
    path = str(tmp_path / "test.db")
    add_user(path, "ani", PASSWORD, "staff")
    add_user(path, "budi", PASSWORD, "staff")
    add_user(path, "admin", PASSWORD, "admin")
    return path


@pytest.fixture
def app(db_path):
    return create_app(db_path, secret_key="kunci-khusus-tes")


def login(app, username):
    client = app.test_client()
    response = client.post("/api/login", json={"username": username, "password": PASSWORD})
    assert response.status_code == 200
    return client


def booking(start="09:00", end="10:00", room="Merapi"):
    return {"room": room, "start_at": f"2026-11-03T{start}", "end_at": f"2026-11-03T{end}"}


def test_tanpa_login_ditolak(app):
    client = app.test_client()
    assert client.get("/api/bookings").status_code == 401
    assert client.post("/api/bookings", json=booking()).status_code == 401
    assert client.delete("/api/bookings/1").status_code == 401


def test_login_salah_memberi_pesan_yang_sama(app):
    client = app.test_client()
    wrong_password = client.post("/api/login", json={"username": "ani", "password": "salah"})
    unknown_user = client.post("/api/login", json={"username": "zaki", "password": PASSWORD})
    assert wrong_password.status_code == unknown_user.status_code == 401
    assert wrong_password.get_json() == unknown_user.get_json()


def test_booked_by_diambil_dari_pengguna_login(app):
    ani = login(app, "ani")
    response = ani.post("/api/bookings", json=booking() | {"booked_by": "budi"})
    assert response.status_code == 201
    assert response.get_json()["booked_by"] == "ani"


def test_bentrok_ditolak_dan_berurutan_boleh(app):
    ani = login(app, "ani")
    assert ani.post("/api/bookings", json=booking("09:00", "10:00")).status_code == 201
    assert ani.post("/api/bookings", json=booking("09:30", "11:00")).status_code == 409
    assert ani.post("/api/bookings", json=booking("10:00", "11:00")).status_code == 201


def test_ruang_tidak_dikenal_ditolak(app):
    ani = login(app, "ani")
    assert ani.post("/api/bookings", json=booking(room="Semeru")).status_code == 400


def test_staff_boleh_menghapus_miliknya(app):
    ani = login(app, "ani")
    booking_id = ani.post("/api/bookings", json=booking()).get_json()["id"]
    assert ani.delete(f"/api/bookings/{booking_id}").status_code == 204
    assert ani.get("/api/bookings").get_json() == []


def test_staff_tidak_boleh_menghapus_milik_orang_lain(app):
    booking_id = login(app, "ani").post("/api/bookings", json=booking()).get_json()["id"]
    assert login(app, "budi").delete(f"/api/bookings/{booking_id}").status_code == 403


def test_admin_boleh_menghapus_milik_siapa_pun(app):
    booking_id = login(app, "ani").post("/api/bookings", json=booking()).get_json()["id"]
    assert login(app, "admin").delete(f"/api/bookings/{booking_id}").status_code == 204


def test_hapus_id_yang_tidak_ada(app):
    assert login(app, "admin").delete("/api/bookings/999").status_code == 404


def test_logout_mengakhiri_sesi(app):
    ani = login(app, "ani")
    assert ani.post("/api/logout").status_code == 204
    assert ani.get("/api/bookings").status_code == 401


def test_sql_injection_di_login_tidak_berbahaya(app, db_path):
    client = app.test_client()
    evil = {"username": "ani' OR '1'='1", "password": "x"}
    assert client.post("/api/login", json=evil).status_code == 401
    with sqlite3.connect(db_path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 3


def test_kata_sandi_tidak_disimpan_polos(db_path):
    with sqlite3.connect(db_path) as conn:
        hashes = [row[0] for row in conn.execute("SELECT password_hash FROM users")]
    assert PASSWORD not in hashes


def test_aplikasi_menolak_jalan_tanpa_secret_key(db_path, monkeypatch):
    monkeypatch.delenv("FLASK_SECRET_KEY", raising=False)
    with pytest.raises(RuntimeError, match="FLASK_SECRET_KEY"):
        create_app(db_path)


def test_kata_sandi_pendek_ditolak(tmp_path):
    with pytest.raises(ValueError, match="8 characters"):
        add_user(str(tmp_path / "x.db"), "cici", "pendek", "staff")
