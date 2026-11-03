# Modul 10: Menjadi AI Champion di Organisasi

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 10](../03-mahir.md#langkah-10-menjadi-ai-champion-di-organisasi) |
| **Sesi** | Sesi 8 (+ dilanjutkan setelah pelatihan) |
| **Durasi** | 60 menit |
| **Prasyarat** | Modul 1–9 |
| **File latihan** | [`training/dasar/`](../dasar/README.md) (materi untuk mengajar), [`latihan/contoh-claude/`](latihan/contoh-claude/) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjalankan workshop vibe coding internal memakai paket Level 1.
2. Menyusun usulan **kebijakan pemakaian AI** yang mencakup klasifikasi data, alat yang disetujui, review manusia, dan kepemilikan aplikasi.
3. Membangun **perpustakaan bersama** tim: prompt, command, skill, dan modul studi kasus.
4. **Mengukur dampak** dengan angka sebelum/sesudah, dengan jujur.
5. Membimbing rekan dengan **pertanyaan**, bukan jawaban.

---

## 📖 Materi

### A. Hero = membuat orang lain ikut bisa

Satu orang yang mahir menghemat waktunya sendiri. Satu orang yang **mengajari 10 rekan** dan memasang pagar pengaman (kebijakan, review, perpustakaan bersama) mengubah cara kerja satu unit. Itulah peran *AI champion*.

### B. Workshop internal

Anda tidak perlu menyusun materi dari nol. Paket [Level 1: Dasar](../dasar/README.md) sudah berisi 10 modul, proyek akhir, evaluasi, dan [panduan fasilitator](../dasar/panduan-fasilitator.md) dengan rundown 4 sesi × 2 jam.

**Tips untuk fasilitator baru:**
- Jalankan semua praktik terpandu sendiri **H-1**.
- Pakai contoh dari fungsi peserta (stok untuk operasional, anggaran untuk keuangan, cuti untuk HR).
- Ajak satu asisten per 10 peserta, idealnya lulusan Level 2.
- Ukur dengan pre-test dan post-test yang sudah tersedia di [evaluasi Level 1](../dasar/evaluasi.md).

### C. Kebijakan pemakaian AI

Usulan kebijakan minimal berisi:

| Bagian | Isi | Contoh |
|--------|-----|--------|
| **Klasifikasi data** | Kategori data dan mana yang boleh masuk ke alat AI | Publik ✅; Internal ✅ di akun perusahaan; Rahasia ⚠️ dengan persetujuan; **Data pribadi** ❌ kecuali ada dasar hukum (UU PDP) |
| **Alat yang disetujui** | Alat dan jenis akun yang boleh dipakai | Claude dengan akun perusahaan; bukan akun pribadi |
| **Review manusia** | Kapan hasil AI wajib diperiksa manusia | Kode yang memengaruhi keputusan bisnis, angka di laporan, dokumen ke pihak luar |
| **Kepemilikan aplikasi** | Setiap aplikasi buatan karyawan punya pemilik dan penerus | Didaftarkan ke tim IT; ada ADR (Modul 9) |
| **Keamanan** | Standar minimal sebelum dipakai orang lain | Daftar periksa Modul 4 & 8; ditinjau tim IT |
| **Pelaporan insiden** | Apa yang dilakukan jika data terlanjur terkirim | Berhenti, laporkan ke DPO/tim keamanan, ganti rahasia (Level 2 Modul 9) |

> ⚠️ Anda **mengusulkan**, bukan menetapkan. Libatkan tim legal, keamanan informasi, IT, dan petugas pelindungan data (DPO) sejak awal. Kebijakan yang disusun bersama lebih mungkin disetujui dan diikuti.

### D. Perpustakaan bersama

Satu repositori tim berisi:
- **Prompt R-C-T-C-O** yang terbukti berhasil, per fungsi bisnis, dengan contoh data **sintetis**.
- **`.claude/commands`, `.claude/skills`, `.claude/agents`, `.claude/settings.json`** tim (Modul 5).
- **Modul studi kasus baru** dari proyek peserta Level 2, mengikuti struktur `modules/NN-<fungsi>/`.
- **ADR** setiap aplikasi tim (Modul 9).

Perlakukan perpustakaan seperti kode: perubahan lewat PR, di-review, dengan CI (Modul 7).

### E. Mengukur dampak dengan jujur

| Alat | Fungsi | Waktu sebelum | Waktu sesudah | Hemat / bulan | Kesalahan berkurang |
|------|--------|---------------|---------------|---------------|---------------------|
| Rekonsiliasi bank | Akuntansi | 6 jam | 1 jam | 20 jam | Ya |
| Cek kontrak | Legal | 3 jam | 15 menit | 11 jam | Tidak ada tenggat terlewat |

Agar angkanya dipercaya:
- Ukur waktu **sebelum** alat dipakai (atau minta pengguna mencatatnya), jangan hanya mengira.
- Hitung juga waktu **merawat** alat dan melatih pengguna.
- Laporkan alat yang **tidak berhasil** juga, beserta pelajarannya.
- Kesalahan yang dicegah sering lebih bernilai daripada jam yang dihemat: tenggat kontrak yang tidak terlewat, pembayaran ganda yang tertangkap.

### F. Mentoring dengan pertanyaan

Saat meninjau pekerjaan rekan, tanyakan, jangan langsung memperbaiki:

| Daripada... | Tanyakan... |
|-------------|-------------|
| "Ini salah, harusnya `>=`." | "Apa yang terjadi jika nilainya **tepat** di batas?" |
| "Tambahkan tes." | "Bagaimana kamu tahu angka ini benar?" |
| "Jangan pakai data itu." | "Data ini termasuk kategori apa di kebijakan kita?" |
| "Pakai SQLite saja." | "Apa jadinya jika aplikasinya mati sehari?" |

Pertanyaan membuat rekan **belajar menemukan sendiri**, persis cara Anda belajar di Level 1–3.

---

## 🛠️ Praktik Terpandu

**1. Rencanakan workshop pertama Anda.** Isi rencana ini:

```
Peserta        : (siapa, berapa orang, fungsi apa)
Tanggal & sesi : (4 sesi × 2 jam, sesuai panduan fasilitator Level 1)
Asisten        :
Persiapan IT   : (akun Claude perusahaan, izin instalasi, akses jaringan)
Contoh per fungsi yang akan dipakai :
Ukuran sukses  : (misalnya: ≥ 80% peserta lulus checklist Level 1)
```

**2. Draf kebijakan AI dengan bantuan Claude.**

```
Bantu saya menyusun draf usulan kebijakan pemakaian AI untuk <unit/perusahaan>,
maksimal 2 halaman, Bahasa Indonesia formal. Bagian: tujuan, klasifikasi data
(publik/internal/rahasia/data pribadi, dan mana yang boleh ke alat AI), alat yang disetujui,
kewajiban review manusia, kepemilikan aplikasi buatan karyawan, standar keamanan minimal,
dan pelaporan insiden. Rujuk UU PDP No. 27/2022 secara umum, tanpa mengutip pasal
yang tidak Anda yakini. Tandai bagian yang perlu ditinjau tim legal.
```

Periksa drafnya: hapus klaim hukum yang tidak bisa Anda verifikasi, lalu bawa ke tim legal.

**3. Mulai perpustakaan bersama.** Buat repositori tim (atau folder di repositori yang ada) dengan satu prompt terbaik Anda dan satu custom command dari Modul 5.

---

## 🏋️ Latihan

### ⭐ Latihan 10.1: Klasifikasi data

Klasifikasikan (publik / internal / rahasia / data pribadi) dan tentukan boleh atau tidak dikirim ke Claude dengan akun perusahaan:
1. Daftar harga produk di situs web perusahaan
2. Notulen rapat tim tentang jadwal proyek internal
3. Harga negosiasi dengan vendor
4. Daftar karyawan beserta NIK dan nomor rekening
5. Kode program aplikasi ruang rapat (tanpa data)

### ⭐⭐ Latihan 10.2: Ubah menjadi pertanyaan

Ubah 3 komentar review berikut menjadi pertanyaan mentoring:
1. "Kamu lupa menangani file CSV kosong."
2. "API key-mu jangan ditaruh di kode."
3. "Tesnya kurang."

### ⭐⭐⭐ Latihan 10.3: Ajari dua rekan

Ajari minimal **2 rekan kerja** sampai mereka lulus [Checklist Level 1](../01-dasar.md#-checklist-kelulusan-level-1). Catat: kesulitan terbesar mereka, modul yang paling membantu, dan satu perbaikan untuk materi ini. (Perbaikan materi bisa Anda kirim sebagai PR ke repositori ini.)

---

## 📝 Kuis

1. Apa perbedaan peran "orang yang mahir" dan "AI champion"?
2. Sebutkan 4 bagian minimal kebijakan pemakaian AI.
3. Mengapa kebijakan AI sebaiknya disusun bersama tim legal, keamanan, IT, dan DPO?
4. Sebutkan 2 cara agar laporan dampak dipercaya manajemen.
5. Mengapa mentoring dengan pertanyaan lebih efektif daripada langsung memberi jawaban?

---

## 📌 Ringkasan

- Champion **mengajar**, memasang **pagar pengaman**, dan **mengukur** dampaknya.
- Pakai paket Level 1 untuk workshop; jangan menyusun ulang dari nol.
- Kebijakan AI: klasifikasi data, alat yang disetujui, review manusia, kepemilikan aplikasi, keamanan, insiden. **Usulkan bersama** tim terkait.
- Perpustakaan bersama diperlakukan seperti kode: PR, review, CI.
- Ukur dengan jujur, termasuk biaya perawatan dan alat yang gagal. Bimbing dengan pertanyaan.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 10.1** (kebijakan tiap perusahaan bisa berbeda; ini contoh yang umum):
1. **Publik**: boleh.
2. **Internal**: boleh di akun perusahaan yang disetujui.
3. **Rahasia**: hanya jika kebijakan dan atasan mengizinkan; jika ragu, samarkan angkanya atau jangan kirim.
4. **Data pribadi** (termasuk data keuangan pribadi = data spesifik UU PDP): **tidak boleh**. Gunakan data sintetis dengan struktur yang sama (Level 2 Modul 9).
5. **Internal**: boleh di akun perusahaan, selama tidak berisi rahasia (API key, kata sandi) atau data asli.

**Latihan 10.2 (contoh)**
1. "Apa yang terjadi kalau file CSV-nya kosong? Coba jalankan."
2. "Kalau repositori ini dibuka orang lain, apa yang bisa mereka lakukan dengan baris ini?"
3. "Kalau besok ada yang mengubah aturan batas ini, tes mana yang akan memberi tahu kita?"

**Latihan 10.3:** yang dinilai: kedua rekan benar-benar lulus checklist (bukan hanya hadir), dan catatan refleksinya spesifik.

**Kuis**
1. Orang yang mahir menyelesaikan pekerjaannya sendiri. AI champion membuat orang lain ikut bisa, dengan aman dan terukur.
2. Pilih empat dari: klasifikasi data, alat yang disetujui, review manusia, kepemilikan aplikasi, standar keamanan, pelaporan insiden.
3. Agar sesuai hukum dan standar keamanan, mendapat dukungan, dan lebih mungkin disetujui serta diikuti.
4. Pilih dua dari: ukur waktu sebelum alat dipakai; hitung biaya perawatan; laporkan juga yang gagal; sertakan kesalahan yang dicegah.
5. Rekan belajar menemukan masalahnya sendiri, sehingga kemampuannya bertambah dan ia tidak bergantung pada Anda.

</details>

---

← [Modul 9](modul-09-arsitek.md) | **Berikutnya: [Proyek Akhir (Capstone) →](proyek-akhir.md)**
