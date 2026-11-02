# Modul 4: Percakapan Pertama dengan Claude Code

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 4](../01-dasar.md#langkah-4-percakapan-pertama-dengan-claude-code) |
| **Sesi** | Sesi 1 |
| **Durasi** | 25 menit |
| **Prasyarat** | Modul 2 (Claude Code terpasang dan sudah login), Modul 3 (dasar terminal) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Memulai Claude Code di folder proyek yang benar.
2. Mengajukan pertanyaan tentang kode dan meminta penjelasan sederhana.
3. **Membaca permintaan izin** dan memutuskan menyetujui atau menolak.
4. Memakai perintah dasar: `/help`, `/clear`, `@file`, `Esc`, `/exit`.

---

## 📖 Materi

### A. Claude Code itu apa?

Claude Code adalah asisten AI yang bekerja **di dalam folder proyek Anda**. Berbeda dengan chat biasa, Claude Code bisa:

| Kemampuan | Contoh |
|-----------|--------|
| **Membaca** file di proyek | "Apa isi `inventory_reorder.py`?" |
| **Menulis dan mengubah** file | "Tambahkan kolom baru di laporan" |
| **Menjalankan perintah** di terminal | Menjalankan `pytest` untuk mengecek hasil |

Karena itu, **folder tempat Anda menjalankan `claude` sangat penting**: Claude hanya "melihat" isi folder tersebut.

### B. Tiga jenis permintaan

| Jenis | Contoh | Apakah Claude minta izin? |
|-------|--------|---------------------------|
| **Bertanya** | "Jelaskan file ini" | Umumnya tidak; Claude hanya membaca |
| **Mengubah file** | "Tambahkan opsi export CSV" | **Ya**, sebelum mengedit file |
| **Menjalankan perintah** | "Jalankan tes" | **Ya**, sebelum menjalankan perintah di terminal |

### C. Membaca permintaan izin: kendali utama Anda

Saat Claude ingin mengubah file atau menjalankan perintah, ia akan berhenti dan bertanya. Tampilannya kurang lebih seperti ini:

```
 Bash command
   pytest modules/01-operations
   Run the operations module tests

 Do you want to proceed?
 ❯ 1. Yes
   2. Yes, and don't ask again for this command
   3. No, and tell Claude what to do differently
```

| Pilihan | Kapan dipakai |
|---------|---------------|
| **Yes** | Anda paham dan setuju dengan perintah ini |
| **Yes, and don't ask again** | Perintah aman yang sering dipakai, misalnya `pytest` |
| **No** | Anda ragu, tidak paham, atau perintahnya berbahaya. Lalu jelaskan apa yang Anda inginkan |

> 💡 **Aturan emas:** jika Anda **tidak paham** sebuah perintah, pilih **No**, lalu tanya: *"Apa yang dilakukan perintah ini? Apa risikonya?"*

**Tanda bahaya yang harus membuat Anda berhenti:**
- `rm`, `del`, `rmdir`: menghapus file atau folder
- `--force`, `-f`: memaksa tindakan, sering tanpa bisa dibatalkan
- `curl ... | bash` atau `irm ... | iex`: mengunduh dan langsung menjalankan program dari internet
- Membaca atau mengirim file berisi data pribadi atau rahasia (`.env`, folder data asli)

### D. Perintah dan tombol penting

| Perintah / tombol | Fungsi |
|-------------------|--------|
| `/help` | Menampilkan bantuan dan daftar perintah |
| `/clear` | Memulai percakapan baru (konteks lama dihapus) |
| `@nama_file` | Menyebut file tertentu, mis. `@modules/02-finance/README.md` |
| `Esc` | Menghentikan Claude yang sedang bekerja |
| `/exit` atau `Ctrl+C` dua kali | Keluar dari Claude Code |

### E. Cara bertanya yang efektif

| ❌ Kurang efektif | ✅ Lebih efektif |
|------------------|-----------------|
| "jelasin" | "Jelaskan @modules/01-operations/inventory_reorder.py tanpa istilah teknis. Saya staf gudang." |
| "ini apa" | "Apa arti `days_of_cover` di file itu? Beri contoh angka." |
| "benerin" | "Jangan ubah apa pun dulu. Jelaskan apa yang akan kamu ubah dan mengapa." |

Anda boleh bertanya dalam **Bahasa Indonesia**. Sebutkan juga **siapa Anda** (mis. "saya staf keuangan, pemula") agar penjelasannya sesuai.

---

## 🛠️ Praktik Terpandu: Tur Repositori

1. Di terminal, pastikan Anda berada di **folder utama** repositori (cek dengan `pwd`), lalu jalankan:

   ```bash
   claude
   ```

2. Kirim pertanyaan berikut satu per satu, dan baca jawabannya:

   ```
   Jelaskan isi repositori ini secara sederhana. Saya pemula dan bekerja di bagian keuangan.
   ```

   ```
   Apa yang dilakukan @modules/01-operations/inventory_reorder.py? Jelaskan tanpa istilah teknis.
   ```

   ```
   Jalankan tes untuk modul operasional dan jelaskan hasilnya.
   ```

3. Pada pertanyaan ketiga, Claude akan **meminta izin** menjalankan `pytest`. Baca perintahnya, lalu pilih **Yes**.
4. Ketik `/clear`, lalu tanyakan topik baru:

   ```
   Modul mana di folder modules yang paling relevan untuk bagian HR? Mengapa?
   ```

5. Keluar dengan `/exit`.

---

## 🏋️ Latihan

### ⭐ Latihan 4.1: Bandingkan dua modul

Minta Claude menjelaskan perbedaan modul `02-finance` dan `06-accounting` dalam **3 kalimat**. Tulis ulang jawabannya dengan kata-kata Anda sendiri.

### ⭐⭐ Latihan 4.2: Setujui atau tolak?

Bayangkan Claude meminta izin untuk perintah berikut. Tentukan: **Setujui**, **Tanya dulu**, atau **Tolak**.

| No | Permintaan izin | Keputusan Anda |
|----|-----------------|----------------|
| 1 | `ls modules` | |
| 2 | `pytest modules/02-finance` | |
| 3 | `python3 modules/01-operations/inventory_reorder.py` | |
| 4 | `pip install pandas` | |
| 5 | `rm -rf modules/03-hr/data` | |
| 6 | `git push --force` | |
| 7 | Membaca file `private/gaji_karyawan.csv` | |
| 8 | Mengedit `modules/01-operations/inventory_reorder.py` setelah Anda memintanya | |

### ⭐⭐⭐ Latihan 4.3: Jadi penanya yang baik

Tulis 3 pertanyaan tentang modul yang paling dekat dengan pekerjaan Anda. Gunakan `@nama_file` dan sebutkan peran Anda. Kirim ke Claude dan nilai: apakah jawabannya mudah dipahami?

---

## 📝 Kuis

1. Mengapa Anda harus menjalankan `claude` dari folder utama repositori?
2. Apa yang sebaiknya Anda lakukan jika tidak memahami perintah yang dimintakan izinnya?
3. Kapan sebaiknya memakai `/clear`?
4. Sebutkan 2 tanda bahaya dalam sebuah perintah.

---

## 📌 Ringkasan

- Claude Code bisa **membaca, mengubah file, dan menjalankan perintah** di folder proyek Anda.
- **Permintaan izin adalah kendali utama Anda.** Tidak paham? Pilih **No**, lalu bertanya.
- Pakai `@nama_file` untuk menunjuk file, `/clear` saat ganti topik, `Esc` untuk menghentikan.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 4.1: poin yang seharusnya muncul**
- **Finance (02)** membandingkan **anggaran vs realisasi** per departemen dan menandai selisih yang melewati ambang batas (perencanaan & kontrol biaya).
- **Accounting (06)** mencocokkan **rekening koran bank dengan buku besar** (rekonsiliasi) dan menampilkan transaksi yang tidak cocok.
- Keduanya memakai `Decimal` untuk uang. Finance melihat ke **rencana**, Accounting memastikan **catatan** sesuai kenyataan.

**Latihan 4.2**

| No | Keputusan | Alasan |
|----|-----------|--------|
| 1 | Setujui | Hanya melihat isi folder |
| 2 | Setujui | Menjalankan tes, tidak mengubah apa pun |
| 3 | Setujui | Menjalankan program latihan yang Anda kenal |
| 4 | **Tanya dulu** | Memasang paket baru. Tanyakan mengapa perlu, karena modul ini cukup memakai library standar |
| 5 | **Tolak** | Menghapus folder data secara permanen |
| 6 | **Tolak** | Memaksa menimpa riwayat di server; bisa menghapus pekerjaan orang lain |
| 7 | **Tolak** | Data pribadi (gaji) tidak boleh dibaca AI. Lihat aturan UU PDP |
| 8 | Setujui (setelah membaca perubahannya) | Anda yang meminta; tetap baca bagian yang diubah |

**Kuis**
1. Claude hanya melihat isi folder tempat ia dijalankan. Dari folder utama, Claude bisa melihat semua modul.
2. Pilih **No**, lalu tanya: *"Apa yang dilakukan perintah ini? Apa risikonya?"*
3. Saat berganti topik atau tugas, agar Claude tidak bingung dengan konteks lama.
4. Contoh: `rm`/`del` (menghapus), `--force` (memaksa), `curl ... | bash` (menjalankan program dari internet), akses ke file data rahasia.

</details>

---

← [Modul 3](modul-03-terminal.md) | **Berikutnya: [Modul 5: Rumus Prompt R-C-T-C-O →](modul-05-prompt-rctco.md)**
