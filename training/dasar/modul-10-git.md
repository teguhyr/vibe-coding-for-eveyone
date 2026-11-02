# Modul 10: Menyimpan Pekerjaan dengan Git

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 10](../01-dasar.md#langkah-10-menyimpan-pekerjaan-dengan-git) |
| **Sesi** | Sesi 2 |
| **Durasi** | 20 menit |
| **Prasyarat** | Modul 9 (ada perubahan di branch `latihan-saya` yang belum disimpan) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan konsep *repository*, *commit*, dan *branch* dengan analogi sehari-hari.
2. Memakai 5 perintah inti: `status`, `diff`, `add`, `commit`, `log`.
3. Menulis pesan commit yang jelas.
4. Membatalkan perubahan yang belum disimpan, dan memastikan file rahasia tidak ikut tersimpan.

---

## 📖 Materi

### A. Git dengan analogi belanja

| Konsep Git | Analogi belanja | Artinya |
|------------|-----------------|---------|
| **Folder kerja** | Rak toko | File yang sedang Anda ubah |
| `git add` | Masukkan barang ke **keranjang** | Pilih file yang akan disimpan |
| `git commit` | Bayar di kasir, dapat **struk** | Simpan versi + catatan apa yang berubah |
| `git log` | Kumpulan **struk** | Riwayat semua versi |
| **Branch** | Keranjang belanja terpisah | Jalur kerja terpisah untuk eksperimen |

```
commit 1          commit 2              commit 3
"Versi awal"  →  "Tambah export CSV" → "Perbaiki format angka"
                                         ▲ Anda di sini; bisa kembali ke commit mana pun
```

### B. Lima perintah inti

| Perintah | Fungsi | Kapan dipakai |
|----------|--------|---------------|
| `git status` | Melihat file apa yang berubah | **Selalu**, sebelum `add` dan `commit` |
| `git diff` | Melihat detail perubahan | Sebelum menyimpan |
| `git add <file>` | Memasukkan file ke "keranjang" | Pilih file yang memang ingin disimpan |
| `git commit -m "pesan"` | Menyimpan versi | Setelah satu perubahan selesai dan teruji |
| `git log --oneline` | Melihat riwayat singkat | Mengecek apa saja yang sudah disimpan |

### C. Pesan commit yang baik

Tulis **apa yang berubah**, dalam satu kalimat perintah:

| ❌ Buruk | ✅ Baik |
|---------|--------|
| `update` | `Tambah opsi export CSV di laporan reorder` |
| `fix` | `Perbaiki perhitungan hari kerja untuk tanggal merah` |
| `asdf` | `Ubah ambang selisih anggaran menjadi 5%` |
| `revisi final final 2` | `Tampilkan reorder point dengan satu desimal` |

### D. Membatalkan perubahan

| Situasi | Perintah |
|---------|----------|
| File diubah, belum `add`, ingin kembali ke versi terakhir | `git restore nama_file` |
| File sudah `add`, ingin dikeluarkan dari "keranjang" | `git restore --staged nama_file` |
| Ingin melihat versi-versi sebelumnya | `git log --oneline` |

> ⚠️ **Hindari** `git reset --hard` dan `git push --force` sampai Anda benar-benar paham. Keduanya bisa menghapus pekerjaan secara permanen.

### E. Jangan menyimpan rahasia

File `.gitignore` berisi daftar file yang **tidak pernah** disimpan Git. Di repositori ini, `.gitignore` sudah memblokir `.env`, file Excel (`*.xlsx`, `*.xls`), database lokal (`*.db`), dan folder `private/`.

**Kebiasaan wajib:** jalankan `git status` **sebelum** `git commit`, lalu pastikan tidak ada file data asli, kata sandi, atau file hasil yang ikut.

### F. Mengatur identitas (sekali saja)

Git mencatat siapa yang membuat setiap commit. Atur sekali per laptop:

```bash
git config --global user.name "Nama Anda"
```

```bash
git config --global user.email "email.kantor@perusahaan.co.id"
```

---

## 🛠️ Praktik Terpandu 1: Repositori Latihan

Kita berlatih dulu di folder terpisah, agar tidak ada risiko.

1. Dari folder utama repositori, naik satu folder dan buat folder latihan:

   ```bash
   cd ..
   ```

   ```bash
   mkdir latihan-git
   ```

   ```bash
   cd latihan-git
   ```

   ```bash
   git init -b main
   ```

2. Di VS Code, buka folder `latihan-git` dan buat file `laporan.txt` berisi satu baris: `Laporan v1`. Simpan.
3. Lihat status, masukkan ke keranjang, lalu simpan:

   ```bash
   git status
   ```

   ```bash
   git add laporan.txt
   ```

   ```bash
   git commit -m "Tambah laporan versi pertama"
   ```

4. **Buat kesalahan:** ubah isi `laporan.txt` menjadi `Laporan v2 - salah`, lalu simpan. Lihat perubahannya dan batalkan:

   ```bash
   git diff
   ```

   ```bash
   git restore laporan.txt
   ```

   Buka lagi `laporan.txt`. Isinya kembali `Laporan v1`. 🎉
5. **Coba branch:**

   ```bash
   git switch -c percobaan
   ```

   Tambahkan baris kedua `Bagian baru` di `laporan.txt`, simpan, lalu:

   ```bash
   git commit -am "Tambah bagian baru di laporan"
   ```

   ```bash
   git switch main
   ```

   Lihat `laporan.txt`: di `main`, baris "Bagian baru" **belum ada**. Gabungkan hasil eksperimen:

   ```bash
   git merge percobaan
   ```

   ```bash
   git log --oneline
   ```

---

## 🛠️ Praktik Terpandu 2: Simpan Pekerjaan Modul 9

Kembali ke repositori pelatihan, di branch `latihan-saya`:

```bash
cd ../vibe-coding-for-eveyone
```

```bash
git status
```

Anda akan melihat `inventory_reorder.py` berubah, dan mungkin `pesan_ulang.csv` sebagai file baru. **Simpan hanya file kode:**

```bash
git add modules/01-operations/inventory_reorder.py
```

```bash
git commit -m "Tambah opsi export CSV di laporan reorder"
```

```bash
git log --oneline
```

Anda juga bisa meminta Claude: *"Buatkan commit untuk perubahan di inventory_reorder.py dengan pesan yang jelas. Jangan sertakan file CSV hasil."* Tetap baca permintaan izinnya.

---

## 🏋️ Latihan

### ⭐ Latihan 10.1: Pesan commit

Tulis pesan commit yang baik untuk perubahan berikut:
1. Menambah status "HAMPIR" di laporan penjualan.
2. Memperbaiki salah ketik nama kolom di file data.
3. Mengubah ambang batas anggaran dari 10% menjadi 15%.

### ⭐⭐ Latihan 10.2: Tiga commit kecil

Di repositori `latihan-git`, buat **3 commit** terpisah (tambah baris, ubah baris, hapus baris). Tunjukkan hasil `git log --oneline` kepada fasilitator.

### ⭐⭐⭐ Latihan 10.3: Uji `.gitignore`

Di repositori pelatihan, buat file `private/contoh.txt` (folder `private` mungkin perlu dibuat dulu), lalu jalankan `git status`. Apakah file itu muncul? Mengapa? Setelah itu hapus file tersebut.

---

## 📝 Kuis

1. Dalam analogi belanja, `git add` dan `git commit` itu seperti apa?
2. Perintah apa yang **selalu** dijalankan sebelum commit, dan mengapa?
3. Anda mengubah file dan ingin membatalkannya (belum di-add). Perintah apa yang dipakai?
4. Mengapa `pesan_ulang.csv` sebaiknya tidak ikut di-commit?

---

## 📌 Ringkasan

- **add** = masukkan ke keranjang, **commit** = bayar dan dapat struk, **log** = kumpulan struk.
- Selalu `git status` sebelum `git commit`. Pastikan tidak ada data rahasia atau file hasil.
- Pesan commit menjelaskan **apa yang berubah**.
- `git restore` membatalkan perubahan yang belum disimpan. Hindari `reset --hard` dan `push --force`.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Praktik Terpandu 1:** hasil akhir `git log --oneline` kurang lebih seperti ini (kode di depan setiap baris akan berbeda di laptop Anda):
```
8de93ee Tambah bagian baru di laporan
03b51de Tambah laporan versi pertama
```
Dan isi `laporan.txt` di `main` setelah `merge`:
```
Laporan v1
Bagian baru
```

**Latihan 10.1: contoh jawaban**
1. `Tambah status HAMPIR di laporan penjualan`
2. `Perbaiki nama kolom on_hand di data inventaris`
3. `Ubah ambang selisih anggaran menjadi 15%`

**Latihan 10.3:** file **tidak muncul** di `git status`, karena folder `private/` tercantum di `.gitignore`. Git sengaja mengabaikannya agar data asli tidak tersimpan secara tidak sengaja.

**Kuis**
1. `git add` = memasukkan barang ke keranjang; `git commit` = membayar di kasir dan mendapat struk.
2. `git status`, agar Anda tahu persis file apa yang akan disimpan dan tidak ada file rahasia atau file hasil yang ikut.
3. `git restore nama_file`.
4. Itu file **hasil** program yang bisa dibuat ulang kapan saja, bukan kode. Menyimpannya membuat riwayat berantakan, dan jika berisi data asli, bisa membocorkan data.

</details>

---

← [Modul 9](modul-09-perubahan-kecil.md) | **Berikutnya: [Proyek Akhir Level 1 →](proyek-akhir.md)**
