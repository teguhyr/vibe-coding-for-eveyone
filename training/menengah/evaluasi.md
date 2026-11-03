# 📝 Evaluasi Level 2: Pre-test, Post-test & Umpan Balik

| | |
|---|---|
| **Kapan** | **Pre-test:** 10 menit pertama Sesi 1. **Post-test:** Sesi 8, setelah presentasi |
| **Durasi** | 10 menit |
| **Tujuan** | Mengukur peningkatan pemahaman peserta dan memperbaiki pelatihan berikutnya |

Pre-test dan post-test memakai **soal yang sama**. Peserta **tidak** diberi kunci jawaban setelah pre-test.

---

## Bagian A: Soal Pilihan Ganda (15 soal)

**1.** Saat meninjau program buatan AI, bagian yang **paling** penting diperiksa adalah...
- a) Tampilan tabel hasil
- b) Aturan bisnis (logika)
- c) Daftar import di bagian atas
- d) Komentar di dalam kode

**2.** Apa akibat `@dataclass(frozen=True)`?
- a) Program berjalan lebih cepat
- b) Objek tidak bisa diubah setelah dibuat
- c) Data otomatis disimpan ke file
- d) Kolom tidak boleh kosong

**3.** Aturan: "klaim terlambat jika diajukan **lebih dari** 30 hari". Tiga nilai yang paling tepat untuk diuji adalah...
- a) 1, 15, 30
- b) 29, 30, 31
- c) 30, 60, 90
- d) 0, 100, 1000

**4.** Tes gagal setelah Claude mengubah kode, dan Claude mengusulkan mengubah tes agar lulus. Tindakan yang tepat adalah...
- a) Setujui, karena tes yang lama pasti salah
- b) Hapus tesnya
- c) Tanyakan dulu: kodenya yang salah, atau aturan bisnisnya memang berubah?
- d) Jalankan ulang pytest sampai lulus

**5.** Dalam teknik "tes dulu", tes untuk aturan baru seharusnya...
- a) Langsung lulus
- b) Gagal dulu, lalu lulus setelah kode diubah
- c) Ditulis setelah kode selesai
- d) Tidak perlu dijalankan

**6.** Traceback berakhir dengan `ValueError: C-12: unknown category 'meals'`. Kemungkinan besar masalahnya ada di...
- a) Data
- b) Kode
- c) Lingkungan (`.venv`)
- d) Koneksi internet

**7.** Program upah lembur berjalan tanpa error, tetapi upah untuk 0 jam lembur tertulis −60.000. Ini adalah...
- a) Masalah lingkungan
- b) Bug kode tanpa pesan error, jenis yang paling berbahaya
- c) Kesalahan data
- d) Perilaku normal

**8.** Saat berada di Plan Mode, Claude Code...
- a) Langsung mengubah semua file
- b) Hanya membaca dan menyusun rencana, tanpa mengubah file
- c) Menjalankan semua tes otomatis
- d) Membuat commit otomatis

**9.** Anda mengubah CSV contoh sebuah modul di repositori ini. Yang **juga** perlu diperiksa adalah...
- a) Hanya file `.py`
- b) `test_sample_data`, contoh output di README, dan materi `training/` yang mengutipnya
- c) Tidak ada
- d) Hanya `.gitignore`

**10.** `ruff check` melaporkan `F821 Undefined name`, padahal program berjalan normal. Artinya...
- a) Pesan bisa diabaikan karena program berjalan
- b) Ada nama yang salah ketik; program akan error saat baris itu dijalankan
- c) Format spasi kurang rapi
- d) Ada import yang tidak terpakai

**11.** Cara **aman** memasukkan input pengguna ke query SQL adalah...
- a) `f"SELECT ... WHERE dept = '{dept}'"`
- b) `"SELECT ... WHERE dept = '" + dept + "'"`
- c) `conn.execute("SELECT ... WHERE dept = ?", (dept,))`
- d) Semua sama amannya

**12.** Isi yang **tidak boleh** ditulis di `CLAUDE.md` adalah...
- a) Perintah untuk menjalankan tes
- b) Aturan bisnis, misalnya tahun fiskal mulai 1 April
- c) Kata sandi database
- d) Larangan membaca folder `private/`

**13.** Merge conflict terjadi ketika...
- a) Tes gagal
- b) Dua branch mengubah baris yang sama dengan cara berbeda
- c) Branch belum di-push
- d) Pesan commit terlalu pendek

**14.** Menurut UU PDP No. 27/2022, yang termasuk **data pribadi spesifik** adalah...
- a) Nama departemen
- b) Data kesehatan dan data keuangan pribadi (misalnya gaji)
- c) Nama kategori klaim
- d) Tanggal libur nasional

**15.** Cara yang benar memakai alat cuti untuk data karyawan **asli** adalah...
- a) Tempel data asli ke Claude agar dihitungkan
- b) Jalankan program yang sudah teruji di terminal biasa dengan data di folder `private/`
- c) Commit data asli ke repositori agar aman
- d) Kirim hasilnya ke Claude untuk diringkas

---

## Bagian B: Penilaian Diri (isi sebelum & sesudah)

Beri skor 1–5 (1 = sama sekali tidak bisa, 5 = sangat yakin bisa):

| Kemampuan | Sebelum | Sesudah |
|-----------|---------|---------|
| Mengenali 4 bagian program dan menentukan bagian yang perlu diperiksa | | |
| Menjalankan, membaca, dan menulis tes pytest, termasuk kasus tepi | | |
| Menerapkan teknik "tes dulu" | | |
| Membaca traceback dan membedakan masalah data, kode, dan lingkungan | | |
| Memakai Plan Mode dan bekerja satu langkah, satu commit | | |
| Memakai ruff untuk merapikan dan memeriksa kode | | |
| Menulis query SQL dasar (SELECT, WHERE, GROUP BY, JOIN) dengan parameter `?` | | |
| Membuat dan merawat `CLAUDE.md` | | |
| Bekerja dengan branch, review, dan menyelesaikan merge conflict | | |
| Memakai data asli dengan aman sesuai UU PDP | | |

---

## Bagian C: Umpan Balik Pelatihan (Sesi 8)

1. Modul mana yang **paling bermanfaat** untuk pekerjaan Anda? Mengapa?
2. Modul mana yang **paling sulit**? Bagian mana yang perlu dijelaskan lebih baik?
3. Apakah durasi pelatihan: terlalu cepat / pas / terlalu lambat?
4. Apakah alat dari proyek akhir Anda sudah dipakai di pekerjaan? Jika belum, apa hambatannya?
5. Seberapa siap Anda melanjutkan ke Level 3 (aplikasi web)? (1–10)
6. Saran untuk fasilitator:

---

## ✅ Kriteria Kelulusan Level 2

Peserta dinyatakan **lulus Level 2** jika:
- [ ] Skor post-test **≥ 12 dari 15** (80%)
- [ ] Proyek akhir lulus (semua kriteria wajib skor ≥ 3, lihat [rubrik](proyek-akhir.md#-rubrik-penilaian))
- [ ] Minimal 3 kasus [Modul 10](modul-10-studi-kasus-lintas-fungsi.md) selesai dengan lembar kerja terisi
- [ ] Semua item [Checklist Kelulusan Level 2](../02-menengah.md#-checklist-kelulusan-level-2) tercentang

---

<details>
<summary>🔑 <b>Kunci Jawaban (untuk fasilitator)</b></summary>

| No | Jawaban | Modul | No | Jawaban | Modul |
|----|---------|-------|----|---------|-------|
| 1 | b | 1 | 9 | b | 4 |
| 2 | b | 1 | 10 | b | 5 |
| 3 | b | 2 | 11 | c | 6 |
| 4 | c | 2 | 12 | c | 7 |
| 5 | b | 2 | 13 | b | 8 |
| 6 | a | 3 | 14 | b | 9 |
| 7 | b | 3 | 15 | b | 9 |
| 8 | b | 4 | | | |

Jika banyak peserta salah pada soal yang sama, ulas kembali modul terkait di awal sesi berikutnya.

</details>

---

← [Proyek Akhir](proyek-akhir.md) | [Daftar Modul](README.md) | **Untuk fasilitator: [Panduan Fasilitator →](panduan-fasilitator.md)**
