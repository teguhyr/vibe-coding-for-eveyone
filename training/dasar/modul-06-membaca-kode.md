# Modul 6: Membaca Kode Tanpa Takut

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 6](../01-dasar.md#langkah-6-membaca-kode-tanpa-takut) |
| **Sesi** | Sesi 2 |
| **Durasi** | 30 menit |
| **Prasyarat** | Modul 3 (menjalankan program dari terminal) |
| **File latihan** | [`latihan/penjualan.py`](latihan/penjualan.py), [`latihan/data/penjualan_cabang.csv`](latihan/data/penjualan_cabang.csv) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Mengenali 6 bahan dasar program: variabel, tipe data, list/dictionary, if, for, fungsi.
2. Membaca program pendek baris demi baris dan menebak hasilnya.
3. Mengubah nilai dan aturan sederhana, lalu memeriksa hasilnya.
4. Membaca 2 pesan error paling umum: `IndentationError` dan `NameError`.

> 💡 **Anda tidak perlu menghafal.** Tujuannya **mengenali**, sehingga Anda bisa mengikuti penjelasan AI dan menilai apakah kodenya masuk akal.

---

## 📖 Materi

### A. Variabel: label pada kotak

```python
target = 80_000_000
nama_cabang = "Jakarta"
```

`target` adalah **nama label**; `80_000_000` adalah **isinya**. Garis bawah `_` di angka hanya agar mudah dibaca (sama dengan 80.000.000).

### B. Tipe data: jenis isi kotak

| Tipe | Contoh | Dipakai untuk |
|------|--------|---------------|
| Bilangan bulat (`int`) | `120`, `80_000_000` | Jumlah barang, Rupiah tanpa sen |
| Bilangan desimal (`float`) | `1.5`, `0.25` | Rata-rata, persentase |
| Teks (`str`) | `"Jakarta"`, `'SKU-001'` | Nama, kode |
| Benar/salah (`bool`) | `True`, `False` | Hasil pengecekan |

> ⚠️ Python memakai **titik** untuk desimal (`1.5`), bukan koma.

### C. List dan dictionary: daftar dan kamus

```python
cabang = ["Jakarta", "Surabaya", "Medan"]  # list: daftar berurutan
penjualan = {"Jakarta": 120_000_000, "Medan": 40_000_000}  # dictionary: kunci → nilai
```

- **List** seperti satu **kolom** di Excel.
- **Dictionary** seperti tabel dua kolom, misalnya **nama cabang → nilai penjualan**. Ambil nilainya dengan `penjualan["Jakarta"]`.

### D. If: aturan "jika... maka..."

```python
if nilai >= target:
    status = "TERCAPAI"
elif nilai >= target * 0.9:
    status = "HAMPIR"
else:
    status = "BELUM"
```

| Simbol | Arti |
|--------|------|
| `>=` / `<=` | lebih dari atau sama dengan / kurang dari atau sama dengan |
| `>` / `<` | lebih dari / kurang dari |
| `==` / `!=` | sama dengan / tidak sama dengan |

Mirip rumus Excel `=IF(B2>=C2, "TERCAPAI", "BELUM")`.

### E. For: "untuk setiap baris..."

```python
for nama, nilai in penjualan.items():
    print(nama, nilai)
```

Artinya: **untuk setiap** pasangan nama dan nilai di `penjualan`, tampilkan keduanya. Sama seperti menarik rumus Excel ke bawah untuk semua baris.

### F. Fungsi: resep yang bisa dipakai berulang

```python
def status_cabang(nilai: int, target: int) -> str:
    if nilai >= target:
        return "TERCAPAI"
    return "BELUM"
```

| Bagian | Arti |
|--------|------|
| `def status_cabang` | Membuat resep bernama `status_cabang` |
| `(nilai: int, target: int)` | Bahan yang dibutuhkan, dan jenisnya |
| `-> str` | Resep ini menghasilkan teks |
| `return "TERCAPAI"` | Hasil yang dikembalikan |

Memakainya: `status_cabang(85_000_000, 80_000_000)` menghasilkan `"TERCAPAI"`.

### G. Indentasi (jarak di awal baris) itu wajib

Baris di dalam `if`, `for`, dan `def` **harus menjorok 4 spasi**. Jika lupa:

```
  File "latihan.py", line 3
    print("TERCAPAI")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```

Artinya: setelah `if` di baris 2, Python mengharapkan baris yang menjorok.

### H. Salah ketik nama variabel

```
NameError: name 'targat' is not defined. Did you mean: 'target'?
```

Python bahkan menyarankan nama yang benar. **Baca pesan error dari baris terakhir.**

---

## 🛠️ Praktik Terpandu

1. Buka [`latihan/penjualan.py`](latihan/penjualan.py) di VS Code:

   ```python
   # Latihan Modul 6: membaca dan mengubah kode sederhana.
   # Data contoh (fiktif): penjualan per cabang dalam Rupiah.
   penjualan = {"Jakarta": 120_000_000, "Surabaya": 85_000_000, "Medan": 40_000_000}
   target = 80_000_000


   def status_cabang(nilai: int, target: int) -> str:
       if nilai >= target:
           return "TERCAPAI"
       return "BELUM"


   for cabang, nilai in penjualan.items():
       print(f"{cabang:<10} Rp{nilai:>13,}  {status_cabang(nilai, target)}")
   ```

2. **Sebelum menjalankan**, tebak: cabang mana yang TERCAPAI?
3. Jalankan dari folder utama repositori:

   ```bash
   python3 training/dasar/latihan/penjualan.py
   ```

   Hasilnya:

   ```
   Jakarta    Rp  120,000,000  TERCAPAI
   Surabaya   Rp   85,000,000  TERCAPAI
   Medan      Rp   40,000,000  BELUM
   ```

4. Baca baris `print(f"...")` bersama fasilitator:
   - `f"..."` adalah teks yang bisa diisi nilai variabel di dalam `{ }`.
   - `{cabang:<10}`: nama cabang, **rata kiri**, lebar 10 karakter.
   - `{nilai:>13,}`: angka, **rata kanan**, lebar 13, dengan **pemisah ribuan**.

5. **Sengaja buat error:** hapus 4 spasi di depan `return "TERCAPAI"`, simpan, jalankan. Baca pesan error-nya, lalu kembalikan spasinya.

---

## 🏋️ Latihan

Kerjakan pada **salinan** file agar file asli tetap utuh:

```bash
cp training/dasar/latihan/penjualan.py latihan_saya.py
```

Di Windows PowerShell: `Copy-Item training\dasar\latihan\penjualan.py latihan_saya.py`. Jalankan dengan `python3 latihan_saya.py`.

### ⭐ Latihan 6.1: Ubah target

Ubah `target` menjadi `100_000_000`. Cabang mana yang berubah status?

### ⭐⭐ Latihan 6.2: Format Rupiah Indonesia

Python menampilkan `120,000,000` (koma). Ubah agar menjadi `Rp120.000.000` (titik). Coba sendiri dulu, lalu minta bantuan Claude:

```
Di @latihan_saya.py, ubah format angka agar memakai titik sebagai pemisah ribuan
seperti di Indonesia (Rp120.000.000). Jelaskan perubahannya baris per baris.
```

### ⭐⭐ Latihan 6.3: Tambah status "HAMPIR"

Tambahkan aturan: jika penjualan **≥ 90% target** tetapi belum mencapai target, statusnya **HAMPIR**. Uji dengan mengubah penjualan Medan menjadi `75_000_000`.

### ⭐⭐⭐ Latihan 6.4: Baca dari file CSV

Ubah program agar membaca data dari [`latihan/data/penjualan_cabang.csv`](latihan/data/penjualan_cabang.csv) (5 cabang), lalu tampilkan juga **total penjualan**, **cabang terbaik**, dan **jumlah cabang yang mencapai target**. Gunakan prompt R-C-T-C-O dari Modul 5.

---

## 📝 Kuis

1. Apa perbedaan list dan dictionary?
2. Apa hasil `status_cabang(80_000_000, 80_000_000)`? Mengapa?
3. Anda melihat `IndentationError`. Apa yang biasanya salah?
4. Apa arti `{nilai:>13,}` di dalam `print(f"...")`?

---

## 📌 Ringkasan

- 6 bahan dasar: **variabel, tipe data, list/dictionary, if, for, fungsi**.
- Indentasi 4 spasi **wajib** di dalam `if`, `for`, `def`.
- Baca pesan error **dari baris terakhir**; Python sering memberi petunjuk perbaikannya.
- Tebak hasil **sebelum** menjalankan program. Ini melatih Anda memverifikasi.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 6.1:** **Surabaya** berubah dari TERCAPAI menjadi **BELUM** (85 juta < 100 juta).
```
Jakarta    Rp  120,000,000  TERCAPAI
Surabaya   Rp   85,000,000  BELUM
Medan      Rp   40,000,000  BELUM
```

**Latihan 6.2 & 6.3:** lihat [`latihan/kunci/penjualan_titik.py`](latihan/kunci/penjualan_titik.py). Inti perubahannya:
```python
def format_rupiah(nilai: int) -> str:
    # Python memakai koma sebagai pemisah ribuan; ganti dengan titik ala Indonesia.
    return "Rp" + f"{nilai:,}".replace(",", ".")


def status_cabang(nilai: int, target: int) -> str:
    if nilai >= target:
        return "TERCAPAI"
    elif nilai >= target * 0.9:
        return "HAMPIR"
    return "BELUM"
```
Dengan Medan = 75 juta (≥ 72 juta, yaitu 90% dari 80 juta):
```
Jakarta      Rp120.000.000  TERCAPAI
Surabaya      Rp85.000.000  TERCAPAI
Medan         Rp75.000.000  HAMPIR
```
Urutan `if` penting: cek TERCAPAI **lebih dulu**, baru HAMPIR. Jika dibalik, Jakarta akan berstatus HAMPIR karena 120 juta juga ≥ 72 juta.

**Latihan 6.4:** lihat [`latihan/kunci/penjualan_csv.py`](latihan/kunci/penjualan_csv.py). Hasilnya:
```
Jakarta    Rp  120,000,000  TERCAPAI
Surabaya   Rp   85,000,000  TERCAPAI
Medan      Rp   40,000,000  BELUM
Makassar   Rp   76,000,000  BELUM
Bandung    Rp   92,000,000  TERCAPAI

Total penjualan : Rp413,000,000
Cabang terbaik  : Jakarta (Rp120,000,000)
Target tercapai : 3 dari 5 cabang
```
Cek manual: 120 + 85 + 40 + 76 + 92 = **413 juta**. ✔

**Kuis**
1. List = daftar berurutan (seperti satu kolom). Dictionary = pasangan kunci → nilai (seperti tabel nama → angka).
2. `"TERCAPAI"`, karena aturannya `>=` (lebih dari **atau sama dengan**).
3. Baris di dalam `if`/`for`/`def` tidak menjorok 4 spasi.
4. Tampilkan `nilai` rata kanan dengan lebar 13 karakter dan pemisah ribuan.

</details>

---

← [Modul 5](modul-05-prompt-rctco.md) | **Berikutnya: [Modul 7: Studi Kasus Operasional →](modul-07-studi-kasus-operasional.md)**
