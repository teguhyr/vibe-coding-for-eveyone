# Modul 5: Kode yang Rapi: Linter & Formatter

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 5](../02-menengah.md#langkah-5-kode-yang-rapi-linter--formatter) |
| **Sesi** | Sesi 3 |
| **Durasi** | 25 menit |
| **Prasyarat** | Modul 2; `pip install -r requirements-dev.txt` sudah dijalankan (memasang `ruff`) |
| **File latihan** | `berantakan.py` (dibuat sendiri dari blok kode di Praktik Terpandu) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Membedakan **formatter** (merapikan tampilan) dan **linter** (mencari potensi bug).
2. Menjalankan `ruff check`, `ruff check --fix`, `ruff format`, dan `ruff format --check`.
3. Membaca kode aturan ruff (misalnya `F821`) dan mencari penjelasannya.
4. Menjadikan "pytest + ruff" kebiasaan sebelum menyatakan pekerjaan selesai.

---

## 📖 Materi

### A. Formatter vs linter

| | Formatter (`ruff format`) | Linter (`ruff check`) |
|---|---|---|
| Analogi | *Auto-format* di Word | *Spell-checker* + editor yang teliti |
| Yang diurus | Spasi, baris kosong, panjang baris, tanda kutip | Import tak terpakai, nama tak dikenal, pola rawan bug |
| Mengubah arti program? | **Tidak pernah** | Perbaikan otomatis (`--fix`) hanya untuk kasus yang aman |

### B. Pengaturan di `pyproject.toml`

```toml
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "UP"]
```

| Kode | Keluarga aturan | Contoh |
|------|-----------------|--------|
| `E`, `W` | Gaya penulisan (pycodestyle) | `E701` dua perintah dalam satu baris |
| `F` | Kesalahan logika sederhana (Pyflakes) | `F401` import tak terpakai, `F821` nama tak dikenal |
| `I` | Urutan import (isort) | `I001` import tidak berurutan |
| `B` | Pola rawan bug (bugbear) | Nilai default berupa list yang bisa berubah |
| `UP` | Sintaks Python modern (pyupgrade) | Memakai sintaks versi baru yang lebih ringkas |

Karena pengaturan ini ada di repositori, **semua orang** (dan Claude) memakai aturan yang sama.

### C. Membaca pesan ruff

```
berantakan.py:18:12: F821 Undefined name `LABEL_BIASAA`
```

`file:baris:kolom: KODE penjelasan`. Ingin tahu lebih lanjut tentang satu aturan?

```bash
ruff rule F821
```

Tanda `[*]` di samping pesan berarti aturan itu bisa diperbaiki otomatis dengan `--fix`.

### D. Rutinitas "selesai berarti hijau"

Sebelum menyatakan pekerjaan selesai, jalankan tiga perintah ini. Semuanya harus lulus:

```bash
pytest
```

```bash
ruff check .
```

```bash
ruff format --check .
```

Atau minta Claude di akhir setiap tugas:

```
Jalankan pytest, ruff check ., dan ruff format --check . Perbaiki semua masalah yang muncul.
Jangan ubah perilaku program, dan jangan ubah tes agar lulus.
```

### E. Ruff di VS Code

Pasang ekstensi **Ruff** (penerbit: Astral Software). Lalu di *Settings* (`Ctrl+,`), cari **Format On Save** dan centang, kemudian pilih Ruff sebagai *Default Formatter* untuk Python. Setiap kali Anda menyimpan file, kodenya otomatis dirapikan, dan garis bergelombang menandai masalah linter.

---

## 🛠️ Praktik Terpandu

**1. Buat file berantakan.** Di folder utama repositori, buat file `berantakan.py` dan salin kode ini **apa adanya**:

<!-- fmt: off -->
```python
import os
import csv
from pathlib import Path

LABEL_BIASA = "BIASA"

def total_klaim(baris,batas = 150000):
    hasil=0
    for b in baris :
        jumlah = int(b["amount"])
        if jumlah>batas: jumlah=batas
        hasil+=jumlah
    return hasil

def label(jumlah):
    if jumlah >= 1_000_000:
        return "PERLU PERSETUJUAN DIREKTUR"
    return LABEL_BIASAA

def baca(path):
    with open(path) as f:
        data = list(csv.DictReader(f))
    return data

print(total_klaim(baca(Path("training/menengah/latihan/data/klaim_reimburse.csv"))))
```
<!-- fmt: on -->

**2. Jalankan programnya.**

```bash
python berantakan.py
```

```
995000
```

Program berjalan tanpa error. Apakah berarti tidak ada bug? Belum tentu.

**3. Jalankan linter.** Opsi `--output-format concise` membuat tampilan satu baris per masalah:

```bash
ruff check berantakan.py --output-format concise
```

```
berantakan.py:1:1: I001 [*] Import block is un-sorted or un-formatted
berantakan.py:1:8: F401 [*] `os` imported but unused
berantakan.py:11:24: E701 Multiple statements on one line (colon)
berantakan.py:18:12: F821 Undefined name `LABEL_BIASAA`
Found 4 errors.
[*] 2 fixable with the `--fix` option.
```

Perhatikan `F821`: **salah ketik** `LABEL_BIASAA` (ada dua huruf A). Program tadi berjalan lancar karena fungsi `label()` tidak pernah dipanggil. Begitu ada yang memanggilnya, program akan berhenti dengan `NameError`. Linter menemukan bug ini **sebelum** terjadi.

**4. Perbaiki yang otomatis, lalu rapikan.**

```bash
ruff check --fix berantakan.py
```

```bash
ruff format berantakan.py
```

Buka file-nya: import sudah berurutan dan `import os` hilang, spasi sudah rapi, ada 2 baris kosong di antara fungsi, dan `if jumlah>batas: jumlah=batas` dipecah menjadi dua baris.

**5. Cek lagi.**

```bash
ruff check berantakan.py --output-format concise
```

```
berantakan.py:20:12: F821 Undefined name `LABEL_BIASAA`
Found 1 error.
```

Tinggal `F821`. Ruff **tidak** memperbaikinya otomatis (lihat Latihan 5.4). Perbaiki sendiri: ganti `LABEL_BIASAA` menjadi `LABEL_BIASA`, lalu jalankan `ruff check` sekali lagi sampai muncul `All checks passed!`.

**6. Hapus file latihan** agar tidak ikut ter-commit:

```bash
rm berantakan.py
```

Di Windows PowerShell: `Remove-Item berantakan.py`.

---

## 🏋️ Latihan

### ⭐ Latihan 5.1: Terjemahkan pesan ruff

Jelaskan dengan bahasa sehari-hari arti `I001`, `F401`, `E701`, dan `F821` dari Praktik Terpandu.

### ⭐⭐ Latihan 5.2: Cari penjelasan aturan

Jalankan `ruff rule E701`. Menurut penjelasan itu, mengapa dua perintah dalam satu baris dianggap masalah?

### ⭐⭐ Latihan 5.3: Rapikan saat menyimpan

Pasang ekstensi Ruff di VS Code dan aktifkan *Format On Save*. Buat ulang `berantakan.py`, simpan, lalu lihat apa yang berubah. Apakah `F821` ikut diperbaiki? Hapus filenya setelah selesai.

### ⭐⭐⭐ Latihan 5.4: Mengapa tidak otomatis?

Ruff memperbaiki `F401` (hapus import) secara otomatis, tetapi tidak `F821`. Jelaskan alasannya. Petunjuk: bayangkan ada konstanta `LABEL_BIASA` **dan** `LABEL_BIASA_BARU`.

---

## 📝 Kuis

1. Apakah `ruff format` bisa mengubah hasil perhitungan program? Jelaskan.
2. Apa arti tanda `[*]` di pesan ruff?
3. Program berjalan tanpa error, tetapi `ruff check` melaporkan `F821`. Apakah programnya aman dipakai?
4. Sebutkan 3 perintah yang harus lulus sebelum pekerjaan dianggap selesai.

---

## 📌 Ringkasan

- **Formatter** merapikan tampilan tanpa mengubah arti. **Linter** mencari potensi bug.
- Aturan ruff ada di `pyproject.toml`, jadi semua orang memakai standar yang sama.
- `ruff check --fix` hanya memperbaiki yang aman. Sisanya (seperti `F821`) **Anda** yang putuskan.
- Selesai berarti hijau: `pytest`, `ruff check .`, `ruff format --check .`.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 5.1**
- `I001`: urutan import tidak rapi (seharusnya berurutan abjad dan dikelompokkan).
- `F401`: `os` di-import tetapi tidak pernah dipakai, jadi hanya mengotori file.
- `E701`: dua perintah ditulis dalam satu baris setelah `:`, sehingga mudah terlewat saat dibaca.
- `F821`: memakai nama yang tidak pernah dibuat, biasanya salah ketik. Program akan error saat baris itu dijalankan.

**Latihan 5.2:** bagian *Why is this bad?* mengutip panduan gaya Python PEP 8: *"compound statements are generally discouraged"* (perintah majemuk dalam satu baris sebaiknya dihindari). Bagian *Example* menunjukkan cara yang benar: pecah menjadi dua baris. Dalam praktik: saat membaca cepat, orang mudah mengira `jumlah=batas` selalu dijalankan.

**Latihan 5.3:** *Format On Save* hanya merapikan tampilan (spasi, baris, pemecahan `if` menjadi dua baris). `F821` **tidak** ikut diperbaiki karena itu masalah arti, bukan tampilan. Garis bergelombang tetap muncul di bawah `LABEL_BIASAA`.

**Latihan 5.4:** menghapus import yang tidak dipakai **tidak mengubah arti** program, jadi aman dilakukan otomatis. Untuk nama yang tidak dikenal, ruff **tidak tahu maksud Anda**: mungkin `LABEL_BIASA`, mungkin `LABEL_BIASA_BARU`, atau mungkin konstantanya memang belum dibuat. Menebak bisa memasang bug baru yang lebih sulit ditemukan. Keputusan seperti ini milik manusia.

**Kuis**
1. Tidak. Formatter hanya mengubah tampilan (spasi, baris, tanda kutip). Arti programnya tetap sama.
2. Masalah itu bisa diperbaiki otomatis dengan `ruff check --fix`.
3. Tidak. Baris yang memakai nama itu akan menimbulkan `NameError` begitu dijalankan. Bug-nya hanya belum terjadi.
4. `pytest`, `ruff check .`, `ruff format --check .`.

</details>

---

← [Modul 4](modul-04-plan-mode.md) | **Berikutnya: [Modul 6: Database & SQL dengan SQLite →](modul-06-sqlite.md)**
