# Modul 8: Memverifikasi Hasil — Keuangan

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 8](../01-dasar.md#langkah-8-memverifikasi-hasil-keuangan) |
| **Sesi** | Sesi 2 |
| **Durasi** | 25 menit |
| **Prasyarat** | Modul 7 |
| **Modul studi kasus** | [`modules/02-finance`](../../modules/02-finance/) |
| **Perlengkapan** | Excel / Google Sheets / kalkulator |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menerapkan aturan **"Cek 3 Baris"** pada setiap laporan buatan program.
2. Memilih baris yang tepat untuk diverifikasi: normal, ekstrem, dan kasus tepi.
3. Memverifikasi hasil program dengan Excel.
4. Menjelaskan mengapa uang dihitung dengan `Decimal`, bukan `float`.

---

## 📖 Materi

### A. Mengapa verifikasi wajib?

Anda tidak akan langsung mengirim laporan buatan **staf baru** ke direksi tanpa memeriksanya. Perlakukan hasil program buatan AI dengan cara yang sama.

> Program yang **berjalan tanpa error** belum tentu **benar**. Hanya verifikasi yang bisa membuktikannya.

### B. Aturan "Cek 3 Baris"

Sebelum mempercayai laporan, hitung **minimal 3 baris** secara manual. Pilih baris dengan cerdas:

| Jenis baris | Contoh di laporan anggaran | Mengapa dipilih |
|-------------|---------------------------|-----------------|
| **1. Normal** | Operations / Fuel | Memastikan rumus dasar benar |
| **2. Ekstrem** | Marketing / Digital Ads (−22,5%) | Memastikan tanda +/− dan status UNDER benar |
| **3. Kasus tepi** | IT / Cloud Hosting (anggaran 0) | Di sinilah bug paling sering bersembunyi |

Jika ketiganya cocok, kepercayaan Anda naik. **Jika satu saja meleset, berhenti dan selidiki** sebelum laporan dipakai.

### C. Konsep selisih anggaran (*variance*)

```
selisih   = realisasi − anggaran            (positif = boros / melebihi anggaran)
selisih % = selisih ÷ anggaran × 100
```

| Status | Aturan (ambang default 10%) |
|--------|-----------------------------|
| `OVER` | selisih % **lebih dari** +10% |
| `UNDER` | selisih % **kurang dari** −10% |
| `OK` | di antara −10% dan +10%, **termasuk tepat** ±10% |
| `UNBUDGETED` | anggaran 0, tetapi ada realisasi |

### D. Mengapa `Decimal`, bukan `float`?

Komputer menyimpan angka `float` dalam bentuk biner, sehingga beberapa pecahan tidak bisa disimpan persis:

```bash
python3 -c "print(0.1 + 0.2)"
```
```
0.30000000000000004
```

```bash
python3 -c "from decimal import Decimal; print(Decimal('0.1') + Decimal('0.2'))"
```
```
0.3
```

Selisih kecil ini, jika terjadi pada ribuan transaksi, bisa membuat laporan **tidak balance**. Karena itu modul keuangan dan akuntansi memakai `Decimal`.

---

## 🛠️ Praktik Terpandu

1. Jalankan laporan:

   ```bash
   python3 modules/02-finance/budget_variance.py
   ```

   ```
   Department   Category                Budget      Actual    Variance    Var %  Status
   ------------------------------------------------------------------------------------
   Operations   Fuel                 50,000.00   58,000.00   +8,000.00   +16.0%  OVER
   Operations   Maintenance          30,000.00   28,500.00   -1,500.00    -5.0%  OK
   Marketing    Digital Ads          40,000.00   31,000.00   -9,000.00   -22.5%  UNDER
   Marketing    Events               25,000.00   26,000.00   +1,000.00    +4.0%  OK
   HR           Training             15,000.00   18,000.00   +3,000.00   +20.0%  OVER
   IT           Software Licenses    20,000.00   20,000.00       +0.00    +0.0%  OK
   IT           Cloud Hosting             0.00    3,500.00   +3,500.00      n/a  UNBUDGETED

   Totals by department
   Operations     80,000.00   86,500.00   +6,500.00    +8.1%
   Marketing      65,000.00   57,000.00   -8,000.00   -12.3%
   HR             15,000.00   18,000.00   +3,000.00   +20.0%
   IT             20,000.00   23,500.00   +3,500.00   +17.5%
   ```

2. Buka `modules/02-finance/data/budget_vs_actual.csv` di Excel. Kolom A–D berisi: department, category, budget, actual.
3. Tambahkan rumus verifikasi di baris 2, lalu tarik ke bawah:

   | Kolom | Judul | Rumus (Excel bahasa Inggris) |
   |-------|-------|------------------------------|
   | E | Selisih | `=D2-C2` |
   | F | Selisih % | `=IF(C2=0,"n/a",E2/C2)` (format sebagai persen) |
   | G | Status | `=IF(C2=0,IF(D2>0,"UNBUDGETED","OK"),IF(F2>10%,"OVER",IF(F2<-10%,"UNDER","OK")))` |

   > Excel berbahasa Indonesia memakai `JIKA` untuk `IF` dan titik koma `;` sebagai pemisah, mis. `=JIKA(C2=0;"n/a";E2/C2)`.

4. Bandingkan kolom E–G dengan hasil program untuk **3 baris pilihan** (normal, ekstrem, kasus tepi).

---

## 🏋️ Latihan

### ⭐ Latihan 8.1: Cek 3 Baris

Verifikasi manual tiga baris: **Operations/Fuel**, **Marketing/Digital Ads**, **IT/Cloud Hosting**. Tuliskan perhitungan Anda.

### ⭐⭐ Latihan 8.2: Ubah ambang batas

Jalankan dengan ambang 5% dan 20%:

```bash
python3 modules/02-finance/budget_variance.py --threshold 5
```

```bash
python3 modules/02-finance/budget_variance.py --threshold 20
```

**Sebelum menjalankan**, tebak status setiap baris. Lalu bandingkan dengan hasil program. Adakah yang mengejutkan?

### ⭐⭐ Latihan 8.3: Verifikasi total

Hitung manual total per departemen untuk **Operations** dan **Marketing** (anggaran, realisasi, selisih, %). Cocokkan dengan bagian "Totals by department".

### ⭐⭐⭐ Latihan 8.4: Tanya "mengapa" ke Claude

```
Mengapa @modules/02-finance/budget_variance.py memakai Decimal, bukan float?
Beri contoh angka anggaran yang hasilnya salah jika memakai float.
```

Lalu tanyakan: *"Mengapa IT/Cloud Hosting berstatus UNBUDGETED, bukan OVER?"* Tulis jawabannya dengan kata-kata Anda sendiri.

---

## 📝 Kuis

1. Tiga jenis baris apa yang dipilih untuk "Cek 3 Baris"?
2. Anggaran 25.000, realisasi 27.500. Berapa selisih %, dan apa statusnya (ambang 10%)?
3. Mengapa `0.1 + 0.2` di Python dengan `float` tidak menghasilkan tepat `0.3`?
4. Jika satu dari tiga baris yang Anda cek tidak cocok, apa yang harus dilakukan?

---

## 📌 Ringkasan

- **"Cek 3 Baris"**: normal, ekstrem, **kasus tepi**. Satu tidak cocok? Berhenti dan selidiki.
- Perhatikan **batas**: tepat ±10% masih `OK`. Batas adalah tempat bug bersembunyi.
- Uang dihitung dengan `Decimal` agar tidak ada selisih pembulatan.
- Excel adalah alat verifikasi yang bagus untuk hasil program.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 8.1**

| Baris | Selisih | Selisih % | Status |
|-------|---------|-----------|--------|
| Operations/Fuel | 58.000 − 50.000 = **+8.000** | 8.000 ÷ 50.000 = **+16%** | > 10% → **OVER** ✔ |
| Marketing/Digital Ads | 31.000 − 40.000 = **−9.000** | −9.000 ÷ 40.000 = **−22,5%** | < −10% → **UNDER** ✔ |
| IT/Cloud Hosting | 3.500 − 0 = **+3.500** | tidak bisa dibagi 0 → **n/a** | anggaran 0, ada realisasi → **UNBUDGETED** ✔ |

**Latihan 8.2**
- **Ambang 5%:** hasilnya **sama persis** dengan ambang 10%. Ini mengejutkan! Maintenance tepat **−5,0%**, dan aturannya "kurang dari −5%", sehingga **tepat −5% masih OK**. Events (+4%) juga tetap OK.
- **Ambang 20%:** Fuel (+16%) menjadi **OK**. HR Training tepat **+20,0%** juga menjadi **OK** karena aturannya "lebih dari 20%". Digital Ads (−22,5%) tetap **UNDER**.

Pelajarannya: **angka yang tepat di batas** selalu layak dicek, dan aturan "lebih dari" vs "lebih dari atau sama dengan" harus ditulis jelas di prompt.

**Latihan 8.3**
- **Operations:** anggaran 50.000 + 30.000 = 80.000; realisasi 58.000 + 28.500 = 86.500; selisih **+6.500**; 6.500 ÷ 80.000 = **+8,1%** ✔
- **Marketing:** anggaran 40.000 + 25.000 = 65.000; realisasi 31.000 + 26.000 = 57.000; selisih **−8.000**; −8.000 ÷ 65.000 = **−12,3%** ✔

**Latihan 8.4: poin jawaban:** Cloud Hosting tidak punya anggaran (0), sehingga persentase tidak bisa dihitung (pembagian dengan nol). Label `OVER` akan menyesatkan karena tidak ada pembandingnya. `UNBUDGETED` memberi tahu bahwa ada **pengeluaran yang tidak direncanakan**, yang justru sering menjadi temuan paling penting.

**Kuis**
1. Baris **normal**, baris **ekstrem**, dan baris **kasus tepi**.
2. Selisih 2.500; 2.500 ÷ 25.000 = **+10%**. Status **OK**, karena tepat 10% tidak "lebih dari" 10%.
3. `float` disimpan dalam bentuk biner, dan 0,1 tidak bisa direpresentasikan persis dalam biner, sehingga muncul selisih kecil.
4. **Berhenti**, jangan pakai laporannya. Cari penyebabnya: data, aturan, atau cara membaca. Tanyakan ke Claude dengan contoh baris yang tidak cocok.

</details>

---

← [Modul 7](modul-07-studi-kasus-operasional.md) | **Berikutnya: [Modul 9: Meminta Perubahan Kecil ke AI →](modul-09-perubahan-kecil.md)**
