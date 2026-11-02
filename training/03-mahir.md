# 🔴 Level 3: Mahir — "Dari Praktisi Menjadi Hero"

| | |
|---|---|
| **Untuk siapa** | Lulusan Level 2: sudah bisa membuat alat yang teruji dan rapi |
| **Durasi** | ± 45 jam (6–8 minggu) |
| **Prasyarat** | Semua item [Checklist Level 2](02-menengah.md#-checklist-kelulusan-level-2) tercentang. Untuk Langkah 3, pasang juga **Node.js LTS** dari https://nodejs.org/ |
| **Hasil akhir** | Anda bisa membangun dan mengamankan aplikasi web untuk tim, mengotomatiskan pemeriksaan kualitas, memakai fitur lanjutan Claude Code dan Claude API, men-deploy aplikasi, dan memimpin adopsi vibe coding di organisasi |

### Daftar Langkah

1. [Dari skrip ke aplikasi: arsitektur 3 lapis](#langkah-1-dari-skrip-ke-aplikasi-arsitektur-3-lapis)
2. [Membangun API dengan Flask + SQLite](#langkah-2-membangun-api-dengan-flask--sqlite)
3. [Membangun tampilan dengan React](#langkah-3-membangun-tampilan-dengan-react)
4. [Keamanan aplikasi (OWASP)](#langkah-4-keamanan-aplikasi-owasp)
5. [Fitur lanjutan Claude Code](#langkah-5-fitur-lanjutan-claude-code)
6. [Integrasi Claude API ke aplikasi Anda](#langkah-6-integrasi-claude-api-ke-aplikasi-anda)
7. [Otomatisasi kualitas dengan CI/CD](#langkah-7-otomatisasi-kualitas-dengan-cicd)
8. [Deploy dengan Docker](#langkah-8-deploy-dengan-docker)
9. [Berpikir seperti arsitek](#langkah-9-berpikir-seperti-arsitek)
10. [Menjadi AI Champion di organisasi](#langkah-10-menjadi-ai-champion-di-organisasi)
- [Proyek Akhir (Capstone)](#-proyek-akhir-capstone-level-3)
- [Checklist "Hero"](#-checklist-hero)

---

## Langkah 1: Dari Skrip ke Aplikasi: Arsitektur 3 Lapis

🎯 **Tujuan:** Memahami kapan skrip sudah tidak cukup, dan bagaimana aplikasi web disusun.

📖 **Konsep:** Skrip cocok untuk **satu orang** yang menjalankannya sendiri. Saat **banyak orang** perlu memakai alat yang sama, membutuhkan **data bersama**, dan bekerja dari **browser**, Anda butuh aplikasi.

Aplikasi web umumnya punya 3 lapis, seperti sebuah restoran:

```
  ┌────────────────────┐      ┌────────────────────┐      ┌────────────────────┐
  │  FRONTEND          │ HTTP │  BACKEND (API)     │ SQL  │  DATABASE          │
  │  "Ruang makan"     │ ───▶ │  "Dapur"           │ ───▶ │  "Gudang bahan"    │
  │  React di browser  │ ◀─── │  Flask (Python)    │ ◀─── │  SQLite/PostgreSQL │
  │  Form, tabel       │ JSON │  Aturan bisnis     │      │  Data tersimpan    │
  └────────────────────┘      └────────────────────┘      └────────────────────┘
```

| Lapis | Tugas | Teknologi di materi ini | Alternatif |
|-------|-------|-------------------------|------------|
| Frontend | Tampilan dan interaksi pengguna | React + TypeScript (Vite) | Vue, HTML biasa |
| Backend | Aturan bisnis, validasi, keamanan | Flask (Python) | FastAPI, Django, **PHP Laravel** |
| Database | Menyimpan data secara permanen | SQLite | PostgreSQL, MySQL/MariaDB |

**Aturan penting:** aturan bisnis dan validasi **wajib ada di backend**. Frontend bisa dimanipulasi pengguna; backend adalah "penjaga gerbang" terakhir.

🛠️ **Praktik:** Kita akan mengubah modul [10-general-affairs](../modules/10-general-affairs/) (cek bentrok ruang rapat) menjadi **aplikasi pemesanan ruang rapat**, tempat setiap tim memesan sendiri dan bentrokan langsung ditolak.

Buat struktur proyek berikut:

```
projects/ruang-rapat/
├── backend/
│   ├── app.py
│   ├── test_app.py
│   └── requirements.txt
└── frontend/          ← dibuat di Langkah 3
```

✅ **Cek pemahaman:** Mengapa pengecekan bentrokan jadwal harus dilakukan di backend, bukan hanya di frontend?

---

## Langkah 2: Membangun API dengan Flask + SQLite

🎯 **Tujuan:** Membuat API yang menyimpan data, menerapkan aturan bisnis, dan diuji otomatis.

📖 **Konsep:** **API** adalah "loket pelayanan" untuk program lain. Frontend mengirim **permintaan** (*request*), dan API membalas dengan **data JSON** dan **kode status**:

| Kode | Arti | Contoh di aplikasi kita |
|------|------|-------------------------|
| `200` | OK | Daftar booking berhasil diambil |
| `201` | Berhasil dibuat | Booking baru tersimpan |
| `400` | Permintaan salah | Data tidak lengkap atau jam selesai sebelum jam mulai |
| `409` | Konflik | Ruang sudah dipesan di jam itu |

🛠️ **Praktik**

**1. Prompt untuk Claude (Plan Mode dulu!):**

```
ROLE: Kamu senior backend developer Python. Jelaskan keputusan desainmu.

CONTEXT: Saya mengubah modules/10-general-affairs/room_booking.py menjadi API.
Data booking: room, booked_by, start_at, end_at (format ISO, mis. 2026-11-03T09:00).

TASK: Buat API Flask di projects/ruang-rapat/backend/app.py dengan:
- GET /api/bookings : daftar semua booking, urut jam mulai
- POST /api/bookings : buat booking baru

CONSTRAINTS:
- Simpan di SQLite. Pakai parameterized query (?) untuk SEMUA query.
- Tolak data tidak lengkap atau jam selesai <= jam mulai (400).
- Tolak booking yang bentrok di ruang yang sama (409). Booking berurutan boleh.
- Gunakan pola create_app(db_path) agar mudah dites dengan database sementara.
- Pesan error dalam Bahasa Indonesia.
- Tulis tes pytest, termasuk tes bahwa input berisi SQL injection tidak berbahaya.

OUTPUT: app.py, test_app.py, requirements.txt, dan cara menjalankannya.
```

**2. Contoh hasil yang baik**, `backend/app.py`:

```python
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
```

**3. Tes**, `backend/test_app.py`:

```python
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
```

**4. `backend/requirements.txt`:**

```
flask==3.1.3
gunicorn==23.0.0
```

**5. Jalankan dan coba** (dari folder `projects/ruang-rapat/backend`):

```bash
pip install -r requirements.txt
```

```bash
pytest
```

```bash
python app.py
```

Di terminal kedua, kirim permintaan uji:

```bash
curl -X POST http://127.0.0.1:5000/api/bookings -H "Content-Type: application/json" -d '{"room": "Merapi", "booked_by": "Tim HR", "start_at": "2026-11-03T09:00", "end_at": "2026-11-03T10:00"}'
```

Jalankan perintah yang sama sekali lagi. Kali ini API harus membalas dengan error **bentrok** (409).

📖 **Hal penting dari kode di atas**
- **Rumus bentrok** `start_at < end_baru AND start_baru < end_at` sama persis dengan modul 10. Logika yang sudah teruji dipakai ulang.
- **Index** `idx_bookings_room_start` mempercepat pencarian bentrok saat data sudah ribuan baris.
- **`create_app(db_path)`** membuat tes memakai database sementara (`tmp_path`), sehingga data asli tidak pernah tersentuh tes.
- Format waktu disamakan (`isoformat(timespec="minutes")`) agar perbandingan teks di SQL selalu benar.

⚠️ **Kesalahan umum**
- **`debug=True` di server produksi.** Mode debug membuka celah keamanan serius. Hanya untuk komputer Anda sendiri (lihat Langkah 8).
- **Validasi hanya di frontend.** Siapa pun bisa mengirim permintaan langsung dengan `curl`, seperti yang baru Anda lakukan.

✅ **Cek pemahaman:** Tambahkan endpoint `DELETE /api/bookings/<id>` (dengan bantuan Claude), lengkap dengan tesnya, termasuk tes untuk ID yang tidak ada (404).

---

## Langkah 3: Membangun Tampilan dengan React

🎯 **Tujuan:** Membuat tampilan web yang memakai API dari Langkah 2.

📖 **Konsep:** React membangun tampilan dari **komponen**, seperti balok LEGO. Setiap komponen punya **state** (data yang bisa berubah), dan saat state berubah, tampilan ikut berubah otomatis.

🛠️ **Praktik**

**1. Buat proyek React** (dari folder `projects/ruang-rapat`):

```bash
npm create vite@latest frontend -- --template react-ts
```

```bash
cd frontend
```

```bash
npm install
```

**2. Hubungkan ke API.** Ubah `frontend/vite.config.ts` agar permintaan ke `/api` diteruskan ke Flask:

```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: { "/api": "http://127.0.0.1:5000" },
  },
});
```

**3. Buat komponen** `frontend/src/BookingApp.tsx`:

```tsx
import { useEffect, useState, type FormEvent } from "react";

type Booking = {
  id: number;
  room: string;
  booked_by: string;
  start_at: string;
  end_at: string;
};

export default function BookingApp() {
  const [bookings, setBookings] = useState<Booking[]>([]);
  const [message, setMessage] = useState("");

  async function loadBookings() {
    const response = await fetch("/api/bookings");
    setBookings(await response.json());
  }

  useEffect(() => {
    loadBookings();
  }, []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const formElement = event.currentTarget; // simpan sebelum await: React mengosongkannya setelahnya
    const form = new FormData(formElement);
    const response = await fetch("/api/bookings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(Object.fromEntries(form)),
    });
    const result = await response.json();
    if (response.ok) {
      setMessage(`Booking #${result.id} berhasil disimpan.`);
      formElement.reset();
      loadBookings();
    } else {
      setMessage(result.error); // React otomatis meng-escape teks, aman dari XSS
    }
  }

  return (
    <main>
      <h1>Pemesanan Ruang Rapat</h1>

      <form onSubmit={handleSubmit}>
        <label>
          Ruang
          <select name="room" required>
            <option>Merapi</option>
            <option>Bromo</option>
            <option>Rinjani</option>
          </select>
        </label>
        <label>
          Tim pemesan
          <input name="booked_by" required />
        </label>
        <label>
          Mulai
          <input name="start_at" type="datetime-local" required />
        </label>
        <label>
          Selesai
          <input name="end_at" type="datetime-local" required />
        </label>
        <button type="submit">Pesan</button>
      </form>

      <p role="status">{message}</p>

      <table>
        <thead>
          <tr>
            <th>Ruang</th>
            <th>Tim</th>
            <th>Mulai</th>
            <th>Selesai</th>
          </tr>
        </thead>
        <tbody>
          {bookings.map((b) => (
            <tr key={b.id}>
              <td>{b.room}</td>
              <td>{b.booked_by}</td>
              <td>{b.start_at}</td>
              <td>{b.end_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
```

**4. Tampilkan komponen.** Ganti isi `frontend/src/App.tsx` dengan:

```tsx
import BookingApp from "./BookingApp";

export default function App() {
  return <BookingApp />;
}
```

**5. Jalankan keduanya.** Terminal 1 (folder `backend`): `python app.py`. Terminal 2 (folder `frontend`):

```bash
npm run dev
```

Buka alamat yang muncul (biasanya http://localhost:5173), lalu coba pesan ruang yang sama dua kali.

📖 **Hal penting dari kode di atas**
- `useState` menyimpan data yang tampil di layar. `useEffect(..., [])` memuat data sekali saat halaman dibuka.
- **`const formElement = event.currentTarget` disimpan sebelum `await`.** Setelah `await`, React mengosongkan `event.currentTarget` menjadi `null`. Jika `event.currentTarget.reset()` dipanggil langsung, aplikasi akan error. Ini **bug yang sering dibuat AI**; kode di atas sudah diperbaiki dan diuji di browser.
- **Aksesibilitas:** setiap input dibungkus `<label>` (bisa dibaca *screen reader*), dan pesan memakai `role="status"` agar diumumkan otomatis.
- Pesan error dari server ditampilkan sebagai **teks** `{message}`. React otomatis meng-escape-nya, sehingga aman dari serangan XSS.

⚠️ **Kesalahan umum**
- **Lupa menjalankan backend** sehingga muncul error koneksi di browser. Kedua server harus berjalan.
- **Menyalin kunci API atau rahasia ke kode frontend.** Semua kode frontend bisa dilihat siapa pun lewat browser.

✅ **Cek pemahaman:** Minta Claude menambahkan tombol **Hapus** di setiap baris tabel, memakai endpoint `DELETE` dari latihan Langkah 2.

---

## Langkah 4: Keamanan Aplikasi (OWASP)

🎯 **Tujuan:** Mengenali dan mencegah celah keamanan paling umum di aplikasi web.

📖 **Konsep:** **OWASP Top 10** adalah daftar risiko keamanan web paling umum (https://owasp.org/Top10/). AI bisa menulis kode yang berfungsi tetapi **tidak aman**, jadi Anda harus tahu apa yang dicari.

### 1. SQL Injection: menggabungkan input ke teks SQL

❌ **Berbahaya** (Python):
```python
db.execute(f"SELECT * FROM bookings WHERE room = '{room}'")
# Jika room = "x' OR '1'='1", semua data bocor
```

✅ **Aman** (Python):
```python
db.execute("SELECT id, room FROM bookings WHERE room = ?", (room,))
```

✅ **Aman** (PHP dengan PDO):
```php
<?php
declare(strict_types=1);

$stmt = $pdo->prepare('SELECT id, room FROM bookings WHERE room = :room');
$stmt->execute(['room' => $room]);
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
```

### 2. XSS (Cross-Site Scripting): menampilkan input sebagai HTML

❌ **Berbahaya** (React): `<div dangerouslySetInnerHTML={{ __html: komentar }} />`

✅ **Aman** (React): `<div>{komentar}</div>`; React meng-escape teks secara otomatis.

✅ **Aman** (PHP): `<?= htmlspecialchars($komentar, ENT_QUOTES, 'UTF-8') ?>`

### 3. Rahasia di dalam kode

❌ `API_KEY = "sk-ant-..."` ditulis langsung di kode, lalu ikut ter-commit ke Git.

✅ Simpan di environment variable atau file `.env` (yang masuk `.gitignore`), lalu baca dengan `os.environ["NAMA_VARIABEL"]`. Commit hanya `.env.example` berisi nama variabel tanpa nilai. **Jika rahasia pernah ter-commit, anggap sudah bocor: segera ganti (*rotate*) kuncinya.**

### 4. Tanpa login dan hak akses

Aplikasi internal tetap butuh **autentikasi** (siapa Anda?) dan **otorisasi** (boleh melakukan apa?). Contoh: staf boleh membuat booking, tetapi hanya admin GA yang boleh menghapus booking orang lain. Jangan membuat sistem login sendiri dari nol; pakai fitur framework (mis. Flask-Login, Laravel Breeze) atau SSO perusahaan.

### Daftar periksa keamanan sebelum rilis

- [ ] Semua query memakai parameter (`?` atau `:nama`)
- [ ] Semua input divalidasi **di backend**
- [ ] Tidak ada rahasia di kode atau di riwayat Git
- [ ] `debug` mati di produksi
- [ ] Ada login, dan hak akses dicek di setiap endpoint yang mengubah data
- [ ] Data pribadi dikumpulkan seminimal mungkin dan diproteksi (UU PDP)
- [ ] Dependensi diperbarui secara berkala (`pip list --outdated`, `npm audit`)

🛠️ **Praktik:** Di Claude Code, jalankan tinjauan keamanan atas perubahan Anda:

```
/security-review
```

Atau minta secara spesifik:

```
Tinjau projects/ruang-rapat dengan sudut pandang OWASP Top 10.
Untuk setiap temuan: jelaskan risikonya, tunjukkan baris kodenya, dan usulkan perbaikan.
Urutkan dari yang paling berbahaya.
```

✅ **Cek pemahaman:** Jelaskan ke rekan kerja yang bukan programmer, dengan analogi, mengapa SQL injection berbahaya.

---

## Langkah 5: Fitur Lanjutan Claude Code

🎯 **Tujuan:** Mengotomatiskan pekerjaan berulang Anda **dengan** Claude Code itu sendiri.

📖 **Konsep:** Setelah mahir, Anda bisa "melatih" Claude Code dengan SOP tim:

| Fitur | Analogi | Lokasi |
|-------|---------|--------|
| **Custom slash command** | Tombol pintas untuk prompt yang sering dipakai | `.claude/commands/<nama>.md` |
| **Skill** | Paket keahlian + instruksi yang dipakai Claude saat relevan | `.claude/skills/<nama>/SKILL.md` |
| **Subagent** | Spesialis dengan tugas khusus, mis. reviewer keamanan | `.claude/agents/<nama>.md` |
| **Hooks** | Aturan otomatis: "setiap kali X terjadi, jalankan Y" | `.claude/settings.json` |
| **Permissions** | Daftar perintah yang boleh atau dilarang | `.claude/settings.json` |
| **MCP server** | Menghubungkan Claude ke sistem lain (database, Jira, dsb.) | `claude mcp add ...` |
| **Mode headless** | Menjalankan Claude dari skrip/otomatisasi | `claude -p "..."` |

🛠️ **Praktik**

**1. Custom slash command:** buat file `.claude/commands/cek-kualitas.md`:

```markdown
Jalankan pemeriksaan kualitas lengkap untuk proyek ini:
1. pytest
2. ruff check .
3. ruff format --check .

Jika ada yang gagal, jelaskan penyebabnya dalam Bahasa Indonesia yang sederhana,
lalu perbaiki. Fokus khusus: $ARGUMENTS
```

Pakai dengan mengetik `/cek-kualitas modul keuangan` di Claude Code.

**2. Skill:** buat `.claude/skills/laporan-bulanan/SKILL.md`:

```markdown
---
name: laporan-bulanan
description: Membuat laporan bulanan anggaran vs realisasi. Gunakan saat pengguna meminta laporan bulanan, rekap anggaran, atau variance report.
---

1. Jalankan `python modules/02-finance/budget_variance.py`.
2. Ringkas hasilnya: 3 temuan terbesar (OVER / UNDER / UNBUDGETED).
3. Tulis ringkasan eksekutif maksimal 5 kalimat dalam Bahasa Indonesia formal.
4. Jangan pernah menyertakan nama karyawan atau data pribadi.
```

**3. Subagent:** buat `.claude/agents/reviewer-keamanan.md`:

```markdown
---
name: reviewer-keamanan
description: Meninjau perubahan kode untuk masalah keamanan (OWASP Top 10) dan perlindungan data pribadi (UU PDP). Gunakan sebelum merge.
tools: Read, Grep, Glob
---

Kamu reviewer keamanan senior. Periksa: SQL injection, XSS, rahasia di kode,
validasi input, hak akses, dan data pribadi yang tidak perlu.
Laporkan temuan dari yang paling berbahaya, dengan nama file dan baris.
Jangan mengubah file apa pun.
```

**4. Hooks & permissions:** buat `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["Bash(pytest:*)", "Bash(ruff check:*)", "Bash(ruff format:*)"],
    "deny": ["Read(./private/**)", "Read(./.env)"]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "ruff format ." }]
      }
    ]
  }
}
```

Artinya: Claude boleh menjalankan pytest dan ruff tanpa bertanya, **dilarang** membaca folder `private/` dan file `.env`, dan **setiap kali** Claude mengedit file, kode otomatis dirapikan.

**5. Mode headless** untuk otomatisasi, misalnya dijadwalkan setiap pagi:

```bash
claude -p "Jalankan pytest dan ringkas hasilnya dalam 3 baris"
```

⚠️ **Kesalahan umum**
- **Memberi izin terlalu luas** seperti `Bash(*)`. Izinkan hanya perintah spesifik yang aman.
- **Hook yang lambat.** Hook dijalankan setiap kali terpicu; pilih perintah yang cepat.

Dokumentasi lengkap dan terbaru: https://code.claude.com/docs

✅ **Cek pemahaman:** Buat satu custom slash command untuk pekerjaan yang paling sering Anda minta ke Claude, lalu bagikan ke tim lewat Git.

---

## Langkah 6: Integrasi Claude API ke Aplikasi Anda

🎯 **Tujuan:** Menambahkan kecerdasan AI **di dalam** aplikasi Anda, bukan hanya memakai AI untuk menulis kode.

📖 **Konsep:** Di modul [09-customer-service](../modules/09-customer-service/), pesan pelanggan dikategorikan dengan **aturan kata kunci**. Aturan ini cepat, gratis, dan mudah dijelaskan, tetapi pesan dengan kata-kata tak terduga masuk ke `other`.

**Pola hibrida** menggabungkan keunggulan keduanya:

```
Pesan masuk → Aturan kata kunci → cocok?  ── ya ──▶ kategori (cepat, gratis)
                                     │
                                    tidak
                                     ▼
                              Claude API ──▶ kategori (cerdas, berbayar)
```

🛠️ **Praktik**

1. Buat API key di Claude Console (https://platform.claude.com/) dan simpan sebagai **environment variable**, bukan di kode:

   ```bash
   export ANTHROPIC_API_KEY="isi-dengan-kunci-anda"
   ```

2. Pasang SDK resmi:

   ```bash
   pip install anthropic
   ```

3. Buat `klasifikasi_ai.py`:

```python
import anthropic

KATEGORI = ["tagihan", "pengiriman", "teknis", "akun", "lainnya"]

client = anthropic.Anthropic()  # membaca ANTHROPIC_API_KEY dari environment


def klasifikasi(pesan: str) -> str:
    response = client.beta.messages.create(
        model="claude-opus-5-5",
        max_tokens=1024,
        output_config={"effort": "low"},  # tugas sederhana: cukup effort rendah
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",  # jika model menolak, API mencoba model cadangan
        system=(
            "Anda mengklasifikasikan pesan layanan pelanggan. "
            f"Jawab HANYA dengan satu kata dari daftar ini: {', '.join(KATEGORI)}."
        ),
        messages=[{"role": "user", "content": pesan}],
    )
    if response.stop_reason == "refusal":
        return "lainnya"
    teks = next((b.text for b in response.content if b.type == "text"), "")
    jawaban = teks.strip().lower()
    return jawaban if jawaban in KATEGORI else "lainnya"  # jangan percaya output mentah


if __name__ == "__main__":
    print(klasifikasi("Paket saya belum sampai padahal sudah seminggu"))
```

📖 **Hal penting dari kode di atas**
- **`system`** berisi instruksi tetap; **`messages`** berisi pesan yang diklasifikasikan.
- **Output AI divalidasi**: jika jawabannya bukan salah satu kategori, program memakai `"lainnya"`. **Jangan pernah langsung memercayai output AI** di dalam program.
- **`effort: "low"`** cukup untuk tugas klasifikasi sederhana, sehingga lebih cepat dan hemat.
- **`fallbacks="default"`**: jika model menolak permintaan karena alasan keamanan, API otomatis mencoba model cadangan. Program tetap memeriksa `stop_reason` untuk berjaga-jaga.
- **Uji tanpa memanggil API sungguhan**: ganti `client.beta.messages.create` dengan fungsi palsu di tes (`monkeypatch`), agar tes cepat, gratis, dan tidak butuh internet.

⚠️ **Hal yang wajib diperhatikan**
- **Data dikirim ke luar perusahaan.** Pesan yang dikirim ke API diproses di server Anthropic. Periksa kebijakan perusahaan dan **jangan kirim data pribadi** (nama + nomor HP, NIK, dsb.) tanpa dasar hukum dan persetujuan sesuai UU PDP. Anonimkan dulu jika memungkinkan.
- **Ada biaya per pemakaian.** Pakai aturan biasa untuk kasus mudah, dan AI hanya untuk sisanya (pola hibrida). Cek harga terbaru di https://www.anthropic.com/pricing.
- **API key adalah rahasia.** Jangan taruh di kode, frontend, atau Git.

✅ **Cek pemahaman:** Gabungkan `klasifikasi()` dengan `categorize()` dari modul 09: pakai AI **hanya** jika hasil aturan kata kunci adalah `other`. Tulis tes dengan klien palsu.

---

## Langkah 7: Otomatisasi Kualitas dengan CI/CD

🎯 **Tujuan:** Setiap perubahan kode otomatis dites, tanpa bergantung pada ingatan manusia.

📖 **Konsep:** **CI (Continuous Integration)** seperti **satpam di pintu gudang**: setiap barang (perubahan kode) yang masuk diperiksa otomatis. Jika tes gagal, perubahan ditandai merah dan tidak boleh digabung.

🛠️ **Praktik:** Buat file `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements-dev.txt
      - run: ruff check .
      - run: ruff format --check .
      - run: pytest
```

Setelah di-push ke GitHub, buka tab **Actions** di repositori. Setiap push dan pull request kini otomatis diperiksa.

Langkah lanjutan: atur **branch protection** di GitHub (*Settings → Branches*) agar pull request hanya bisa di-merge jika CI hijau dan sudah di-review.

✅ **Cek pemahaman:** Buat PR yang sengaja membuat satu tes gagal, lalu lihat CI menjadi merah. Perbaiki dan lihat CI kembali hijau.

---

## Langkah 8: Deploy dengan Docker

🎯 **Tujuan:** Mengemas aplikasi agar berjalan sama persis di komputer mana pun, dan siap dipakai tim.

📖 **Konsep:** **Docker** seperti **kontainer pengiriman**: aplikasi dan semua kebutuhannya dikemas jadi satu, sehingga "di laptop saya jalan" juga berarti "di server jalan".

Di produksi, jangan pakai `python app.py` (server pengembangan). Pakai server produksi seperti **gunicorn**.

🛠️ **Praktik:** Buat `projects/ruang-rapat/backend/Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Simpan database di volume agar data tidak hilang saat kontainer diganti
VOLUME /app/data
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app('/app/data/bookings.db')"]
```

Bangun dan jalankan:

```bash
docker build -t ruang-rapat-api .
```

```bash
docker run -p 8000:8000 -v ruang-rapat-data:/app/data ruang-rapat-api
```

Untuk frontend, jalankan `npm run build`. Hasilnya adalah file statis di `frontend/dist/` yang bisa disajikan oleh web server mana pun (mis. Nginx).

**Daftar periksa sebelum rilis ke tim:**
- [ ] Mode debug mati, server produksi (gunicorn) dipakai
- [ ] Rahasia dibaca dari environment, bukan dari file di image
- [ ] Database punya **backup** terjadwal
- [ ] Ada **log** untuk melacak error
- [ ] Ada login dan hak akses (Langkah 4)
- [ ] Tim IT/keamanan perusahaan sudah meninjau dan menyetujui
- [ ] Ada panduan singkat untuk pengguna

⚠️ **Kesalahan umum:** Men-deploy aplikasi internal ke internet publik tanpa izin tim IT. Selalu ikuti kebijakan infrastruktur perusahaan.

✅ **Cek pemahaman:** Aplikasi berjalan di Docker, dan data booking **tetap ada** setelah kontainer dihentikan lalu dijalankan ulang.

---

## Langkah 9: Berpikir Seperti Arsitek

🎯 **Tujuan:** Mengambil keputusan teknis yang tepat **sebelum** menulis kode.

📖 **Konsep: pilih alat yang paling sederhana yang cukup**

| Kebutuhan | Solusi paling sederhana |
|-----------|-------------------------|
| Satu orang, sesekali, data kecil | Rumus Excel / Google Sheets |
| Satu orang, rutin, aturan rumit | **Skrip Python** (Level 1–2) |
| Beberapa orang, data bersama, perlu riwayat | **Aplikasi web + database** (Level 3) |
| Ribuan pengguna, kritis bagi bisnis | Proyek tim IT dengan arsitektur penuh |

**Pertanyaan wajib sebelum membangun:**
1. **Masalahnya apa**, dan berapa biayanya sekarang (jam kerja, kesalahan, risiko)?
2. **Siapa penggunanya**, berapa orang, dan seberapa sering?
3. **Data apa** yang disimpan? Ada data pribadi? (UU PDP)
4. **Apa jadinya jika aplikasi mati** satu hari? Satu minggu?
5. **Siapa yang merawat** aplikasi ini setelah Anda pindah tugas?

🛠️ **Praktik: tulis catatan keputusan (*Architecture Decision Record*)**

```
Bantu saya menulis Architecture Decision Record (ADR) untuk aplikasi ruang rapat:
konteks, pilihan yang dipertimbangkan (Google Sheets, skrip, aplikasi web),
keputusan, alasan, dan konsekuensinya. Maksimal 1 halaman, Bahasa Indonesia.
```

Simpan sebagai `docs/adr/001-aplikasi-ruang-rapat.md`. Enam bulan lagi, Anda (atau penerus Anda) akan berterima kasih.

✅ **Cek pemahaman:** Untuk salah satu pekerjaan berulang yang Anda catat di Level 1, tentukan solusi paling sederhana yang cukup, dan jelaskan alasannya.

---

## Langkah 10: Menjadi AI Champion di Organisasi

🎯 **Tujuan:** Menyebarkan kemampuan vibe coding ke tim, dengan aman dan terukur.

📖 **Konsep:** "Hero" bukan hanya orang yang paling jago, tetapi orang yang **membuat orang lain ikut bisa**.

🛠️ **Praktik**

**1. Jalankan workshop internal** memakai materi ini:

| Sesi | Durasi | Isi |
|------|--------|-----|
| 1 | 2 jam | Level 1, Langkah 1–5: pola pikir, alat, prompt R-C-T-C-O |
| 2 | 2 jam | Level 1, Langkah 6–10: studi kasus + verifikasi + Git |
| 3 | 2 jam | Studi kasus sesuai fungsi peserta (modul 01–10) |
| 4 | 2 jam | Presentasi proyek akhir peserta + umpan balik |

**2. Usulkan kebijakan pemakaian AI** ke manajemen, minimal berisi:
- **Klasifikasi data:** publik / internal / rahasia / data pribadi, dan mana yang **boleh** masuk ke alat AI
- **Alat yang disetujui** (mis. Claude dengan akun perusahaan)
- **Wajib review manusia** untuk kode yang dipakai dalam keputusan bisnis
- **Siapa pemilik** setiap aplikasi buatan karyawan, dan siapa yang merawatnya

**3. Bangun perpustakaan bersama** di satu repositori tim:
- Prompt R-C-T-C-O yang terbukti berhasil, per fungsi bisnis
- Custom slash command dan skill tim (Langkah 5)
- Modul studi kasus baru dari proyek peserta

**4. Ukur dampaknya.** Contoh format laporan:

| Alat | Fungsi | Waktu sebelum | Waktu sesudah | Hemat / bulan | Kesalahan berkurang |
|------|--------|---------------|---------------|---------------|---------------------|
| Rekonsiliasi bank | Akuntansi | 6 jam | 1 jam | 20 jam | Ya |
| Cek kontrak | Legal | 3 jam | 15 menit | 11 jam | Tidak ada tenggat terlewat |

**5. Mentoring.** Saat meninjau pekerjaan rekan, ajukan pertanyaan, bukan langsung memberi jawaban: *"Bagaimana kamu memverifikasi angka ini?"* *"Apa yang terjadi jika datanya kosong?"*

✅ **Cek pemahaman:** Ajari minimal **2 rekan kerja** sampai mereka lulus Checklist Level 1.

---

## 🏆 Proyek Akhir (Capstone) Level 3

**Tujuan:** Membangun **aplikasi web multi-pengguna** untuk satu proses bisnis nyata, dari ide sampai siap dipakai tim.

**Pilih satu tema** (atau usulkan sendiri):

| Fungsi | Ide aplikasi | Modul dasar |
|--------|--------------|-------------|
| HR | Pengajuan & persetujuan cuti online (karyawan → atasan → HR) | [03-hr](../modules/03-hr/) |
| Keuangan | Pengajuan & persetujuan anggaran per departemen | [02-finance](../modules/02-finance/) |
| Pengadaan | Portal perbandingan penawaran vendor dengan skor otomatis | [08-procurement](../modules/08-procurement/) |
| Layanan Pelanggan | Dashboard tiket dengan triase hibrida (aturan + Claude API) | [09-customer-service](../modules/09-customer-service/) |
| Legal | Register kontrak dengan pengingat tenggat otomatis | [07-legal](../modules/07-legal/) |
| General Affairs | Pemesanan ruang rapat lengkap dengan login dan peran admin | [10-general-affairs](../modules/10-general-affairs/) |

**Wajib ada:**
1. **ADR** (Langkah 9): mengapa aplikasi web, dan bukan solusi lain
2. **Backend API** dengan database, validasi, dan aturan bisnis (Langkah 2)
3. **Frontend** yang mudah dipakai dan aksesibel (Langkah 3)
4. **Login dan minimal 2 peran** (mis. staf & admin) dengan hak akses berbeda (Langkah 4)
5. **Tes otomatis** untuk aturan bisnis, validasi, hak akses, dan keamanan
6. **Hasil `/security-review`** yang temuannya sudah ditindaklanjuti
7. **CI** yang hijau (Langkah 7)
8. **Dockerfile** dan panduan deploy (Langkah 8)
9. **README** untuk pengguna dan untuk pengembang berikutnya, serta **`CLAUDE.md`** proyek
10. **Demo** 15 menit ke calon pengguna, lalu kumpulkan umpan baliknya

**Kriteria lulus:**
- [ ] Minimal 3 orang nyata mencoba aplikasi dan memberi umpan balik
- [ ] Semua tes dan CI lulus; tidak ada temuan keamanan tingkat tinggi yang terbuka
- [ ] Tidak ada data pribadi asli atau rahasia di repositori
- [ ] Orang lain bisa menjalankan aplikasi hanya dengan mengikuti README
- [ ] Dampak terukur (waktu dihemat / kesalahan berkurang) sudah dihitung

---

## ✅ Checklist "Hero"

- [ ] Saya bisa menjelaskan arsitektur 3 lapis dan memilih solusi paling sederhana yang cukup
- [ ] Saya bisa membangun API dengan database, validasi, dan tes otomatis
- [ ] Saya bisa membangun frontend React yang terhubung ke API dan aksesibel
- [ ] Saya bisa mengenali dan mencegah SQL injection, XSS, kebocoran rahasia, dan masalah hak akses
- [ ] Saya memakai custom command, skill, subagent, hooks, dan permissions di Claude Code
- [ ] Saya bisa mengintegrasikan Claude API dengan aman: validasi output, biaya, dan data pribadi
- [ ] Repositori saya punya CI yang memblokir perubahan yang merusak
- [ ] Saya bisa mengemas dan menjalankan aplikasi dengan Docker
- [ ] Saya mendokumentasikan keputusan penting dalam ADR
- [ ] Saya sudah mengajari rekan kerja dan membantu menyusun kebijakan pemakaian AI
- [ ] Proyek capstone saya dipakai oleh orang lain

---

## 🎓 Selamat, Anda Sudah Menjadi Hero!

Perjalanan Anda: dari **tidak pernah membuka terminal**, sampai **membangun aplikasi yang aman, teruji, dan dipakai tim**, serta **mengajari orang lain**.

**Langkah selanjutnya:**
- Perdalam satu stack: **Python** (FastAPI, Django), **PHP** (Laravel), atau **JavaScript** (Next.js)
- Pelajari database produksi: **PostgreSQL**, migrasi skema, backup & restore
- Kontribusikan modul baru ke repositori ini untuk fungsi bisnis yang belum ada

**Referensi:**
- Claude Code: https://code.claude.com/docs
- Claude API: https://platform.claude.com/docs
- Python: https://docs.python.org/3/tutorial/
- Flask: https://flask.palletsprojects.com/
- React: https://react.dev/learn
- OWASP Top 10: https://owasp.org/Top10/
- UU PDP No. 27/2022: https://peraturan.bpk.go.id/ (cari "UU 27 tahun 2022")

← [Kembali ke Peta Belajar](README.md)
