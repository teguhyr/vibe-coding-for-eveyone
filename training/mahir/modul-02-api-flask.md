# Modul 2: Membangun API dengan Flask + SQLite

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 2](../03-mahir.md#langkah-2-membangun-api-dengan-flask--sqlite) |
| **Sesi** | Sesi 2 |
| **Durasi** | 110 menit |
| **Prasyarat** | Modul 1; Level 2 Modul 2 (pytest) dan Modul 6 (SQLite) |
| **File latihan** | [`latihan/ruang-rapat/backend/`](latihan/ruang-rapat/backend/) (contoh jadi), [`latihan/kunci/backend-lengkap/`](latihan/kunci/backend-lengkap/) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Membuat API Flask dengan *route* `GET`, `POST`, dan `DELETE` yang membalas JSON dan kode status yang tepat.
2. Memakai pola **`create_app(db_path)`** agar API mudah diuji dengan database sementara.
3. Menyimpan data di SQLite dengan **parameterized query** dan *index* yang tepat.
4. Memindahkan aturan bisnis yang sudah teruji (rumus bentrok modul 10) ke dalam API.
5. Menguji API dengan `test_client` tanpa menjalankan server.

---

## 📖 Materi

### A. Flask dalam 10 baris

```python
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/api/hello")
def hello():
    name = request.args.get("name", "dunia")  # /api/hello?name=Ani
    return jsonify(message=f"Halo, {name}!")  # otomatis 200 + JSON
```

| Bagian | Arti |
|--------|------|
| `@app.get("/api/hello")` | "Jika ada permintaan `GET` ke alamat ini, jalankan fungsi di bawahnya" (*route*) |
| `request.args` | Parameter di alamat setelah `?` |
| `request.get_json(silent=True)` | Isi permintaan berformat JSON (`None` jika bukan JSON yang valid) |
| `return jsonify(...), 201` | Balasan JSON dengan kode status 201 |

### B. Pola `create_app(db_path)`

```python
def create_app(db_path: str = "bookings.db") -> Flask:
    app = Flask(__name__)
    ...
    return app
```

Aplikasi dibuat oleh sebuah **fungsi** yang menerima lokasi database. Hasilnya:
- Tes memakai database sementara (`tmp_path`), sehingga **data asli tidak pernah tersentuh tes**.
- Produksi memakai lokasi lain (Modul 8: `/app/data/bookings.db`) tanpa mengubah kode.

### C. Koneksi database per permintaan

```python
def get_db() -> sqlite3.Connection:
    if "db" not in g:
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row  # baris bisa dibaca seperti dict: row["room"]
    return g.db


@app.teardown_appcontext
def close_db(_error):
    db = g.pop("db", None)
    if db is not None:
        db.close()
```

Kedua fungsi ini ditulis **di dalam** `create_app`, sehingga bisa memakai `db_path`. `g` adalah "meja kerja" untuk **satu** permintaan. Koneksi dibuka saat dibutuhkan dan **selalu ditutup** di akhir permintaan, bahkan jika terjadi error.

### D. Skema, index, dan parameter

```sql
CREATE TABLE IF NOT EXISTS bookings (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    room      TEXT NOT NULL,
    booked_by TEXT NOT NULL,
    start_at  TEXT NOT NULL,
    end_at    TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_bookings_room_start ON bookings (room, start_at);
```

- **Index** `(room, start_at)` seperti indeks di belakang buku: pencarian bentrok "ruang X di sekitar jam Y" tidak perlu membaca semua baris. Belum terasa untuk 10 baris, sangat terasa untuk 100.000 baris.
- **Semua** nilai dari pengguna masuk lewat `?`, tidak pernah digabung ke teks SQL (Level 2 Modul 6).

### E. Aturan bisnis yang dipakai ulang

```python
conflict = db.execute(
    "SELECT id FROM bookings WHERE room = ? AND start_at < ? AND ? < end_at",
    (room, end_at, start_at),
).fetchone()
```

Ini rumus yang sama dengan `overlaps()` di [`room_booking.py`](../../modules/10-general-affairs/room_booking.py): `a.start < b.end and b.start < a.end`. **Jangan menulis ulang logika yang sudah teruji** jika tidak perlu; cukup pindahkan ke tempat baru dan pertahankan tesnya.

Mengapa membandingkan **teks** tanggal aman? Karena semua waktu dinormalkan dulu dengan `isoformat(timespec="minutes")` menjadi `2026-11-03T09:00`. Format `YYYY-MM-DDTHH:MM` yang seragam bisa diurutkan seperti teks biasa. Tanpa normalisasi, `2026-11-03T9:00` dan `2026-11-03T09:00` akan dibandingkan dengan salah.

### F. Kode status yang tepat

| Situasi | Kode | Pesan (contoh) |
|---------|------|----------------|
| Booking dibuat | `201` | data booking baru |
| Data tidak lengkap / format salah | `400` | `Wajib diisi: room, booked_by, start_at, end_at (format ISO)` |
| Jam selesai ≤ jam mulai | `400` | `Data tidak valid: jam selesai harus setelah jam mulai` |
| Bentrok | `409` | `Bentrok dengan booking #1` |
| Booking yang mau dihapus tidak ada | `404` | `Booking #999 tidak ditemukan` |
| Berhasil dihapus | `204` | (tanpa isi) |

### G. Menguji API tanpa server

```python
@pytest.fixture
def client(tmp_path):
    return create_app(str(tmp_path / "test.db")).test_client()


def test_booking_bentrok_ditolak(client):
    client.post("/api/bookings", json=booking("09:00", "10:00"))
    assert client.post("/api/bookings", json=booking("09:30", "11:00")).status_code == 409
```

`test_client()` mengirim permintaan langsung ke aplikasi di memori: cepat, tanpa port, tanpa internet. Setiap tes mendapat database baru dari `tmp_path`, sehingga tes tidak saling memengaruhi.

---

## 🛠️ Praktik Terpandu

**1. Buat folder proyek** (dari folder utama repositori):

```bash
mkdir -p projects/ruang-rapat/backend
```

Di Windows PowerShell: `New-Item -ItemType Directory -Force projects\ruang-rapat\backend`.

**2. Minta rencana di Plan Mode.** Jalankan `claude`, masuk Plan Mode (`Shift+Tab`), lalu kirim prompt dari [Langkah 2 rencana training](../03-mahir.md#langkah-2-membangun-api-dengan-flask--sqlite) (bagian *Prompt untuk Claude*). Tinjau rencananya: apakah menyebut `create_app(db_path)`, parameter `?`, kode 400/409, dan tes SQL injection?

**3. Biarkan Claude membuat file**, lalu bandingkan dengan contoh jadi di [`latihan/ruang-rapat/backend/app.py`](latihan/ruang-rapat/backend/app.py). Kode Anda boleh berbeda, tetapi periksa 4 hal:

- [ ] Semua query memakai `?`
- [ ] Waktu dinormalkan sebelum disimpan dan dibandingkan
- [ ] Rumus bentrok memakai `<` (bukan `<=`), agar booking berurutan boleh
- [ ] Data yang salah membalas 400, bukan 500

**4. Jalankan tes** (dari folder `projects/ruang-rapat/backend`):

```bash
pytest
```

Contoh jadi menghasilkan `6 passed`. Untuk membandingkan, jalankan juga tes contoh jadi dari folder utama repositori:

```bash
pytest training/mahir/latihan/ruang-rapat/backend
```

> ⚠️ Jangan jalankan kedua folder itu dalam **satu** perintah `pytest`. Keduanya punya `app.py` dan `test_app.py`, dan nama file yang sama akan bentrok (aturan yang sama dengan modul-modul di repositori ini).

**5. Uji dengan `curl`** seperti di Modul 1: jalankan `python app.py`, kirim booking yang sama dua kali, pastikan yang kedua `409`.

**6. Commit** proyek Anda (tanpa `bookings.db`, yang sudah diblokir `.gitignore`):

```bash
git add projects/ruang-rapat/backend
```

```bash
git commit -m "Add meeting room booking API with conflict check"
```

---

## 🏋️ Latihan

### ⭐ Latihan 2.1: Baca kodenya

Di `app.py`, temukan: (a) baris yang menolak jam selesai ≤ jam mulai; (b) baris yang membuat index; (c) mengapa `except` menangkap `KeyError`, `AttributeError`, `TypeError`, **dan** `ValueError`. Kirim satu permintaan untuk memicu masing-masing jenis error.

### ⭐⭐ Latihan 2.2: Endpoint DELETE

Tambahkan `DELETE /api/bookings/<id>`: `204` jika berhasil, `404` jika ID tidak ada. Tulis tesnya **dulu**.

### ⭐⭐ Latihan 2.3: Filter per ruang

`GET /api/bookings?room=Bromo` hanya menampilkan booking ruang Bromo. Tanpa parameter, tampilkan semua. Pastikan nilai `room` masuk lewat `?`.

### ⭐⭐⭐ Latihan 2.4: Daftar ruang yang sah

Saat ini ruang apa pun diterima, termasuk salah ketik seperti `Merpi`. Tolak ruang di luar daftar `Merapi`, `Bromo`, `Rinjani` dengan `400` dan pesan yang menyebut pilihan yang sah. Perhatikan efek dominonya: tes `test_sql_injection_tidak_berbahaya` memakai nama ruang yang aneh. Apa yang harus Anda lakukan dengan tes itu, dan mengapa?

---

## 📝 Kuis

1. Apa keuntungan pola `create_app(db_path)` untuk pengujian?
2. Mengapa waktu dinormalkan dengan `isoformat(timespec="minutes")` sebelum disimpan?
3. Booking A 09:00–10:00 sudah ada. Apakah booking B 10:00–11:00 bentrok menurut rumus `start_at < ? AND ? < end_at`? Jelaskan.
4. Kode status apa yang tepat untuk "booking yang mau dihapus tidak ada"?
5. Mengapa `test_client()` tidak membutuhkan server yang berjalan?

---

## 📌 Ringkasan

- *Route* Flask = alamat + metode → fungsi yang membalas JSON + kode status.
- `create_app(db_path)` membuat API mudah diuji dengan database sementara.
- **Semua** query memakai `?`; index mempercepat pencarian yang sering dilakukan.
- Pindahkan aturan bisnis yang sudah teruji, jangan menulis ulang; normalkan data sebelum dibandingkan.
- Uji dengan `test_client()`: 201, 400, 404, 409, dan input berbahaya.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 2.1**
- (a) `if not room or not booked_by or end <= start:` → 400.
- (b) `CREATE INDEX IF NOT EXISTS idx_bookings_room_start ON bookings (room, start_at);` di `SCHEMA`.
- (c) Setiap jenis error mewakili satu cara data bisa salah:

| Error | Dipicu oleh | Contoh isi permintaan |
|-------|-------------|-----------------------|
| `KeyError` | Kolom tidak ada | `{"room": "Merapi"}` |
| `AttributeError` | `room` bukan teks, sehingga `.strip()` gagal | `{"room": 123, ...}` |
| `TypeError` | Waktu bukan teks, sehingga `fromisoformat` gagal | `{"start_at": 900, ...}` |
| `ValueError` | Teks waktu tidak valid | `{"start_at": "besok pagi", ...}` |

Tanpa menangkap keempatnya, salah satu jenis data akan menghasilkan **500** (bug), bukan **400**.

**Latihan 2.2** (sudah diuji: 8 tes lulus bersama 6 tes awal):
```python
    @app.delete("/api/bookings/<int:booking_id>")
    def delete_booking(booking_id: int):
        db = get_db()
        cursor = db.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify(error=f"Booking #{booking_id} tidak ditemukan"), 404
        return "", 204
```
```python
def test_hapus_booking(client):
    booking_id = client.post("/api/bookings", json=booking()).get_json()["id"]
    assert client.delete(f"/api/bookings/{booking_id}").status_code == 204
    assert client.get("/api/bookings").get_json() == []


def test_hapus_id_yang_tidak_ada(client):
    assert client.delete("/api/bookings/999").status_code == 404
```
`<int:booking_id>` membuat Flask otomatis membalas 404 untuk `/api/bookings/abc`. `cursor.rowcount` = jumlah baris yang terhapus; 0 berarti ID tidak ada.

**Latihan 2.3** (sudah diuji):
```python
    @app.get("/api/bookings")
    def list_bookings():
        query = "SELECT id, room, booked_by, start_at, end_at FROM bookings"
        params: tuple[str, ...] = ()
        room = request.args.get("room")
        if room:
            query += " WHERE room = ?"
            params = (room,)
        rows = get_db().execute(query + " ORDER BY start_at", params).fetchall()
        return jsonify([dict(row) for row in rows])
```
Yang digabung ke teks SQL hanya potongan **tetap** (`" WHERE room = ?"`) yang ditulis programmer. Nilai dari pengguna tetap lewat parameter.

**Latihan 2.4:** lihat [`latihan/kunci/backend-lengkap/booking_api.py`](latihan/kunci/backend-lengkap/booking_api.py) (konstanta `ROOMS`). Tes SQL injection **tidak dihapus**, tetapi **dipindahkan** ke input yang masih berupa teks bebas. Di kunci, tes itu menguji kolom `username` saat login (`test_sql_injection_di_login_tidak_berbahaya`). Tujuan tesnya (membuktikan input berbahaya tidak dieksekusi sebagai SQL) tetap terpenuhi. Mengubah tes boleh jika **aturan bisnisnya memang berubah**, dan alasan perubahan itu harus jelas.

**Kuis**
1. Tes bisa memakai database sementara yang baru untuk setiap tes, sehingga data asli tidak tersentuh dan tes tidak saling memengaruhi.
2. Agar semua waktu punya format yang sama persis, sehingga perbandingan teks di SQL (`<`) memberi hasil yang benar.
3. Tidak bentrok. `start_at(A) 09:00 < end(B) 11:00` benar, tetapi `start(B) 10:00 < end_at(A) 10:00` **salah**. Kedua syarat harus benar agar bentrok.
4. `404`.
5. `test_client()` memanggil aplikasi langsung di memori, tanpa membuka port jaringan.

</details>

---

← [Modul 1](modul-01-arsitektur-3-lapis.md) | **Berikutnya: [Modul 3: Membangun Tampilan dengan React →](modul-03-react.md)**
