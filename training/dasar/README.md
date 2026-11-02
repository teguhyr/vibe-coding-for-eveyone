# 📘 Paket Materi Modul — Level 1: Dasar

Paket ini berisi **materi lengkap** untuk [Rencana Training Level 1: Dasar](../01-dasar.md). Setiap **Langkah** di rencana training punya **satu modul** dengan penjelasan yang lebih dalam, praktik terpandu, latihan bertingkat, kuis, dan kunci jawaban.

| | |
|---|---|
| **Peserta** | Pemula total dari semua fungsi bisnis (operasional, keuangan, HR, marketing, IT, akuntansi, legal, pengadaan, layanan pelanggan, GA) |
| **Total waktu** | ± 12 jam: 4 sesi tatap muka × 2 jam + ± 4 jam latihan mandiri |
| **Bahasa** | Materi dalam Bahasa Indonesia; nama perintah dan istilah teknis tetap asli |

---

## Daftar Modul

| Modul | Judul | Langkah di rencana | Sesi | Durasi |
|-------|-------|--------------------|------|--------|
| [Modul 1](modul-01-pola-pikir.md) | Memahami Vibe Coding & Pola Pikir yang Benar | Langkah 1 | Sesi 1 | 20 menit |
| [Modul 2](modul-02-menyiapkan-alat.md) | Menyiapkan Alat Kerja | Langkah 2 | Pra-sesi + Sesi 1 | 60 menit (mandiri) + 15 menit |
| [Modul 3](modul-03-terminal.md) | Mengenal Terminal | Langkah 3 | Sesi 1 | 15 menit |
| [Modul 4](modul-04-claude-code-pertama.md) | Percakapan Pertama dengan Claude Code | Langkah 4 | Sesi 1 | 25 menit |
| [Modul 5](modul-05-prompt-rctco.md) | Rumus Prompt R-C-T-C-O | Langkah 5 | Sesi 1 | 30 menit |
| [Modul 6](modul-06-membaca-kode.md) | Membaca Kode Tanpa Takut | Langkah 6 | Sesi 2 | 30 menit |
| [Modul 7](modul-07-studi-kasus-operasional.md) | Studi Kasus Pertama: Operasional | Langkah 7 | Sesi 2 | 20 menit |
| [Modul 8](modul-08-verifikasi-keuangan.md) | Memverifikasi Hasil: Keuangan | Langkah 8 | Sesi 2 | 25 menit |
| [Modul 9](modul-09-perubahan-kecil.md) | Meminta Perubahan Kecil ke AI | Langkah 9 | Sesi 2 | 25 menit |
| [Modul 10](modul-10-git.md) | Menyimpan Pekerjaan dengan Git | Langkah 10 | Sesi 2 | 20 menit |
| [Proyek Akhir](proyek-akhir.md) | Saran Jumlah Pesan + rubrik penilaian | Proyek Akhir Level 1 | Sesi 3–4 | 4 jam |
| [Evaluasi](evaluasi.md) | Pre-test / post-test + umpan balik | Checklist Kelulusan | Awal Sesi 1 & akhir Sesi 4 | 2 × 10 menit |

**Untuk fasilitator/trainer:** [Panduan Fasilitator](panduan-fasilitator.md) berisi persiapan, rundown menit demi menit, dan solusi masalah umum.

---

## Jadwal Pelaksanaan (2 Minggu)

```
 MINGGU 1                                      MINGGU 2
 ─────────────────────────────────────────     ─────────────────────────────────────────
 Pra-sesi   Sesi 1 (2 jam)   Sesi 2 (2 jam)    Mandiri    Sesi 3 (2 jam)   Sesi 4 (2 jam)
 Instalasi  Modul 1–5        Modul 6–10        Latihan +  Studi kasus +    Presentasi
 (Modul 2)  + pre-test                         proyek     proyek akhir     + post-test
```

| Sesi | Isi | Hasil di akhir sesi |
|------|-----|---------------------|
| **Pra-sesi** (mandiri, H-3) | Modul 2: instalasi semua alat | Ketiga perintah cek versi berhasil |
| **Sesi 1** | Pre-test, Modul 1, 2 (verifikasi), 3, 4, 5 | Peserta bisa membuka Claude Code dan menulis prompt R-C-T-C-O pertama |
| **Sesi 2** | Modul 6, 7, 8, 9, 10 | Peserta sudah mengubah program lewat prompt dan menyimpannya dengan Git |
| **Mandiri** | Latihan bintang ⭐⭐⭐ dari tiap modul, mulai Proyek Akhir | Draf prompt proyek akhir |
| **Sesi 3** | Klinik proyek akhir, studi kasus sesuai fungsi peserta | Proyek akhir berjalan dan terverifikasi |
| **Sesi 4** | Presentasi proyek, post-test, umpan balik | Peserta lulus Checklist Level 1 |

---

## Struktur Setiap Modul

| Bagian | Isi |
|--------|-----|
| 🎯 **Tujuan Pembelajaran** | Kemampuan yang dicapai peserta setelah modul |
| 📖 **Materi** | Penjelasan konsep dengan analogi dan contoh dari dunia kerja |
| 🛠️ **Praktik Terpandu** | Langkah demi langkah, dikerjakan bersama fasilitator |
| 🏋️ **Latihan** | ⭐ mudah, ⭐⭐ sedang, ⭐⭐⭐ tantangan (untuk latihan mandiri) |
| 📝 **Kuis** | 3–5 soal singkat untuk mengecek pemahaman |
| 📌 **Ringkasan** | Poin penting yang harus diingat |
| 🔑 **Kunci Jawaban** | Tersembunyi; klik untuk membuka setelah mencoba sendiri |

---

## File Latihan

Folder [`latihan/`](latihan/) berisi file untuk praktik:

| File | Dipakai di |
|------|-----------|
| `latihan/penjualan.py` | Modul 6: program pertama yang dibaca dan diubah |
| `latihan/data/penjualan_cabang.csv` | Modul 6: latihan ⭐⭐⭐ membaca CSV (data fiktif) |
| `latihan/kunci/penjualan_titik.py` | Kunci Latihan 6.2 & 6.3 |
| `latihan/kunci/penjualan_csv.py` | Kunci Latihan 6.4 |

Semua data di paket ini **fiktif**. Lihat aturan keamanan data di [peta belajar](../README.md#-aturan-emas-keamanan-data-berlaku-di-semua-level).

---

**Mulai dari [Modul 1: Memahami Vibe Coding →](modul-01-pola-pikir.md)**
