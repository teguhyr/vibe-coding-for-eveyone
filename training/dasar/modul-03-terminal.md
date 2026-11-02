# Modul 3: Mengenal Terminal

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 3](../01-dasar.md#langkah-3-mengenal-terminal) |
| **Sesi** | Sesi 1 |
| **Durasi** | 15 menit |
| **Prasyarat** | Modul 2 selesai (semua alat terpasang) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Membuka terminal di VS Code.
2. Mengetahui posisi folder saat ini dan berpindah folder.
3. Melihat isi folder dan isi file.
4. Menjalankan dan menghentikan program Python.

---

## 📖 Materi

### A. Terminal itu apa?

| File Explorer / Finder | Terminal |
|------------------------|----------|
| Klik ikon folder | Ketik `cd nama_folder` |
| Lihat isi folder | Ketik `ls` |
| Klik dua kali file program | Ketik `python nama_file.py` |
| Seperti **memesan lewat menu bergambar** | Seperti **memesan langsung ke dapur**: lebih cepat dan tepat |

Claude Code juga bekerja di terminal. Jadi, sedikit paham terminal membuat Anda bisa **membaca dan menilai** perintah yang akan dijalankan Claude.

### B. Membaca baris terminal

```
(.venv) budi@laptop:~/vibe-coding-for-eveyone$ ▌
   │      │            │                       │
   │      │            │                       └── tempat Anda mengetik
   │      │            └── folder tempat Anda sekarang berada
   │      └── nama pengguna & komputer
   └── lingkungan virtual aktif
```

Tampilan di Windows sedikit berbeda, misalnya `(.venv) PS C:\Users\budi\vibe-coding-for-eveyone>`, tetapi maknanya sama.

### C. Folder dan jalur (*path*)

Struktur repositori ini seperti lemari arsip:

```
vibe-coding-for-eveyone/          ← folder utama (root)
├── modules/
│   ├── 01-operations/
│   │   ├── data/
│   │   │   └── inventory.csv
│   │   └── inventory_reorder.py
│   └── 02-finance/ ...
└── training/
```

| Simbol | Arti | Contoh |
|--------|------|--------|
| `/` (Windows: `\`) | Pemisah folder | `modules/01-operations/data` |
| `.` | Folder saat ini | `ls .` |
| `..` | Satu folder di atas | `cd ..` |
| `~` | Folder rumah (*home*) Anda | `cd ~` |

### D. Perintah inti

| Perintah (macOS/Linux) | Windows (PowerShell) | Fungsi |
|------------------------|----------------------|--------|
| `pwd` | `pwd` | Saya sedang di folder mana? |
| `ls` | `ls` atau `dir` | Apa isi folder ini? |
| `cd nama_folder` | `cd nama_folder` | Masuk ke folder |
| `cd ..` | `cd ..` | Naik satu folder |
| `cat nama_file` | `type nama_file` | Tampilkan isi file |
| `head -3 nama_file` | `Get-Content nama_file -TotalCount 3` | Tampilkan 3 baris pertama |
| `wc -l nama_file` | `(Get-Content nama_file).Count` | Hitung jumlah baris |
| `python3 nama_file.py` | `python nama_file.py` | Jalankan program |
| `clear` | `cls` | Bersihkan layar |

### E. Tombol yang menghemat waktu

| Tombol | Fungsi |
|--------|--------|
| `Tab` | Melengkapi nama file/folder otomatis. Ketik `cd mod` lalu `Tab` → `cd modules/` |
| `↑` (panah atas) | Mengulang perintah sebelumnya |
| `Ctrl+C` | **Menghentikan** program yang sedang berjalan |

---

## 🛠️ Praktik Terpandu

Ikuti bersama fasilitator, dimulai dari folder utama repositori:

```bash
pwd
```

```bash
ls
```

```bash
ls modules
```

```bash
cd modules/01-operations
```

```bash
ls data
```

```bash
head -3 data/inventory.csv
```

Hasilnya:

```
sku,name,on_hand,avg_daily_usage,lead_time_days,safety_stock
SKU-001,A4 Paper (ream),120,15,5,30
SKU-002,Printer Toner,8,1.5,7,5
```

Kembali ke folder utama, lalu jalankan program pertama Anda:

```bash
cd ../..
```

```bash
python3 modules/01-operations/inventory_reorder.py
```

---

## 🏋️ Latihan

### ⭐ Latihan 3.1: Berburu informasi

Gunakan hanya terminal (jangan pakai File Explorer):

1. Ada berapa folder di dalam `modules`?
2. File apa saja yang ada di `modules/07-legal`?
3. Apa nama file data di `modules/02-finance/data`?

### ⭐⭐ Latihan 3.2: Membaca data

1. Ada berapa **baris data** (tidak termasuk baris judul) di `modules/05-it/data/tickets.csv`?
2. Apa saja nama kolom di `modules/07-legal/data/contracts.csv`?

### ⭐⭐⭐ Latihan 3.3: Navigasi tanpa melihat

Tanpa melihat catatan: dari folder utama, masuk ke `modules/02-finance`, tampilkan isi file data-nya, jalankan programnya dengan `python3 budget_variance.py`, lalu kembali ke folder utama.

---

## 📝 Kuis

1. Perintah apa untuk mengetahui Anda sedang di folder mana?
2. Apa arti `cd ..`?
3. Program Anda tidak berhenti-berhenti. Tombol apa untuk menghentikannya?
4. Apa fungsi tombol `Tab` di terminal?

---

## 📌 Ringkasan

- Terminal = memberi perintah lewat teks. Paham sedikit terminal membuat Anda bisa **menilai** perintah Claude.
- 5 perintah inti: `pwd`, `ls`, `cd`, `cat`/`head`, `python3`.
- `Tab` melengkapi nama, `↑` mengulang perintah, `Ctrl+C` menghentikan program.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 3.1**
1. **11 folder**: `00-getting-started` sampai `10-general-affairs` (`ls modules`).
2. `README.md`, `contract_renewals.py`, `data`, `test_contract_renewals.py` (`ls modules/07-legal`). Jika muncul folder `__pycache__`, itu file sementara buatan Python dan boleh diabaikan.
3. `budget_vs_actual.csv` (`ls modules/02-finance/data`).

**Latihan 3.2**
1. **7 baris data.** `wc -l modules/05-it/data/tickets.csv` menampilkan `8` (termasuk 1 baris judul), jadi 8 − 1 = 7.
2. `head -1 modules/07-legal/data/contracts.csv` menampilkan:
   `contract_id,counterparty,contract_type,end_date,notice_days,auto_renew`

**Latihan 3.3**
```bash
cd modules/02-finance
cat data/budget_vs_actual.csv
python3 budget_variance.py
cd ../..
```

**Kuis**
1. `pwd`
2. Naik (pindah) satu folder ke atas.
3. `Ctrl+C`
4. Melengkapi nama file atau folder secara otomatis.

</details>

---

← [Modul 2](modul-02-menyiapkan-alat.md) | **Berikutnya: [Modul 4: Percakapan Pertama dengan Claude Code →](modul-04-claude-code-pertama.md)**
