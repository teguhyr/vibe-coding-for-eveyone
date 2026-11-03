# 🧑‍🏫 Panduan Fasilitator — Level 2: Menengah

Panduan ini untuk **trainer/fasilitator** yang membawakan [Paket Materi Level 2](README.md). Isinya: persiapan, rundown menit demi menit, tips mengajar, dan solusi masalah yang sering muncul.

---

## 1. Ringkasan Pelatihan

| | |
|---|---|
| **Format** | 8 sesi tatap muka × 2 jam dalam 4 minggu (2 sesi per minggu) + ± 9 jam latihan mandiri |
| **Ukuran kelas** | Ideal 8–16 peserta. Rasio 1 fasilitator + 1 asisten per 8 peserta (lebih banyak praktik mandiri daripada Level 1) |
| **Peserta** | Lulusan [Level 1](../dasar/evaluasi.md#-kriteria-kelulusan-level-1), campuran fungsi bisnis |
| **Ruang** | Proyektor, Wi-Fi stabil, colokan listrik untuk semua laptop |
| **Hasil** | Peserta lulus [kriteria kelulusan Level 2](evaluasi.md#-kriteria-kelulusan-level-2) |

---

## 2. Persiapan

### H-7: Undangan & prasyarat

- [ ] Kirim undangan berisi jadwal 8 sesi dan tautan ke [Daftar Modul](README.md).
- [ ] Pastikan semua peserta **lulus Level 1** dan masih punya repositori pelatihan yang berfungsi.
- [ ] Minta peserta memperbarui repositori (`git switch main`, lalu `git pull`) dan menjalankan `pip install -r requirements-dev.txt` di dalam `.venv` (memasang `pytest` dan `ruff`).
- [ ] Minta peserta membawa **daftar 3 pekerjaan berulang** dari [Latihan 1.1 Level 1](../dasar/modul-01-pola-pikir.md#-latihan-11-peta-pekerjaan-berulang). Ini bahan proyek akhir.

### H-3: Cek kesiapan

Minta peserta mengirim tangkapan layar dari tiga perintah ini (semua harus lulus):

```bash
pytest
```

```bash
ruff check .
```

```bash
python training/menengah/latihan/expense_claims.py
```

### H-1: Persiapan fasilitator

- [ ] Jalankan seluruh praktik terpandu Modul 1–10 di laptop presentasi.
- [ ] Jalankan `pytest training/menengah/latihan/kunci` (harus `11 passed`) dan `pytest training/menengah/latihan/test_overtime_pay.py` (harus **1 failed, 3 passed**: bug untuk Modul 3 disengaja).
- [ ] Siapkan **lembar pre-test** ([Evaluasi](evaluasi.md)), cetak atau dalam bentuk formulir online.
- [ ] Perbesar ukuran huruf terminal dan VS Code (minimal 18pt) untuk proyektor.

---

## 3. Rundown Sesi

### Minggu 1

#### Sesi 1 (120 menit): Anatomi Program & Tes

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:10 | Pembukaan + **pre-test** | [Evaluasi](evaluasi.md) | Tekankan: pre-test tidak dinilai |
| 0:10–0:45 | Anatomi program | [Modul 1](modul-01-anatomi-program.md) | Latihan 1.2 (tebak keputusan) dikerjakan berpasangan, lalu diskusi urutan aturan (1.3) |
| 0:45–1:55 | Tes otomatis | [Modul 2](modul-02-pytest.md) | Demo tes gagal (SKU-001) maksimal 5 menit. Latihan 2.2–2.3 di kelas. **Pastikan semua mengembalikan `inventory.csv`** |
| 1:55–2:00 | Penutup | — | Tugas mandiri: Latihan 1.4, 2.4, 2.5 |

#### Sesi 2 (120 menit): Debugging & Plan Mode

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab tugas mandiri | — | Fokus pada Latihan 2.5 (merah → hijau) |
| 0:05–0:55 | Debugging | [Modul 3](modul-03-debugging.md) | Praktik 1: minta peserta **membacakan** baris terakhir error sebelum memperbaiki. Praktik 2: biarkan peserta menemukan bug sendiri 5 menit sebelum bertanya ke Claude |
| 0:55–1:55 | Plan Mode | [Modul 4](modul-04-plan-mode.md) | Rencana Claude tiap peserta berbeda; bandingkan 2–3 rencana di layar dengan checklist. Ingatkan: **jangan merge** ke `main` |
| 1:55–2:00 | Penutup | — | Tugas mandiri: Latihan 3.3, 3.4, 4.2, 4.4 |

### Minggu 2

#### Sesi 3 (120 menit): Linter & SQLite

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab tugas mandiri | — | |
| 0:05–0:30 | Linter & formatter | [Modul 5](modul-05-linter-formatter.md) | Momen "aha": program berjalan, tetapi `F821` menemukan bug. Pastikan semua menghapus `berantakan.py` |
| 0:30–1:55 | Database & SQL | [Modul 6](modul-06-sqlite.md) | Tulis query di papan tulis/layar dulu, baru di kode. Latihan 6.1–6.3 di kelas; 6.4 untuk yang cepat |
| 1:55–2:00 | Penutup | — | Tugas mandiri: Latihan 5.3, 6.4 |

#### Sesi 4 (120 menit): CLAUDE.md, Branch & Review, Data Aman

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab tugas mandiri | — | |
| 0:05–0:40 | `CLAUDE.md` | [Modul 7](modul-07-claude-md.md) | Pastikan semua berhasil membuat `~/proyek-reimburse` dengan `git init -b main`; Modul 8 bergantung padanya |
| 0:40–1:25 | Branch & review | [Modul 8](modul-08-branch-review.md) | Latihan 8.2 (jadilah reviewer) didiskusikan bersama; minta peserta menemukan ketiga masalah sebelum kunci dibuka |
| 1:25–1:55 | Data asli dengan aman | [Modul 9](modul-09-data-aman.md) | Latihan 9.3 (aman atau tidak) cocok sebagai kuis cepat seluruh kelas |
| 1:55–2:00 | Penutup | — | Tugas mandiri: Latihan 7.2, 8.4, 9.4. Bawa ide proyek akhir ke Sesi 6 |

### Minggu 3

#### Sesi 5 (120 menit): Studi Kasus Lintas Fungsi

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Pembagian kelompok per fungsi | — | Kelompokkan 2–3 orang dengan kasus yang sesuai fungsinya |
| 0:05–1:55 | Studi kasus | [Modul 10](modul-10-studi-kasus-lintas-fungsi.md) | Peserta mengerjakan 1–2 kasus dengan alur lengkap. Fasilitator berkeliling memeriksa **lembar kerja** (aturan, tes, kasus tepi) sebelum peserta menulis prompt |
| 1:55–2:00 | Penutup | — | Tugas mandiri: selesaikan minimal 3 kasus; isi kanvas masalah proyek akhir |

#### Sesi 6 (120 menit): Proyek Akhir — Perencanaan

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:15 | Brief & rubrik | Tunjukkan [rubrik](proyek-akhir.md#-rubrik-penilaian) dan contoh referensi (pemeriksa klaim reimburse) |
| 0:15–0:45 | Kanvas masalah + data sintetis | Periksa ukuran proyek: **satu laporan, 3–5 aturan**. Periksa bagian "Data sensitif?" setiap peserta |
| 0:45–1:45 | Plan Mode + daftar tes | Peserta menulis prompt R-C-T-C-O, meminta rencana, lalu menulis tes dulu |
| 1:45–1:55 | Tukar rencana | Berpasangan: saling membaca rencana dan daftar tes, cari 1 kasus tepi yang terlewat |
| 1:55–2:00 | Penutup | Tugas mandiri: tes merah → implementasi |

### Minggu 4

#### Sesi 7 (120 menit): Proyek Akhir — Klinik

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:10 | Tanya jawab umum | Kumpulkan masalah yang dialami banyak peserta, jawab untuk seluruh kelas |
| 0:10–1:30 | Klinik implementasi | Fasilitator & asisten berkeliling. Prioritaskan peserta yang tesnya belum ada |
| 1:30–1:50 | Review berpasangan | Peserta saling meninjau branch dengan checklist reviewer, lalu meminta review Claude |
| 1:50–2:00 | Persiapan presentasi | Ingatkan format 10 menit dan cek "selesai berarti hijau" |

#### Sesi 8 (120 menit): Presentasi & Kelulusan

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:05 | Pembukaan | Urutan presentasi diundi |
| 0:05–1:25 | Presentasi proyek (10 menit/peserta) | Untuk kelas > 8 orang, bagi menjadi 2 ruang paralel (fasilitator dan asisten masing-masing menilai satu ruang dengan rubrik) |
| 1:25–1:35 | **Post-test** | Soal sama dengan pre-test |
| 1:35–1:50 | Penilaian diri & umpan balik | Bagian B & C di [Evaluasi](evaluasi.md) |
| 1:50–2:00 | Penutupan | Umumkan kelulusan, perkenalkan [Level 3: Mahir](../03-mahir.md) ([paket materi](../mahir/README.md)) |

### Rekap waktu

| | Jam |
|---|---|
| 8 sesi tatap muka × 2 jam | 16 |
| Latihan mandiri (latihan ⭐⭐⭐, kasus Modul 10, proyek akhir) | ± 9 |
| **Total** | **± 25** |

---

## 4. Tips Mengajar

1. **Kurangi demo, perbanyak praktik.** Peserta Level 2 sudah bisa memakai alat. Demo maksimal 5 menit per modul.
2. **Tanyakan "bagaimana Anda tahu itu benar?"** setiap kali peserta bilang "sudah jalan". Jawaban yang diharapkan: tes, hitungan manual, atau keduanya.
3. **Biarkan error terjadi.** Di Modul 3, jangan langsung menunjukkan letak bug. Beri waktu peserta membaca dan menebak.
4. **Hasil AI berbeda-beda, dan itu wajar.** Nilai **perilaku** dan angka verifikasi di kunci jawaban, bukan kesamaan kode.
5. **Jaga ukuran proyek akhir.** Proyek yang terlalu besar adalah penyebab utama peserta tidak lulus. Lebih baik satu laporan kecil yang benar dan teruji.
6. **Tegakkan aturan data.** Proyek akhir sering memakai masalah nyata. Periksa data contoh setiap peserta; hentikan dengan sopan jika ada data asli, dan jelaskan [Modul 9](modul-09-data-aman.md).
7. **Jangan mengetik di laptop peserta.** Pandu dengan pertanyaan.

---

## 5. Masalah Umum & Solusi

| Masalah | Solusi cepat |
|---------|--------------|
| `pytest: command not found` atau `ModuleNotFoundError: No module named 'pytest'` | `.venv` belum aktif, atau `pip install -r requirements-dev.txt` belum dijalankan |
| `ruff: command not found` | Sama seperti di atas; `ruff` dipasang lewat `requirements-dev.txt` |
| `pytest training/menengah/latihan` menunjukkan 1 tes gagal | **Disengaja**: `test_zero_hours_pays_nothing` untuk Modul 3. Jalankan file tes tertentu saja |
| `test_sample_data` gagal di modul 01–07 | Peserta lupa mengembalikan data atau masih di branch latihan. Cek `git branch` dan `git status`; kembalikan dengan `git checkout -- <file>` |
| Peserta tidak menemukan *plan mode* | Tekan `Shift+Tab` beberapa kali dan perhatikan tulisan di bawah kotak input; atau mulai ulang dengan `claude --permission-mode plan` |
| `git init -b main` gagal (Git versi lama) | Jalankan `git init` lalu `git branch -m main` setelah commit pertama |
| Peserta ingin memakai data asli di proyek akhir | Tolak dengan sopan; bantu membuat data sintetis dari **struktur** datanya ([Modul 9](modul-09-data-aman.md)) |
| Peserta terlalu cepat | Arahkan ke latihan ⭐⭐⭐, kasus Modul 10 tambahan, atau Latihan 10.3 (tukar review) |
| Peserta tertinggal | Fokus pada praktik terpandu dan satu kasus Modul 10; latihan ⭐⭐⭐ boleh dikerjakan setelah pelatihan |

---

## 6. Penilaian & Sertifikat

- Rekap skor pre-test, post-test, jumlah kasus Modul 10 yang selesai, dan rubrik proyek akhir setiap peserta.
- **Lulus Level 2:** post-test ≥ 12/15, proyek akhir lulus, minimal 3 kasus Modul 10, checklist kelulusan lengkap.
- Peserta yang belum lulus: beri kesempatan memperbaiki proyek dalam 2 minggu.
- Laporkan ke manajemen: rata-rata kenaikan skor pre→post test, jumlah peserta lulus, dan **daftar alat dari proyek akhir beserta estimasi jam yang dihemat per bulan**. Daftar ini adalah bukti manfaat pelatihan dan bahan pemilihan proyek untuk Level 3.

---

← [Daftar Modul](README.md)
