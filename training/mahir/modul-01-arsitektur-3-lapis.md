# Modul 1: Dari Skrip ke Aplikasi: Arsitektur 3 Lapis

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 1](../03-mahir.md#langkah-1-dari-skrip-ke-aplikasi-arsitektur-3-lapis) |
| **Sesi** | Sesi 1 |
| **Durasi** | 105 menit |
| **Prasyarat** | Lulus Level 2; `curl` tersedia di terminal (sudah ada di Windows 10+, macOS, dan Linux) |
| **File latihan** | [`latihan/ruang-rapat/backend/app.py`](latihan/ruang-rapat/backend/app.py), [`modules/10-general-affairs/`](../../modules/10-general-affairs/) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menentukan kapan sebuah skrip perlu "naik kelas" menjadi aplikasi.
2. Menjelaskan tugas **frontend**, **backend**, dan **database**, dan mengapa aturan bisnis wajib ada di backend.
3. Membaca satu **permintaan dan balasan HTTP**: metode, alamat, header, isi, dan kode status.
4. Mengirim permintaan ke API dengan `curl` dan membaca balasan JSON-nya.
5. Merancang daftar *endpoint* untuk satu proses bisnis.

---

## 📖 Materi

### A. Kapan skrip tidak cukup lagi?

| Tanda | Contoh |
|-------|--------|
| **Banyak orang** memakai alat yang sama | 10 tim memesan ruang rapat |
| Butuh **data bersama** yang selalu terbaru | Semua orang harus melihat jadwal yang sama, saat itu juga |
| Ada **aturan yang harus ditegakkan saat input**, bukan diperiksa belakangan | Bentrok jadwal harus **ditolak**, bukan dilaporkan besok |
| Pengguna **bukan programmer** | Staf ingin memakai browser, bukan terminal |
| Butuh **hak akses berbeda** | Staf memesan, admin GA boleh menghapus pesanan siapa pun |

Skrip `modules/10-general-affairs/room_booking.py` di Level 1–2 **mendeteksi** bentrok setelah terjadi. Aplikasi di Level 3 **mencegah** bentrok saat orang memesan.

### B. Tiga lapis, seperti restoran

```
  ┌────────────────────┐      ┌────────────────────┐      ┌────────────────────┐
  │  FRONTEND          │ HTTP │  BACKEND (API)     │ SQL  │  DATABASE          │
  │  "Ruang makan"     │ ───▶ │  "Dapur"           │ ───▶ │  "Gudang bahan"    │
  │  React di browser  │ ◀─── │  Flask (Python)    │ ◀─── │  SQLite/PostgreSQL │
  │  Form, tabel       │ JSON │  Aturan bisnis     │      │  Data tersimpan    │
  └────────────────────┘      └────────────────────┘      └────────────────────┘
```

| Lapis | Tugasnya | **Bukan** tugasnya |
|-------|----------|--------------------|
| Frontend (ruang makan) | Menampilkan menu, menerima pesanan, memberi tahu jika pesanan ditolak | Memutuskan pesanan sah atau tidak |
| Backend (dapur) | Memeriksa pesanan, menerapkan aturan, mengambil dan menyimpan bahan | Menghias meja |
| Database (gudang) | Menyimpan data dengan aman dan rapi | Memutuskan aturan bisnis |

> ⚠️ **Aturan emas:** semua validasi dan aturan bisnis **wajib** ada di backend. Frontend boleh memeriksa juga (agar pengguna cepat tahu kesalahannya), tetapi frontend berjalan di komputer pengguna dan **bisa dilewati**. Siapa pun bisa mengirim permintaan langsung ke backend dengan `curl`, seperti yang akan Anda lakukan di modul ini.

### C. HTTP: bahasa antara frontend dan backend

Setiap interaksi adalah **satu permintaan** (*request*) dan **satu balasan** (*response*), seperti formulir yang diserahkan ke loket.

**Permintaan:**

```
POST /api/bookings HTTP/1.1                ← metode + alamat
Content-Type: application/json             ← header: "isi saya berformat JSON"

{"room": "Merapi", "booked_by": "Tim HR",  ← isi (body)
 "start_at": "2026-11-03T09:00", "end_at": "2026-11-03T10:00"}
```

**Balasan:**

```
HTTP/1.1 201 CREATED                        ← kode status
Content-Type: application/json

{"id": 1, "room": "Merapi", ...}            ← isi balasan
```

| Metode | Arti | Contoh |
|--------|------|--------|
| `GET` | Ambil data (tidak mengubah apa pun) | Daftar booking |
| `POST` | Buat data baru | Booking baru |
| `PUT` / `PATCH` | Ubah data yang ada | Ganti jam booking |
| `DELETE` | Hapus data | Batalkan booking |

| Kode | Kelompok | Arti |
|------|----------|------|
| `200`, `201`, `204` | 2xx: berhasil | OK / dibuat / berhasil tanpa isi balasan |
| `400`, `401`, `403`, `404`, `409` | 4xx: **kesalahan peminta** | Data salah / belum login / tidak berhak / tidak ditemukan / bentrok |
| `500` | 5xx: **kesalahan server** | Bug di backend |

> 💡 Cara mudah mengingat: **4xx = salah pengirim, 5xx = salah server.** Jika aplikasi Anda membalas 500 untuk data yang salah, itu bug: seharusnya 400.

### D. JSON: format pertukaran data

JSON mirip dictionary dan list Python:

```json
[
  {"id": 1, "room": "Merapi", "booked_by": "Tim HR", "start_at": "2026-11-03T09:00", "end_at": "2026-11-03T10:00"}
]
```

`[ ]` = daftar, `{ }` = objek dengan pasangan `"kunci": nilai`. Teks selalu memakai tanda kutip ganda.

### E. Alamat lokal dan port

`http://127.0.0.1:5000` berarti "komputer ini sendiri, pintu nomor 5000". Backend Flask mendengarkan di port 5000; nanti frontend React di port 5173. Alamat `127.0.0.1` (atau `localhost`) hanya bisa dibuka dari komputer Anda sendiri.

---

## 🛠️ Praktik Terpandu

**1. Siapkan lingkungan.** Dari folder utama repositori, dengan `.venv` aktif:

```bash
pip install -r training/mahir/latihan/ruang-rapat/backend/requirements.txt
```

**2. Jalankan backend contoh.** Ini adalah API yang akan Anda bangun sendiri di Modul 2.

```bash
cd training/mahir/latihan/ruang-rapat/backend
```

```bash
python app.py
```

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

Biarkan terminal ini terbuka. Perhatikan peringatannya: ini **server pengembangan**, bukan untuk produksi (Modul 8).

**3. Ambil data (GET).** Buka **terminal kedua**:

```bash
curl http://127.0.0.1:5000/api/bookings
```

```
[]
```

Daftar masih kosong. Anda juga bisa membuka alamat yang sama di browser.

**4. Kirim data (POST).** Agar mudah di semua sistem operasi, simpan isi permintaan di file. Di terminal kedua (masih di folder `backend`), buat file `booking.json`:

```json
{"room": "Merapi", "booked_by": "Tim HR", "start_at": "2026-11-03T09:00", "end_at": "2026-11-03T10:00"}
```

Lalu kirim. Opsi `-i` menampilkan kode status dan header balasan:

```bash
curl -i -X POST http://127.0.0.1:5000/api/bookings -H "Content-Type: application/json" -d @booking.json
```

```
HTTP/1.1 201 CREATED
Server: Werkzeug/3.1.9 Python/3.13.18
Content-Type: application/json
...

{
  "end_at": "2026-11-03T10:00",
  "id": 1,
  "room": "Merapi",
  "start_at": "2026-11-03T09:00"
}
```

Di Windows PowerShell, tulis `curl.exe` (bukan `curl`) agar yang dipakai adalah program curl asli.

**5. Kirim lagi permintaan yang sama.**

```
HTTP/1.1 409 CONFLICT
...
{
  "error": "Bentrok dengan booking #1"
}
```

Backend **menolak** bentrok. Inilah perbedaan utama dengan skrip modul 10.

**6. Coba data yang salah.** Kirim hanya ruangnya:

```bash
curl -X POST http://127.0.0.1:5000/api/bookings -H "Content-Type: application/json" -d "{\"room\": \"Merapi\"}"
```

```
{
  "error": "Wajib diisi: room, booked_by, start_at, end_at (format ISO)"
}
```

Kode statusnya 400. Lihat dengan menambahkan `-i`. Jika tanda kutip di PowerShell menyulitkan, simpan `{"room": "Merapi"}` di file seperti langkah 4 dan kirim dengan `-d @namafile.json`.

**7. Bersihkan.** Hentikan server dengan `Ctrl+C`. Hapus `booking.json` dan `bookings.db` dari folder `backend`. `bookings.db` sudah diabaikan Git (aturan `*.db`), tetapi `booking.json` tidak, jadi jangan sampai ikut ter-commit.

---

## 🏋️ Latihan

### ⭐ Latihan 1.1: Lapis mana?

Untuk setiap tugas, tentukan lapisnya (frontend, backend, atau database):

1. Menampilkan pesan "Booking berhasil disimpan" dengan warna hijau
2. Menolak booking yang jam selesainya sebelum jam mulai
3. Menyimpan booking secara permanen
4. Menampilkan pilihan ruang dalam bentuk *dropdown*
5. Memastikan hanya admin yang boleh menghapus booking orang lain
6. Mempercepat pencarian booking per ruang dengan *index*

### ⭐⭐ Latihan 1.2: Tebak kode statusnya

Tanpa menjalankan, tebak kode status untuk setiap permintaan ke API contoh (sudah ada booking Merapi 09:00–10:00):

1. `GET /api/bookings`
2. `POST` booking Merapi 10:00–11:00
3. `POST` booking Merapi 09:30–10:30
4. `POST` booking Bromo 09:00–10:00
5. `POST` booking tanpa `booked_by`
6. `GET /api/rooms` (alamat yang tidak ada)

Lalu periksa dengan `curl`.

### ⭐⭐ Latihan 1.3: Rancang endpoint

Rancang daftar *endpoint* untuk aplikasi **pengajuan cuti** (karyawan mengajukan, atasan menyetujui atau menolak). Untuk setiap endpoint, tulis: metode, alamat, siapa yang boleh memanggilnya, dan kode status untuk kasus berhasil dan gagal.

### ⭐⭐⭐ Latihan 1.4: Skrip atau aplikasi?

Ambil 3 pekerjaan berulang dari daftar Anda di Level 1. Untuk masing-masing, tentukan apakah cukup skrip (Level 1–2) atau perlu aplikasi (Level 3), memakai tabel di bagian A sebagai alasan.

---

## 📝 Kuis

1. Mengapa validasi tidak cukup dilakukan di frontend saja?
2. Apa beda kode status 4xx dan 5xx?
3. Metode HTTP apa yang dipakai untuk membatalkan booking?
4. Apa arti `http://127.0.0.1:5000`?
5. API membalas `500` saat pengguna mengirim tanggal yang formatnya salah. Apakah ini benar? Kode apa yang seharusnya?

---

## 📌 Ringkasan

- Naik dari skrip ke aplikasi saat ada **banyak pengguna**, **data bersama**, **aturan yang ditegakkan saat input**, dan **hak akses**.
- Frontend = ruang makan, backend = dapur, database = gudang. **Aturan bisnis wajib di backend.**
- HTTP = permintaan (metode, alamat, header, isi) + balasan (kode status, isi). **4xx salah pengirim, 5xx salah server.**
- `curl` adalah cara tercepat menguji API, dan sekaligus bukti bahwa frontend bisa dilewati.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 1.1**
1. Frontend
2. **Backend** (frontend boleh ikut memeriksa demi kenyamanan, tetapi backend yang menentukan)
3. Database
4. Frontend
5. **Backend**: hak akses harus dicek di server pada setiap permintaan
6. Database

**Latihan 1.2**
1. `200`
2. `201`: berurutan (10:00 tepat saat booking lain selesai) tidak bentrok
3. `409`: tumpang tindih 09:30–10:00
4. `201`: ruang berbeda
5. `400`
6. `404`: alamat tidak ada (Flask otomatis membalas 404)

**Latihan 1.3 (contoh)**

| Metode | Alamat | Siapa | Berhasil | Gagal |
|--------|--------|-------|----------|-------|
| `GET` | `/api/leave-requests` | Karyawan (miliknya), atasan (timnya), HR (semua) | 200 | 401 belum login |
| `POST` | `/api/leave-requests` | Karyawan | 201 | 400 tanggal salah/sisa cuti kurang, 401 |
| `POST` | `/api/leave-requests/<id>/approve` | Atasan langsung | 200 | 403 bukan atasannya, 404, 409 sudah diputuskan |
| `POST` | `/api/leave-requests/<id>/reject` | Atasan langsung | 200 | 403, 404, 409 |
| `DELETE` | `/api/leave-requests/<id>` | Pemilik, selama masih pending | 204 | 403, 404, 409 sudah disetujui |

Ciri rancangan yang baik: hak akses ditulis per endpoint, dan ada kode untuk kasus "sudah diputuskan" (409), bukan hanya kasus berhasil.

**Latihan 1.4:** jawaban berbeda tiap peserta. Yang dinilai: alasannya memakai kriteria bagian A (jumlah pengguna, data bersama, penegakan aturan saat input, hak akses), dan pilihan **paling sederhana** yang cukup (lihat juga Modul 9).

**Kuis**
1. Frontend berjalan di komputer pengguna dan bisa dilewati; siapa pun bisa mengirim permintaan langsung ke backend (misalnya dengan `curl`).
2. 4xx = kesalahan peminta (data salah, belum login, tidak berhak); 5xx = kesalahan di server (bug).
3. `DELETE`.
4. Komputer ini sendiri (`127.0.0.1`), di port 5000. Hanya bisa dibuka dari komputer yang sama.
5. Tidak benar. Format salah adalah kesalahan pengirim, jadi seharusnya `400` dengan pesan yang jelas. `500` berarti ada error yang tidak ditangani di kode.

</details>

---

← [Daftar Modul](README.md) | **Berikutnya: [Modul 2: Membangun API dengan Flask + SQLite →](modul-02-api-flask.md)**
