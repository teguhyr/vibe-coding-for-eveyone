# Modul 7: Otomatisasi Kualitas dengan CI/CD

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 7](../03-mahir.md#langkah-7-otomatisasi-kualitas-dengan-cicd) |
| **Sesi** | Sesi 7 |
| **Durasi** | 50 menit |
| **Prasyarat** | Level 2 Modul 8 (branch & review); repositori Anda ada di GitHub |
| **File latihan** | [`latihan/ci/ci.yml`](latihan/ci/ci.yml) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan CI (*Continuous Integration*) dan CD (*Continuous Delivery/Deployment*).
2. Membaca dan menulis workflow GitHub Actions: `on`, `jobs`, `steps`, `uses`, `run`.
3. Menjalankan ruff dan pytest otomatis untuk setiap push dan pull request, termasuk untuk subfolder proyek.
4. Memasang **branch protection** agar PR hanya bisa di-merge jika CI hijau dan sudah di-review.
5. Menyimpan rahasia untuk CI di **GitHub Secrets**, bukan di file workflow.

---

## 📖 Materi

### A. CI = satpam di pintu gudang

Di Level 2, Anda menjalankan `pytest` dan `ruff` **sendiri** sebelum commit. CI memastikan pemeriksaan itu **selalu** terjadi, untuk **semua orang**, di komputer yang bersih:

```
push / pull request ──▶ GitHub menyiapkan komputer baru ──▶ install ──▶ ruff ──▶ pytest
                                                                                    │
                                                         ✅ hijau: boleh di-merge   │
                                                         ❌ merah: perbaiki dulu ◀──┘
```

- **CI:** setiap perubahan otomatis dites.
- **CD:** setelah lulus, aplikasi otomatis dikemas (*delivery*) atau bahkan dipasang (*deployment*). Untuk aplikasi internal, mulai dari CI dulu; deploy otomatis hanya dengan persetujuan tim IT.

> 💡 "Di laptop saya lulus" bukan bukti. CI berjalan di komputer **baru** setiap kali, jadi ia menangkap hal yang terlupa: dependensi yang tidak dicatat di `requirements.txt`, file yang lupa di-commit, atau tes yang bergantung pada data lokal.

### B. Anatomi workflow

[`latihan/ci/ci.yml`](latihan/ci/ci.yml):

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  modules:
    name: Modul (ruff + pytest)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements-dev.txt
      - run: ruff check .
      - run: ruff format --check .
      - run: pytest
```

| Bagian | Arti |
|--------|------|
| `on` | **Kapan** dijalankan: setiap `push` dan `pull_request` |
| `jobs` | Daftar pekerjaan. Setiap job berjalan di komputer sendiri, **paralel** |
| `runs-on` | Sistem operasi komputernya |
| `steps` | Langkah berurutan. Jika satu gagal, sisanya berhenti dan job merah |
| `uses` | Memakai *action* siap pakai: `checkout` mengambil kode, `setup-python` memasang Python |
| `run` | Perintah terminal biasa |

Job kedua di file contoh, `backend`, memakai `defaults.run.working-directory` agar semua perintahnya berjalan di folder backend. Pola yang sama dipakai untuk `projects/ruang-rapat/backend` Anda.

> ⚠️ YAML **peka spasi**. Indentasi memakai spasi (bukan tab), dan tingkatnya harus konsisten. Kesalahan indentasi adalah penyebab paling umum workflow gagal dibaca.

### C. Branch protection

Di GitHub: **Settings → Branches → Add rule** (atau *Rulesets*) untuk branch `main`:
- ✅ *Require a pull request before merging* + minimal 1 *approval*
- ✅ *Require status checks to pass* → pilih job CI Anda
- ✅ *Do not allow bypassing* (agar admin pun mengikuti aturan)

Dengan ini, aturan "satu fitur = satu branch, review, lalu merge" dari Level 2 **ditegakkan oleh sistem**, bukan hanya kesepakatan.

### D. Rahasia di CI

Jika tes membutuhkan rahasia (sebaiknya tidak, karena tes yang baik memakai klien palsu seperti di Modul 6), simpan di **Settings → Secrets and variables → Actions**, lalu baca di workflow:

```yaml
      - run: pytest
        env:
          FLASK_SECRET_KEY: ${{ secrets.FLASK_SECRET_KEY }}
```

GitHub menyamarkan nilainya di log. **Jangan** menulis rahasia langsung di file `.yml`, karena file itu ikut di-commit.

---

## 🛠️ Praktik Terpandu

**1. Pasang workflow** di repositori GitHub Anda (salinan repositori pelatihan atau proyek Anda sendiri):

```bash
mkdir -p .github/workflows
```

```bash
cp training/mahir/latihan/ci/ci.yml .github/workflows/ci.yml
```

Jika proyek Anda bukan repositori pelatihan, sesuaikan job `backend` ke folder backend Anda (atau hapus job itu).

**2. Commit dan push** di sebuah branch:

```bash
git switch -c ci/tambah-workflow
```

```bash
git add .github/workflows/ci.yml
```

```bash
git commit -m "Add CI workflow for ruff and pytest"
```

```bash
git push -u origin ci/tambah-workflow
```

**3. Buka tab Actions** di repositori GitHub. Klik run yang sedang berjalan, lalu klik setiap job dan langkahnya untuk melihat log.

**4. Buat PR** dari branch ini. Di halaman PR, status setiap job tampil di bagian bawah.

**5. Buat CI merah dengan sengaja.** Di branch yang sama, ubah satu angka di tes (misalnya hasil yang diharapkan di `test_sample_data` sebuah modul), commit, push. Lihat CI menjadi merah dan baca log langkah `pytest`. Kembalikan perubahannya, push lagi, dan lihat CI kembali hijau.

**6. Pasang branch protection** untuk `main` seperti bagian C, lalu coba merge PR saat CI merah. GitHub harus menolak.

---

## 🏋️ Latihan

### ⭐ Latihan 7.1: Baca log yang merah

Langkah `ruff format --check .` gagal dengan pesan `1 file would be reformatted`. Apa artinya, dan perintah apa yang Anda jalankan di komputer sendiri untuk memperbaikinya?

### ⭐⭐ Latihan 7.2: Job frontend

Tambahkan job `frontend` yang memasang Node.js 22, menjalankan `npm ci` dan `npm run build` di folder `projects/ruang-rapat/frontend`. File apa yang **wajib** sudah di-commit agar `npm ci` berhasil?

### ⭐⭐ Latihan 7.3: Kenapa merah di CI, hijau di laptop?

Tes lulus di laptop Anda, tetapi gagal di CI dengan `ModuleNotFoundError: No module named 'flask'`. Apa penyebab paling mungkin, dan bagaimana memperbaikinya?

### ⭐⭐⭐ Latihan 7.4: Uji konfigurasi dulu

Sebelum push, bagaimana Anda bisa memastikan perintah di workflow benar-benar berjalan? Tulis urutan perintah yang Anda jalankan di komputer sendiri, persis seperti yang akan dijalankan CI, mulai dari folder kosong (petunjuk: `git clone`, `python -m venv`).

---

## 📝 Kuis

1. Apa beda CI dan CD?
2. Mengapa CI menangkap masalah yang tidak terlihat di laptop Anda?
3. Apa yang terjadi pada langkah-langkah berikutnya jika satu langkah di job gagal?
4. Apa fungsi branch protection "Require status checks to pass"?
5. Di mana menyimpan rahasia yang dibutuhkan workflow?

---

## 📌 Ringkasan

- CI menjalankan **ruff + pytest** otomatis untuk setiap push dan PR, di komputer yang bersih.
- Workflow = `on` (kapan) + `jobs` (paralel) + `steps` (berurutan: `uses` atau `run`).
- **Branch protection** membuat "CI hijau + review" menjadi syarat merge.
- Rahasia di **GitHub Secrets**, tidak pernah di file `.yml`.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 7.1:** ada file yang formatnya tidak sesuai `ruff format`. Jalankan `ruff format .` di komputer sendiri, periksa perubahannya dengan `git diff`, commit, lalu push. Log CI biasanya menyebut file mana yang dimaksud. (Ingat dari Level 2: `ruff format` juga merapikan blok kode Python di file `.md`.)

**Latihan 7.2**
```yaml
  frontend:
    name: Frontend (build)
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: projects/ruang-rapat/frontend
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - run: npm ci
      - run: npm run build
```
`package-lock.json` **wajib** di-commit. `npm ci` memasang versi yang persis tercatat di file itu, dan gagal jika file itu tidak ada. Ini membuat hasil di CI sama dengan di laptop. Folder `node_modules/` justru **tidak** boleh di-commit (Vite sudah menambahkannya ke `.gitignore` proyek frontend).

**Latihan 7.3:** `flask` terpasang di `.venv` laptop Anda, tetapi tidak tercatat di file yang dipasang CI (misalnya job hanya memasang `requirements-dev.txt`, bukan `requirements.txt` backend). Perbaiki dengan mencatat dependensinya di `requirements.txt` dan memasang file itu di workflow, seperti job `backend` di [`ci.yml`](latihan/ci/ci.yml).

**Latihan 7.4 (contoh, macOS/Linux)**
```bash
git clone <alamat-repo> /tmp/cek-ci && cd /tmp/cek-ci
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
ruff check . && ruff format --check . && pytest
```
Lalu ulangi untuk setiap job (misalnya `cd` ke folder backend, pasang `requirements.txt`-nya, jalankan `pytest`). Mulai dari clone baru memastikan Anda tidak bergantung pada file yang hanya ada di folder kerja Anda.

**Kuis**
1. CI = otomatis menguji setiap perubahan. CD = otomatis mengemas atau memasang aplikasi setelah lulus.
2. CI berjalan di komputer baru setiap kali, tanpa file atau library yang kebetulan ada di laptop Anda.
3. Langkah berikutnya tidak dijalankan, dan job ditandai gagal (merah).
4. PR tidak bisa di-merge sebelum job CI yang dipilih lulus.
5. Di GitHub: Settings → Secrets and variables → Actions, lalu dibaca dengan `${{ secrets.NAMA }}`.

</details>

---

← [Modul 6](modul-06-claude-api.md) | **Berikutnya: [Modul 8: Deploy dengan Docker →](modul-08-docker.md)**
