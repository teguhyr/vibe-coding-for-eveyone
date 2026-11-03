# 🧑‍🏫 Panduan Fasilitator — Level 1: Dasar

Panduan ini untuk **trainer/fasilitator** yang membawakan [Paket Materi Level 1](README.md). Isinya: persiapan, rundown menit demi menit, tips mengajar, dan solusi masalah yang sering muncul.

---

## 1. Ringkasan Pelatihan

| | |
|---|---|
| **Format** | 4 sesi tatap muka × 2 jam dalam 2 minggu + ± 4 jam latihan mandiri |
| **Ukuran kelas** | Ideal 10–20 peserta. Rasio 1 fasilitator + 1 asisten per 10 peserta |
| **Peserta** | Campuran fungsi bisnis, tanpa latar belakang pemrograman |
| **Ruang** | Proyektor, Wi-Fi stabil, colokan listrik untuk semua laptop |
| **Hasil** | Peserta lulus [kriteria kelulusan Level 1](evaluasi.md#-kriteria-kelulusan-level-1) |

---

## 2. Persiapan

### H-7: Undangan & instalasi

- [ ] Kirim undangan berisi jadwal 4 sesi dan tautan ke [Modul 2: Menyiapkan Alat Kerja](modul-02-menyiapkan-alat.md).
- [ ] Pastikan setiap peserta punya **akun Claude** yang disetujui perusahaan.
- [ ] Koordinasi dengan **tim IT**: izin instalasi Python, VS Code, Git, Claude Code; akses ke `claude.ai`, `github.com`, `pypi.org`; kebijakan PowerShell di laptop Windows.
- [ ] Siapkan alamat repositori pelatihan yang bisa di-*clone* peserta.

### H-3: Cek instalasi

- [ ] Minta peserta mengirim hasil [Latihan 2.1](modul-02-menyiapkan-alat.md#-latihan-21-lembar-cek-instalasi) (lembar cek instalasi).
- [ ] Tawarkan **"klinik instalasi" online 30 menit** untuk yang masih bermasalah.

### H-1: Persiapan fasilitator

- [ ] Jalankan seluruh praktik terpandu Modul 3–10 di laptop presentasi.
- [ ] Pastikan `pytest` lulus di repositori pelatihan.
- [ ] Siapkan **lembar pre-test** ([Evaluasi](evaluasi.md)), cetak atau dalam bentuk formulir online.
- [ ] Perbesar ukuran huruf terminal dan VS Code (minimal 18pt) untuk proyektor.

---

## 3. Rundown Sesi

### Sesi 1 (120 menit): Pola Pikir, Alat, dan Prompt

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:10 | Pembukaan + **pre-test** | [Evaluasi](evaluasi.md) | Tekankan: pre-test tidak dinilai, hanya untuk mengukur kemajuan |
| 0:10–0:30 | Vibe coding & pola pikir | [Modul 1](modul-01-pola-pikir.md) | Diskusi kelompok per fungsi 5 menit; minta 2–3 kelompok berbagi |
| 0:30–0:45 | Verifikasi instalasi | [Modul 2](modul-02-menyiapkan-alat.md) | Semua peserta menjalankan `pytest`. Asisten membantu yang bermasalah |
| 0:45–1:00 | Terminal | [Modul 3](modul-03-terminal.md) | Praktik bersama; Latihan 3.1 dikerjakan di kelas |
| 1:00–1:25 | Claude Code pertama | [Modul 4](modul-04-claude-code-pertama.md) | Demo langsung di layar; Latihan 4.2 (setujui/tolak) didiskusikan bersama |
| 1:25–1:55 | Prompt R-C-T-C-O | [Modul 5](modul-05-prompt-rctco.md) | Bandingkan prompt buruk vs baik di layar; peserta mulai Latihan 5.3 |
| 1:55–2:00 | Penutup | — | Tugas mandiri: Latihan 1.1, 5.3, dan semua latihan ⭐⭐ Modul 1–5 |

### Sesi 2 (120 menit): Kode, Studi Kasus, Verifikasi, Git

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:30 | Review singkat + membaca kode | [Modul 6](modul-06-membaca-kode.md) | Mulai dengan 5 menit tanya jawab tugas mandiri. Minta peserta **menebak** output sebelum menjalankan |
| 0:30–0:50 | Studi kasus operasional | [Modul 7](modul-07-studi-kasus-operasional.md) | Latihan 7.1 & 7.2 di kelas. **Pastikan semua mengembalikan data** dengan `git checkout` |
| 0:50–1:15 | Verifikasi keuangan | [Modul 8](modul-08-verifikasi-keuangan.md) | Latihan 8.2 (ambang 5% & 20%) adalah momen "aha" tentang angka di batas; beri waktu diskusi |
| 1:15–1:40 | Perubahan kecil | [Modul 9](modul-09-perubahan-kecil.md) | Hasil Claude tiap peserta bisa berbeda; nilai dengan **kriteria lulus perubahan**, bukan kesamaan kode |
| 1:40–2:00 | Git | [Modul 10](modul-10-git.md) | Praktik 1 di folder latihan, lalu Praktik 2 menyimpan hasil Modul 9 |

**Tugas mandiri sebelum Sesi 3:** latihan ⭐⭐⭐ Modul 6–10, dan Langkah 1–2 [Proyek Akhir](proyek-akhir.md) (menulis prompt).

### Sesi 3 (120 menit): Klinik Proyek Akhir

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:10 | Tanya jawab tugas mandiri | Kumpulkan pertanyaan umum, jawab untuk seluruh kelas |
| 0:10–0:20 | Penjelasan brief & rubrik | Tunjukkan [rubrik penilaian](proyek-akhir.md#-rubrik-penilaian) agar ekspektasi jelas |
| 0:20–1:30 | Klinik proyek | Fasilitator & asisten berkeliling. Tinjau **prompt** peserta sebelum dikirim ke Claude |
| 1:30–1:55 | Tantangan per fungsi | Kelompokkan peserta per fungsi; kerjakan satu [tantangan tambahan](proyek-akhir.md#-tantangan-tambahan-opsional-untuk-sesi-3) |
| 1:55–2:00 | Persiapan presentasi | Ingatkan format presentasi 5 menit |

### Sesi 4 (120 menit): Presentasi & Kelulusan

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:05 | Pembukaan | Urutan presentasi diundi |
| 0:05–1:25 | Presentasi proyek (5 menit/peserta) | Untuk kelas > 14 orang, bagi menjadi 2 ruang paralel. Nilai dengan rubrik |
| 1:25–1:35 | **Post-test** | Soal sama dengan pre-test |
| 1:35–1:50 | Penilaian diri & umpan balik | Bagian B & C di [Evaluasi](evaluasi.md) |
| 1:50–2:00 | Penutupan | Umumkan kelulusan, perkenalkan [Level 2: Menengah](../02-menengah.md) ([paket materi](../menengah/README.md)) |

---

## 4. Tips Mengajar

1. **Tunjukkan, lalu biarkan mencoba.** Demo maksimal 5 menit, lalu peserta langsung praktik.
2. **Rayakan error.** Saat ada error, ajak kelas membaca pesannya bersama. Error adalah bahan belajar terbaik.
3. **Hasil AI berbeda-beda, dan itu wajar.** Claude bisa menulis kode yang berbeda untuk setiap peserta. Nilai **perilaku** (hasil benar, tes lulus), bukan kesamaan kode.
4. **Pakai contoh dari fungsi peserta.** Saat menjelaskan, sesuaikan analogi: stok gudang untuk operasional, anggaran untuk keuangan, cuti untuk HR.
5. **Tegakkan aturan data.** Jika ada peserta yang ingin memakai data asli, hentikan dengan sopan dan jelaskan [aturan keamanan data](../README.md#-aturan-emas-keamanan-data-berlaku-di-semua-level).
6. **Teknik "sticky note":** peserta menempel kertas hijau di laptop jika selesai, merah jika butuh bantuan. Asisten mendatangi yang merah.
7. **Jangan mengetik di laptop peserta.** Pandu dengan pertanyaan agar peserta yang melakukannya sendiri.

---

## 5. Masalah Umum & Solusi

| Masalah | Solusi cepat |
|---------|--------------|
| Instalasi belum selesai di Sesi 1 | Pasangkan dengan peserta lain (*pair*) agar tetap bisa mengikuti; selesaikan instalasi saat istirahat bersama asisten |
| `python` / `pip` / `pytest` tidak dikenali | Lihat [Pemecahan Masalah di Modul 2](modul-02-menyiapkan-alat.md#-pemecahan-masalah). Paling sering: `.venv` belum aktif |
| Claude Code tidak bisa login | Cek akses jaringan kantor ke `claude.ai`; coba hotspot ponsel untuk memastikan |
| `test_sample_data` gagal di Modul 7–9 | Peserta lupa mengembalikan data: `git checkout -- modules/01-operations/data/inventory.csv` |
| Claude mengubah terlalu banyak | Minta peserta menolak (No), lalu menulis ulang prompt dengan batasan "jangan ubah yang lain" |
| Peserta terlalu cepat | Arahkan ke latihan ⭐⭐⭐ atau tantangan tambahan di Proyek Akhir |
| Peserta tertinggal | Fokus pada praktik terpandu; latihan ⭐⭐ dan ⭐⭐⭐ boleh dikerjakan mandiri |
| Git meminta nama/email saat commit | Jalankan dua perintah `git config --global` di [Modul 10](modul-10-git.md#f-mengatur-identitas-sekali-saja) |

---

## 6. Penilaian & Sertifikat

- Rekap skor pre-test, post-test, dan rubrik proyek akhir setiap peserta.
- **Lulus Level 1:** post-test ≥ 12/15, proyek akhir lulus, checklist kelulusan lengkap.
- Peserta yang belum lulus: beri kesempatan memperbaiki proyek dalam 1 minggu.
- Laporkan ke manajemen: rata-rata kenaikan skor pre→post test, jumlah peserta lulus, dan daftar ide otomatisasi dari [Latihan 1.1](modul-01-pola-pikir.md#-latihan-11-peta-pekerjaan-berulang) peserta. Daftar ide ini adalah bahan berharga untuk Level 2.

---

← [Daftar Modul](README.md)
