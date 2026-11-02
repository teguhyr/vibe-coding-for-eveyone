# Modul 9: Meminta Perubahan Kecil ke AI

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 9](../01-dasar.md#langkah-9-meminta-perubahan-kecil-ke-ai) |
| **Sesi** | Sesi 2 |
| **Durasi** | 25 menit |
| **Prasyarat** | Modul 4, 5, 7, 8 |
| **Modul studi kasus** | [`modules/01-operations`](../../modules/01-operations/) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Membuat *branch* latihan agar file asli aman.
2. Meminta perubahan kecil dan spesifik kepada Claude.
3. Membaca *diff* (tampilan perubahan): baris yang ditambah dan dihapus.
4. Memverifikasi perubahan, dan membatalkannya jika perlu.

---

## 📖 Materi

### A. Prinsip perubahan kecil

| ❌ Perubahan besar sekaligus | ✅ Perubahan kecil bertahap |
|-----------------------------|----------------------------|
| "Tambahkan export CSV, grafik, email otomatis, dan dashboard" | "Tambahkan opsi export CSV. Jangan ubah yang lain." |
| Sulit diperiksa, sulit dicari letak kesalahannya | Mudah diperiksa, mudah dibatalkan |

**Satu permintaan = satu perubahan yang bisa Anda periksa.**

### B. Membaca *diff*

*Diff* menunjukkan **apa yang berubah** pada file:

```diff
     parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
+    parser.add_argument("--output", type=Path, help="Simpan hasil ke file CSV ini")
     args = parser.parse_args()
```

| Tanda | Arti | Warna di layar |
|-------|------|----------------|
| `+` di awal baris | Baris **ditambahkan** | Hijau |
| `-` di awal baris | Baris **dihapus** | Merah |
| (tanpa tanda) | Baris tidak berubah, hanya ditampilkan sebagai konteks | Putih/abu-abu |

Pertanyaan yang Anda ajukan saat membaca *diff*:
1. Apakah yang berubah **hanya** yang saya minta?
2. Adakah baris penting yang **dihapus** (merah) tanpa alasan?
3. Apakah saya **paham** maksud baris yang ditambahkan? Jika tidak, tanyakan.

### C. Cara membatalkan perubahan

| Situasi | Cara |
|---------|------|
| Claude sedang bekerja ke arah yang salah | Tekan `Esc` untuk menghentikan |
| Ingin kembali ke titik sebelumnya dalam percakapan | Tekan `Esc` dua kali (*rewind*) |
| Perubahan sudah dibuat, tetapi belum di-commit | Minta Claude: *"Batalkan perubahan terakhir"*, atau `git restore nama_file` |
| Ingin meninggalkan seluruh eksperimen | Pindah kembali ke branch utama: `git switch main` |

### D. Prompt lanjutan yang sering dipakai

| Situasi | Prompt |
|---------|--------|
| Tidak paham kode | *"Jelaskan baris 40–55 seperti ke orang awam."* |
| Hasil salah | *"Untuk SKU-002 hasilnya 16, padahal seharusnya 15,5. Mengapa? Perbaiki."* |
| Ingin batal | *"Batalkan perubahan terakhir dan kembalikan seperti semula."* |
| Ingin yakin | *"Apa saja kasus yang bisa membuat program ini salah?"* |
| Ingin cek dampak | *"Jalankan tes modul ini dan jelaskan hasilnya."* |

---

## 🛠️ Praktik Terpandu: Tambah Opsi Export CSV

**Tujuan:** daftar barang yang perlu dipesan juga bisa disimpan sebagai file CSV, sehingga tim pembelian bisa membukanya di Excel.

1. **Buat branch latihan** (penjelasan lengkap ada di Modul 10):

   ```bash
   git checkout -b latihan-saya
   ```

2. **Jalankan Claude** dan kirim permintaan:

   ```
   Di modules/01-operations/inventory_reorder.py, tambahkan opsi --output nama_file.csv
   agar daftar barang yang perlu dipesan juga disimpan ke file CSV yang bisa dibuka di Excel.
   Jangan ubah perilaku yang sudah ada. Jelaskan setiap perubahan yang kamu buat.
   ```

3. **Baca permintaan izin edit.** Sebelum memilih *Yes*, periksa *diff*-nya dengan 3 pertanyaan di bagian B.
4. **Verifikasi perilaku lama tidak berubah.** Tanpa opsi baru, hasilnya harus sama seperti di Modul 7:

   ```bash
   python3 modules/01-operations/inventory_reorder.py
   ```

5. **Coba opsi baru:**

   ```bash
   python3 modules/01-operations/inventory_reorder.py --output pesan_ulang.csv
   ```

   Buka `pesan_ulang.csv` di Excel. Isinya harus 3 barang yang sama dengan tabel di layar: SKU-006, SKU-004, SKU-002.

6. **Pastikan tes masih lulus:**

   ```bash
   pytest modules/01-operations
   ```

7. **Lihat semua perubahan:**

   ```bash
   git diff
   ```

> ⚠️ File `pesan_ulang.csv` adalah **hasil**, bukan kode. Jangan ikut menyimpannya ke Git di Modul 10. Hapus atau biarkan saja.

---

## 🏋️ Latihan

### ⭐ Latihan 9.1: Baca *diff*

Dari hasil `git diff` di praktik, tuliskan:
- berapa baris yang **ditambahkan** (`+`),
- berapa baris yang **dihapus** (`-`),
- satu baris tambahan yang paling penting, dan artinya.

### ⭐⭐ Latihan 9.2: Uji perilaku tanpa barang yang perlu dipesan

Apa yang terjadi jika **tidak ada** barang yang perlu dipesan dan Anda memakai `--output`? Apakah file tetap dibuat? Tanyakan ke Claude, lalu buktikan sendiri dengan mengubah data contoh sementara (ingat untuk mengembalikannya dengan `git checkout -- modules/01-operations/data/inventory.csv`).

### ⭐⭐⭐ Latihan 9.3: Perubahan kedua

Minta satu perubahan kecil lagi, misalnya: *"Tampilkan reorder point dengan satu angka desimal (15,5, bukan 16)."* Periksa *diff*, jalankan program, dan jalankan tes. **Apakah tes masih lulus?** Jika tidak, tanyakan ke Claude mengapa sebelum menyetujui perbaikan apa pun.

---

## 📝 Kuis

1. Mengapa membuat branch sebelum meminta perubahan?
2. Di *diff*, apa arti baris yang diawali `-`?
3. Setelah perubahan, apa 3 hal yang Anda cek?
4. Claude terlanjur mengubah file dengan cara yang tidak Anda inginkan dan belum di-commit. Sebutkan 2 cara membatalkannya.

---

## 📌 Ringkasan

- **Satu permintaan = satu perubahan** yang bisa diperiksa. Sebutkan juga apa yang **tidak boleh** diubah.
- Baca *diff* sebelum menyetujui: `+` ditambah, `-` dihapus.
- Setelah perubahan, cek: (1) perilaku lama tetap sama, (2) fitur baru bekerja, (3) tes lulus.
- Bisa dibatalkan: `Esc`, `Esc Esc`, minta Claude membatalkan, `git restore`, atau `git switch main`.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Praktik: contoh perubahan yang baik.** Kode buatan Claude di laptop Anda bisa berbeda, dan itu wajar. Yang penting, ia memenuhi kriteria di bawah. Contoh yang sudah diuji:

```python
def save_csv(items: list[Item], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sku", "name", "on_hand", "reorder_point", "days_of_cover"])
        for item in items:
            writer.writerow(
                [
                    item.sku,
                    item.name,
                    item.on_hand,
                    round(item.reorder_point, 1),
                    round(item.days_of_cover, 1),
                ]
            )
```

dan di dalam `main()`:

```python
    parser.add_argument("--output", type=Path, help="Simpan hasil ke file CSV ini")
    args = parser.parse_args()

    due = items_to_reorder(load_items(args.csv_file))
    if args.output:
        save_csv(due, args.output)
        print(f"Disimpan ke {args.output}")
```

Isi `pesan_ulang.csv`:
```
sku,name,on_hand,reorder_point,days_of_cover
SKU-006,Pallet Wrap,3,16.0,1.5
SKU-004,Cardboard Box M,55,68.0,4.6
SKU-002,Printer Toner,8,15.5,5.3
```

**Kriteria lulus perubahan:**
- [ ] Tanpa `--output`, hasil sama persis dengan sebelumnya
- [ ] Dengan `--output`, file CSV dibuat dan isinya sama dengan tabel di layar
- [ ] `pytest modules/01-operations` tetap lulus
- [ ] File terbuka dengan benar di Excel

**Latihan 9.2:** tergantung kode buatan Claude. Pada contoh di atas, `save_csv` dipanggil **sebelum** pengecekan "tidak ada barang", sehingga file **tetap dibuat** hanya berisi baris judul. Ini perilaku yang baik: tim pembelian tetap menerima file dan tahu tidak ada yang perlu dipesan. Jika kode Anda tidak membuat file, putuskan perilaku mana yang Anda inginkan, lalu minta Claude menyesuaikan.

**Latihan 9.3:** Tes **tetap lulus**, karena tes memeriksa **perhitungan dan urutan**, bukan format tampilan. Jika ada tes yang gagal, jangan langsung minta Claude "mengubah tes agar lulus". Tanyakan dulu mengapa gagal.

**Kuis**
1. Agar versi asli tetap aman; eksperimen yang gagal tinggal ditinggalkan.
2. Baris itu **dihapus**.
3. (1) Perilaku lama tetap sama, (2) fitur baru bekerja sesuai permintaan, (3) tes lulus.
4. Contoh: minta Claude "batalkan perubahan terakhir"; `git restore nama_file`; tekan `Esc` dua kali untuk *rewind*.

</details>

---

← [Modul 8](modul-08-verifikasi-keuangan.md) | **Berikutnya: [Modul 10: Menyimpan Pekerjaan dengan Git →](modul-10-git.md)**
