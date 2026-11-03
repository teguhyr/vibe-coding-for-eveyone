# Modul 8: Branch, Review, dan Kolaborasi

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 8](../02-menengah.md#langkah-8-branch-review-dan-kolaborasi) |
| **Sesi** | Sesi 4 |
| **Durasi** | 45 menit |
| **Prasyarat** | Modul 7 (folder `~/proyek-reimburse` sudah dibuat dan di-commit), Level 1 Modul 10 (Git) |
| **File latihan** | `~/proyek-reimburse/expense_claims.py` (salinan dari [`latihan/expense_claims.py`](latihan/expense_claims.py)) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Membuat, berpindah, menggabungkan (*merge*), dan menghapus branch.
2. Membandingkan branch dengan `main` memakai `git diff`.
3. Meminta Claude meninjau perubahan sebagai **reviewer**, dan meninjau sendiri dengan checklist.
4. Menjelaskan alur **Pull Request** di GitHub.
5. Menyelesaikan **merge conflict** sederhana.

---

## 📖 Materi

### A. Branch = "Save As" ke draf

Sebelum mengedit dokumen penting, Anda menyimpan salinan draf. Setelah draf diperiksa dan disetujui, isinya dipindah ke versi resmi. Branch bekerja persis seperti itu, tetapi untuk seluruh proyek.

```
main            ●────────●────────────────●  (versi resmi, selalu lulus tes)
                 \                       /
fitur/filter      ●────●────●───────────     (kerja → review → merge)
```

### B. Perintah inti

| Perintah | Fungsi |
|----------|--------|
| `git switch -c fitur/nama` | Buat branch baru dan pindah ke sana |
| `git branch` | Lihat semua branch (`*` = branch aktif) |
| `git switch main` | Pindah ke branch `main` |
| `git diff main` | Bandingkan isi file sekarang dengan `main` |
| `git log --oneline --graph --all` | Lihat riwayat semua branch sebagai gambar |
| `git merge fitur/nama` | Gabungkan branch itu ke branch aktif |
| `git branch -d fitur/nama` | Hapus branch yang sudah di-merge |

**Nama branch** yang baik menjelaskan isinya: `fitur/filter-departemen`, `perbaikan/lembur-nol-jam`, `latihan/goal-kampanye`.

### C. Checklist reviewer

Review adalah **pemeriksaan kedua** sebelum perubahan masuk ke versi resmi. Gunakan 5 pertanyaan ini, baik saat Anda meninjau sendiri maupun membaca hasil review Claude:

| # | Pertanyaan |
|---|------------|
| 1 | **Benar?** Apakah perilakunya sesuai aturan bisnis, termasuk di batas? |
| 2 | **Teruji?** Ada tes untuk perilaku baru? Ada tes yang dihapus atau dilemahkan? |
| 3 | **Input salah?** Apa yang terjadi dengan data kosong, salah ketik, atau tidak dikenal? |
| 4 | **Aman?** Ada rahasia, data pribadi, atau file yang tidak seharusnya ikut? |
| 5 | **Jelas?** Nama, pesan commit, dan dokumentasi mudah dipahami? |

### D. Pull Request (PR)

Di GitHub, perubahan dari branch tidak langsung di-merge. Anda membuat **Pull Request**: halaman berisi daftar perubahan, tempat rekan memberi komentar, dan hasil pemeriksaan otomatis. Setelah disetujui, PR di-merge ke `main`.

```
push branch ──▶ buka PR ──▶ review + tes otomatis ──▶ perbaiki ──▶ disetujui ──▶ merge
```

Prinsipnya sama dengan yang Anda lakukan di komputer sendiri di modul ini. Level 3 membahas tes otomatis di GitHub (CI).

### E. Merge conflict

*Conflict* terjadi jika **dua branch mengubah baris yang sama** dengan cara berbeda. Git tidak bisa memutuskan mana yang benar, jadi ia menandainya:

```
<<<<<<< HEAD
MAX_SUBMIT_DAYS = 45
=======
MAX_SUBMIT_DAYS = 60
>>>>>>> batas-60
```

| Penanda | Arti |
|---------|------|
| `<<<<<<< HEAD` sampai `=======` | Versi di branch aktif (yang sudah ada) |
| `=======` sampai `>>>>>>> batas-60` | Versi dari branch yang sedang di-merge |

Cara menyelesaikan: **tanyakan dulu ke pemilik aturan bisnis** mana yang benar, edit file sehingga hanya tersisa versi yang benar (hapus ketiga penanda), jalankan tes, lalu `git add` dan `git commit`. Jika ragu, `git merge --abort` membatalkan merge dan mengembalikan keadaan semula.

> ⚠️ Conflict bukan masalah teknis, melainkan **pertanyaan bisnis**: "kebijakan mana yang berlaku?" Jangan biarkan siapa pun, termasuk AI, menebak jawabannya.

---

## 🛠️ Praktik Terpandu: Filter Departemen

**Kebutuhan:** manajer departemen ingin melihat klaim departemennya saja, dengan perintah seperti `python expense_claims.py --department it`. Huruf besar/kecil tidak berpengaruh.

**1. Buat branch** di proyek dari Modul 7:

```bash
cd ~/proyek-reimburse
```

```bash
git switch -c fitur/filter-departemen
```

**2. Minta perubahan dengan tes dulu.** Jalankan `claude`, lalu:

```
Di @expense_claims.py tambahkan argumen --department untuk menampilkan klaim satu
departemen saja (tidak peka huruf besar/kecil). Logikanya harus di fungsi murni
filter_by_department(decisions, department). Tulis tes pytest dulu untuk fungsi itu
(termasuk "it" vs "IT"), tunjukkan ke saya, baru ubah kode. Tanpa --department,
hasil program harus sama persis seperti sekarang.
```

**3. Verifikasi.**

```bash
pytest
```

```bash
python expense_claims.py --department it
```

```
Claim  Emp   Category       Amount    Payable  Status
C-05   K003  transport     100,000          0  REJECTED: no receipt
C-06   K003  meal           85,000     85,000  APPROVED

Payable by department
IT               85,000
TOTAL            85,000
```

Jalankan juga tanpa `--department`: hasilnya harus sama dengan Modul 1.

**4. Commit.**

```bash
git add expense_claims.py test_expense_claims.py
```

```bash
git commit -m "Add --department filter to expense claim report"
```

**5. Minta review.**

```
Tinjau semua perubahan di branch ini dibandingkan main (git diff main).
Pakai checklist: benar, teruji, input salah, aman, jelas.
Cari bug dan kasus tepi yang terlewat. Urutkan dari yang paling serius.
Jangan ubah file apa pun.
```

Coba sendiri juga: `python expense_claims.py --department Marketing`. Apa yang terjadi? Apakah itu perilaku yang baik? (Lihat kunci.)

**6. Merge ke `main`** setelah temuan penting diperbaiki dan tes lulus:

```bash
git switch main
```

```bash
git merge fitur/filter-departemen
```

```bash
git branch -d fitur/filter-departemen
```

```bash
git log --oneline --graph --all
```

---

## 🏋️ Latihan

### ⭐ Latihan 8.1: Branch untuk setiap fitur

Tuliskan nama branch yang baik untuk: (a) menambah kategori `parking`; (b) memperbaiki bug lembur 0 jam; (c) eksperimen membaca file Excel yang mungkin dibuang.

### ⭐⭐ Latihan 8.2: Jadilah reviewer

Seorang rekan mengirim *diff* ini. Temukan **3 masalah** dengan checklist reviewer:

```diff
--- a/expense_claims.py
+++ b/expense_claims.py
@@
 MAX_SUBMIT_DAYS = 30
 RECEIPT_REQUIRED_FROM = 100_000
+EXPORT_TOKEN = "tok_live_CONTOH_PALSU_123"
@@
 def review_claim(claim: Claim) -> Decision:
-    if claim.days_to_submit > MAX_SUBMIT_DAYS:
+    if claim.days_to_submit >= MAX_SUBMIT_DAYS:
         return Decision(claim, REJECTED_LATE, 0)
--- a/test_expense_claims.py
+++ b/test_expense_claims.py
@@
-def test_late_claim_is_rejected():
-    decision = review_claim(claim(days_late=45))
-    assert (decision.status, decision.payable) == (REJECTED_LATE, 0)
```

Pesan commit-nya: `rapikan kode`.

### ⭐⭐ Latihan 8.3: Departemen yang tidak ada

Perbaiki perilaku `--department` untuk departemen yang tidak ada di data (temuan dari Praktik langkah 5). Kerjakan di branch baru, tes dulu, lalu merge.

### ⭐⭐⭐ Latihan 8.4: Selesaikan merge conflict

Di `~/proyek-reimburse`, buat conflict dengan sengaja:

```bash
git switch -c batas-45
```

Ubah `MAX_SUBMIT_DAYS = 30` menjadi `45`, lalu `git commit -am "Allow claims up to 45 days"`.

```bash
git switch main
```

```bash
git switch -c batas-60
```

Ubah `MAX_SUBMIT_DAYS = 30` menjadi `60`, lalu `git commit -am "Allow claims up to 60 days"`.

```bash
git switch main
```

```bash
git merge batas-45
```

```bash
git merge batas-60
```

Merge kedua menghasilkan `CONFLICT`. Anggap Manajer Keuangan memutuskan **45 hari**. Selesaikan conflict-nya. Tes mana yang perlu disesuaikan karena kebijakan berubah?

---

## 📝 Kuis

1. Mengapa sebaiknya tidak bekerja langsung di `main`?
2. Apa yang ditunjukkan `git diff main` saat Anda berada di branch fitur?
3. Sebutkan 5 pertanyaan checklist reviewer.
4. Kapan merge conflict terjadi?
5. Anda bingung saat merge conflict dan ingin kembali ke keadaan sebelum merge. Perintah apa yang dipakai?

---

## 📌 Ringkasan

- **Satu fitur = satu branch.** `main` selalu dalam keadaan lulus tes.
- Sebelum merge: `pytest`, ruff, lalu **review** dengan 5 pertanyaan: benar, teruji, input salah, aman, jelas.
- Pull Request = review yang sama, tetapi di GitHub dan bersama rekan.
- Merge conflict adalah **pertanyaan bisnis**. Tanyakan ke pemilik aturan, jangan menebak.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Praktik langkah 5 (temuan review yang diharapkan):**
`--department Marketing` menampilkan tabel kosong dan `TOTAL 0` **tanpa peringatan**:

```
Claim  Emp   Category       Amount    Payable  Status

Payable by department
TOTAL                 0
```

Manajer bisa mengira "departemen saya tidak punya klaim", padahal mungkin salah ketik nama departemen. Perilaku yang lebih baik: cetak pesan seperti `No claims for department 'Marketing'. Known departments: Finance, IT, Operations, Sales` dan keluar dengan kode error. Temuan lain yang mungkin muncul: spasi di awal/akhir nama departemen, dan apakah filter juga perlu memakai kode departemen.

Contoh implementasi inti (detail buatan Claude bisa berbeda):
```python
def filter_by_department(decisions: list[Decision], department: str) -> list[Decision]:
    wanted = department.strip().lower()
    return [d for d in decisions if d.claim.department.lower() == wanted]
```

**Latihan 8.1 (contoh):** (a) `fitur/kategori-parking`; (b) `perbaikan/lembur-nol-jam`; (c) `eksperimen/baca-excel`.

**Latihan 8.2:** tiga masalah:
1. **Aman?** Ada token/rahasia yang ditulis di kode (`EXPORT_TOKEN`). Tolak, minta dipindah ke variabel lingkungan (`.env`). Jika itu token asli yang sudah ter-push, token harus **diganti (rotate)**.
2. **Benar?** `>` diganti `>=`: klaim yang diajukan **tepat 30 hari** kini ditolak. Ini mengubah kebijakan tanpa dibahas, dan `C-07` di data contoh akan berubah dari `APPROVED` menjadi `REJECTED: late`.
3. **Teruji?** Tes `test_late_claim_is_rejected` **dihapus**. Menghapus tes agar perubahan "lulus" adalah tanda bahaya.

Bonus: pesan commit `rapikan kode` menyesatkan, karena perubahan ini mengubah perilaku, bukan sekadar merapikan.

**Latihan 8.3 (contoh):** buat fungsi murni untuk daftar departemen, uji dulu:
```python
def decision_for(department: str) -> Decision:
    expense = date(2026, 10, 1)
    return review_claim(Claim("X", "K1", department, "meal", expense, expense, 10_000, True))


def test_known_departments_are_listed_once_and_sorted():
    decisions = [decision_for("Sales"), decision_for("IT"), decision_for("Sales")]
    assert known_departments(decisions) == ["IT", "Sales"]
```
```python
def known_departments(decisions: list[Decision]) -> list[str]:
    return sorted({d.claim.department for d in decisions})
```
Lalu di `main()`, simpan daftar sebelum difilter sebagai `all_decisions`, dan hentikan program jika hasil filter kosong:
```python
    all_decisions = [review_claim(c) for c in load_claims(args.csv_file)]
    decisions = all_decisions
    if args.department:
        decisions = filter_by_department(all_decisions, args.department)
        if not decisions:
            known = ", ".join(known_departments(all_decisions))
            parser.error(f"no claims for department {args.department!r}. Known: {known}")
```
```
usage: expense_claims.py [-h] [--department DEPARTMENT] [csv_file]
expense_claims.py: error: no claims for department 'Marketing'. Known: Finance, IT, Operations, Sales
```
`parser.error` mencetak pesan dan menghentikan program dengan kode error 2. Yang dinilai: ada tes, pesannya jelas, dan perilaku tanpa `--department` tidak berubah.

**Latihan 8.4:** setelah `git merge batas-60`:

```
Auto-merging expense_claims.py
CONFLICT (content): Merge conflict in expense_claims.py
Automatic merge failed; fix conflicts and then commit the result.
```

Edit bagian yang ditandai menjadi:

```python
MAX_SUBMIT_DAYS = 45
```

(hapus `<<<<<<<`, `=======`, `>>>>>>>` dan baris `= 60`). Lalu:

```bash
pytest
```

```bash
git add expense_claims.py
```

```bash
git commit -m "Merge batas-60: keep 45-day limit decided by Finance Manager"
```

Tes yang perlu disesuaikan: tes yang memakai batas 30 hari. `test_late_claim_is_rejected` (45 hari) **gagal**, karena 45 hari kini masih tepat waktu. Ganti contohnya menjadi 46 hari, tambahkan tes "tepat 45 hari masih tepat waktu", dan perbarui docstring + `CLAUDE.md` (aturan "> 30 hari"). Ini sah karena **aturan bisnisnya memang berubah**, bukan agar tes lulus. Perhatikan juga: `C-03` (39 hari) kini disetujui, jadi total contoh berubah.

**Kuis**
1. Agar eksperimen atau pekerjaan setengah jadi tidak merusak versi resmi yang dipakai orang lain.
2. Semua perbedaan isi file antara keadaan sekarang dan branch `main`.
3. Benar? Teruji? Input salah? Aman? Jelas?
4. Saat dua branch mengubah baris yang sama dengan cara berbeda.
5. `git merge --abort`.

</details>

---

← [Modul 7](modul-07-claude-md.md) | **Berikutnya: [Modul 9: Data Asli dengan Aman →](modul-09-data-aman.md)**
