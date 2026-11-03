"""Kunci Modul 2 & 4: API ruang rapat dengan DELETE, login, dan dua peran (staff/admin).

Perbedaan dari latihan/ruang-rapat/backend/app.py:
- Semua endpoint /api/bookings wajib login (401 jika belum).
- booked_by diambil dari pengguna yang login, bukan dari isi permintaan.
- DELETE /api/bookings/<id>: staff hanya boleh menghapus miliknya (403), admin boleh semua.
- Ruang harus salah satu dari ROOMS.
- Kata sandi disimpan sebagai hash; SECRET_KEY wajib dari environment.
"""

from __future__ import annotations

import argparse
import os
import sqlite3
from datetime import datetime

from flask import Flask, g, jsonify, request, session
from werkzeug.security import check_password_hash, generate_password_hash

ROOMS = ("Merapi", "Bromo", "Rinjani")
ROLES = ("staff", "admin")

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL CHECK (role IN ('staff', 'admin'))
);
CREATE TABLE IF NOT EXISTS bookings (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    room      TEXT NOT NULL,
    owner_id  INTEGER NOT NULL REFERENCES users (id),
    start_at  TEXT NOT NULL,
    end_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bookings_room_start ON bookings (room, start_at);
"""

BOOKING_COLUMNS = """
    SELECT b.id, b.room, u.username AS booked_by, b.start_at, b.end_at
    FROM bookings AS b JOIN users AS u ON u.id = b.owner_id
"""


def connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def add_user(db_path: str, username: str, password: str, role: str) -> None:
    if role not in ROLES:
        raise ValueError(f"role must be one of {ROLES}, got {role!r}")
    if len(password) < 8:
        raise ValueError("password must be at least 8 characters")
    with connect(db_path) as conn:
        conn.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, generate_password_hash(password), role),
        )


def create_app(db_path: str = "bookings.db", secret_key: str | None = None) -> Flask:
    secret_key = secret_key or os.environ.get("FLASK_SECRET_KEY")
    if not secret_key:
        # Tanpa kunci rahasia, cookie sesi bisa dipalsukan. Lebih baik gagal di awal.
        raise RuntimeError("Set the FLASK_SECRET_KEY environment variable")

    app = Flask(__name__)
    app.config.update(SECRET_KEY=secret_key, SESSION_COOKIE_SAMESITE="Lax")

    def get_db() -> sqlite3.Connection:
        if "db" not in g:
            g.db = connect(db_path)
        return g.db

    @app.teardown_appcontext
    def close_db(_error):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    def current_user() -> sqlite3.Row | None:
        user_id = session.get("user_id")
        if user_id is None:
            return None
        query = "SELECT id, username, role FROM users WHERE id = ?"
        return get_db().execute(query, (user_id,)).fetchone()

    def unauthorized():
        return jsonify(error="Silakan login terlebih dahulu"), 401

    @app.post("/api/login")
    def login():
        data = request.get_json(silent=True) or {}
        username, password = data.get("username"), data.get("password")
        if not isinstance(username, str) or not isinstance(password, str):
            return jsonify(error="Wajib diisi: username, password"), 400
        user = (
            get_db()
            .execute(
                "SELECT id, username, role, password_hash FROM users WHERE username = ?",
                (username,),
            )
            .fetchone()
        )
        # Pesan sama untuk "user tidak ada" dan "kata sandi salah": jangan bocorkan mana yang benar.
        if user is None or not check_password_hash(user["password_hash"], password):
            return jsonify(error="Username atau kata sandi salah"), 401
        session.clear()
        session["user_id"] = user["id"]
        return jsonify(username=user["username"], role=user["role"])

    @app.post("/api/logout")
    def logout():
        session.clear()
        return "", 204

    @app.get("/api/bookings")
    def list_bookings():
        if current_user() is None:
            return unauthorized()
        rows = get_db().execute(BOOKING_COLUMNS + " ORDER BY b.start_at").fetchall()
        return jsonify([dict(row) for row in rows])

    @app.post("/api/bookings")
    def create_booking():
        user = current_user()
        if user is None:
            return unauthorized()
        data = request.get_json(silent=True) or {}
        try:
            room = data["room"].strip()
            start = datetime.fromisoformat(data["start_at"])
            end = datetime.fromisoformat(data["end_at"])
        except (KeyError, AttributeError, TypeError, ValueError):
            return jsonify(error="Wajib diisi: room, start_at, end_at (format ISO)"), 400
        if room not in ROOMS:
            return jsonify(error=f"Ruang tidak dikenal. Pilihan: {', '.join(ROOMS)}"), 400
        if end <= start:
            return jsonify(error="Data tidak valid: jam selesai harus setelah jam mulai"), 400

        start_at, end_at = start.isoformat(timespec="minutes"), end.isoformat(timespec="minutes")
        db = get_db()
        conflict = db.execute(
            "SELECT id FROM bookings WHERE room = ? AND start_at < ? AND ? < end_at",
            (room, end_at, start_at),
        ).fetchone()
        if conflict:
            return jsonify(error=f"Bentrok dengan booking #{conflict['id']}"), 409

        cursor = db.execute(
            "INSERT INTO bookings (room, owner_id, start_at, end_at) VALUES (?, ?, ?, ?)",
            (room, user["id"], start_at, end_at),
        )
        db.commit()
        booking = db.execute(BOOKING_COLUMNS + " WHERE b.id = ?", (cursor.lastrowid,)).fetchone()
        return jsonify(dict(booking)), 201

    @app.delete("/api/bookings/<int:booking_id>")
    def delete_booking(booking_id: int):
        user = current_user()
        if user is None:
            return unauthorized()
        db = get_db()
        booking = db.execute("SELECT owner_id FROM bookings WHERE id = ?", (booking_id,)).fetchone()
        if booking is None:
            return jsonify(error=f"Booking #{booking_id} tidak ditemukan"), 404
        # Otorisasi dicek di backend: staff hanya boleh menghapus booking miliknya sendiri.
        if user["role"] != "admin" and booking["owner_id"] != user["id"]:
            return jsonify(error="Anda tidak berhak menghapus booking ini"), 403
        db.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        db.commit()
        return "", 204

    return app


def main() -> None:
    parser = argparse.ArgumentParser(description="Meeting room booking API.")
    parser.add_argument("--db", default="bookings.db")
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add-user", help="Create a user")
    add.add_argument("username")
    add.add_argument("role", choices=ROLES)
    sub.add_parser("run", help="Run the development server (local use only)")
    args = parser.parse_args()

    if args.command == "add-user":
        # Kata sandi dibaca dari environment agar tidak tersimpan di riwayat terminal.
        password = os.environ.get("NEW_USER_PASSWORD", "")
        add_user(args.db, args.username, password, args.role)
        print(f"User {args.username!r} ({args.role}) created")
    else:
        create_app(args.db).run(debug=True)


if __name__ == "__main__":
    main()
