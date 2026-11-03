# ADR 001: Aplikasi Web untuk Pemesanan Ruang Rapat

| | |
|---|---|
| **Status** | Diterima |
| **Tanggal** | 2026-11-03 |
| **Pemilik** | Tim General Affairs (contoh fiktif) |

## Konteks

Pemesanan 3 ruang rapat (Merapi, Bromo, Rinjani) saat ini dicatat di satu file Excel bersama. Sekitar 120 pemesanan per bulan dari 10 tim. Dalam 3 bulan terakhir terjadi 9 kali pemesanan ganda karena dua orang mengedit file pada waktu bersamaan, dan staf GA menghabiskan ± 4 jam per bulan untuk merapikan jadwal. Skrip `modules/10-general-affairs/room_booking.py` bisa **mendeteksi** bentrok, tetapi hanya setelah terjadi dan hanya dijalankan oleh satu orang.

Data yang disimpan: nama tim/pengguna, ruang, jam mulai dan selesai. Tidak ada data pribadi spesifik.

## Pilihan yang dipertimbangkan

| Pilihan | Kelebihan | Kekurangan |
|---------|-----------|------------|
| Google Sheets + validasi data | Murah, cepat, sudah dikenal | Tidak bisa menolak bentrok secara andal saat diedit bersamaan; hak akses per baris sulit |
| Skrip Python yang dijalankan GA | Sudah ada dan teruji | Tetap manual; bentrok baru ketahuan setelah terjadi |
| Fitur kalender ruang di sistem email perusahaan | Tidak perlu membangun apa pun | Perlu lisensi dan persetujuan tim IT (sedang ditanyakan) |
| **Aplikasi web kecil (Flask + SQLite + React)** | Bentrok ditolak **saat** memesan; riwayat tersimpan; login dan peran admin | Perlu dirawat; butuh server internal |

## Keputusan

Membangun aplikasi web kecil, dengan aturan bentrok yang sama dengan modul 10 (`start < end_lain AND start_lain < end`), dijalankan di server internal lewat Docker. Dua peran: **staf** (memesan dan menghapus pesanannya sendiri) dan **admin GA** (menghapus pesanan siapa pun).

## Alasan

- Masalah utamanya adalah **pemakaian bersamaan oleh banyak orang**. Hanya penyimpanan bersama dengan pengecekan di server yang bisa menolak bentrok secara andal.
- Aturan bisnisnya sederhana dan sudah teruji di modul 10, jadi risikonya kecil.
- SQLite cukup untuk ± 120 pemesanan per bulan dan satu server. Tidak perlu server database terpisah.

## Konsekuensi

- **Perawatan:** Tim GA menunjuk satu pemilik aplikasi dan satu cadangan. Kode, `README.md`, dan `CLAUDE.md` ada di repositori tim.
- **Operasional:** backup harian file database; log error dipantau; pembaruan dependensi setiap bulan.
- **Keamanan:** login wajib, `FLASK_SECRET_KEY` dari environment, `debug` mati di produksi, ditinjau tim IT sebelum dipakai.
- **Jika aplikasi mati 1 hari:** kembali sementara ke file Excel; data dipindahkan setelah pulih. Tidak kritis.
- **Ditinjau ulang** jika pemakaian > 1.000 pemesanan/bulan, jika butuh integrasi kalender email, atau jika tim IT menyediakan fitur kalender ruang resmi.
