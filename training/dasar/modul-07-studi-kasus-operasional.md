# Modul 7: Studi Kasus Pertama — Operasional

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 7](../01-dasar.md#langkah-7-menjalankan-studi-kasus-pertama-operasional) |
| **Sesi** | Sesi 2 |
| **Durasi** | 20 menit |
| **Prasyarat** | Modul 3 dan Modul 6 |
| **Modul studi kasus** | [`modules/01-operations`](../../modules/01-operations/) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan konsep *reorder point* (titik pemesanan ulang).
2. Menjalankan program studi kasus dan membaca setiap kolom hasilnya.
3. Melihat pengaruh perubahan data terhadap hasil.
4. Memahami pola **data masuk → aturan → hasil keluar**.

---

## 📖 Materi

### A. Masalah bisnis

Tim gudang mengecek stok setiap pagi di spreadsheet. Kadang barang **habis** karena terlambat memesan, kadang **menumpuk** karena memesan "jaga-jaga". Mereka butuh daftar harian: **barang apa yang harus dipesan sekarang, mulai dari yang paling mendesak**.

### B. Konsep reorder point, dengan analogi galon air

Kantor Anda memakai **2 galon air per hari**. Depot butuh **6 hari** untuk mengantar. Agar aman, Anda menyimpan **4 galon cadangan**.

```
reorder point = (pemakaian harian × waktu antar) + stok pengaman
              = (2 × 6) + 4
              = 16 galon
```

Begitu sisa galon **16 atau kurang**, saatnya memesan. Jika menunggu sampai 10 galon, air habis sebelum kiriman datang.

| Istilah di data | Arti |
|-----------------|------|
| `on_hand` | Stok saat ini |
| `avg_daily_usage` | Rata-rata pemakaian per hari |
| `lead_time_days` | Waktu antar dari pemasok (hari) |
| `safety_stock` | Stok pengaman |
| **Reorder pt** | Titik pemesanan ulang (dihitung) |
| **Days left** | Perkiraan sisa hari stok bertahan = `on_hand ÷ avg_daily_usage` |

### C. Pola semua program: data → aturan → hasil

```
 data/inventory.csv  ──▶  aturan: on_hand ≤ reorder point?  ──▶  daftar barang yang dipesan
      (DATA)                         (ATURAN)                           (HASIL)
```

Jika hasilnya terasa aneh, periksa ketiganya: **datanya** benar? **aturannya** benar? **cara membacanya** benar?

---

## 🛠️ Praktik Terpandu

1. Baca bagian "The business problem" di [`modules/01-operations/README.md`](../../modules/01-operations/README.md).
2. Lihat datanya:

   ```bash
   cat modules/01-operations/data/inventory.csv
   ```

3. Jalankan program:

   ```bash
   python3 modules/01-operations/inventory_reorder.py
   ```

   Hasilnya:

   ```
   SKU      Item                  On hand Reorder pt Days left
   SKU-006  Pallet Wrap                 3         16       1.5
   SKU-004  Cardboard Box M            55         68       4.6
   SKU-002  Printer Toner               8         16       5.3
   ```

4. Baca hasilnya bersama: **Pallet Wrap** paling atas karena stoknya hanya cukup **1,5 hari**, jadi paling mendesak.
5. Tanyakan ke Claude:

   ```
   Di @modules/01-operations/inventory_reorder.py, bagian mana yang menghitung reorder point
   dan bagian mana yang mengurutkan hasil? Jelaskan dengan bahasa orang gudang.
   ```

---

## 🏋️ Latihan

> ⚠️ Latihan ini **mengubah data contoh**. Setelah selesai, **kembalikan** file seperti semula dengan perintah di bagian akhir latihan; jika tidak, tes otomatis modul ini akan gagal.

### ⭐ Latihan 7.1: Stok kertas menipis

Di `modules/01-operations/data/inventory.csv`, ubah `on_hand` untuk `SKU-001` (A4 Paper) dari `120` menjadi `90`. Simpan, lalu jalankan program lagi.
- Apakah A4 Paper muncul? Di urutan ke berapa? Mengapa?

### ⭐⭐ Latihan 7.2: Tepat di batas

Ubah `on_hand` untuk `SKU-003` (Packing Tape) dari `40` menjadi `28`. Jalankan lagi.
- Hitung reorder point Packing Tape secara manual. Apakah barang ini muncul? Apa artinya bagi aturan `≤`?

### ⭐⭐ Latihan 7.3: Hitung semua secara manual

Lengkapi tabel ini **dengan data asli** (sebelum diubah), lalu bandingkan dengan hasil program:

| SKU | Pemakaian/hari | Waktu antar | Stok pengaman | Reorder point | Stok | Pesan? |
|-----|----------------|-------------|---------------|---------------|------|--------|
| SKU-001 | 15 | 5 | 30 | | 120 | |
| SKU-002 | 1,5 | 7 | 5 | | 8 | |
| SKU-003 | 6 | 3 | 10 | | 40 | |
| SKU-004 | 12 | 4 | 20 | | 55 | |
| SKU-005 | 10 | 10 | 50 | | 200 | |
| SKU-006 | 2 | 6 | 4 | | 3 | |

### ⭐⭐⭐ Latihan 7.4: Angka yang dibulatkan

Program menampilkan reorder point Printer Toner sebagai **16**. Hitung sendiri: 1,5 × 7 + 5 = ? Mengapa tampilannya 16? Apakah ini masalah? Tanyakan juga ke Claude.

**Kembalikan data seperti semula** setelah semua latihan:

```bash
git checkout -- modules/01-operations/data/inventory.csv
```

Pastikan tes kembali lulus:

```bash
pytest modules/01-operations
```

---

## 📝 Kuis

1. Pemakaian 10 unit/hari, waktu antar 3 hari, stok pengaman 5. Berapa reorder point-nya?
2. Mengapa hasil diurutkan berdasarkan *days left*, bukan berdasarkan jumlah stok?
3. Barang dengan stok **tepat sama** dengan reorder point: dipesan atau tidak?
4. Apa yang terjadi pada tes otomatis jika data contoh diubah dan tidak dikembalikan?

---

## 📌 Ringkasan

- **Reorder point** = pemakaian harian × waktu antar + stok pengaman.
- Program = **data → aturan → hasil**. Hasil aneh? Periksa ketiganya.
- Batas `≤` berarti stok **tepat di** reorder point juga dipesan.
- **Tampilan** angka bisa dibulatkan, walaupun perhitungan di dalamnya tepat.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 7.1:** A4 Paper muncul di **urutan ke-4 (terakhir)**. Reorder point = 15 × 5 + 30 = **105**; stok 90 ≤ 105, jadi harus dipesan. Sisa hari = 90 ÷ 15 = **6,0**, paling longgar dibanding tiga barang lain, sehingga di urutan terakhir.
```
SKU      Item                  On hand Reorder pt Days left
SKU-006  Pallet Wrap                 3         16       1.5
SKU-004  Cardboard Box M            55         68       4.6
SKU-002  Printer Toner               8         16       5.3
SKU-001  A4 Paper (ream)            90        105       6.0
```

**Latihan 7.2:** Reorder point Packing Tape = 6 × 3 + 10 = **28**. Stok 28 **≤** 28, jadi **muncul** (sisa 28 ÷ 6 = 4,7 hari). Ini membuktikan aturan memakai "kurang dari **atau sama dengan**". Jika programnya memakai `<`, barang ini tidak akan muncul dan berisiko kehabisan.

**Latihan 7.3**

| SKU | Reorder point | Stok | Pesan? |
|-----|---------------|------|--------|
| SKU-001 | 15 × 5 + 30 = **105** | 120 | Tidak |
| SKU-002 | 1,5 × 7 + 5 = **15,5** | 8 | **Ya** |
| SKU-003 | 6 × 3 + 10 = **28** | 40 | Tidak |
| SKU-004 | 12 × 4 + 20 = **68** | 55 | **Ya** |
| SKU-005 | 10 × 10 + 50 = **150** | 200 | Tidak |
| SKU-006 | 2 × 6 + 4 = **16** | 3 | **Ya** |

Tiga barang dipesan: SKU-002, SKU-004, SKU-006, sama dengan hasil program. ✔

**Latihan 7.4:** 1,5 × 7 + 5 = **15,5**. Program menghitung 15,5 dengan tepat, tetapi **menampilkannya** tanpa desimal (format `.0f`), sehingga dibulatkan menjadi 16. Keputusan pesan/tidak tetap memakai 15,5, jadi hasilnya benar. Namun bagi pembaca laporan, tampilan ini bisa membingungkan; Anda bisa meminta Claude menampilkan satu angka desimal.

**Kuis**
1. 10 × 3 + 5 = **35**.
2. Karena yang penting adalah **berapa lama stok bertahan**. Stok 55 kotak bisa lebih mendesak daripada 8 toner jika kotak dipakai jauh lebih cepat.
3. **Dipesan**, karena aturannya `≤`.
4. Tes `test_sample_data` **gagal**, karena hasilnya tidak lagi sama dengan yang diharapkan. Tes sedang menjaga data contoh.

</details>

---

← [Modul 6](modul-06-membaca-kode.md) | **Berikutnya: [Modul 8: Memverifikasi Hasil (Keuangan) →](modul-08-verifikasi-keuangan.md)**
