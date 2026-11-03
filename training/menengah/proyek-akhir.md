# 🏆 Proyek Akhir Level 2: Alat Otomatisasi dari Pekerjaan Anda

| | |
|---|---|
| **Rencana training** | [Proyek Akhir Level 2](../02-menengah.md#-proyek-akhir-level-2) |
| **Sesi** | Perencanaan di **Sesi 6** → klinik di **Sesi 7** → presentasi di **Sesi 8** |
| **Durasi** | ± 10 jam (Sesi 6–7 + ± 6 jam mandiri) |
| **Prasyarat** | Modul 1–10 selesai, minimal 3 kasus Modul 10 dikerjakan |

## 🎯 Tujuan

Membuktikan bahwa Anda bisa membangun alat kerja **dari masalah Anda sendiri** dengan standar yang sama seperti modul di repositori ini: benar, teruji, rapi, aman, dan terdokumentasi.

---

## 📋 Brief Proyek

1. Pilih satu dari 3 pekerjaan berulang yang Anda catat di Level 1 ([Latihan 1.1](../dasar/modul-01-pola-pikir.md#-latihan-11-peta-pekerjaan-berulang)).
2. Bangun alat Python yang menyelesaikannya, dalam folder modul baru:

   ```
   modules/11-<fungsi-anda>/
   ├── README.md               # struktur sama dengan modul lain (lihat Langkah 6)
   ├── data/contoh.csv         # data SINTETIS saja
   ├── <nama_unik>.py          # program
   └── test_<nama_unik>.py     # tes, termasuk test_sample_data
   ```

3. **Nama file harus unik** di seluruh repositori (lihat aturan di [`CLAUDE.md`](../../CLAUDE.md)). `report.py` atau `test_app.py` bisa bentrok dengan modul lain; pakai nama yang deskriptif, misalnya `overtime_recap.py`.
4. Presentasikan 10 menit di Sesi 8.

### Ide proyek per fungsi

| Fungsi | Contoh masalah |
|--------|----------------|
| Operasional | Rekap barang rusak per gudang, jadwal servis kendaraan |
| Keuangan | Umur piutang (*aging*) 0–30/31–60/61–90/>90 hari |
| HR | Rekap lembur bulanan dengan batas 4 jam/hari dan 18 jam/minggu |
| Marketing | Rekap leads per sumber dan tingkat konversi |
| IT | Lisensi software yang akan habis dalam 30 hari |
| Akuntansi | Daftar jurnal yang debit ≠ kredit |
| Legal | Status dokumen perizinan dan tanggal perpanjangan |
| Pengadaan | Pembandingan harga PO dengan harga kontrak |
| Layanan pelanggan | Waktu respons pertama per agen |
| General Affairs | Jadwal perawatan AC dan kendaraan dinas |

---

## 🪜 Langkah Pengerjaan

### Langkah 1: Kanvas masalah (Sesi 6)

Isi sebelum membuka Claude:

```
Masalah        : (apa yang dikerjakan manual sekarang, berapa lama per bulan)
Pengguna       : (siapa yang memakai hasilnya)
Input          : (nama kolom, format tanggal/uang, contoh 1 baris FIKTIF)
Aturan bisnis  : (bernomor, dengan angka dan batas yang jelas)
Output         : (tabel/kolom apa yang ditampilkan)
Input salah    : (apa yang harus ditolak, dan pesan error-nya)
Kasus tepi     : (minimal 3)
Data sensitif? : (kolom apa yang TIDAK boleh ada di data contoh)
```

> ⚠️ **Data sensitif?** Jika input Anda di dunia nyata berisi data pribadi atau rahasia, ikuti [Modul 9](modul-09-data-aman.md): bangun dengan data sintetis, jalankan data asli di terminal biasa.

### Langkah 2: Data sintetis

Buat `data/contoh.csv` (6–10 baris) yang **sengaja** memuat kasus tepi: nilai tepat di batas, nol, dan baris yang memicu setiap aturan. Minta Claude membuatnya dari **struktur**, bukan dari data asli.

### Langkah 3: Rencana di Plan Mode (Sesi 6)

```bash
git switch -c proyek/<nama-alat>
```

Tulis prompt R-C-T-C-O dari kanvas Anda, lalu minta rencana di Plan Mode. Tinjau dengan [checklist Modul 4](modul-04-plan-mode.md#-praktik-terpandu-kolom-goal-di-modul-marketing). Minta pasangan Anda membaca rencananya juga.

### Langkah 4: Tes dulu

Daftar tes **sebelum** kode. Minimal 5 tes:

| # | Tes | Jenis |
|---|-----|-------|
| 1 | Kasus normal | Aturan |
| 2 | Tepat di batas | Kasus tepi |
| 3 | Satu langkah di atas batas | Kasus tepi |
| 4 | Input salah ditolak, pesan menyebut ID | `pytest.raises` |
| 5 | `test_sample_data` mengunci hasil CSV contoh | Foto hasil |

Pastikan tes gagal (merah) sebelum kode dibuat.

### Langkah 5: Implementasi (Sesi 7)

Satu langkah, satu commit. Setelah setiap langkah:

```bash
pytest modules/11-<fungsi-anda>
```

### Langkah 6: README

Ikuti urutan bagian yang sama dengan modul lain:

1. *The business problem*
2. *The concept*
3. *Step 1: The prompt* (prompt R-C-T-C-O Anda; **batasannya harus sesuai dengan kode**)
4. *Step 2: Run it* (perintah + output persis)
5. *Step 3: How it works*
6. *Verify by hand* (minimal 3 baris dihitung manual)
7. *Common mistakes*
8. *Exercises*

Boleh ditulis dalam Bahasa Indonesia atau Inggris. Tambahkan juga baris modul Anda ke tabel modul di [`README.md`](../../README.md) utama.

### Langkah 7: Selesai berarti hijau

```bash
pytest
```

```bash
ruff check .
```

```bash
ruff format --check .
```

### Langkah 8: Review & commit (Sesi 7)

```
Tinjau semua perubahan di branch ini dibandingkan main (git diff main).
Pakai checklist: benar, teruji, input salah, aman, jelas.
Periksa juga: apakah batasan di prompt README sama dengan perilaku kode?
Apakah ada data pribadi di data/contoh.csv? Urutkan temuan dari yang paling serius.
Jangan ubah file apa pun.
```

Perbaiki temuan penting, lalu periksa riwayat dan pastikan tidak ada file terlarang:

```bash
git log --oneline main..HEAD
```

```bash
git status
```

### Langkah 9: Hitung manfaatnya

```
Waktu manual per bulan   : ... jam
Waktu dengan alat        : ... menit
Hemat per bulan          : ... jam
Risiko yang dikurangi    : (salah hitung, tenggat terlewat, ...)
```

---

## 🎤 Presentasi (Sesi 8, 10 menit per peserta)

1. **Masalah** (1 menit): pekerjaan apa, siapa yang memakai, berapa lama dikerjakan manual.
2. **Aturan bisnis & kasus tepi** (2 menit): tunjukkan kanvas masalah.
3. **Demo** (2 menit): jalankan program pada data contoh, lalu tunjukkan satu input salah yang ditolak.
4. **Bukti** (2 menit): jalankan `pytest -v` pada modul Anda; jelaskan satu tes kasus tepi.
5. **Keamanan data** (1 menit): bagaimana alat ini dipakai pada data asli tanpa melanggar UU PDP.
6. **Manfaat & refleksi** (1 menit): waktu yang dihemat, satu hal yang dipelajari.
7. **Tanya jawab** (1 menit).

---

## 📊 Rubrik Penilaian

| Kriteria | 1 — Belum | 2 — Cukup | 3 — Baik | 4 — Sangat baik |
|----------|-----------|-----------|----------|-----------------|
| **Masalah nyata** *(wajib)* | Contoh buatan tanpa pengguna | Masalah nyata, manfaat tidak jelas | Masalah nyata, pengguna dan manfaat jelas | + manfaat dihitung (jam/bulan) dan sudah dicoba pengguna |
| **Kebenaran** *(wajib)* | Hasil salah | Benar untuk kasus normal | Benar, termasuk kasus tepi; verifikasi manual 3 baris cocok | + perilaku di batas dijelaskan dan disepakati pengguna |
| **Tes** *(wajib)* | < 3 tes atau gagal | 3–4 tes | ≥ 5 tes lulus, termasuk kasus tepi dan `test_sample_data` | + tes ditulis lebih dulu (terlihat di riwayat commit) dan tes input salah |
| **Validasi input** *(wajib)* | Data salah dilewati diam-diam | Error tanpa keterangan | `ValueError` yang menyebut ID baris | + semua kolom penting divalidasi |
| **Keamanan data** *(wajib)* | Ada data pribadi/rahasia asli | — | Hanya data sintetis; tidak ada rahasia di kode | + rencana pemakaian data asli dijelaskan (pertahanan berlapis) |
| **Kerapian & Git** | ruff gagal, 1 commit besar | ruff lulus, commit besar | ruff lulus, beberapa commit kecil dengan pesan jelas | + branch, review terdokumentasi, temuan diperbaiki |
| **README** | Tidak ada | Sebagian bagian | Semua 8 bagian, output persis | + prompt dan kode konsisten, latihan bertingkat |
| **Presentasi** | Tidak jelas | Demo saja | Semua 7 bagian dalam 10 menit | + menjawab pertanyaan dengan bukti (tes/angka) |

**Lulus:** semua kriteria **wajib** minimal skor **3**.

---

<details>
<summary>🔑 <b>Contoh Referensi untuk Fasilitator: Pemeriksa Klaim Reimburse</b></summary>

Program latihan [`latihan/expense_claims.py`](latihan/expense_claims.py) disusun persis seperti proyek akhir yang diharapkan. Gunakan sebagai contoh saat menjelaskan brief di Sesi 6.

**Kanvas masalah**
```
Masalah        : Tim keuangan memeriksa ±200 klaim reimburse per bulan secara manual (± 8 jam).
Pengguna       : Staf keuangan; manajer departemen (melihat total per departemen).
Input          : claim_id,employee_id,department,category,expense_date,submitted_date,amount,receipt
                 C-01,K001,Sales,meal,2026-10-05,2026-10-06,120000,yes   (FIKTIF)
Aturan bisnis  : 1. Diajukan > 30 hari setelah tanggal biaya → REJECTED: late
                 2. >= Rp100.000 tanpa bukti → REJECTED: no receipt
                 3. Di atas batas kategori (meal 150rb, transport 500rb, lodging 1,2jt) → PARTIAL
                 4. Selain itu → APPROVED. Aturan diperiksa berurutan 1 → 4.
Output         : tabel per klaim + total dibayar per departemen
Input salah    : kategori tak dikenal, receipt bukan yes/no, nominal <= 0,
                 tanggal tidak valid, diajukan sebelum tanggal biaya → ValueError "<claim_id>: ..."
Kasus tepi     : tepat 30 hari; tepat Rp100.000 tanpa bukti; tepat di batas kategori;
                 terlambat DAN tanpa bukti
Data sensitif? : data asli memuat nama dan rekening karyawan → tidak dipakai; data contoh fiktif
```

**Prompt R-C-T-C-O yang menghasilkan program ini**
```
ROLE: Kamu adalah developer Python yang membantu tim keuangan.

CONTEXT: Kami memeriksa klaim reimburse dari CSV dengan kolom claim_id, employee_id,
department, category (meal/transport/lodging), expense_date, submitted_date (YYYY-MM-DD),
amount (Rupiah, bilangan bulat), receipt (yes/no). Contoh baris FIKTIF:
C-01,K001,Sales,meal,2026-10-05,2026-10-06,120000,yes

TASK: Buat expense_claims.py yang menentukan status dan jumlah dibayar setiap klaim,
lalu menampilkan total dibayar per departemen. Buat juga test_expense_claims.py.

CONSTRAINTS:
- Aturan diperiksa berurutan: (1) > 30 hari → "REJECTED: late", dibayar 0;
  (2) >= 100000 tanpa bukti → "REJECTED: no receipt", dibayar 0;
  (3) di atas batas kategori (meal 150000, transport 500000, lodging 1200000) → "PARTIAL",
  dibayar sebesar batas; (4) selain itu "APPROVED", dibayar penuh.
- Tepat 30 hari masih tepat waktu. Tepat di batas kategori dibayar penuh.
- Data salah (kategori tak dikenal, receipt bukan yes/no, nominal <= 0, tanggal tidak valid,
  diajukan sebelum tanggal biaya) → ValueError yang diawali claim_id. Jangan lewati diam-diam.
- Hanya library standar Python. Uang sebagai int. Aturan bisnis sebagai fungsi murni.
- @dataclass(frozen=True) untuk satu klaim; argparse dengan file CSV default di data/.

OUTPUT: Kode lengkap kedua file, tes kasus tepi untuk setiap batas, dan test_sample_data.
Jelaskan bagian mana yang paling perlu saya periksa.
```

**Tes yang diharapkan:** lihat [`latihan/kunci/test_expense_claims_kunci.py`](latihan/kunci/test_expense_claims_kunci.py): batas 30/31 hari, batas Rp100.000, batas kategori, urutan aturan, 4 jenis data salah, dan `test_sample_data`.

**Kesalahan umum peserta di proyek akhir:**
- Memilih masalah terlalu besar ("sistem HR lengkap"). Arahkan ke **satu laporan** dengan 3–5 aturan.
- Data contoh tidak memuat kasus tepi, sehingga `test_sample_data` tidak menguji apa pun yang menarik.
- Batasan di prompt README berbeda dengan perilaku kode (misalnya prompt bilang "≥ 30 hari", kode memakai `> 30`).
- Nama file umum (`report.py`) yang bentrok dengan modul lain saat `pytest` dijalankan dari folder utama.
- Ikut meng-commit data asli, file `.xlsx`, atau `.db`. Cek `git status` sebelum setiap commit.

</details>

---

← [Modul 10](modul-10-studi-kasus-lintas-fungsi.md) | **Berikutnya: [Evaluasi →](evaluasi.md)**
