# 🟡 Level 2: Menengah — "Membuat Alat yang Benar, Teruji, dan Rapi"

| | |
|---|---|
| **Untuk siapa** | Lulusan Level 1: sudah bisa menjalankan dan memodifikasi skrip dengan prompt |
| **Durasi** | ± 25 jam (4 minggu) |
| **Prasyarat** | Semua item [Checklist Level 1](01-dasar.md#-checklist-kelulusan-level-1) tercentang |
| **Hasil akhir** | Anda bisa membaca kode buatan AI, membuktikan kebenarannya dengan tes, memperbaiki error, memakai database SQL, dan membangun alat otomatisasi dari pekerjaan Anda sendiri |
| **Materi modul** | [Paket Materi Level 2](menengah/README.md): 10 modul, file latihan, proyek akhir, evaluasi, dan panduan fasilitator |

### Daftar Langkah

1. [Membaca anatomi program buatan AI](#langkah-1-membaca-anatomi-program-buatan-ai)
2. [Tes otomatis dengan pytest](#langkah-2-tes-otomatis-dengan-pytest)
3. [Debugging bersama AI](#langkah-3-debugging-bersama-ai)
4. [Merencanakan perubahan besar (Plan Mode)](#langkah-4-merencanakan-perubahan-besar-plan-mode)
5. [Kode yang rapi: linter & formatter](#langkah-5-kode-yang-rapi-linter--formatter)
6. [Database & SQL dengan SQLite](#langkah-6-database--sql-dengan-sqlite)
7. [CLAUDE.md: "SOP" untuk asisten AI Anda](#langkah-7-claudemd-sop-untuk-asisten-ai-anda)
8. [Branch, review, dan kolaborasi](#langkah-8-branch-review-dan-kolaborasi)
9. [Data asli dengan aman](#langkah-9-data-asli-dengan-aman)
10. [Latihan studi kasus lintas fungsi](#langkah-10-latihan-studi-kasus-lintas-fungsi)
- [Proyek Akhir Level 2](#-proyek-akhir-level-2)
- [Checklist Kelulusan](#-checklist-kelulusan-level-2)

---

## Langkah 1: Membaca Anatomi Program Buatan AI

> 📘 **Materi lengkap:** [Modul 1: Membaca Anatomi Program Buatan AI](menengah/modul-01-anatomi-program.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Memahami *struktur* program, bukan setiap baris, agar Anda tahu bagian mana yang harus diperiksa.

📖 **Konsep:** Hampir semua alat bisnis kecil punya 4 bagian, seperti alur kerja di kantor:

```
┌─────────────┐    ┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
│ 1. MODEL    │    │ 2. MEMBACA   │    │ 3. ATURAN BISNIS │    │ 4. TAMPILAN  │
│ DATA        │ →  │ DATA         │ →  │ (logika)         │ →  │ HASIL        │
│ "formulir"  │    │ "input"      │    │ "SOP"            │    │ "laporan"    │
│ @dataclass  │    │ load_*()     │    │ fungsi murni     │    │ main()       │
└─────────────┘    └──────────────┘    └──────────────────┘    └──────────────┘
```

**Bagian 3 (aturan bisnis) adalah yang paling penting diperiksa.** Di sanalah keputusan bisnis diterjemahkan menjadi kode.

🛠️ **Praktik:** Buka [`modules/03-hr/leave_tracker.py`](../modules/03-hr/leave_tracker.py), lalu temukan keempat bagian tersebut:

| Bagian | Di file ini |
|--------|-------------|
| 1. Model data | `class Employee`, `class LeaveRequest`, `class Balance` |
| 2. Membaca data | `load_employees`, `load_requests`, `load_holidays` |
| 3. Aturan bisnis | `working_days`, `calculate_balances` |
| 4. Tampilan | `main` |

Minta Claude:

```
Jelaskan fungsi working_days di @modules/03-hr/leave_tracker.py baris per baris.
Lalu beri 3 contoh tanggal yang hasilnya mungkin mengejutkan orang HR.
```

✅ **Cek pemahaman:** Tanpa menjalankan program, berapa hari kerja dari Jumat 30 Oktober 2026 sampai Selasa 3 November 2026? Periksa jawaban Anda di `test_leave_tracker.py`.

---

## Langkah 2: Tes Otomatis dengan pytest

> 📘 **Materi lengkap:** [Modul 2: Tes Otomatis dengan pytest](menengah/modul-02-pytest.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Membuktikan program benar secara otomatis, bukan hanya "kelihatannya benar".

📖 **Konsep:** Tes adalah **daftar periksa (checklist) yang dijalankan komputer**. Anda menulis "jika input X, hasilnya harus Y", lalu komputer memeriksanya dalam hitungan detik, setiap kali kode berubah.

Analogi: auditor yang memeriksa ulang **seluruh** laporan setiap kali satu angka diubah, tanpa lelah.

🛠️ **Praktik**

**A. Jalankan tes**

```bash
pytest
```

Semua modul diuji. Titik (`.`) berarti lulus, `F` berarti gagal.

```bash
pytest modules/03-hr -v
```

`-v` menampilkan nama setiap tes. Baca namanya; nama tes yang baik terbaca seperti aturan bisnis.

**B. Lihat tes gagal (dengan sengaja)**

1. Di `modules/01-operations/data/inventory.csv`, ubah stok `SKU-001` dari `120` menjadi `90`.
2. Jalankan `pytest modules/01-operations`. Hasilnya:

   ```
   >       assert [i.sku for i in due] == ["SKU-006", "SKU-004", "SKU-002"]
   E       AssertionError: assert ['SKU-006', '...2', 'SKU-001'] == ['SKU-006', '...4', 'SKU-002']
   E         Left contains one more item: 'SKU-001'
   ```

   Artinya: tes mengharapkan 3 barang, tetapi sekarang ada 4 (SKU-001 ikut masuk). **Tes menangkap perubahan.**
3. Kembalikan file seperti semula:

   ```bash
   git checkout modules/01-operations/data/inventory.csv
   ```

**C. Minta AI menulis tes untuk kasus tepi**

```
Lihat @modules/02-finance/budget_variance.py dan tesnya.
Kasus tepi apa yang belum diuji? Tambahkan tesnya (misalnya angka negatif,
anggaran sangat besar, threshold 0). Jalankan pytest dan pastikan semua lulus.
```

**D. Teknik "tes dulu" (test-first)**

Tulis aturan bisnis sebagai tes **sebelum** kodenya ada. Ini cara paling ampuh agar AI tidak salah paham:

```
Saya ingin menambah aturan: cuti setengah hari dihitung 0,5.
JANGAN ubah kode dulu. Tulis dulu tes pytest yang menggambarkan aturan ini,
tunjukkan ke saya, lalu setelah saya setujui, baru ubah kodenya sampai tes lulus.
```

⚠️ **Kesalahan umum**
- **Membiarkan AI mengubah tes agar lulus.** Jika tes gagal, tanyakan dulu: kodenya yang salah, atau tesnya? Tes yang ditulis dari aturan bisnis yang benar **tidak boleh** diubah demi lulus.
- **Hanya menguji kasus normal.** Bug bersembunyi di batas: nilai 0, tanggal yang sama, data kosong, persis di ambang batas.

✅ **Cek pemahaman:** Tambahkan satu tes baru ke modul mana pun (dengan bantuan Claude) dan pastikan `pytest` lulus.

---

## Langkah 3: Debugging Bersama AI

> 📘 **Materi lengkap:** [Modul 3: Debugging Bersama AI](menengah/modul-03-debugging.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Membaca pesan error dan memperbaikinya secara sistematis.

📖 **Konsep:** Pesan error (*traceback*) adalah **petunjuk, bukan hukuman**. Bacalah **dari bawah ke atas**: baris terakhir menyebutkan *apa* masalahnya, baris-baris di atasnya menunjukkan *di mana*.

🛠️ **Praktik**

Misalkan di file cuti ada salah ketik `aproved` (seharusnya `approved`). Program akan berhenti dengan:

```
  File ".../modules/03-hr/leave_tracker.py", line 94, in load_requests
    raise ValueError(f"Unknown leave status {r['status']!r} for {r['employee_id']}")
ValueError: Unknown leave status 'aproved' for E002
```

Cara membacanya:
1. **Baris terakhir:** `ValueError: Unknown leave status 'aproved' for E002` berarti ada status tidak dikenal untuk karyawan E002.
2. **Baris di atasnya:** errornya terjadi di fungsi `load_requests`, baris 94.
3. **Kesimpulan:** masalahnya ada di **data**, bukan di kode. Perbaiki CSV-nya.

> 💡 Ini contoh program yang baik: data yang salah **dihentikan dengan pesan jelas**, bukan diam-diam dihitung salah.

**Template prompt debugging (4 bagian):**

```
1. YANG SAYA LAKUKAN: Saya menjalankan python modules/03-hr/leave_tracker.py
2. YANG SAYA HARAPKAN: Tabel sisa cuti
3. YANG TERJADI: Error berikut:
   <tempel pesan error lengkap>
4. PERMINTAAN: Jelaskan penyebabnya dengan sederhana. Jangan langsung ubah kode;
   beri tahu dulu apakah masalahnya di data atau di kode.
```

**Jika Claude salah arah:**
- Tekan `Esc` untuk menghentikannya.
- Tekan `Esc` dua kali untuk **kembali ke titik sebelumnya** (*rewind*) dan mencoba instruksi yang lebih jelas.

⚠️ **Kesalahan umum**
- **Hanya menempel sebagian error.** Tempel **seluruh** traceback.
- **"Perbaiki saja"** tanpa memahami penyebab. Minta penjelasan dulu, agar Anda belajar dan bisa menilai perbaikannya.

✅ **Cek pemahaman:** Buat error dengan sengaja (misalnya hapus satu kolom di CSV salinan), jalankan program, lalu jelaskan error tersebut **sebelum** bertanya ke Claude.

---

## Langkah 4: Merencanakan Perubahan Besar (Plan Mode)

> 📘 **Materi lengkap:** [Modul 4: Merencanakan Perubahan Besar (Plan Mode)](menengah/modul-04-plan-mode.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Memecah tugas besar menjadi langkah kecil yang bisa diperiksa.

📖 **Konsep:** Untuk perubahan yang menyentuh banyak bagian, minta **rencana dulu, kode belakangan**. Seperti membangun rumah: gambar arsitek disetujui dulu sebelum mulai mengecor.

Claude Code punya **Plan Mode**: Claude hanya membaca dan menyusun rencana, tanpa mengubah file. Tekan `Shift+Tab` untuk berpindah mode sampai muncul tanda *plan mode*.

🛠️ **Praktik** dengan modul Marketing ([`modules/04-marketing`](../modules/04-marketing/)):

1. Aktifkan Plan Mode, lalu ketik:

   ```
   Saya ingin menambah kolom "goal" (awareness atau sales) di campaigns.csv.
   Kampanye awareness tidak boleh ditandai "below target ROAS".
   Buat rencana langkah demi langkah: file apa yang diubah, tes apa yang ditambah,
   dan apa risikonya. Jangan ubah apa pun dulu.
   ```

2. **Tinjau rencananya.** Apakah ada yang terlewat? Misalnya: README juga perlu diperbarui, dan tes `test_sample_data` akan berubah.
3. Setujui rencana, keluar dari Plan Mode, dan biarkan Claude mengerjakannya **satu langkah per satu waktu**.
4. Setelah setiap langkah: jalankan `pytest`, lalu commit.

📖 **Aturan "Satu Langkah, Satu Commit":** setiap langkah kecil yang lulus tes langsung di-commit. Jika langkah berikutnya merusak sesuatu, Anda tinggal kembali satu langkah.

✅ **Cek pemahaman:** Fitur "goal" selesai, semua tes lulus, dan riwayat Git berisi beberapa commit kecil, bukan satu commit raksasa.

---

## Langkah 5: Kode yang Rapi: Linter & Formatter

> 📘 **Materi lengkap:** [Modul 5: Kode yang Rapi: Linter & Formatter](menengah/modul-05-linter-formatter.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Menjaga kode tetap konsisten dan mudah dibaca, oleh Anda, rekan kerja, dan AI.

📖 **Konsep**
- **Formatter** (`ruff format`) seperti fitur *auto-format* di Word: merapikan spasi dan baris secara otomatis.
- **Linter** (`ruff check`) seperti *spell-checker* untuk kode: menemukan potensi kesalahan, misalnya variabel yang tidak dipakai atau import yang hilang.

🛠️ **Praktik**

```bash
ruff check .
```

```bash
ruff format --check .
```

Jika ada yang perlu dirapikan:

```bash
ruff format .
```

```bash
ruff check --fix .
```

Biasakan prompt penutup ini setiap selesai mengubah kode:

```
Jalankan pytest, ruff check, dan ruff format --check. Perbaiki semua masalah yang muncul.
```

⚠️ **Kesalahan umum:** Mengabaikan peringatan linter. Banyak bug nyata, seperti variabel salah ketik, tertangkap di sini.

✅ **Cek pemahaman:** Ketiga perintah (pytest, ruff check, ruff format --check) lulus tanpa error.

---

## Langkah 6: Database & SQL dengan SQLite

> 📘 **Materi lengkap:** [Modul 6: Database & SQL dengan SQLite](menengah/modul-06-sqlite.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Memindahkan data dari CSV ke database, dan mengambil data dengan SQL.

📖 **Konsep:** Jika CSV adalah **satu lembar Excel**, database adalah **lemari arsip** berisi banyak tabel yang saling terhubung, dengan aturan yang menjaga data tetap rapi. **SQL** adalah bahasa untuk "meminta" data dari lemari itu.

**SQLite** adalah database dalam satu file, sudah termasuk di Python, dan tidak perlu instalasi.

| SQL | Arti | Mirip di Excel |
|-----|------|----------------|
| `SELECT kolom` | Ambil kolom tertentu | Memilih kolom |
| `FROM tabel` | Dari tabel mana | Memilih sheet |
| `WHERE kondisi` | Saring baris | Filter |
| `ORDER BY kolom` | Urutkan | Sort |
| `GROUP BY kolom` | Kelompokkan | Pivot table |

🛠️ **Praktik:** Simpan kode berikut sebagai `latihan_sqlite.py` di folder utama, lalu jalankan dengan `python latihan_sqlite.py`.

```python
import csv
import sqlite3
from pathlib import Path

CSV_FILE = Path("modules/01-operations/data/inventory.csv")

conn = sqlite3.connect("inventory.db")
conn.execute("DROP TABLE IF EXISTS inventory")
conn.execute("""
    CREATE TABLE inventory (
        sku             TEXT PRIMARY KEY,
        name            TEXT NOT NULL,
        on_hand         INTEGER NOT NULL,
        avg_daily_usage REAL NOT NULL,
        lead_time_days  INTEGER NOT NULL,
        safety_stock    INTEGER NOT NULL
    )
""")
with CSV_FILE.open(newline="", encoding="utf-8") as f:
    rows = [
        (
            r["sku"],
            r["name"],
            int(r["on_hand"]),
            float(r["avg_daily_usage"]),
            int(r["lead_time_days"]),
            int(r["safety_stock"]),
        )
        for r in csv.DictReader(f)
    ]
# Tanda ? adalah "parameter": data dimasukkan dengan aman, tidak digabung ke teks SQL.
conn.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?, ?, ?)", rows)
conn.commit()

query = """
    SELECT sku, name, on_hand,
           avg_daily_usage * lead_time_days + safety_stock AS reorder_point
    FROM inventory
    WHERE on_hand <= avg_daily_usage * lead_time_days + safety_stock
    ORDER BY on_hand / avg_daily_usage
"""
for row in conn.execute(query):
    print(row)
conn.close()
```

Hasilnya sama dengan modul 01, tetapi kali ini dihitung oleh database:

```
('SKU-006', 'Pallet Wrap', 3, 16.0)
('SKU-004', 'Cardboard Box M', 55, 68.0)
('SKU-002', 'Printer Toner', 8, 15.5)
```

**Latihan lanjutan (minta Claude membantu):**
1. *"Muat `modules/03-hr/data/employees.csv` dan `leave_requests.csv` ke SQLite sebagai dua tabel. Tulis query dengan JOIN untuk menampilkan nama karyawan beserta jumlah pengajuan cutinya."*
2. *"Tulis query GROUP BY untuk menghitung total realisasi anggaran per departemen dari modul 02."*

⚠️ **Kesalahan umum**
- **Menggabungkan input ke teks SQL**, misalnya `f"SELECT ... WHERE sku = '{input_user}'"`. Ini membuka celah **SQL injection** (dibahas di Level 3). Selalu gunakan parameter `?`.
- **Lupa `conn.commit()`.** Tanpanya, data tidak benar-benar tersimpan.
- **Meng-commit file database.** File `.db` sebaiknya tidak masuk Git. Repositori ini sudah memblokir `*.db` lewat `.gitignore`; lakukan hal yang sama di proyek Anda.

✅ **Cek pemahaman:** Jelaskan arti setiap baris dari query di atas dengan kata-kata Anda sendiri.

---

## Langkah 7: CLAUDE.md: "SOP" untuk Asisten AI Anda

> 📘 **Materi lengkap:** [Modul 7: CLAUDE.md: "SOP" untuk Asisten AI Anda](menengah/modul-07-claude-md.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Membuat Claude memahami proyek Anda tanpa harus dijelaskan ulang setiap kali.

📖 **Konsep:** `CLAUDE.md` adalah file yang **otomatis dibaca Claude** setiap kali bekerja di proyek Anda. Anggap saja **SOP + buku panduan untuk karyawan baru**: perintah apa yang dipakai, aturan apa yang wajib, dan jebakan apa yang harus dihindari.

🛠️ **Praktik**

1. Baca [`CLAUDE.md`](../CLAUDE.md) di repositori ini sebagai contoh.
2. Di proyek Anda sendiri, jalankan `claude`, lalu ketik:

   ```
   /init
   ```

   Claude akan menganalisis proyek dan membuat draf `CLAUDE.md`.
3. **Edit drafnya.** Tambahkan hal yang **hanya Anda yang tahu**, misalnya:

   ```markdown
   ## Aturan bisnis
   - Tahun fiskal perusahaan dimulai 1 April, bukan 1 Januari.
   - Semua nilai uang dalam Rupiah, tanpa desimal.
   - Kode departemen: OPS, FIN, HRD, MKT, ITS.

   ## Perintah
   - Jalankan tes: pytest
   - Laporan bulanan: python laporan.py --bulan 2026-10

   ## Larangan
   - Jangan pernah membaca folder data_asli/ (berisi data pribadi karyawan).
   ```

⚠️ **Kesalahan umum**
- **Terlalu panjang dan umum** ("tulis kode yang bagus"). Isi dengan hal **spesifik** proyek Anda.
- **Tidak diperbarui.** Saat aturan berubah, perbarui `CLAUDE.md` juga.

✅ **Cek pemahaman:** Mulai percakapan baru (`/clear`), lalu tanya *"Kapan tahun fiskal kita dimulai?"*. Claude seharusnya menjawab dari `CLAUDE.md`.

---

## Langkah 8: Branch, Review, dan Kolaborasi

> 📘 **Materi lengkap:** [Modul 8: Branch, Review, dan Kolaborasi](menengah/modul-08-branch-review.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Bekerja dengan aman di tim: eksperimen tidak merusak versi utama, dan setiap perubahan ditinjau.

📖 **Konsep:** **Branch** adalah salinan kerja terpisah, seperti "Save As" ke file draf sebelum mengedit dokumen penting. Setelah draf diperiksa dan disetujui, perubahannya digabung (*merge*) ke versi utama.

```
main     ●────────●────────────────●  (versi resmi)
          \                       /
fitur-x    ●────●────●───────────    (eksperimen → review → merge)
```

🛠️ **Praktik**

```bash
git switch -c fitur-export-excel
```
Membuat branch baru dan pindah ke sana.

```bash
git branch
```
Melihat semua branch (tanda `*` = branch aktif).

Setelah selesai dan commit, minta Claude meninjau pekerjaan Anda **sebagai reviewer**:

```
Tinjau semua perubahan di branch ini dibandingkan main (git diff main).
Cari bug, kasus tepi yang terlewat, dan masalah keamanan data.
Urutkan dari yang paling serius.
```

Jika repositori ada di GitHub, langkah berikutnya adalah membuat **Pull Request (PR)**: permintaan agar rekan meninjau sebelum perubahan digabung.

```bash
git switch main
```

```bash
git merge fitur-export-excel
```

⚠️ **Kesalahan umum:** Bekerja langsung di `main`. Biasakan: **satu fitur = satu branch**.

✅ **Cek pemahaman:** Buat branch, lakukan satu perubahan kecil, minta Claude meninjaunya, lalu merge ke `main`.

---

## Langkah 9: Data Asli dengan Aman

> 📘 **Materi lengkap:** [Modul 9: Data Asli dengan Aman](menengah/modul-09-data-aman.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Memakai alat buatan Anda pada data asli **tanpa** membocorkan data pribadi atau rahasia.

📖 **Konsep: Pola "Bangun dengan Data Palsu, Jalankan dengan Data Asli"**

```
   ┌──────────────────────────────┐           ┌──────────────────────────────┐
   │  TAHAP BANGUN (bersama AI)   │           │  TAHAP PAKAI (tanpa AI)      │
   │  • Data sintetis/contoh      │  ──────▶  │  • Data asli                 │
   │  • Prompt, kode, tes         │           │  • Di komputer Anda sendiri  │
   │  • Boleh dibagikan           │           │  • Hasil tidak dikirim ke AI │
   └──────────────────────────────┘           └──────────────────────────────┘
```

🛠️ **Praktik**

1. **Buat data sintetis dengan AI.** Berikan **struktur** (nama kolom), bukan isinya:

   ```
   Buat file CSV berisi 30 baris data karyawan FIKTIF dengan kolom:
   id_karyawan, nama, departemen, tanggal_masuk, jatah_cuti.
   Pakai nama Indonesia yang umum dan jelas fiktif. Jangan pakai data orang nyata.
   ```

2. **Anonimkan jika perlu contoh nyata.** Ganti nama dengan kode (`Karyawan-001`), hapus kolom NIK, NPWP, rekening, dan gaji, lalu acak angka sensitif.
3. **Simpan data asli di folder terpisah** yang diblokir Git (repositori ini sudah memblokir folder `private/` dan file Excel lewat `.gitignore`), dan tulis larangan di `CLAUDE.md` (lihat Langkah 7).
4. **Jalankan alat jadi di terminal biasa**, bukan lewat percakapan dengan AI:

   ```bash
   python modules/03-hr/leave_tracker.py --data-dir private/hr_oktober
   ```

⚠️ **Data yang WAJIB dilindungi (UU PDP No. 27/2022)**

| Kategori | Contoh |
|----------|--------|
| Data pribadi umum | Nama lengkap + kontak, alamat, tanggal lahir |
| Nomor identitas | KTP/NIK, NPWP, paspor, BPJS |
| Data keuangan | Gaji, rekening bank, nomor kartu |
| Data spesifik (sensitif) | Kesehatan, biometrik, catatan kejahatan, data anak |
| Rahasia perusahaan | Isi kontrak, harga negosiasi, strategi, kata sandi, API key |

✅ **Cek pemahaman:** Jelaskan ke rekan kerja, dalam 3 kalimat, cara memakai alat cuti untuk data karyawan asli tanpa melanggar UU PDP.

---

## Langkah 10: Latihan Studi Kasus Lintas Fungsi

> 📘 **Materi lengkap:** [Modul 10: Studi Kasus Lintas Fungsi](menengah/modul-10-studi-kasus-lintas-fungsi.md): materi mendalam, latihan bertingkat, kuis, dan kunci jawaban.

🎯 **Tujuan:** Melatih semua keterampilan Level 2 pada berbagai fungsi bisnis.

🛠️ **Praktik:** Kerjakan **minimal 3** dari latihan berikut. Untuk setiap latihan: buat branch, rencanakan (Plan Mode), tulis tes dulu, implementasi, jalankan pytest + ruff, minta review, lalu commit.

| Fungsi | Modul | Latihan | Keterampilan yang dilatih |
|--------|-------|---------|---------------------------|
| HR | [03-hr](../modules/03-hr/) | Dukung cuti setengah hari (kolom `half_day`) | Tes dulu, perubahan model data |
| Marketing | [04-marketing](../modules/04-marketing/) | Ringkasan per channel dari **total**, bukan rata-rata | Logika agregasi |
| IT | [05-it](../modules/05-it/) | Peringatan dini: tiket terbuka yang akan melanggar SLA dalam 2 jam | Aritmetika waktu, kasus tepi |
| Akuntansi | [06-accounting](../modules/06-accounting/) | Muat bank & ledger ke SQLite, lakukan pencocokan dengan JOIN | SQL |
| Legal | [07-legal](../modules/07-legal/) | Ekspor tenggat pemberitahuan ke file kalender `.ics` | Format file baru |

✅ **Cek pemahaman:** Untuk setiap latihan, Anda bisa menjelaskan **aturan bisnisnya**, **tes yang membuktikannya**, dan **satu kasus tepi** yang Anda temukan.

---

## 🏆 Proyek Akhir Level 2

**Tujuan:** Membangun alat otomatisasi **dari pekerjaan Anda sendiri**, dengan standar yang sama seperti modul di repositori ini.

**Tugas:**
1. Pilih satu dari 3 pekerjaan berulang yang Anda catat di Level 1.
2. Buat folder modul baru, misalnya `modules/11-<fungsi-anda>/`, dengan struktur:

   ```
   modules/11-<fungsi>/
   ├── README.md               # masalah, konsep, prompt, cara jalan, verifikasi, kesalahan umum, latihan
   ├── data/contoh.csv         # data SINTETIS saja
   ├── <nama_unik>.py          # program
   └── test_<nama_unik>.py     # tes, termasuk test_sample_data
   ```

   Nama file harus unik di seluruh repositori (lihat aturan di `CLAUDE.md`).
3. Mulai di Plan Mode, dan tulis tes **sebelum** kode.
4. Pastikan `pytest`, `ruff check .`, dan `ruff format --check .` lulus.
5. Minta Claude meninjau sebagai reviewer, perbaiki temuan penting, lalu commit.
6. **Presentasikan** (10 menit) ke rekan atau atasan: masalahnya, demo, cara verifikasi, dan berapa waktu yang dihemat per bulan.

📘 **Materi lengkap, kanvas masalah, rubrik, dan contoh referensi:** [Proyek Akhir Level 2](menengah/proyek-akhir.md)

**Kriteria lulus:**
- [ ] Menyelesaikan masalah nyata dari pekerjaan Anda
- [ ] Minimal 5 tes, termasuk kasus tepi dan `test_sample_data`
- [ ] Data input yang salah dihentikan dengan pesan error yang jelas
- [ ] README mengikuti struktur modul yang ada
- [ ] Tidak ada data pribadi atau rahasia asli di repositori
- [ ] Riwayat Git berisi beberapa commit kecil dengan pesan yang jelas

---

## ✅ Checklist Kelulusan Level 2

- [ ] Saya bisa mengenali 4 bagian program: model data, pembacaan data, aturan bisnis, tampilan
- [ ] Saya bisa menjalankan, membaca, dan menulis tes pytest, termasuk teknik "tes dulu"
- [ ] Saya tahu: tes yang gagal **tidak boleh** diubah hanya agar lulus
- [ ] Saya bisa membaca traceback dari bawah ke atas dan memakai template prompt debugging
- [ ] Saya memakai Plan Mode untuk perubahan besar dan commit per langkah kecil
- [ ] Saya menjalankan pytest + ruff sebelum menganggap pekerjaan selesai
- [ ] Saya bisa menulis query SQL dasar (SELECT, WHERE, ORDER BY, GROUP BY, JOIN) dengan parameter `?`
- [ ] Saya sudah membuat `CLAUDE.md` untuk proyek saya sendiri
- [ ] Saya bekerja di branch dan meminta review sebelum merge
- [ ] Saya menerapkan pola "bangun dengan data palsu, jalankan dengan data asli"

---

**Luar biasa! 🚀 Anda sudah menjadi praktisi vibe coding. Lanjut ke [Level 3: Mahir →](03-mahir.md)**
