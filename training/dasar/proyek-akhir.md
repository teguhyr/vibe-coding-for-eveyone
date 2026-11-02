# 🏆 Proyek Akhir Level 1: Saran Jumlah Pesan

| | |
|---|---|
| **Rencana training** | [Proyek Akhir Level 1](../01-dasar.md#-proyek-akhir-level-1) |
| **Sesi** | Dimulai mandiri → klinik di **Sesi 3** → presentasi di **Sesi 4** |
| **Durasi** | ± 4 jam (2 jam mandiri + Sesi 3) |
| **Prasyarat** | Modul 1–10 selesai, branch `latihan-saya` sudah ada (Modul 9–10) |

## 🎯 Tujuan

Membuktikan bahwa Anda bisa menjalankan **seluruh siklus vibe coding sendiri**: menulis prompt, membiarkan AI membuat perubahan, memverifikasi hasil, dan menyimpan pekerjaan. Semua dilakukan **hanya dengan prompt**, tanpa mengetik kode sendiri.

---

## 📋 Brief Proyek

Tim pembelian senang dengan laporan reorder (Modul 7), tetapi mereka bertanya:

> *"Oke, kami tahu barang mana yang harus dipesan. Tapi **berapa banyak** yang harus dipesan?"*

**Tugas Anda:** tambahkan kolom **"Saran Jumlah Pesan"** ke laporan di [`modules/01-operations/inventory_reorder.py`](../../modules/01-operations/inventory_reorder.py), yaitu jumlah yang harus dipesan agar stok cukup untuk **30 hari**.

**Aturan bisnis** (dari tim pembelian):
- `saran = (pemakaian harian × 30) − stok sekarang`
- Hasil **dibulatkan ke atas** (tidak bisa memesan setengah kotak)
- Hasil **tidak boleh negatif**; jika stok sudah cukup, sarannya 0

---

## 🪜 Langkah Pengerjaan

### Langkah 1: Siapkan branch

```bash
git switch latihan-saya
```

### Langkah 2: Tulis prompt R-C-T-C-O

Tulis prompt Anda sendiri dengan kelima bagian. Kerangka berikut boleh dipakai, tetapi **isi sendiri** bagian yang kosong:

```
ROLE: ...

CONTEXT: File modules/01-operations/inventory_reorder.py membuat daftar barang yang
perlu dipesan dari data/inventory.csv (kolom: ...).

TASK: Tambahkan kolom "Order" (saran jumlah pesan) ke tabel hasil.

CONSTRAINTS:
- Rumus: ...
- Pembulatan: ...
- Tidak boleh negatif: ...
- Contoh perhitungan: ...
- Jangan ubah perilaku lain. Tes yang ada harus tetap lulus.

OUTPUT: ...
```

Periksa dengan [checklist prompt di Modul 5](modul-05-prompt-rctco.md#f-checklist-sebelum-menekan-enter) sebelum dikirim.

### Langkah 3: Kirim ke Claude dan tinjau perubahannya

Baca *diff* dengan [3 pertanyaan di Modul 9](modul-09-perubahan-kecil.md#b-membaca-diff) sebelum menyetujui.

### Langkah 4: Jalankan dan verifikasi "Cek 3 Baris"

```bash
python3 modules/01-operations/inventory_reorder.py
```

Isi tabel verifikasi manual ini:

| SKU | Pemakaian/hari × 30 | − Stok | = Saran (dibulatkan ke atas, min 0) | Hasil program | Cocok? |
|-----|---------------------|--------|--------------------------------------|---------------|--------|
| | | | | | |
| | | | | | |
| | | | | | |

### Langkah 5: Pastikan tes lulus

```bash
pytest modules/01-operations
```

### Langkah 6: Simpan dengan Git

```bash
git status
```

```bash
git add modules/01-operations/inventory_reorder.py
```

```bash
git commit -m "Tambah kolom saran jumlah pesan untuk stok 30 hari"
```

### Langkah 7: Tulis refleksi (5 kalimat)

1. Apa yang berhasil pada percobaan pertama?
2. Apa yang harus diulang atau diperbaiki?
3. Bagian prompt mana yang paling menentukan hasil?
4. Apa yang akan Anda tulis berbeda di prompt berikutnya?
5. Pekerjaan apa di unit Anda yang ingin Anda otomatiskan berikutnya? (lihat [Latihan 1.1](modul-01-pola-pikir.md#-latihan-11-peta-pekerjaan-berulang))

---

## 🌟 Tantangan Tambahan (opsional, untuk Sesi 3)

Sudah selesai lebih cepat? Pilih tantangan sesuai fungsi Anda. Pakai cara yang sama: branch → prompt → verifikasi → commit.

| Fungsi | Modul | Tantangan |
|--------|-------|-----------|
| Keuangan | [02-finance](../../modules/02-finance/) | Ekspor baris yang ditandai (OVER/UNDER/UNBUDGETED) ke `flagged.csv` |
| HR | [03-hr](../../modules/03-hr/) | Tampilkan karyawan yang sisa cutinya ≤ 2 hari |
| Marketing | [04-marketing](../../modules/04-marketing/) | Tambahkan ringkasan total biaya dan total pendapatan semua kampanye |
| IT | [05-it](../../modules/05-it/) | Tampilkan rata-rata jam penyelesaian per prioritas |
| Akuntansi | [06-accounting](../../modules/06-accounting/) | Tampilkan jumlah total transaksi yang cocok (bukan hanya banyaknya) |
| Legal | [07-legal](../../modules/07-legal/) | Tambahkan kolom "sisa hari menuju tenggat" |
| Pengadaan | [08-procurement](../../modules/08-procurement/) | Tampilkan selisih harga vendor terpilih dengan vendor termurah |
| Layanan pelanggan | [09-customer-service](../../modules/09-customer-service/) | Tambahkan kata kunci Bahasa Indonesia: `tagihan`, `pengiriman`, `kata sandi` |
| General Affairs | [10-general-affairs](../../modules/10-general-affairs/) | Tampilkan total jam pemakaian per ruang |

---

## 🎤 Presentasi (Sesi 4, 5 menit per peserta)

1. **Masalah** (30 detik): apa yang diminta tim pembelian?
2. **Prompt** (1 menit): tunjukkan prompt R-C-T-C-O Anda.
3. **Demo** (1,5 menit): jalankan program, tunjukkan kolom baru.
4. **Verifikasi** (1 menit): tunjukkan tabel "Cek 3 Baris".
5. **Refleksi** (1 menit): satu hal yang Anda pelajari.

---

## 📊 Rubrik Penilaian

| Kriteria | 1 — Belum | 2 — Cukup | 3 — Baik | 4 — Sangat baik |
|----------|-----------|-----------|----------|-----------------|
| **Prompt R-C-T-C-O** *(wajib)* | Kurang dari 3 bagian | 3–4 bagian | 5 bagian lengkap | 5 bagian + contoh perhitungan + kasus "tidak boleh negatif" disebut jelas |
| **Program berjalan** *(wajib)* | Error | Berjalan, kolom salah | Berjalan, kolom benar | Benar, dan perilaku lama tidak berubah |
| **Verifikasi** *(wajib)* | Tidak ada | 1–2 baris | 3 baris cocok | 3 baris cocok, termasuk satu kasus tepi (saran 0) |
| **Git** *(wajib)* | Tidak di-commit | Commit dengan pesan buruk / ikut file hasil | Commit hanya file kode, pesan jelas | Beberapa commit kecil, pesan jelas |
| **Tes** | Tes gagal | — | Tes lulus | Tes lulus, dan bisa menjelaskan apa yang diuji |
| **Refleksi & presentasi** | Tidak ada | Refleksi umum | 5 kalimat sesuai panduan | Refleksi tajam + rencana otomatisasi berikutnya |

**Lulus:** semua kriteria **wajib** minimal skor **3**.

---

<details>
<summary>🔑 <b>Kunci Referensi untuk Fasilitator</b></summary>

**Hasil yang diharapkan** (dengan data contoh asli):
```
SKU      Item                  On hand Reorder pt Days left  Order
SKU-006  Pallet Wrap                 3         16       1.5     57
SKU-004  Cardboard Box M            55         68       4.6    305
SKU-002  Printer Toner               8         16       5.3     37
```

**Verifikasi manual:**

| SKU | Pemakaian × 30 | − Stok | = Saran |
|-----|----------------|--------|---------|
| SKU-006 | 2 × 30 = 60 | − 3 | **57** |
| SKU-004 | 12 × 30 = 360 | − 55 | **305** |
| SKU-002 | 1,5 × 30 = 45 | − 8 | **37** |

**Kasus tepi "tidak boleh negatif":** barang dengan stok 100 dan pemakaian 2/hari → 60 − 100 = −40 → saran **0**. Barang seperti ini tidak muncul di laporan karena stoknya di atas reorder point, jadi minta peserta mengujinya dengan bertanya ke Claude atau lewat tes.

**Contoh implementasi yang sudah diuji** (nama dan detail buatan Claude bisa berbeda):
```python
TARGET_COVER_DAYS = 30


def suggested_order_qty(item: Item, cover_days: int = TARGET_COVER_DAYS) -> int:
    """Jumlah yang perlu dipesan agar stok cukup untuk `cover_days` hari."""
    needed = item.avg_daily_usage * cover_days - item.on_hand
    return max(0, math.ceil(needed))  # dibulatkan ke atas, tidak pernah negatif
```
Ditambah `import math` di bagian atas file, dan kolom `Order` di baris `print` pada `main()`.

**Kesalahan umum peserta:**
- Lupa pembulatan ke atas → saran desimal seperti `37.0`, atau dibulatkan ke bawah.
- Lupa batas minimum 0 → kode tidak menangani stok berlebih.
- Ikut meng-commit `pesan_ulang.csv` dari Modul 9.
- Mengubah urutan atau isi tabel sehingga `test_sample_data` gagal.

</details>

---

← [Modul 10](modul-10-git.md) | **Berikutnya: [Evaluasi →](evaluasi.md)**
