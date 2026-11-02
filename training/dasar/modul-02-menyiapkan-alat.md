# Modul 2: Menyiapkan Alat Kerja

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 2](../01-dasar.md#langkah-2-menyiapkan-alat-kerja) |
| **Sesi** | **Pra-sesi** (dikerjakan mandiri sebelum Sesi 1) + verifikasi 15 menit di Sesi 1 |
| **Durasi** | ± 60 menit mandiri |
| **Prasyarat** | Laptop dengan hak instal aplikasi (minta izin tim IT jika perlu), koneksi internet, akun Claude |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Memasang Python, VS Code, Git, dan Claude Code.
2. Mengunduh materi latihan dan membuat lingkungan virtual Python.
3. Memeriksa bahwa semua alat berfungsi.
4. Mengatasi 5 masalah instalasi yang paling umum.

---

## 📖 Materi

### A. Empat alat dan fungsinya

| Alat | Analogi | Fungsi | Wajib? |
|------|---------|--------|--------|
| **Python** | Mesin mobil | Menjalankan program | Ya |
| **VS Code** | Meja kerja | Membuka, membaca, dan mengedit file | Ya |
| **Git** | Mesin fotokopi + lemari arsip | Menyimpan versi pekerjaan | Ya |
| **Claude Code** | Asisten pribadi | AI yang menulis dan menjalankan kode | Ya |

### B. Apa itu "lingkungan virtual" (`.venv`)?

Bayangkan setiap proyek punya **kotak peralatan sendiri**. Jika proyek A butuh obeng versi 1 dan proyek B butuh obeng versi 2, keduanya tidak akan bertabrakan karena masing-masing punya kotak sendiri. Itulah **lingkungan virtual**: folder `.venv` berisi Python dan *library* khusus untuk satu proyek.

---

## 🛠️ Praktik Terpandu: Instalasi Langkah demi Langkah

> ✅ Centang setiap langkah setelah berhasil. Jika macet, lihat [Pemecahan Masalah](#-pemecahan-masalah) di bawah.

### Langkah 1: Python 3.10 atau lebih baru

- [ ] Unduh dari https://www.python.org/downloads/
- **Windows:** saat instalasi, **centang "Add python.exe to PATH"** di layar pertama, lalu klik *Install Now*.
- **macOS:** jalankan file `.pkg` yang diunduh. Setelah itu gunakan perintah `python3` (bukan `python`).
- **Linux:** biasanya sudah terpasang. Cek dengan `python3 --version`.

### Langkah 2: VS Code

- [ ] Unduh dari https://code.visualstudio.com/ dan pasang.
- [ ] Buka VS Code → klik ikon **Extensions** (kotak-kotak di sisi kiri) → cari **Python** (dari Microsoft) → **Install**.

### Langkah 3: Git

- [ ] Unduh dari https://git-scm.com/downloads dan pasang dengan pilihan bawaan (*default*).
- **macOS:** jika muncul jendela "install command line developer tools", klik **Install**.

### Langkah 4: Claude Code

- [ ] Ikuti petunjuk resmi di https://code.claude.com/docs. Perintah instalasi yang umum:

  macOS / Linux (Terminal):
  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  ```

  Windows (PowerShell):
  ```powershell
  irm https://claude.ai/install.ps1 | iex
  ```

- [ ] Jalankan `claude` sekali, lalu ikuti petunjuk **login** di browser dengan akun Claude Anda.
- (Opsional) Pasang ekstensi **Claude Code** di VS Code.

### Langkah 5: Periksa semua alat

Buka terminal (di VS Code: menu **Terminal → New Terminal**), lalu jalankan satu per satu:

```bash
python3 --version
```

```bash
git --version
```

```bash
claude --version
```

Di Windows, gunakan `python --version` jika `python3` tidak dikenali.

**Hasil yang benar** berupa nomor versi, misalnya `Python 3.12.7` dan `git version 2.47.0`. Angka persisnya boleh berbeda.

### Langkah 6: Unduh materi latihan

Ganti `<alamat-repositori>` dengan alamat yang diberikan fasilitator:

```bash
git clone <alamat-repositori> vibe-coding-for-eveyone
```

```bash
cd vibe-coding-for-eveyone
```

Lalu buka folder ini di VS Code: **File → Open Folder** → pilih `vibe-coding-for-eveyone`.

### Langkah 7: Buat lingkungan virtual & pasang alat uji

```bash
python3 -m venv .venv
```

Aktifkan lingkungan virtual:

| Sistem | Perintah aktivasi |
|--------|-------------------|
| macOS / Linux | `source .venv/bin/activate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (Command Prompt) | `.venv\Scripts\activate.bat` |

Jika berhasil, baris terminal diawali `(.venv)`. Lalu pasang alat uji:

```bash
pip install -r requirements-dev.txt
```

### Langkah 8: Uji coba akhir

```bash
pytest
```

**Hasil yang benar:** baris terakhir berbunyi `... passed` (misalnya `63 passed`), tanpa `failed`.

Di VS Code, tekan `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`) → ketik **Python: Select Interpreter** → pilih yang berlabel `.venv`.

---

## 🧯 Pemecahan Masalah

| Gejala | Penyebab | Solusi |
|--------|----------|--------|
| `python` / `python3` is not recognized (Windows) | Python tidak masuk PATH | Instal ulang Python dan **centang "Add python.exe to PATH"** |
| `running scripts is disabled on this system` saat aktivasi `.venv` (PowerShell) | Kebijakan keamanan PowerShell | Jalankan `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`, lalu coba lagi. Jika tidak diizinkan kantor, pakai Command Prompt dan `activate.bat` |
| `pip: command not found` | Lingkungan virtual belum aktif | Jalankan perintah aktivasi dulu; pastikan muncul `(.venv)` |
| `pytest: command not found` | Sama seperti di atas, atau `pip install` belum dijalankan | Aktifkan `.venv`, lalu `pip install -r requirements-dev.txt` |
| `claude: command not found` | Terminal belum mengenali instalasi baru | Tutup semua terminal, buka terminal baru, lalu coba lagi |
| Instalasi diblokir laptop kantor | Kebijakan IT | Minta bantuan tim IT; tunjukkan daftar alat di modul ini |

> ⚠️ **Ingat setiap kali membuka terminal baru:** aktifkan lagi `.venv` sebelum menjalankan `pytest` atau `pip`.

---

## 🏋️ Latihan

### ⭐ Latihan 2.1: Lembar cek instalasi

Isi tabel ini dan bawa ke Sesi 1:

| Perintah | Hasil di laptop saya |
|----------|----------------------|
| `python3 --version` | |
| `git --version` | |
| `claude --version` | |
| `pytest` (baris terakhir) | |

### ⭐⭐ Latihan 2.2: Ulangi dari awal

Tutup VS Code dan semua terminal. Buka lagi, masuk ke folder repositori, aktifkan `.venv`, lalu jalankan `pytest`. Tujuannya: hafal urutan "buka → masuk folder → aktifkan → jalankan".

### ⭐⭐⭐ Latihan 2.3: Tolong rekan

Bantu satu rekan kerja menyelesaikan instalasi. Catat masalah yang ia alami dan cara mengatasinya.

---

## 📝 Kuis

1. Apa fungsi folder `.venv`?
2. Tanda apa yang menunjukkan lingkungan virtual sudah aktif?
3. Anda membuka terminal baru dan `pytest` tidak dikenali. Apa yang pertama kali Anda cek?
4. Di Windows, centang apa yang **wajib** dipilih saat memasang Python?

---

## 📌 Ringkasan

- Empat alat wajib: **Python, VS Code, Git, Claude Code**.
- `.venv` = kotak peralatan khusus proyek. **Aktifkan setiap kali membuka terminal baru.**
- Uji akhir: `pytest` menampilkan `passed` tanpa `failed`.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

1. Menyimpan Python dan *library* khusus satu proyek, agar tidak bercampur dengan proyek lain.
2. Baris terminal diawali tulisan `(.venv)`.
3. Apakah `.venv` sudah diaktifkan (ada tulisan `(.venv)`). Jika belum, jalankan perintah aktivasi.
4. **"Add python.exe to PATH"**.

</details>

---

← [Modul 1](modul-01-pola-pikir.md) | **Berikutnya: [Modul 3: Mengenal Terminal →](modul-03-terminal.md)**
