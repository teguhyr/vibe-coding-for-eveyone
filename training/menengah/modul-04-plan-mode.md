# Modul 4: Merencanakan Perubahan Besar (Plan Mode)

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 4](../02-menengah.md#langkah-4-merencanakan-perubahan-besar-plan-mode) |
| **Sesi** | Sesi 2 |
| **Durasi** | 60 menit |
| **Prasyarat** | Modul 2 (tes), Level 1 Modul 10 (Git) |
| **File latihan** | [`modules/04-marketing/`](../../modules/04-marketing/) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Mengenali kapan sebuah perubahan perlu **rencana dulu**.
2. Memakai **Plan Mode** di Claude Code untuk meminta rencana tanpa mengubah file.
3. Meninjau rencana dengan checklist, termasuk **efek domino** ke tes, README, dan materi lain.
4. Mengerjakan rencana **satu langkah, satu commit**.

---

## 📖 Materi

### A. Kapan perlu rencana?

Seperti renovasi rumah: mengganti bohlam tidak perlu gambar arsitek, tetapi menambah kamar perlu. Minta rencana dulu jika perubahan:

- menyentuh **lebih dari satu file**;
- mengubah **model data** atau kolom CSV;
- mengubah **hasil** yang sudah dipakai orang lain (laporan, contoh output);
- menambah **aturan bisnis** baru yang berinteraksi dengan aturan lama.

### B. Plan Mode

Di Plan Mode, Claude **hanya membaca dan menyusun rencana**. Ia tidak mengubah file dan tidak menjalankan perintah yang mengubah apa pun.

| Cara | Langkah |
|------|---------|
| Saat Claude Code sudah berjalan | Tekan `Shift+Tab` berulang kali. Mode berganti: normal → *auto-accept edits* → *plan mode*. Berhenti saat muncul tanda **plan mode** di bawah kotak input |
| Saat memulai | `claude --permission-mode plan` |

Setelah rencana disetujui, Claude akan menawarkan untuk keluar dari Plan Mode dan mulai bekerja. Anda tetap menyetujui setiap perubahan seperti biasa.

> ⚠️ Hindari memilih mode *auto-accept edits* saat belajar. Anda kehilangan kesempatan meninjau setiap perubahan.

### C. Isi rencana yang baik

| Bagian | Contoh |
|--------|--------|
| **File yang diubah** | `campaign_metrics.py`, `test_campaign_metrics.py`, `data/campaigns.csv`, `README.md` |
| **Urutan langkah** | Tes dulu → model data → pembacaan CSV → aturan → data contoh → dokumentasi |
| **Tes yang ditambah** | "Kampanye awareness dengan ROAS 0 tidak ditandai" |
| **Risiko** | `test_sample_data` berubah; nilai `goal` salah ketik di CSV |
| **Yang TIDAK diubah** | Rumus CTR/CPC/CPA/ROAS, urutan ranking |

### D. Efek domino di repositori ini

Repositori ini punya aturan (lihat [`CLAUDE.md`](../../CLAUDE.md)): **mengubah CSV contoh akan mematahkan `test_sample_data` dan contoh output di README modul itu**. Materi di folder `training/` juga mengutip output modul. Satu perubahan bisa merambat:

```
data/campaigns.csv ──▶ test_sample_data ──▶ README modul (Step 2: Run it) ──▶ training/*.md
```

Rencana yang baik **menyebut semua mata rantai ini**. Cari kutipan output di materi dengan:

```bash
grep -rn "below target" training/
```

### E. Satu langkah, satu commit

```
●── tes: awareness tidak ditandai (MERAH)
●── model + CSV: kolom goal (HIJAU)
●── validasi: goal tidak dikenal ditolak
●── docs: README modul 04
```

Setiap langkah yang lulus tes langsung di-commit. Jika langkah berikutnya kacau, Anda tinggal kembali satu langkah (`git checkout -- .` untuk membuang perubahan yang belum di-commit).

---

## 🛠️ Praktik Terpandu: Kolom "goal" di Modul Marketing

**Kebutuhan bisnis:** kampanye *awareness* (memperkenalkan merek) memang tidak ditujukan untuk penjualan langsung. Menandainya "below target ROAS" membuat tim marketing salah menilai. Tambahkan kolom `goal` (`awareness` atau `sales`). Kampanye `awareness` **tidak boleh** ditandai.

**1. Buat branch** (pekerjaan ini **tidak** di-merge ke `main`, lihat langkah 7):

```bash
git switch -c latihan/goal-kampanye
```

**2. Minta rencana di Plan Mode.** Jalankan `claude`, tekan `Shift+Tab` sampai muncul *plan mode*, lalu ketik:

```
Saya ingin menambah kolom "goal" (awareness atau sales) di
modules/04-marketing/data/campaigns.csv. Kampanye awareness tidak boleh ditandai
"below target ROAS". Influencer Trial dan City Billboard adalah awareness; sisanya sales.
Nilai goal selain awareness/sales harus ditolak dengan ValueError yang menyebut nama kampanye.
Buat rencana langkah demi langkah: file apa yang diubah, tes apa yang ditambah (tes dulu),
dan apa risikonya. Jangan ubah apa pun dulu.
```

**3. Tinjau rencananya** dengan checklist ini:

- [ ] Ada langkah **tes dulu**?
- [ ] `test_sample_data` disebut akan berubah?
- [ ] README modul 04 (contoh output) disebut?
- [ ] Ada validasi untuk nilai `goal` yang salah?
- [ ] Ada yang disebut **tidak** diubah (rumus, urutan ranking)?

Jika ada yang kurang, minta Claude memperbaiki rencananya **sebelum** keluar dari Plan Mode.

**4. Kerjakan satu langkah per satu waktu.** Setelah setiap langkah:

```bash
pytest modules/04-marketing
```

```bash
git add modules/04-marketing
```

```bash
git commit -m "<pesan yang menjelaskan langkah ini>"
```

**5. Periksa hasilnya.**

```bash
python modules/04-marketing/campaign_metrics.py
```

Hanya **Display Retarget** yang masih bertanda `<-- below target ROAS`.

**6. Periksa riwayatnya.**

```bash
git log --oneline -5
```

Harus berisi beberapa commit kecil, bukan satu commit raksasa.

**7. Kembali ke `main` tanpa merge.** Materi Level 1 dan Level 2 mengutip output asli modul 04, jadi perubahan ini tetap tinggal di branch latihan:

```bash
git switch main
```

> 💡 Inilah efek domino dalam praktik. Jika fitur ini sungguhan, rencana harus menyertakan pembaruan materi `training/` yang mengutip output modul 04.

---

## 🏋️ Latihan

### ⭐ Latihan 4.1: Temukan yang kurang

Claude memberi rencana ini untuk "tambah kategori `parking` (batas Rp50.000) di `expense_claims.py`":

```
1. Tambahkan "parking": 50_000 ke CATEGORY_LIMITS.
2. Jalankan program untuk memastikan tidak ada error.
```

Sebutkan minimal 3 hal yang kurang.

### ⭐⭐ Latihan 4.2: Tulis prompt rencana

Tim HR ingin [`modules/03-hr/leave_tracker.py`](../../modules/03-hr/leave_tracker.py) menampilkan karyawan yang sisa cutinya **≤ 2 hari** di bagian terpisah. Tulis prompt Plan Mode yang lengkap (kebutuhan, batasan, apa yang tidak boleh berubah, permintaan rencana).

### ⭐⭐ Latihan 4.3: Commit yang terlalu besar

Seorang rekan membuat satu commit berjudul `update` yang mengubah 6 file sekaligus: kode, tes, CSV, README, dan dua file yang tidak berhubungan. Sebutkan 2 masalah yang muncul saat salah satu perubahan ternyata salah.

### ⭐⭐⭐ Latihan 4.4: Rencana berisiko

Atasan meminta: *"Program reimburse harus bisa membaca file Excel langsung, bukan CSV."* Di Plan Mode, minta Claude menyusun rencana, lalu temukan **risiko yang khusus untuk repositori ini**. Petunjuk: baca bagian *Commands* di [`CLAUDE.md`](../../CLAUDE.md) dan isi [`.gitignore`](../../.gitignore).

---

## 📝 Kuis

1. Apa yang **tidak** dilakukan Claude saat berada di Plan Mode?
2. Bagaimana cara masuk ke Plan Mode saat Claude Code sudah berjalan?
3. Sebutkan 3 file yang biasanya ikut berubah jika Anda mengubah CSV contoh sebuah modul.
4. Mengapa "satu langkah, satu commit" memudahkan saat terjadi kesalahan?

---

## 📌 Ringkasan

- Perubahan besar: **rencana dulu, kode belakangan**.
- Plan Mode (`Shift+Tab`) = Claude membaca dan merencanakan, **tanpa** mengubah file.
- Tinjau rencana: tes dulu, efek domino (tes, README, materi), validasi, dan apa yang tidak berubah.
- Kerjakan **satu langkah, satu commit**, dengan `pytest` di setiap langkah.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Praktik terpandu (hasil yang diharapkan).** Detail kode buatan Claude bisa berbeda, tetapi perilakunya harus sama:

```
Campaign           Channel        CTR    CPC     CPA   ROAS
Email Newsletter   Email         5.0%   0.25    6.25   12.0
Search Brand       Google Ads    6.0%   0.83   20.00    5.0
Ramadan Promo      Instagram     2.0%   1.00   25.00    4.8
Display Retarget   Google Ads    0.3%   1.67   66.67    1.2  <-- below target ROAS
Influencer Trial   TikTok        1.5%   1.48     n/a    0.0
City Billboard     Offline        n/a    n/a     n/a    0.0
```

Jika Claude menambah kolom `Goal` ke tabel, tidak masalah, asalkan disebut di rencana dan README. Contoh tes "tes dulu":

```python
def test_awareness_campaign_is_never_flagged():
    c = Campaign("A", "Test", 100.0, 1000, 50, 0, 0.0, goal="awareness")
    assert not needs_review(c)
```

Rencana yang lengkap biasanya berisi: (1) tes untuk awareness & goal tidak dikenal; (2) field `goal` di `Campaign`; (3) pembacaan + validasi di `load_campaigns`; (4) aturan di `needs_review`; (5) kolom baru di `campaigns.csv`; (6) perbarui `test_sample_data`; (7) perbarui README modul 04; (8) catat bahwa materi `training/` mengutip output ini.

**Latihan 4.1:** yang kurang:
- Tidak ada **tes** (tes dulu: parkir 60.000 → `PARTIAL` 50.000; parkir 50.000 → penuh).
- Tidak menyebut **docstring** di atas file yang memuat daftar aturan.
- "Tidak ada error" bukan verifikasi; perlu `pytest` dan cek angka.
- Tidak menyebut apa yang **tidak** berubah (hasil 8 klaim contoh tetap sama).
- Tidak ada langkah commit.

**Latihan 4.2 (contoh)**
```
Di @modules/03-hr/leave_tracker.py, setelah tabel utama, tambahkan bagian
"Low balance (<= 2 days)" yang mendaftar karyawan dengan sisa cuti <= 2 hari,
termasuk yang minus. Batas 2 hari harus bisa diubah dengan argumen --low-balance.
Jangan ubah tabel utama, aturan hari kerja, atau test_sample_data.
Buat rencana: fungsi baru apa (sebaiknya fungsi murni), tes apa (termasuk tepat 2 hari
dan sisa minus), dan bagian README mana yang perlu diperbarui. Jangan ubah apa pun dulu.
```
Dengan data contoh, bagian itu akan berisi E002 (sisa 2, tepat di batas) dan E004 (sisa −1).

**Latihan 4.3:** (1) tidak bisa membatalkan satu perubahan tanpa ikut membatalkan yang lain; (2) sulit ditinjau dan sulit dicari kapan/mengapa suatu baris berubah (pesan `update` tidak menjelaskan apa pun). Bonus: dua file yang tidak berhubungan mungkin ikut ter-commit tanpa sengaja, termasuk file rahasia.

**Latihan 4.4:** risiko khusus repositori ini:
- Modul memakai **hanya library standar Python**. Membaca Excel butuh library tambahan (misalnya `openpyxl`) yang harus dipasang dan dicatat versinya.
- `.gitignore` **memblokir** `*.xlsx` dan `*.xls` agar data asli tidak ikut ter-commit. Data contoh Excel tidak akan masuk Git. Ini disengaja.
- Alternatif yang lebih sederhana: tetap CSV, dan pengguna menyimpan Excel sebagai CSV (*Save As → CSV UTF-8*). Rencana yang baik menawarkan pilihan ini.

**Kuis**
1. Tidak mengubah file dan tidak menjalankan perintah yang mengubah apa pun; ia hanya membaca dan merencanakan.
2. `Shift+Tab` berulang kali sampai muncul tanda *plan mode*.
3. `test_<nama>.py` (karena `test_sample_data`), `README.md` modul, dan materi `training/` yang mengutip output.
4. Anda bisa kembali tepat ke langkah terakhir yang benar, tanpa kehilangan pekerjaan yang sudah benar.

</details>

---

← [Modul 3](modul-03-debugging.md) | **Berikutnya: [Modul 5: Linter & Formatter →](modul-05-linter-formatter.md)**
