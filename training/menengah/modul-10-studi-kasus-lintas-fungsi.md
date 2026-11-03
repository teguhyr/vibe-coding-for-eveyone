# Modul 10: Studi Kasus Lintas Fungsi

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 10](../02-menengah.md#langkah-10-latihan-studi-kasus-lintas-fungsi) |
| **Sesi** | Sesi 5 (+ latihan mandiri) |
| **Durasi** | 110 menit di kelas: 1–2 kasus. Sisanya (minimal 3 kasus total) dikerjakan mandiri |
| **Prasyarat** | Modul 1–9 |
| **File latihan** | [`modules/03-hr`](../../modules/03-hr/) sampai [`modules/07-legal`](../../modules/07-legal/), [`latihan/kunci/reconcile_sqlite.py`](latihan/kunci/reconcile_sqlite.py) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjalankan **alur kerja Level 2 lengkap** tanpa dipandu langkah demi langkah.
2. Menerjemahkan kebutuhan bisnis menjadi **aturan, tes, dan kasus tepi**.
3. Menilai hasil buatan AI dengan angka yang dihitung sendiri.
4. Menjelaskan pekerjaannya: aturan bisnis, tes yang membuktikannya, dan satu kasus tepi yang ditemukan.

---

## 📖 Materi

### A. Alur kerja Level 2

Gunakan alur ini untuk **setiap** kasus. Centang setiap langkahnya.

| # | Langkah | Modul | Bukti selesai |
|---|---------|-------|---------------|
| 1 | Buat branch `latihan/<kasus>` | 8 | `git branch` menunjukkan branch aktif |
| 2 | Minta rencana di Plan Mode, tinjau efek domino | 4 | Rencana menyebut kode, tes, CSV, README |
| 3 | Tulis tes **dulu**, pastikan gagal | 2 | Tes merah |
| 4 | Implementasi sampai tes hijau | 2, 3 | `pytest` lulus |
| 5 | Rapikan | 5 | `ruff check .` dan `ruff format --check .` lulus |
| 6 | Verifikasi manual dengan angka sendiri | 1 | Tabel "dihitung sendiri vs program" cocok |
| 7 | Minta review, perbaiki temuan penting | 8 | Daftar temuan + tindakan |
| 8 | Commit kecil-kecil | 4 | `git log --oneline` |

> ⚠️ **Jangan merge kasus ini ke `main`.** Materi Level 1 dan 2 mengutip output asli modul-modul ini. Biarkan pekerjaan Anda tinggal di branch latihan, lalu kembali ke `main` dengan `git switch main`.

### B. Lembar kerja per kasus

Sebelum membuka Claude, isi lembar ini di kertas atau di file catatan:

```
Kasus           :
Aturan bisnis   : (tulis dengan angka dan batas yang jelas)
Tes yang ditulis: 1. ...  2. ...  3. ...
Kasus tepi      :
Hitungan manual : (input → hasil yang diharapkan)
Hasil program   :
Cocok?          :
```

---

## 🛠️ Lima Kasus

### Kasus 1 — HR: Cuti Setengah Hari

**Modul:** [`03-hr`](../../modules/03-hr/) · **Keterampilan:** tes dulu, perubahan model data

**Kebutuhan:** karyawan boleh mengambil cuti setengah hari. Tambahkan kolom `half_day` (`yes`/`no`) di `leave_requests.csv`.

**Aturan:**
- Cuti setengah hari dihitung **0,5** hari.
- Cuti setengah hari hanya boleh untuk **satu tanggal** (`start_date` = `end_date`). Jika tidak, tolak dengan `ValueError` yang menyebut ID karyawan.
- Cuti setengah hari di akhir pekan atau hari libur dihitung **0**.
- Nilai `half_day` selain yes/no ditolak.

**Data uji:** isi `no` untuk semua baris lama, lalu tambahkan satu baris `E003,2026-11-04,2026-11-04,approved,yes`.

### Kasus 2 — Marketing: Ringkasan per Channel dari Total

**Modul:** [`04-marketing`](../../modules/04-marketing/) · **Keterampilan:** logika agregasi

**Kebutuhan:** tambahkan tabel ringkasan per channel di bawah tabel kampanye.

**Aturan:** metrik per channel dihitung dari **total** (jumlah pendapatan ÷ jumlah biaya), **bukan** rata-rata metrik setiap kampanye. Pembagian dengan nol tetap menghasilkan `n/a`.

**Pertanyaan pemanasan:** channel mana yang punya lebih dari satu kampanye? Hitung ROAS-nya dengan dua cara (total vs rata-rata) sebelum menulis prompt.

### Kasus 3 — IT: Peringatan Dini SLA

**Modul:** [`05-it`](../../modules/05-it/) · **Keterampilan:** aritmetika waktu, kasus tepi

**Kebutuhan:** tampilkan tiket **terbuka** yang akan melanggar SLA dalam **2 jam** ke depan, agar tim sempat bertindak.

**Aturan:**
- Sisa waktu = target SLA − jam berjalan.
- Masuk peringatan jika tiket masih terbuka, **belum** melanggar SLA, dan sisa waktu **≤ 2 jam**.
- Batas 2 jam bisa diubah dengan argumen `--warn-hours`.
- Tiket yang sudah melanggar tetap muncul di daftar pelanggaran, **bukan** di daftar peringatan.

**Uji dengan beberapa waktu:** `--now 2026-11-02T12:00`, `14:00`, `14:30`, `16:00`, `16:01`.

### Kasus 4 — Akuntansi: Rekonsiliasi dengan SQL JOIN

**Modul:** [`06-accounting`](../../modules/06-accounting/) · **Keterampilan:** SQL

**Kebutuhan:** muat `bank_statement.csv` dan `ledger.csv` ke SQLite, lalu cocokkan dengan `JOIN`: nominal sama dan selisih tanggal **≤ 3 hari**. Tampilkan pasangan yang cocok, transaksi yang hanya ada di bank, dan yang hanya ada di ledger.

**Aturan:**
- Simpan uang dalam **satuan sen** (`INTEGER`), bukan `REAL`.
- Hasil harus sama dengan `python modules/06-accounting/bank_reconciliation.py`.
- Pakai `sqlite3.connect(":memory:")` agar tidak ada file `.db`.

**Pertanyaan penting:** program Python memastikan **satu entri ledger hanya dipakai sekali**. Apakah query `JOIN` Anda juga menjamin itu?

### Kasus 5 — Legal: Ekspor Tenggat ke Kalender

**Modul:** [`07-legal`](../../modules/07-legal/) · **Keterampilan:** format file baru

**Kebutuhan:** tim legal ingin tenggat pemberitahuan muncul di kalender (Outlook/Google Calendar). Tambahkan argumen `--ics <file>` yang menulis file kalender `.ics`.

**Aturan:**
- Hanya kontrak berstatus **ACT NOW** yang diekspor (tenggatnya masih di depan).
- Satu acara sepanjang hari (*all-day*) per kontrak, pada tanggal **Notice by**.
- Judul acara: `Notice deadline: <ID> <counterparty>`.
- Format mengikuti standar iCalendar (RFC 5545): `BEGIN:VCALENDAR`, `VERSION:2.0`, `PRODID`, lalu satu `VEVENT` per kontrak dengan `UID`, `DTSTAMP`, `DTSTART;VALUE=DATE`, `SUMMARY`. Baris diakhiri `\r\n`.

**Uji dengan:** `--today 2026-11-02`, lalu impor file hasilnya ke aplikasi kalender Anda.

---

## 🏋️ Latihan

### ⭐⭐ Latihan 10.1: Satu kasus di kelas

Kerjakan **satu** kasus sesuai fungsi Anda dengan alur di bagian A, sampai langkah 8.

### ⭐⭐⭐ Latihan 10.2: Minimal tiga kasus

Selesaikan minimal **3** dari 5 kasus (boleh mandiri). Untuk setiap kasus, isi lembar kerja di bagian B.

### ⭐⭐⭐ Latihan 10.3: Tukar review

Tukar branch dengan satu rekan dari fungsi lain. Tinjau pekerjaannya dengan [checklist reviewer di Modul 8](modul-08-branch-review.md#c-checklist-reviewer) dan tulis minimal 2 temuan atau pertanyaan.

---

## 📝 Kuis

1. Mengapa kasus-kasus ini tidak di-merge ke `main`?
2. Di Kasus 2, mengapa rata-rata ROAS kampanye bisa menyesatkan?
3. Di Kasus 3, apakah tiket dengan sisa waktu tepat 0 jam masuk peringatan atau pelanggaran? Mengapa?
4. Di Kasus 4, mengapa uang disimpan dalam sen?
5. Di Kasus 5, mengapa kontrak berstatus NOTICE PERIOD PASSED tidak diekspor?

---

## 📌 Ringkasan

- Alur Level 2: **branch → rencana → tes dulu → implementasi → ruff → verifikasi manual → review → commit**.
- Setiap kasus selalu punya **aturan**, **tes yang membuktikan**, dan **kasus tepi**.
- Hitung sendiri sebelum percaya pada hasil program, baik buatan AI maupun buatan manusia.

---

<details>
<summary>🔑 <b>Kunci Jawaban (angka verifikasi)</b></summary>

Kode buatan Claude bisa berbeda-beda. Nilai **perilaku** dan **angka**, bukan kesamaan kode.

**Kasus 1 — HR.** Dengan baris tambahan `E003,2026-11-04,2026-11-04,approved,yes`:

| ID | Used | Left | Pending |
|----|------|------|---------|
| E001 | 9 | 3 | 0 |
| E002 | 10 | 2 | 4 |
| E003 | **3.5** | **11.5** | 0 |
| E004 | 13 | −1 | 0 |

Tes minimal: setengah hari di hari kerja = 0,5; setengah hari di hari Sabtu = 0; setengah hari dengan `start_date` ≠ `end_date` → `ValueError` yang menyebut ID; `half_day` berisi `maybe` → `ValueError`. Kasus tepi yang sering terlewat: **tipe data** berubah dari bilangan bulat ke desimal, sehingga format tabel (`{b.used:>5}`) dan `test_sample_data` ikut berubah. Alternatif yang rapi: hitung dalam satuan **setengah hari** (bilangan bulat) dan bagi 2 hanya saat ditampilkan.

**Kasus 2 — Marketing**

| Channel | Spend | Revenue | ROAS dari total ✅ | Rata-rata ROAS kampanye ❌ |
|---------|-------|---------|-------------------|---------------------------|
| Email | 500 | 6.000 | 12.0 | 12.0 |
| Instagram | 5.000 | 24.000 | 4.8 | 4.8 |
| Google Ads | 5.000 | 17.400 | **3.5** (3,48) | **3.1** ((5,0 + 1,2) ÷ 2) |
| TikTok | 4.000 | 0 | 0.0 | 0.0 |
| Offline | 8.000 | 0 | 0.0 | 0.0 |

Google Ads punya dua kampanye dengan biaya berbeda (3.000 dan 2.000). Rata-rata biasa memperlakukan keduanya sama berat, padahal uang yang dibelanjakan berbeda. CTR Google Ads dari total: 4.800 ÷ 460.000 = **1,0%**, sedangkan rata-rata CTR kampanye (6,0% + 0,3%) ÷ 2 = 3,15%, jauh lebih tinggi. Offline: impresi 0 → CTR `n/a`.

**Kasus 3 — IT.** Satu-satunya tiket terbuka yang belum melanggar adalah `INC-1005` (P2, dibuka 08:00, SLA 8 jam → melanggar setelah 16:00).

| `--now` | Sisa waktu INC-1005 | Masuk peringatan? |
|---------|--------------------|-------------------|
| 2026-11-02T12:00 | 4,0 jam | Tidak |
| 2026-11-02T14:00 | 2,0 jam | **Ya** (tepat di batas, ≤ 2) |
| 2026-11-02T14:30 | 1,5 jam | **Ya** |
| 2026-11-02T16:00 | 0,0 jam | **Ya** (belum melanggar, karena pelanggaran = jam berjalan **>** SLA) |
| 2026-11-02T16:01 | −0,02 jam | Tidak, kini masuk daftar **pelanggaran** sebagai `OPEN` |

`INC-1006` (P4) sudah melanggar sejak awal, jadi tidak pernah masuk peringatan. Tes minimal: tepat 2 jam masuk; 2 jam 1 menit tidak; tepat 0 jam masuk; tiket yang sudah selesai tidak pernah masuk.

**Kasus 4 — Akuntansi.** Contoh solusi: [`latihan/kunci/reconcile_sqlite.py`](latihan/kunci/reconcile_sqlite.py).

```bash
python training/menengah/latihan/kunci/reconcile_sqlite.py
```

```
Cocok:
  2026-10-01 Transfer in - customer     = 2026-10-01 INV-2038 receipt    15,000.00
  2026-10-03 Office rent October        = 2026-10-02 Rent Oct            -8,000.00
  2026-10-07 Customer payment INV-2041  = 2026-10-05 INV-2041 receipt     4,250.50
  2026-10-15 Payroll transfer           = 2026-10-15 Payroll Oct        -12,000.00
  2026-10-20 Supplier payment PO-881    = 2026-10-20 PO-881 payment      -1,875.25

Hanya di bank (catat di pembukuan):
  2026-10-31 Bank admin fee                 -25.00
  2026-10-31 Interest income                 12.40

Hanya di ledger (cek waktu/kesalahan):
  2026-10-29 CHQ-5512 Utilities            -640.00
  2026-10-30 INV-2050 receipt             2,300.00
```

Hasilnya sama dengan modul 06 (5 cocok, 2 hanya di bank, 2 hanya di ledger). ✔

**Jawaban pertanyaan penting:** **tidak**. Jika bank punya **dua** baris `-100.00` di tanggal yang sama dan ledger hanya **satu**, `JOIN` mencocokkan **keduanya** dengan entri ledger yang sama (2 pasangan), dan `NOT EXISTS` menganggap tidak ada yang tersisa di bank. Program Python menghasilkan 1 pasangan + 1 baris "hanya di bank", dan itulah yang benar. Pelajarannya: SQL hebat untuk mencari kandidat, tetapi aturan "satu entri hanya dipakai sekali" perlu langkah tambahan (misalnya memilih pasangan dengan Python, atau window function `ROW_NUMBER()`). Tulis tes untuk kasus dobel ini.

**Kasus 5 — Legal.** Dengan `--today 2026-11-02`, hanya 2 kontrak berstatus ACT NOW: `CTR-001` (Notice by 2026-12-16) dan `CTR-005` (Notice by 2026-12-17). Contoh isi file:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Vibe Coding Training//Contract Renewals//EN
BEGIN:VEVENT
UID:CTR-001-notice@contract-renewals
DTSTAMP:20261102T000000Z
DTSTART;VALUE=DATE:20261216
SUMMARY:Notice deadline: CTR-001 PT Sample Logistics
END:VEVENT
BEGIN:VEVENT
UID:CTR-005-notice@contract-renewals
DTSTAMP:20261102T000000Z
DTSTART;VALUE=DATE:20261217
SUMMARY:Notice deadline: CTR-005 Sample Cleaning Services
END:VEVENT
END:VCALENDAR
```

Tes minimal: hanya ACT NOW yang diekspor; tanggal `DTSTART` = `notice_deadline`; jumlah `BEGIN:VEVENT` = jumlah kontrak ACT NOW; setiap baris diakhiri `\r\n`. Kasus tepi: nama pihak yang mengandung koma atau titik koma (misalnya `PT Maju, Tbk`) harus di-*escape* menjadi `PT Maju\, Tbk` menurut RFC 5545; `UID` harus tetap sama setiap kali ekspor agar kalender tidak membuat acara dobel saat file diimpor ulang.

**Kuis**
1. Materi pelatihan dan README mengutip output asli modul-modul ini. Merge akan membuat materi itu salah (efek domino, Modul 4).
2. Rata-rata biasa memberi bobot sama pada kampanye kecil dan besar. ROAS seharusnya mencerminkan total uang yang dibelanjakan dan didapat.
3. Peringatan. Tiket melanggar SLA hanya jika jam berjalan **lebih dari** target. Tepat 0 jam tersisa berarti tepat di target, belum melanggar.
4. Agar penjumlahan persis. `REAL` (float) bisa menimbulkan selisih pembulatan kecil, dan rekonsiliasi membutuhkan kecocokan yang persis.
5. Tenggatnya sudah lewat. Acara kalender di masa lalu tidak membantu siapa pun bertindak. Kontrak seperti itu perlu ditangani langsung, bukan diingatkan.

</details>

---

← [Modul 9](modul-09-data-aman.md) | **Berikutnya: [Proyek Akhir Level 2 →](proyek-akhir.md)**
