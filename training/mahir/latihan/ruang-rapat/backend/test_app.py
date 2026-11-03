import pytest
from app import create_app


@pytest.fixture
def client(tmp_path):
    return create_app(str(tmp_path / "test.db")).test_client()


def booking(start="09:00", end="10:00", room="Merapi"):
    return {
        "room": room,
        "booked_by": "Tim HR",
        "start_at": f"2026-11-03T{start}",
        "end_at": f"2026-11-03T{end}",
    }


def test_booking_baru_berhasil(client):
    assert client.post("/api/bookings", json=booking()).status_code == 201
    assert len(client.get("/api/bookings").get_json()) == 1


def test_booking_bentrok_ditolak(client):
    client.post("/api/bookings", json=booking("09:00", "10:00"))
    assert client.post("/api/bookings", json=booking("09:30", "11:00")).status_code == 409


def test_booking_berurutan_boleh(client):
    client.post("/api/bookings", json=booking("09:00", "10:00"))
    assert client.post("/api/bookings", json=booking("10:00", "11:00")).status_code == 201


def test_ruang_berbeda_tidak_bentrok(client):
    client.post("/api/bookings", json=booking(room="Merapi"))
    assert client.post("/api/bookings", json=booking(room="Bromo")).status_code == 201


def test_data_tidak_valid_ditolak(client):
    assert client.post("/api/bookings", json={"room": "Merapi"}).status_code == 400
    assert client.post("/api/bookings", json=booking("10:00", "09:00")).status_code == 400


def test_sql_injection_tidak_berbahaya(client):
    evil = booking(room="Merapi'; DROP TABLE bookings; --")
    assert client.post("/api/bookings", json=evil).status_code == 201
    assert client.get("/api/bookings").status_code == 200
