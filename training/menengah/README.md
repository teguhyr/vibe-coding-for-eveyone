# 📘 Paket Materi Modul — Level 2: Menengah

Paket ini berisi **materi lengkap** untuk [Rencana Training Level 2: Menengah](../02-menengah.md). Setiap **Langkah** di rencana training punya **satu modul** dengan penjelasan yang lebih dalam, praktik terpandu, latihan bertingkat, kuis, dan kunci jawaban.

| | |
|---|---|
| **Peserta** | Lulusan [Level 1: Dasar](../dasar/README.md) dari semua fungsi bisnis |
| **Total waktu** | ± 25 jam: 8 sesi tatap muka × 2 jam + ± 9 jam latihan mandiri, dalam 4 minggu |
| **Bahasa** | Materi dalam Bahasa Indonesia; kode, nama perintah, dan istilah teknis tetap asli |
| **Hasil akhir** | Alat otomatisasi dari pekerjaan peserta sendiri, lengkap dengan tes, README, dan data sintetis |

---

## Daftar Modul

| Modul | Judul | Langkah di rencana | Sesi | Durasi |
|-------|-------|--------------------|------|--------|
| [Modul 1](modul-01-anatomi-program.md) | Membaca Anatomi Program Buatan AI | Langkah 1 | Sesi 1 | 35 menit |
| [Modul 2](modul-02-pytest.md) | Tes Otomatis dengan pytest | Langkah 2 | Sesi 1 | 70 menit |
| [Modul 3](modul-03-debugging.md) | Debugging Bersama AI | Langkah 3 | Sesi 2 | 50 menit |
| [Modul 4](modul-04-plan-mode.md) | Merencanakan Perubahan Besar (Plan Mode) | Langkah 4 | Sesi 2 | 60 menit |
| [Modul 5](modul-05-linter-formatter.md) | Kode yang Rapi: Linter & Formatter | Langkah 5 | Sesi 3 | 25 menit |
| [Modul 6](modul-06-sqlite.md) | Database & SQL dengan SQLite | Langkah 6 | Sesi 3 | 85 menit |
| [Modul 7](modul-07-claude-md.md) | CLAUDE.md: "SOP" untuk Asisten AI Anda | Langkah 7 | Sesi 4 | 35 menit |
| [Modul 8](modul-08-branch-review.md) | Branch, Review, dan Kolaborasi | Langkah 8 | Sesi 4 | 45 menit |
| [Modul 9](modul-09-data-aman.md) | Data Asli dengan Aman | Langkah 9 | Sesi 4 | 30 menit |
| [Modul 10](modul-10-studi-kasus-lintas-fungsi.md) | Studi Kasus Lintas Fungsi | Langkah 10 | Sesi 5 (+ mandiri) | 110 menit |
| [Proyek Akhir](proyek-akhir.md) | Alat otomatisasi dari pekerjaan sendiri + rubrik | Proyek Akhir Level 2 | Sesi 6–8 | ± 10 jam (termasuk mandiri) |
| [Evaluasi](evaluasi.md) | Pre-test / post-test + umpan balik | Checklist Kelulusan | Awal Sesi 1 & Sesi 8 | 2 × 10 menit |

**Untuk fasilitator/trainer:** [Panduan Fasilitator](panduan-fasilitator.md) berisi persiapan, rundown menit demi menit untuk 8 sesi, dan solusi masalah umum.

---

## Jadwal Pelaksanaan (4 Minggu)

```
 MINGGU 1                 MINGGU 2                 MINGGU 3                 MINGGU 4
 ──────────────────────   ──────────────────────   ──────────────────────   ──────────────────────
 Sesi 1      Sesi 2       Sesi 3      Sesi 4       Sesi 5      Sesi 6       Sesi 7      Sesi 8
 Pre-test    Modul 3–4    Modul 5–6   Modul 7–9    Modul 10    Proyek:      Proyek:     Presentasi
 Modul 1–2   Debug, Plan  ruff, SQL   CLAUDE.md,   Studi kasus perencanaan  klinik      + post-test
 Anatomi,tes                          branch, data
```

| Sesi | Isi | Hasil di akhir sesi |
|------|-----|---------------------|
| **Sesi 1** | Pre-test, Modul 1, 2 | Peserta bisa memetakan program dan menulis tes kasus tepi |
| **Sesi 2** | Modul 3, 4 | Peserta menemukan bug lewat tes dan mengerjakan fitur dari rencana Plan Mode |
| **Sesi 3** | Modul 5, 6 | Kode lulus ruff; peserta menulis query SQL dengan parameter `?` |
| **Sesi 4** | Modul 7, 8, 9 | Proyek sendiri punya `CLAUDE.md`, fitur di-merge lewat branch + review, data asli terlindungi |
| **Sesi 5** | Modul 10 | 1–2 kasus lintas fungsi selesai dengan alur lengkap |
| **Mandiri** | Latihan ⭐⭐⭐, minimal 3 kasus Modul 10, kanvas proyek | Kanvas masalah proyek akhir terisi |
| **Sesi 6** | Proyek akhir: kanvas, data sintetis, rencana, tes dulu | Rencana dan daftar tes disetujui pasangan |
| **Sesi 7** | Proyek akhir: klinik implementasi dan review | Proyek lulus `pytest` + ruff, sudah di-review |
| **Sesi 8** | Presentasi, post-test, umpan balik | Peserta lulus Checklist Level 2 |

---

## Struktur Setiap Modul

| Bagian | Isi |
|--------|-----|
| 🎯 **Tujuan Pembelajaran** | Kemampuan yang dicapai peserta setelah modul |
| 📖 **Materi** | Penjelasan konsep dengan analogi dan contoh dari dunia kerja |
| 🛠️ **Praktik Terpandu** | Langkah demi langkah, dikerjakan bersama fasilitator |
| 🏋️ **Latihan** | ⭐ mudah, ⭐⭐ sedang, ⭐⭐⭐ tantangan (untuk latihan mandiri) |
| 📝 **Kuis** | 4–5 soal singkat untuk mengecek pemahaman |
| 📌 **Ringkasan** | Poin penting yang harus diingat |
| 🔑 **Kunci Jawaban** | Tersembunyi; klik untuk membuka setelah mencoba sendiri |

---

## File Latihan

Folder [`latihan/`](latihan/) berisi file untuk praktik. Semua perintah di materi dijalankan dari **folder utama repositori**.

| File | Dipakai di |
|------|-----------|
| `latihan/expense_claims.py` | Modul 1, 2, 7, 8: pemeriksa klaim reimburse (program utama Level 2, juga contoh referensi proyek akhir) |
| `latihan/test_expense_claims.py` | Modul 2: tes awal yang Anda lengkapi |
| `latihan/data/klaim_reimburse.csv` | Modul 1, 2, 6: 8 klaim fiktif yang memuat setiap aturan dan kasus tepi |
| `latihan/data/klaim_rusak.csv` | Modul 3: data dengan 3 kesalahan untuk latihan debugging |
| `latihan/overtime_pay.py` | Modul 3: kalkulator lembur yang **sengaja berisi bug** |
| `latihan/test_overtime_pay.py` | Modul 3: tes yang **sengaja gagal** 1 dari 4 sampai bug diperbaiki |
| `latihan/data/lembur_oktober.csv` | Modul 3, 9: data lembur fiktif |
| `latihan/kunci/test_expense_claims_kunci.py` | Kunci Latihan 2.2–2.4 (`kunci/conftest.py` membuatnya bisa mengimpor `expense_claims.py`) |
| `latihan/kunci/claims_sqlite.py` | Kunci Latihan 6.2–6.3 |
| `latihan/kunci/sqlite_lanjutan.py` | Kunci Latihan 6.4 (JOIN data HR, GROUP BY data keuangan) |
| `latihan/kunci/reconcile_sqlite.py` | Kunci Kasus 4 Modul 10 (rekonsiliasi bank dengan SQL) |

Perintah cek cepat:

```bash
pytest training/menengah/latihan/test_expense_claims.py training/menengah/latihan/kunci
```

Semua lulus. Untuk `test_overtime_pay.py`, hasil **`1 failed, 3 passed`** adalah keadaan awal yang benar sampai Anda memperbaiki bug di Modul 3.

> 💡 File latihan **tidak** ikut dijalankan oleh `pytest` tanpa argumen (yang hanya menguji folder `modules/`), tetapi tetap diperiksa oleh `ruff check .`.

Semua data di paket ini **fiktif**. Lihat aturan keamanan data di [peta belajar](../README.md#-aturan-emas-keamanan-data-berlaku-di-semua-level) dan [Modul 9](modul-09-data-aman.md).

---

**Mulai dari [Modul 1: Membaca Anatomi Program Buatan AI →](modul-01-anatomi-program.md)**
