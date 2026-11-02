# 🟢 Level 1: Dasar — "Dari Nol Sampai Bisa Menjalankan & Mengubah Program"

| | |
|---|---|
| **Untuk siapa** | Pemula total: belum pernah menulis kode, belum pernah memakai terminal |
| **Durasi** | ± 12 jam (2 minggu, 2 sesi × 2 jam + latihan mandiri) |
| **Prasyarat** | Laptop (Windows, macOS, atau Linux), koneksi internet, akun Claude |
| **Hasil akhir** | Anda bisa menyiapkan alat, menulis prompt yang jelas, menjalankan dan memodifikasi skrip, memverifikasi hasilnya, dan menyimpan versi pekerjaan dengan Git |

### Daftar Langkah

1. [Memahami vibe coding & pola pikir yang benar](#langkah-1-memahami-vibe-coding--pola-pikir-yang-benar)
2. [Menyiapkan alat kerja](#langkah-2-menyiapkan-alat-kerja)
3. [Mengenal terminal](#langkah-3-mengenal-terminal)
4. [Percakapan pertama dengan Claude Code](#langkah-4-percakapan-pertama-dengan-claude-code)
5. [Rumus prompt R-C-T-C-O](#langkah-5-rumus-prompt-r-c-t-c-o)
6. [Membaca kode tanpa takut](#langkah-6-membaca-kode-tanpa-takut)
7. [Menjalankan studi kasus pertama (Operasional)](#langkah-7-menjalankan-studi-kasus-pertama-operasional)
8. [Memverifikasi hasil (Keuangan)](#langkah-8-memverifikasi-hasil-keuangan)
9. [Meminta perubahan kecil ke AI](#langkah-9-meminta-perubahan-kecil-ke-ai)
10. [Menyimpan pekerjaan dengan Git](#langkah-10-menyimpan-pekerjaan-dengan-git)
- [Proyek Akhir Level 1](#-proyek-akhir-level-1)
- [Checklist Kelulusan](#-checklist-kelulusan-level-1)

---

## Langkah 1: Memahami Vibe Coding & Pola Pikir yang Benar

🎯 **Tujuan:** Memahami apa itu vibe coding, dan peran Anda di dalamnya.

📖 **Konsep**

**Vibe coding** adalah cara membuat program dengan **menjelaskan keinginan Anda dalam bahasa sehari-hari** kepada AI. AI yang menulis kodenya.

Bayangkan Anda seorang **manajer proyek**, dan Claude adalah **programmer junior yang sangat cepat dan rajin, tetapi kadang salah paham**.

| Tugas Anda (manusia) | Tugas AI |
|----------------------|----------|
| Menentukan **masalah apa** yang mau diselesaikan | Menulis kode |
| Menjelaskan **aturan bisnis** dengan jelas | Menjelaskan kode jika ditanya |
| **Memeriksa hasil**: apakah angkanya benar? | Memperbaiki kode jika diminta |
| Mengambil **keputusan akhir** | Memberi saran dan alternatif |

Siklus kerja yang akan Anda ulangi terus:

```
  1. JELASKAN  →  2. AI MEMBUAT  →  3. JALANKAN  →  4. PERIKSA  →  5. PERBAIKI
       ▲                                                              │
       └──────────────────────────────────────────────────────────────┘
```

⚠️ **Kesalahan umum**
- **Percaya buta.** AI bisa menghasilkan kode yang *terlihat* benar tapi angkanya salah. Selalu periksa.
- **Meminta terlalu banyak sekaligus.** "Buatkan sistem ERP lengkap" pasti gagal. Mulai dari satu masalah kecil.

✅ **Cek pemahaman:** Tuliskan **3 pekerjaan berulang** di kantor Anda yang memakan waktu, misalnya merekap laporan mingguan, mencocokkan dua file Excel, atau mengecek tanggal jatuh tempo. Simpan daftar ini; akan dipakai di Proyek Akhir.

---

## Langkah 2: Menyiapkan Alat Kerja

🎯 **Tujuan:** Semua alat terpasang dan berfungsi.

📖 **Konsep:** Anda butuh empat alat:

| Alat | Analogi | Fungsi |
|------|---------|--------|
| **Python** | Mesin | Menjalankan program |
| **VS Code** | Meja kerja | Tempat membuka dan melihat file kode |
| **Git** | Mesin fotokopi + arsip | Menyimpan versi pekerjaan |
| **Claude Code** | Asisten | AI yang menulis dan menjalankan kode |

🛠️ **Praktik**

1. **Python 3.10 atau lebih baru:** unduh di https://www.python.org/downloads/. Pengguna Windows: **centang "Add Python to PATH"** saat instalasi.
2. **VS Code:** unduh di https://code.visualstudio.com/, lalu pasang ekstensi **Python** (dari Microsoft).
3. **Git:** unduh di https://git-scm.com/downloads.
4. **Claude Code:** ikuti petunjuk resmi di https://code.claude.com/docs. Di macOS/Linux, Anda bisa memakai:

   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```

   Claude Code juga tersedia sebagai **ekstensi VS Code**, aplikasi desktop, dan versi web (claude.ai/code).

5. **Periksa instalasi.** Buka terminal (lihat Langkah 3), lalu ketik satu per satu:

   ```bash
   python3 --version
   ```

   ```bash
   git --version
   ```

   ```bash
   claude --version
   ```

   Di Windows, gunakan `python --version` jika `python3` tidak dikenali.

6. **Unduh materi latihan** (ganti URL dengan alamat repositori ini):

   ```bash
   git clone https://github.com/<pemilik>/vibe-coding-for-eveyone.git
   ```

   ```bash
   cd vibe-coding-for-eveyone
   ```

7. **Buat lingkungan virtual** (ruang kerja Python khusus proyek ini, agar tidak bercampur dengan proyek lain):

   ```bash
   python3 -m venv .venv
   ```

   ```bash
   source .venv/bin/activate
   ```

   Di Windows: `.venv\Scripts\activate`. Jika berhasil, muncul tulisan `(.venv)` di awal baris terminal.

   ```bash
   pip install -r requirements-dev.txt
   ```

⚠️ **Kesalahan umum**
- `python` tidak dikenali (Windows): instal ulang Python dan centang **Add to PATH**.
- Lupa mengaktifkan `.venv`: setiap kali membuka terminal baru, jalankan lagi perintah `activate`.

✅ **Cek pemahaman:** Ketiga perintah versi di atas menampilkan angka versi, bukan pesan error.

---

## Langkah 3: Mengenal Terminal

🎯 **Tujuan:** Bisa berpindah folder dan menjalankan perintah tanpa ragu.

📖 **Konsep:** Terminal adalah cara "mengobrol" dengan komputer lewat teks. Ibaratnya, File Explorer adalah *menu bergambar*, sedangkan terminal adalah *memesan langsung ke dapur*: lebih cepat dan lebih tepat.

Di VS Code, buka terminal lewat menu **Terminal → New Terminal**.

🛠️ **Praktik: 6 perintah yang cukup untuk memulai**

| Perintah (macOS/Linux) | Windows (PowerShell) | Fungsi |
|------------------------|----------------------|--------|
| `pwd` | `pwd` | Saya sedang di folder mana? |
| `ls` | `ls` atau `dir` | Apa isi folder ini? |
| `cd modules` | `cd modules` | Masuk ke folder `modules` |
| `cd ..` | `cd ..` | Naik satu folder |
| `python3 nama_file.py` | `python nama_file.py` | Menjalankan program Python |
| `clear` | `cls` | Membersihkan layar |

Coba urutan ini:

```bash
pwd
```

```bash
ls modules
```

```bash
cd modules/01-operations
```

```bash
ls
```

```bash
cd ../..
```

💡 **Tips:** Tekan **Tab** untuk melengkapi nama folder secara otomatis, dan **panah atas** untuk mengulang perintah sebelumnya.

✅ **Cek pemahaman:** Tanpa melihat catatan, masuklah ke folder `modules/02-finance`, lihat isinya, lalu kembali ke folder utama.

---

## Langkah 4: Percakapan Pertama dengan Claude Code

🎯 **Tujuan:** Bisa memulai Claude Code, bertanya, dan memahami permintaan izin.

🛠️ **Praktik**

1. Dari folder utama repositori, jalankan:

   ```bash
   claude
   ```

2. Ketik pertanyaan pertama Anda (boleh dalam Bahasa Indonesia):

   ```
   Jelaskan isi repositori ini secara sederhana. Saya pemula dan bekerja di bagian keuangan.
   ```

3. Lanjutkan dengan:

   ```
   Apa yang dilakukan file modules/01-operations/inventory_reorder.py? Jelaskan tanpa istilah teknis.
   ```

4. **Kenali permintaan izin.** Saat Claude ingin **menjalankan perintah** atau **mengubah file**, ia akan meminta izin. **Baca dulu apa yang akan dilakukan** sebelum menyetujui. Ini kendali utama Anda.

📖 **Perintah penting di dalam Claude Code**

| Perintah / tombol | Fungsi |
|-------------------|--------|
| `/help` | Menampilkan bantuan |
| `/clear` | Memulai percakapan baru (konteks lama dihapus) |
| `@nama_file` | Menyebut file tertentu, mis. `@modules/02-finance/README.md` |
| `Esc` | Menghentikan Claude yang sedang bekerja |
| `/exit` atau `Ctrl+C` dua kali | Keluar dari Claude Code |

⚠️ **Kesalahan umum**
- **Menyetujui semua izin tanpa membaca.** Biasakan membaca setiap perintah dan perubahan file.
- **Satu percakapan untuk semua topik.** Gunakan `/clear` saat berganti tugas agar Claude tidak bingung.

✅ **Cek pemahaman:** Minta Claude menjelaskan perbedaan modul `02-finance` dan `06-accounting` dalam 3 kalimat.

---

## Langkah 5: Rumus Prompt R-C-T-C-O

🎯 **Tujuan:** Menulis prompt yang menghasilkan program sesuai keinginan pada percobaan pertama.

📖 **Konsep:** Prompt yang baik seperti **brief kerja untuk vendor**: makin jelas, makin sedikit revisi. Gunakan lima bagian berikut:

| Huruf | Bagian | Pertanyaan | Contoh (HR) |
|-------|--------|------------|-------------|
| **R** | *Role* (Peran) | AI berperan sebagai siapa? | "Kamu developer Python yang membantu tim HR." |
| **C** | *Context* (Konteks) | Situasi dan datanya apa? | "Saya punya file `cuti.csv` dengan kolom: id_karyawan, tanggal_mulai, tanggal_selesai, status." |
| **T** | *Task* (Tugas) | Apa yang harus dibuat? | "Hitung sisa cuti tiap karyawan." |
| **C** | *Constraints* (Batasan) | Aturan apa yang wajib dipatuhi? | "Hanya hari Senin–Jumat. Abaikan status 'ditolak'. Tanpa library tambahan." |
| **O** | *Output* (Hasil) | Hasilnya seperti apa? | "Tabel di layar, lalu jelaskan cara menjalankannya." |

🛠️ **Praktik: bandingkan prompt buruk dan baik**

❌ **Prompt buruk:**
```
buatin program cek budget
```

✅ **Prompt baik:**
```
ROLE: Kamu developer Python yang membantu tim keuangan. Jelaskan kodemu dengan sederhana.

CONTEXT: Saya punya file data/anggaran.csv dengan kolom:
departemen, kategori, anggaran, realisasi
(Contoh baris: Marketing,Iklan Digital,40000000,31000000)

TASK: Buat skrip yang menghitung selisih (realisasi - anggaran) dan persentase selisih
untuk setiap baris.

CONSTRAINTS:
- Hanya library standar Python.
- Gunakan Decimal untuk uang, bukan float.
- Tandai "LEBIH" jika selisih > 10%, "KURANG" jika < -10%, selain itu "OK".
- Jika anggaran 0, jangan error; tandai "TANPA ANGGARAN".

OUTPUT: Tabel di layar. Setelah itu jelaskan cara menjalankan dan cara kerja bagian utamanya.
```

Template lengkap ada di [`modules/00-getting-started/prompt-template.md`](../modules/00-getting-started/prompt-template.md).

⚠️ **Kesalahan umum**
- **Tidak memberi contoh data.** AI harus menebak nama kolom, dan tebakannya sering salah.
- **Aturan bisnis yang ambigu.** "Lebih dari 10%": apakah tepat 10% termasuk? Tulis dengan jelas.

✅ **Cek pemahaman:** Tulis prompt R-C-T-C-O untuk salah satu dari 3 pekerjaan berulang yang Anda catat di Langkah 1.

---

## Langkah 6: Membaca Kode Tanpa Takut

🎯 **Tujuan:** Mengenali 6 konsep dasar pemrograman agar bisa mengikuti penjelasan AI. Anda **tidak perlu menghafal**, cukup bisa mengenali.

📖 **Konsep: 6 bahan dasar semua program**

| Konsep | Analogi | Contoh Python |
|--------|---------|---------------|
| **Variabel** | Label pada kotak | `target = 80_000_000` |
| **Tipe data** | Jenis isi kotak | angka `120`, teks `"Jakarta"`, benar/salah `True` |
| **List & dictionary** | Daftar & kamus | `["A", "B"]`, `{"Jakarta": 120}` |
| **If (kondisi)** | Aturan "jika... maka..." | `if nilai >= target:` |
| **For (perulangan)** | "Untuk setiap baris di Excel..." | `for cabang in penjualan:` |
| **Fungsi** | Resep yang bisa dipakai berulang | `def status_cabang(nilai, target):` |

🛠️ **Praktik:** Buat file baru `latihan.py` di VS Code, salin kode ini, lalu jalankan dengan `python3 latihan.py`.

```python
# Daftar penjualan per cabang (data contoh)
penjualan = {"Jakarta": 120_000_000, "Surabaya": 85_000_000, "Medan": 40_000_000}
target = 80_000_000


def status_cabang(nilai: int, target: int) -> str:
    if nilai >= target:
        return "TERCAPAI"
    return "BELUM"


for cabang, nilai in penjualan.items():
    print(f"{cabang:<10} Rp{nilai:>13,}  {status_cabang(nilai, target)}")
```

Hasilnya:

```
Jakarta    Rp  120,000,000  TERCAPAI
Surabaya   Rp   85,000,000  TERCAPAI
Medan      Rp   40,000,000  BELUM
```

Baca kodenya baris demi baris:
- Baris `penjualan = {...}` adalah **dictionary**: nama cabang → nilai penjualan.
- `def status_cabang(...)` adalah **fungsi** yang mengembalikan teks "TERCAPAI" atau "BELUM".
- `for cabang, nilai in penjualan.items():` berarti "untuk setiap cabang dan nilainya...".
- `print(f"...")` menampilkan teks. `:<10` artinya rata kiri dengan lebar 10 karakter.

⚠️ **Kesalahan umum:** Python **peka terhadap spasi di awal baris (indentasi)**. Baris di dalam `if`, `for`, dan `def` harus menjorok ke dalam (4 spasi).

✅ **Cek pemahaman**
1. Ubah `target` menjadi `100_000_000`, lalu jalankan lagi. Cabang mana yang berubah status?
2. Minta Claude: *"Ubah agar format ribuan memakai titik seperti di Indonesia (120.000.000), lalu jelaskan perubahannya."*

---

## Langkah 7: Menjalankan Studi Kasus Pertama (Operasional)

🎯 **Tujuan:** Menjalankan program nyata, membaca hasilnya, dan melihat pengaruh perubahan data.

🛠️ **Praktik**

1. Buka dan baca [`modules/01-operations/README.md`](../modules/01-operations/README.md). Pahami masalah bisnisnya: **kapan barang di gudang harus dipesan ulang?**
2. Jalankan program:

   ```bash
   python modules/01-operations/inventory_reorder.py
   ```

3. Buka file data `modules/01-operations/data/inventory.csv` di VS Code (atau Excel).
4. **Eksperimen:** ubah `on_hand` untuk `SKU-001` (A4 Paper) dari `120` menjadi `90`, simpan, lalu jalankan program lagi. Apakah A4 Paper sekarang muncul di daftar? Mengapa?
5. **Kembalikan** nilainya ke `120`. Data contoh yang diubah akan membuat tes gagal; Anda akan mempelajari tes di Level 2.

📖 **Konsep:** Program = **data masuk → aturan → hasil keluar**. Jika hasilnya aneh, periksa ketiganya: datanya benar? aturannya benar? cara membaca hasilnya benar?

✅ **Cek pemahaman:** Hitung sendiri reorder point A4 Paper: 15 × 5 + 30 = ? Dengan stok 90, apakah perlu dipesan?

---

## Langkah 8: Memverifikasi Hasil (Keuangan)

🎯 **Tujuan:** Membiasakan diri memeriksa hasil program, sama seperti Anda memeriksa pekerjaan staf baru.

📖 **Konsep:** Aturan **"Cek 3 Baris"**: sebelum mempercayai laporan apa pun yang dibuat program, hitung **minimal 3 baris secara manual** (pakai kalkulator atau Excel). Jika ketiganya cocok, kepercayaan Anda naik. Jika satu saja meleset, berhenti dan selidiki.

🛠️ **Praktik**

1. Jalankan laporan selisih anggaran:

   ```bash
   python modules/02-finance/budget_variance.py
   ```

2. Buka `modules/02-finance/data/budget_vs_actual.csv` di Excel. Hitung selisih dan persentase untuk 3 baris secara manual.
3. Bandingkan dengan hasil program. Apakah cocok?
4. Coba ambang batas yang berbeda:

   ```bash
   python modules/02-finance/budget_variance.py --threshold 5
   ```

5. Tanyakan ke Claude: *"Mengapa program ini memakai Decimal, bukan float? Beri contoh angka yang salah jika memakai float."*

⚠️ **Kesalahan umum:** Hanya memeriksa baris "normal". Periksa juga **kasus tepi**, misalnya baris dengan anggaran 0 (IT/Cloud Hosting). Di sanalah bug biasanya bersembunyi.

✅ **Cek pemahaman:** Jelaskan dengan kata-kata Anda: mengapa Cloud Hosting berstatus `UNBUDGETED`, bukan `OVER`?

---

## Langkah 9: Meminta Perubahan Kecil ke AI

🎯 **Tujuan:** Melakukan siklus *jelaskan → buat → periksa* untuk perubahan nyata, dan meninjau apa yang diubah AI.

🛠️ **Praktik**

1. Buat branch latihan agar file asli aman (penjelasan lengkap ada di Langkah 10):

   ```bash
   git checkout -b latihan-saya
   ```

2. Jalankan `claude`, lalu minta perubahan kecil:

   ```
   Di modules/01-operations/inventory_reorder.py, tambahkan opsi --output nama_file.csv
   agar daftar barang yang perlu dipesan juga disimpan ke file CSV yang bisa dibuka di Excel.
   Jangan ubah perilaku yang sudah ada. Jelaskan setiap perubahan yang kamu buat.
   ```

3. **Tinjau perubahan.** Saat Claude meminta izin mengubah file, baca bagian yang ditambah (hijau) dan dihapus (merah).
4. Jalankan program dengan opsi baru dan buka CSV hasilnya di Excel:

   ```bash
   python modules/01-operations/inventory_reorder.py --output pesan_ulang.csv
   ```

5. Lihat semua perubahan sekaligus:

   ```bash
   git diff
   ```

📖 **Konsep: prompt lanjutan yang sering dipakai**

| Situasi | Prompt |
|---------|--------|
| Tidak paham kode | *"Jelaskan baris 40–55 seperti ke orang awam."* |
| Hasil salah | *"Untuk SKU-002 hasilnya 16, padahal seharusnya 15,5. Mengapa? Perbaiki."* |
| Ingin batal | *"Batalkan perubahan terakhir dan kembalikan seperti semula."* |
| Ingin yakin | *"Apa saja kasus yang bisa membuat program ini salah?"* |

✅ **Cek pemahaman:** File CSV hasil terbuka di Excel dan isinya sama dengan tabel di layar.

---

## Langkah 10: Menyimpan Pekerjaan dengan Git

🎯 **Tujuan:** Menyimpan versi pekerjaan dan bisa kembali jika ada yang rusak.

📖 **Konsep:** Git seperti fitur **"Version History"** di Google Docs, tetapi Anda sendiri yang menentukan kapan menyimpan versi. Setiap simpanan disebut **commit**, lengkap dengan catatan apa yang berubah.

```
commit 1          commit 2              commit 3
"Versi awal"  →  "Tambah export CSV" → "Perbaiki format angka"
                                         ▲ Anda di sini; bisa kembali ke commit mana pun
```

🛠️ **Praktik: 5 perintah Git untuk pemula**

```bash
git status
```
Melihat file apa saja yang berubah.

```bash
git diff
```
Melihat detail perubahan.

```bash
git add modules/01-operations/inventory_reorder.py
```
Menandai file yang akan disimpan.

```bash
git commit -m "Tambah opsi export CSV di laporan reorder"
```
Menyimpan versi dengan catatan.

```bash
git log --oneline
```
Melihat riwayat versi.

Anda juga bisa meminta Claude: *"Buatkan commit untuk perubahan ini dengan pesan yang jelas."*

⚠️ **Kesalahan umum**
- **Pesan commit tidak jelas** seperti "update" atau "fix". Tulislah *apa* yang berubah.
- **Meng-commit file rahasia** seperti `.env` atau data asli. File `.gitignore` di repositori ini sudah memblokir sebagian, tapi tetap periksa dengan `git status` sebelum commit.

✅ **Cek pemahaman:** `git log --oneline` menampilkan commit Anda di branch `latihan-saya`.

---

## 🏆 Proyek Akhir Level 1

**Tujuan:** Memodifikasi modul Operasional sesuai kebutuhan nyata, **hanya dengan prompt**.

**Tugas:**
1. Di branch `latihan-saya`, minta Claude menambahkan kolom **"Saran Jumlah Pesan"** ke laporan reorder: jumlah yang perlu dipesan agar stok cukup untuk **30 hari**.
2. Tulis prompt Anda memakai format **R-C-T-C-O**. Definisikan rumusnya dengan jelas, misalnya: `saran = (pemakaian_harian × 30) − stok_sekarang`, dan jangan negatif.
3. Jalankan programnya. **Verifikasi 3 baris secara manual** (aturan "Cek 3 Baris").
4. Simpan dengan `git commit`.
5. Tulis refleksi singkat (5 kalimat): apa yang berhasil, apa yang harus diulang, dan apa yang akan Anda tulis berbeda di prompt berikutnya.

**Kriteria lulus:**
- [ ] Prompt memakai kelima bagian R-C-T-C-O
- [ ] Program berjalan tanpa error
- [ ] 3 baris sudah diverifikasi manual dan cocok
- [ ] Perubahan tersimpan dalam commit dengan pesan yang jelas

---

## ✅ Checklist Kelulusan Level 1

Centang semua sebelum lanjut ke Level 2:

- [ ] Saya bisa menjelaskan apa itu vibe coding dan peran saya di dalamnya
- [ ] Python, VS Code, Git, dan Claude Code sudah terpasang dan berfungsi
- [ ] Saya bisa berpindah folder dan menjalankan program dari terminal
- [ ] Saya bisa memulai Claude Code dan **membaca permintaan izin sebelum menyetujui**
- [ ] Saya bisa menulis prompt R-C-T-C-O lengkap dengan contoh data
- [ ] Saya bisa mengenali variabel, if, for, dan fungsi dalam kode
- [ ] Saya sudah menjalankan modul 01 (Operasional) dan 02 (Keuangan)
- [ ] Saya selalu memverifikasi minimal 3 baris hasil secara manual
- [ ] Saya bisa membuat commit dan melihat riwayat dengan Git
- [ ] Saya paham: **tidak boleh** memasukkan data pribadi atau rahasia asli ke AI

---

**Selamat! 🎉 Anda sudah melewati tahap "Zero". Lanjut ke [Level 2: Menengah →](02-menengah.md)**
