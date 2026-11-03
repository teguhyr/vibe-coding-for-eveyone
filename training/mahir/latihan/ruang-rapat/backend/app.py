"""API pemesanan ruang rapat: Flask + SQLite."""

import sqlite3
from datetime import datetime

from flask import Flask, g, jsonify, request

SCHEMA = """
CREATE TABLE IF NOT EXISTS bookings (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    room      TEXT NOT NULL,
    booked_by TEXT NOT NULL,
    start_at  TEXT NOT NULL,
    end_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bookings_room_start ON bookings (room, start_at);
"""


def create_app(db_path: str = "bookings.db") -> Flask:
    app = Flask(__name__)

    def get_db() -> sqlite3.Connection:
        if "db" not in g:
            g.db = sqlite3.connect(db_path)
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(_error):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    with app.app_context():
        get_db().executescript(SCHEMA)

    @app.get("/api/bookings")
    def list_bookings():
        rows = (
            get_db()
            .execute("SELECT id, room, booked_by, start_at, end_at FROM bookings ORDER BY start_at")
            .fetchall()
        )
        return jsonify([dict(row) for row in rows])

    @app.post("/api/bookings")
    def create_booking():
        data = request.get_json(silent=True) or {}
        try:
            room = data["room"].strip()
            booked_by = data["booked_by"].strip()
            start = datetime.fromisoformat(data["start_at"])
            end = datetime.fromisoformat(data["end_at"])
        except (KeyError, AttributeError, TypeError, ValueError):
            return jsonify(error="Wajib diisi: room, booked_by, start_at, end_at (format ISO)"), 400
        if not room or not booked_by or end <= start:
            return jsonify(error="Data tidak valid: jam selesai harus setelah jam mulai"), 400

        start_at, end_at = start.isoformat(timespec="minutes"), end.isoformat(timespec="minutes")
        db = get_db()
        # Tanda ? = parameterized query: input pengguna tidak pernah digabung ke teks SQL.
        conflict = db.execute(
            "SELECT id FROM bookings WHERE room = ? AND start_at < ? AND ? < end_at",
            (room, end_at, start_at),
        ).fetchone()
        if conflict:
            return jsonify(error=f"Bentrok dengan booking #{conflict['id']}"), 409

        cursor = db.execute(
            "INSERT INTO bookings (room, booked_by, start_at, end_at) VALUES (?, ?, ?, ?)",
            (room, booked_by, start_at, end_at),
        )
        db.commit()
        return jsonify(id=cursor.lastrowid, room=room, start_at=start_at, end_at=end_at), 201

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
