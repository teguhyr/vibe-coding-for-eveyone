# 📘 Paket Materi Modul — Level 3: Mahir

Paket ini berisi **materi lengkap** untuk [Rencana Training Level 3: Mahir](../03-mahir.md). Setiap **Langkah** di rencana training punya **satu modul** dengan penjelasan yang lebih dalam, praktik terpandu, latihan bertingkat, kuis, dan kunci jawaban.

| | |
|---|---|
| **Peserta** | Lulusan [Level 2: Menengah](../menengah/README.md) dari semua fungsi bisnis |
| **Total waktu** | ± 45 jam: 12 sesi tatap muka × 2 jam + ± 21 jam mandiri (latihan + capstone), dalam 6 minggu (+ cadangan 1–2 minggu untuk uji coba pengguna) |
| **Bahasa** | Materi dalam Bahasa Indonesia; kode, nama perintah, dan istilah teknis tetap asli |
| **Alat tambahan** | Node.js LTS (Modul 3), Docker (Modul 8), akun GitHub dengan Actions (Modul 7), API key Claude dari perusahaan (opsional, Modul 6) |
| **Hasil akhir** | Aplikasi web multi-pengguna (capstone) yang aman, teruji, bisa di-deploy, dan dicoba pengguna nyata |

---

## Daftar Modul

| Modul | Judul | Langkah di rencana | Sesi | Durasi |
|-------|-------|--------------------|------|--------|
| [Modul 1](modul-01-arsitektur-3-lapis.md) | Dari Skrip ke Aplikasi: Arsitektur 3 Lapis | Langkah 1 | Sesi 1 | 105 menit |
| [Modul 2](modul-02-api-flask.md) | Membangun API dengan Flask + SQLite | Langkah 2 | Sesi 2 | 110 menit |
| [Modul 3](modul-03-react.md) | Membangun Tampilan dengan React | Langkah 3 | Sesi 3 | 110 menit |
| [Modul 4](modul-04-keamanan-owasp.md) | Keamanan Aplikasi (OWASP) | Langkah 4 | Sesi 4 | 110 menit |
| [Modul 5](modul-05-claude-code-lanjutan.md) | Fitur Lanjutan Claude Code | Langkah 5 | Sesi 5 | 110 menit |
| [Modul 6](modul-06-claude-api.md) | Integrasi Claude API ke Aplikasi Anda | Langkah 6 | Sesi 6 | 110 menit |
| [Modul 7](modul-07-ci-cd.md) | Otomatisasi Kualitas dengan CI/CD | Langkah 7 | Sesi 7 | 50 menit |
| [Modul 8](modul-08-docker.md) | Deploy dengan Docker | Langkah 8 | Sesi 7 | 60 menit |
| [Modul 9](modul-09-arsitek.md) | Berpikir Seperti Arsitek | Langkah 9 | Sesi 8 | 50 menit |
| [Modul 10](modul-10-ai-champion.md) | Menjadi AI Champion di Organisasi | Langkah 10 | Sesi 8 | 60 menit |
| [Proyek Akhir](proyek-akhir.md) | Capstone: aplikasi web untuk tim + rubrik | Proyek Akhir (Capstone) | Sesi 9–12 | ± 23 jam (termasuk mandiri) |
| [Evaluasi](evaluasi.md) | Pre-test / post-test + umpan balik | Checklist "Hero" | Awal Sesi 1 & Sesi 12 | 2 × 10 menit |

**Untuk fasilitator/trainer:** [Panduan Fasilitator](panduan-fasilitator.md) berisi koordinasi dengan IT, rundown menit demi menit untuk 12 sesi, dan solusi masalah umum.

---

## Jadwal Pelaksanaan (6 Minggu)

```
 MINGGU 1        MINGGU 2        MINGGU 3        MINGGU 4        MINGGU 5        MINGGU 6
 ─────────────   ─────────────   ─────────────   ─────────────   ─────────────   ─────────────
 S1     S2       S3     S4       S5     S6       S7     S8       S9     S10      S11    S12
 Arsit. Flask    React  Keaman. Claude Claude   CI/CD  Arsitek  Caps.  Caps.    Caps.  Demo +
 +pre-  API             OWASP   Code   API      Docker Champion rencana backend  FE+sec post-
 test                           lanjut                                           +Docker test
```

| Sesi | Isi | Hasil di akhir sesi |
|------|-----|---------------------|
| **Sesi 1** | Pre-test, Modul 1 | Peserta mengirim permintaan HTTP dengan `curl` dan membaca balasannya |
| **Sesi 2** | Modul 2 | API booking sendiri lulus tes (201/400/409) |
| **Sesi 3** | Modul 3 | Frontend React terhubung ke API |
| **Sesi 4** | Modul 4 | Peserta menemukan celah keamanan dan memahami login + peran |
| **Sesi 5** | Modul 5 | Proyek peserta punya command, skill, subagent, permissions, dan hook |
| **Sesi 6** | Modul 6 | Klasifikasi hibrida teruji dengan klien palsu |
| **Sesi 7** | Modul 7, 8 | CI hijau di GitHub; backend berjalan di Docker |
| **Sesi 8** | Modul 9, 10 | Draf ADR capstone dan draf usulan kebijakan AI |
| **Sesi 9** | Capstone: perencanaan | ADR, rancangan endpoint, daftar tes |
| **Sesi 10** | Capstone: klinik backend | Backend + tes + CI hijau |
| **Sesi 11** | Capstone: frontend, keamanan, Docker, uji "orang lain" | Siap diuji pengguna |
| **Mandiri** | Uji coba dengan 3 pengguna nyata | Umpan balik tercatat, perbaikan utama selesai |
| **Sesi 12** | Demo, post-test, umpan balik | Peserta lulus Level 3 ("Hero") |

---

## Struktur Setiap Modul

| Bagian | Isi |
|--------|-----|
| 🎯 **Tujuan Pembelajaran** | Kemampuan yang dicapai peserta setelah modul |
| 📖 **Materi** | Penjelasan konsep dengan analogi dan contoh dari dunia kerja |
| 🛠️ **Praktik Terpandu** | Langkah demi langkah, dikerjakan bersama fasilitator |
| 🏋️ **Latihan** | ⭐ mudah, ⭐⭐ sedang, ⭐⭐⭐ tantangan (untuk latihan mandiri) |
| 📝 **Kuis** | 5 soal singkat untuk mengecek pemahaman |
| 📌 **Ringkasan** | Poin penting yang harus diingat |
| 🔑 **Kunci Jawaban** | Tersembunyi; klik untuk membuka setelah mencoba sendiri |

---

## File Latihan

Folder [`latihan/`](latihan/) berisi contoh jadi dan kunci untuk **dibandingkan** dengan pekerjaan Anda di `projects/ruang-rapat/`. Semua perintah dijalankan dari **folder utama repositori**.

| File | Dipakai di |
|------|-----------|
| `latihan/ruang-rapat/backend/app.py`, `test_app.py`, `requirements.txt` | Modul 1–2: API booking (sama dengan contoh di rencana training) |
| `latihan/ruang-rapat/backend/Dockerfile`, `.dockerignore` | Modul 8 |
| `latihan/kunci/backend-lengkap/booking_api.py`, `test_booking_api.py`, `.env.example` | Kunci Modul 2 & 4: DELETE, daftar ruang, login, 2 peran, 14 tes keamanan |
| `latihan/kunci/frontend/BookingApp.tsx` | Kunci Modul 3: tombol Hapus dan pesan saat backend mati |
| `latihan/klasifikasi/hybrid_triage.py`, `test_hybrid_triage.py` | Modul 6: triase hibrida (aturan modul 09 + Claude API), diuji dengan klien palsu |
| `latihan/contoh-claude/` | Modul 5: command, skill, subagent, `settings.json`, dan hook `protect_data.py` |
| `latihan/ci/ci.yml` | Modul 7: workflow GitHub Actions |
| `latihan/kunci/adr/001-aplikasi-ruang-rapat.md` | Modul 9: contoh ADR |

**Persiapan dan cek cepat:**

```bash
pip install -r training/mahir/latihan/ruang-rapat/backend/requirements.txt
```

```bash
pytest training/mahir/latihan/ruang-rapat/backend
```

```bash
pytest training/mahir/latihan/kunci/backend-lengkap
```

```bash
pytest training/mahir/latihan/klasifikasi
```

Hasilnya `6 passed`, `14 passed`, dan `9 passed`. Tes klasifikasi **tidak** membutuhkan SDK `anthropic` maupun API key.

> 💡 File latihan **tidak** ikut dijalankan oleh `pytest` tanpa argumen (yang hanya menguji folder `modules/`), tetapi tetap diperiksa oleh `ruff check .`. Jalankan setiap folder latihan **terpisah** dari proyek Anda sendiri, karena nama file seperti `app.py` dan `test_app.py` akan bentrok jika digabung dalam satu perintah `pytest`.

**Apa yang sudah diuji di paket ini:** semua tes di atas; API contoh dijalankan dengan gunicorn dan `curl` (201 → 409); frontend kunci di-*build* dengan Vite dan diuji di browser (Playwright): simpan, bentrok, hapus, dan pesan saat backend mati; `hybrid_triage.py` mengirim permintaan yang benar lewat SDK `anthropic` ke server tiruan (tanpa biaya API). **Belum** diuji di sini: `docker build` (tanpa Docker daemon), workflow di GitHub Actions sungguhan, panggilan Claude API sungguhan, dan fitur interaktif Claude Code. Fasilitator mencobanya saat persiapan H-1.

Semua data di paket ini **fiktif**. Lihat aturan keamanan data di [peta belajar](../README.md#-aturan-emas-keamanan-data-berlaku-di-semua-level).

---

**Mulai dari [Modul 1: Dari Skrip ke Aplikasi →](modul-01-arsitektur-3-lapis.md)**
