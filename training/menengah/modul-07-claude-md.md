# Modul 7: CLAUDE.md: "SOP" untuk Asisten AI Anda

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 7](../02-menengah.md#langkah-7-claudemd-sop-untuk-asisten-ai-anda) |
| **Sesi** | Sesi 4 |
| **Durasi** | 35 menit |
| **Prasyarat** | Modul 1–6 |
| **File latihan** | [`CLAUDE.md`](../../CLAUDE.md) di repositori ini (sebagai contoh) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan apa itu `CLAUDE.md` dan kapan Claude membacanya.
2. Membuat draf dengan `/init`, lalu mengisinya dengan pengetahuan yang **hanya Anda** miliki.
3. Membedakan isi yang berguna (spesifik) dan yang tidak (umum, rahasia).
4. Menguji apakah Claude benar-benar memakai isi `CLAUDE.md`.

---

## 📖 Materi

### A. Apa itu `CLAUDE.md`?

`CLAUDE.md` adalah file teks biasa (format Markdown) yang **otomatis dibaca Claude Code** saat bekerja di proyek Anda. Anggap saja **SOP + buku panduan karyawan baru**: Claude tidak perlu dijelaskan ulang setiap kali Anda membuka percakapan baru.

| Lokasi | Berlaku untuk |
|--------|---------------|
| `CLAUDE.md` di folder utama proyek | Semua orang yang bekerja di proyek itu (ikut di-commit ke Git) |
| `CLAUDE.md` di subfolder | Dibaca saat Claude bekerja dengan file di subfolder itu |
| `~/.claude/CLAUDE.md` | Preferensi pribadi Anda di semua proyek (tidak dibagikan) |

Perintah `/memory` di Claude Code membuka file-file ini untuk diedit.

### B. Isi yang berguna

| Bagian | Contoh |
|--------|--------|
| **Perintah** | Cara menjalankan tes, linter, dan program utama |
| **Struktur proyek** | "Satu folder per laporan; tidak ada import antar-folder" |
| **Aturan bisnis** | "Tahun fiskal mulai 1 April", "Uang dalam Rupiah tanpa desimal" |
| **Konvensi** | "Nama kolom CSV pakai `snake_case`", "Pesan error menyebut ID baris" |
| **Larangan** | "Jangan baca folder `private/`", "Jangan ubah tes agar lulus" |
| **Jebakan** | "Mengubah CSV contoh mematahkan `test_sample_data` dan README" |

### C. Isi yang **tidak** perlu

- **Hal umum** yang sudah diketahui semua programmer: "tulis kode yang bersih", "beri nama variabel yang jelas".
- **Hal yang mudah dilihat dari kode**: daftar semua fungsi, isi setiap file.
- **Rahasia**: kata sandi, API key, data pelanggan. `CLAUDE.md` ikut di-commit ke Git dan dibaca AI. **Jangan pernah** menaruh rahasia di sini.
- **Terlalu panjang**: semakin panjang, semakin besar kemungkinan instruksi penting tenggelam. Tulis ringkas.

### D. Membuat draf dengan `/init`

Di dalam Claude Code, ketik `/init`. Claude membaca proyek dan menulis draf `CLAUDE.md` berisi perintah dan struktur yang **bisa dilihat dari kode**. Tugas Anda: menambahkan yang **tidak bisa dilihat dari kode**, yaitu aturan bisnis, larangan, dan alasan di balik keputusan.

### E. Merawat `CLAUDE.md`

- Saat Anda **mengoreksi Claude untuk kedua kalinya** tentang hal yang sama, tulis koreksinya di `CLAUDE.md`.
- Saat aturan bisnis berubah, perbarui `CLAUDE.md` di commit yang sama dengan perubahan kodenya.
- Tinjau perubahan `CLAUDE.md` seperti meninjau kode, karena isinya memengaruhi semua pekerjaan Claude berikutnya.

---

## 🛠️ Praktik Terpandu

**1. Baca contoh.** Buka [`CLAUDE.md`](../../CLAUDE.md) di repositori ini. Temukan bagian *Commands* dan *Architecture: Business-Function Modules*. Perhatikan kalimat seperti *"File names must be unique across all modules"*: ini pengetahuan yang **tidak** langsung terlihat dari satu file kode.

**2. Siapkan proyek latihan sendiri** di luar repositori pelatihan:

```bash
mkdir ~/proyek-reimburse
```

```bash
cp training/menengah/latihan/expense_claims.py training/menengah/latihan/test_expense_claims.py ~/proyek-reimburse/
```

```bash
mkdir ~/proyek-reimburse/data
```

```bash
cp training/menengah/latihan/data/klaim_reimburse.csv ~/proyek-reimburse/data/
```

```bash
cd ~/proyek-reimburse
```

```bash
git init -b main
```

`-b main` memberi nama `main` pada branch pertama (dipakai lagi di Modul 8). Di Windows PowerShell, ganti `cp` dengan `Copy-Item` dan `~` dengan `$HOME`.

**3. Buat draf.** Jalankan `claude` di folder itu, lalu ketik:

```
/init
```

Baca drafnya. Bagian mana yang benar? Mana yang terlalu umum?

**4. Tambahkan pengetahuan Anda.** Edit `CLAUDE.md` dan tambahkan (sesuaikan dengan kantor Anda):

```markdown
## Aturan bisnis
- Uang dalam Rupiah, disimpan sebagai int (tanpa sen).
- Klaim terlambat jika diajukan > 30 hari setelah tanggal biaya. Tepat 30 hari masih tepat waktu.
- Urutan aturan: terlambat → tanpa bukti → potong ke batas → disetujui.
- Perubahan batas kategori harus disetujui Manajer Keuangan.

## Perintah
- Tes: pytest
- Lint: ruff check . && ruff format --check .
- Jalankan: python expense_claims.py data/klaim_reimburse.csv

## Larangan
- Jangan pernah membaca folder private/ (berisi data klaim asli karyawan).
- Jangan ubah tes agar lulus. Jika tes gagal, jelaskan dulu penyebabnya.
```

**5. Uji.** Ketik `/clear` untuk memulai percakapan baru, lalu tanya:

```
Kalau klaim diajukan tepat 30 hari setelah tanggal biaya, apakah terlambat?
Dari mana kamu tahu?
```

Claude seharusnya menjawab "tidak terlambat" dan menyebut `CLAUDE.md` (atau kodenya) sebagai sumber.

**6. Commit.**

```bash
git add CLAUDE.md expense_claims.py test_expense_claims.py data/klaim_reimburse.csv
```

```bash
git commit -m "Add expense claim checker with CLAUDE.md"
```

---

## 🏋️ Latihan

### ⭐ Latihan 7.1: Spesifik atau umum?

Tandai setiap baris sebagai **berguna** atau **tidak perlu** untuk `CLAUDE.md`:

1. "Tulis kode yang bersih dan mudah dibaca."
2. "Tahun fiskal dimulai 1 April."
3. "API key: sk-ant-abc123..."
4. "Jalankan laporan bulanan: `python laporan.py --bulan 2026-10`."
5. "File `expense_claims.py` berisi fungsi `review_claim`, `parse_claim`, `load_claims`, dan `main`."
6. "Kode departemen resmi: OPS, FIN, HRD, MKT, ITS. Jangan pakai nama lengkap."

### ⭐⭐ Latihan 7.2: Aturan bisnis unit Anda

Tulis bagian `## Aturan bisnis` (minimal 5 butir) untuk salah satu pekerjaan berulang yang Anda catat di Level 1. Setiap butir harus bisa **diuji** (ada angka, tanggal, atau kondisi yang jelas).

### ⭐⭐ Latihan 7.3: Uji tiga pertanyaan

Setelah `/clear`, ajukan 3 pertanyaan yang jawabannya **hanya** ada di `CLAUDE.md` Anda. Berapa yang dijawab benar? Jika ada yang salah, perbaiki kalimat di `CLAUDE.md` agar lebih jelas, lalu uji lagi.

### ⭐⭐⭐ Latihan 7.4: Perbaiki `CLAUDE.md` yang buruk

```markdown
# Proyek
Ini proyek Python. Tolong kerjakan dengan baik dan hati-hati.
Gunakan best practice. Database password: Rahasia2026!
Data ada di folder data dan data_karyawan_asli.
```

Sebutkan 4 masalahnya, lalu tulis ulang versi yang baik.

---

## 📝 Kuis

1. Kapan Claude membaca `CLAUDE.md` di folder utama proyek?
2. Apa yang dibuat oleh `/init`, dan apa yang tetap harus Anda tambahkan sendiri?
3. Mengapa rahasia tidak boleh ditulis di `CLAUDE.md`?
4. Anda sudah dua kali mengingatkan Claude "pakai titik untuk pemisah ribuan". Apa yang sebaiknya dilakukan?

---

## 📌 Ringkasan

- `CLAUDE.md` = SOP yang otomatis dibaca Claude di proyek Anda.
- `/init` membuat draf dari kode. **Anda** menambahkan aturan bisnis, larangan, dan jebakan.
- Tulis yang **spesifik dan bisa diuji**. Hindari hal umum, hal yang terlihat dari kode, dan **rahasia**.
- Rawat seperti kode: perbarui saat aturan berubah, tinjau setiap perubahannya.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 7.1**
1. Tidak perlu: terlalu umum.
2. **Berguna**: aturan bisnis yang tidak terlihat dari kode.
3. **Berbahaya!** Rahasia tidak boleh ada di `CLAUDE.md` maupun di Git. Jika terlanjur, anggap bocor: **ganti (rotate)** key-nya segera.
4. **Berguna**: perintah yang sering dipakai.
5. Tidak perlu: Claude bisa membacanya langsung dari kode, dan daftar ini cepat usang.
6. **Berguna**: konvensi dan larangan yang spesifik.

**Latihan 7.2 (contoh untuk HR)**
```markdown
## Aturan bisnis
- Hari kerja = Senin–Jumat, dikurangi libur nasional di data/holidays.csv.
- Jatah cuti tahunan 12 hari; karyawan dengan masa kerja >= 5 tahun mendapat 15 hari.
- Cuti yang belum disetujui (pending) tidak mengurangi sisa, tetapi ditampilkan terpisah.
- Sisa cuti boleh minus, tetapi harus ditandai "OVER ENTITLEMENT".
- Status yang sah hanya: approved, pending, rejected. Status lain menghentikan program.
```

**Latihan 7.3:** contoh pertanyaan untuk `proyek-reimburse`: "Siapa yang harus menyetujui perubahan batas kategori?", "Folder mana yang tidak boleh kamu baca?", "Urutan aturan reimburse apa?" Jika Claude menjawab dengan menebak, biasanya kalimatnya terlalu samar atau tersembunyi di tengah paragraf panjang. Pecah menjadi butir pendek.

**Latihan 7.4:** masalahnya:
1. **Kata sandi database tertulis**: rahasia bocor ke Git dan ke AI. Hapus, **ganti kata sandinya**, simpan di `.env` (yang diblokir `.gitignore`).
2. "Kerjakan dengan baik", "best practice" terlalu umum, tidak memberi informasi.
3. Folder `data_karyawan_asli` **tidak dilarang**, sehingga Claude mungkin membacanya. Pindahkan ke `private/` dan tulis larangannya.
4. Tidak ada perintah, aturan bisnis, atau jebakan yang spesifik.

Versi yang baik:
```markdown
# CLAUDE.md

## Perintah
- Tes: pytest
- Lint: ruff check . && ruff format --check .

## Aturan bisnis
- (aturan spesifik proyek, masing-masing bisa diuji)

## Data
- data/ hanya berisi data SINTETIS untuk tes dan contoh.
- Data asli ada di private/ (diblokir .gitignore). Jangan pernah membaca folder ini.
- Kredensial dibaca dari variabel lingkungan (.env), tidak pernah ditulis di kode atau di file ini.
```

**Kuis**
1. Otomatis di setiap sesi Claude Code yang dijalankan di proyek itu.
2. Draf berisi perintah dan struktur yang terlihat dari kode. Anda menambahkan aturan bisnis, larangan, alasan, dan jebakan yang tidak terlihat dari kode.
3. File itu ikut di-commit ke Git (bisa dibaca siapa pun yang punya akses repositori) dan dikirim ke AI setiap sesi.
4. Tulis aturannya di `CLAUDE.md` (bagian konvensi), misalnya: "Format Rupiah memakai titik sebagai pemisah ribuan: Rp1.200.000."

</details>

---

← [Modul 6](modul-06-sqlite.md) | **Berikutnya: [Modul 8: Branch, Review, dan Kolaborasi →](modul-08-branch-review.md)**
