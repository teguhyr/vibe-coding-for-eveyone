# Modul 6: Database & SQL dengan SQLite

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 6](../02-menengah.md#langkah-6-database--sql-dengan-sqlite) |
| **Sesi** | Sesi 3 |
| **Durasi** | 85 menit |
| **Prasyarat** | Modul 1 |
| **File latihan** | [`latihan/data/klaim_reimburse.csv`](latihan/data/klaim_reimburse.csv), [`modules/01-operations/data/inventory.csv`](../../modules/01-operations/data/inventory.csv) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan perbedaan CSV dan database, serta kapan memakai masing-masing.
2. Membuat tabel dengan *primary key* dan aturan kolom (`NOT NULL`, `CHECK`).
3. Menulis query `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `COUNT`/`SUM`, dan `JOIN`.
4. Memasukkan data dengan **parameter `?`** dan menjelaskan bahaya *SQL injection*.
5. Menghindari 3 jebakan: lupa `commit()`, pembagian bilangan bulat, dan meng-commit file `.db`.

---

## 📖 Materi

### A. CSV vs database

| | CSV | Database (SQLite) |
|---|---|---|
| Analogi | Satu lembar Excel | Lemari arsip berisi banyak map yang saling terhubung |
| Aturan isi | Tidak ada; kolom bisa diisi apa saja | Bisa dipaksa: wajib diisi, harus angka positif, tidak boleh dobel |
| Menghubungkan data | VLOOKUP manual | `JOIN` |
| Cocok untuk | Bertukar data, data kecil | Data yang terus bertambah, dipakai beberapa program, perlu dicari cepat |

**SQLite** adalah database dalam **satu file**, sudah termasuk di Python (`import sqlite3`), tanpa instalasi atau server.

### B. Tabel, kolom, dan aturan

```sql
CREATE TABLE claims (
    claim_id   TEXT PRIMARY KEY,
    department TEXT NOT NULL,
    amount     INTEGER NOT NULL CHECK (amount > 0),
    receipt    TEXT NOT NULL CHECK (receipt IN ('yes', 'no'))
)
```

| Bagian | Arti |
|--------|------|
| `PRIMARY KEY` | Kunci unik setiap baris, seperti nomor klaim. Tidak boleh dobel |
| `TEXT`, `INTEGER`, `REAL` | Teks, bilangan bulat, bilangan desimal |
| `NOT NULL` | Wajib diisi |
| `CHECK (...)` | Aturan isi. Database **menolak** baris yang melanggarnya |

> 💡 Tanggal di SQLite disimpan sebagai teks `YYYY-MM-DD`. Format ini bisa diurutkan dan dihitung dengan fungsi `julianday()`.

### C. Kosakata SQL

| SQL | Arti | Mirip di Excel |
|-----|------|----------------|
| `SELECT kolom` | Ambil kolom tertentu | Memilih kolom |
| `FROM tabel` | Dari tabel mana | Memilih sheet |
| `WHERE kondisi` | Saring baris | Filter |
| `ORDER BY kolom` / `DESC` | Urutkan naik / turun | Sort |
| `GROUP BY kolom` | Kelompokkan | Pivot table |
| `COUNT(*)`, `SUM(kolom)` | Hitung baris, jumlahkan | `COUNTIF`, `SUMIF` |
| `AS nama` | Beri nama kolom hasil | Judul kolom |
| `JOIN ... ON ...` | Gabungkan dua tabel dengan kolom yang sama | `VLOOKUP` / `XLOOKUP` |

Urutan penulisannya selalu: `SELECT → FROM → JOIN → WHERE → GROUP BY → ORDER BY`.

### D. Parameter `?` dan SQL injection

❌ **Berbahaya:** menggabungkan input ke teks SQL.

```python
dept = input("Departemen: ")
conn.execute(f"SELECT * FROM claims WHERE department = '{dept}'")
```

Jika seseorang mengetik `x' OR '1'='1`, query berubah menjadi `... WHERE department = 'x' OR '1'='1'`: **semua** baris terambil. Dengan input yang lebih jahat, data bisa dihapus. Ini disebut *SQL injection*, salah satu celah keamanan paling sering di dunia (dibahas lebih dalam di Level 3).

✅ **Aman:** pakai parameter `?`. Database memperlakukan input sebagai **data**, bukan perintah.

```python
conn.execute("SELECT claim_id FROM claims WHERE department = ?", (dept,))
```

> ⚠️ Perhatikan koma di `(dept,)`. Tanpa koma, Python tidak menganggapnya sebagai *tuple* dan query gagal.

### E. Tiga jebakan

1. **Lupa `conn.commit()`**: perubahan (`INSERT`, `UPDATE`, `DELETE`) tidak benar-benar tersimpan ke file.
2. **Pembagian bilangan bulat**: di SQLite, `7 / 2` menghasilkan `3`, bukan `3.5`. Jika kedua kolom `INTEGER`, kalikan salah satunya dengan `1.0` atau pakai kolom `REAL`.
3. **Meng-commit file `.db`**: file database bisa berisi data asli dan ukurannya terus bertambah. Repositori ini memblokir `*.db` di `.gitignore`. Untuk latihan, Anda juga bisa memakai `sqlite3.connect(":memory:")`: database sementara di memori, hilang saat program selesai.

### F. Uang di database

Seperti di Python (`Decimal`), hindari menyimpan uang sebagai `REAL` jika butuh hasil persis. Rupiah tanpa sen bisa disimpan sebagai `INTEGER`. Untuk mata uang dengan sen, simpan dalam **satuan sen** (`15000.00` → `1500000`), lalu bagi 100 saat ditampilkan.

---

## 🛠️ Praktik Terpandu

**1. Inventaris ke SQLite.** Simpan kode berikut sebagai `latihan_sqlite.py` di folder utama repositori:

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

```bash
python latihan_sqlite.py
```

```
('SKU-006', 'Pallet Wrap', 3, 16.0)
('SKU-004', 'Cardboard Box M', 55, 68.0)
('SKU-002', 'Printer Toner', 8, 15.5)
```

Hasilnya sama dengan modul 01 (Level 1), tetapi kali ini dihitung oleh database.

**2. Baca query-nya bersama.**

| Baris | Arti |
|-------|------|
| `SELECT sku, name, on_hand, ... AS reorder_point` | Ambil 3 kolom + 1 kolom hitungan bernama `reorder_point` |
| `FROM inventory` | Dari tabel `inventory` |
| `WHERE on_hand <= ...` | Hanya barang yang stoknya sudah di/di bawah titik pesan ulang |
| `ORDER BY on_hand / avg_daily_usage` | Urutkan dari yang paling cepat habis (sisa hari terkecil) |

**3. Pastikan file `.db` tidak ikut Git.**

```bash
git status
```

`inventory.db` **tidak** muncul, karena diblokir `.gitignore`. Anda boleh menghapus `latihan_sqlite.py` dan `inventory.db` setelah selesai.

**4. Minta Claude menulis query, lalu periksa sendiri.**

```
Di @latihan_sqlite.py, tambahkan query yang menampilkan barang dengan sisa hari < 5
(on_hand / avg_daily_usage), dibulatkan 1 desimal, diurutkan dari yang paling kecil.
Jelaskan query-nya baris per baris.
```

Bandingkan hasilnya dengan kunci Latihan 6.1.

---

## 🏋️ Latihan

### ⭐ Latihan 6.1: Sisa hari < 5

Tulis (atau minta Claude menulis) query untuk barang dengan sisa hari **kurang dari 5**. Hasil apa yang Anda harapkan berdasarkan tabel Level 1? Periksa apakah cocok.

### ⭐⭐ Latihan 6.2: Klaim reimburse ke SQLite

Buat program yang memuat [`latihan/data/klaim_reimburse.csv`](latihan/data/klaim_reimburse.csv) ke tabel `claims` (pakai `PRIMARY KEY`, `NOT NULL`, dan `CHECK`). Tulis query `GROUP BY` untuk **jumlah klaim dan total nilai yang diajukan per departemen**, urut dari total terbesar.

### ⭐⭐ Latihan 6.3: Query dengan parameter

Di program yang sama, tulis:
1. Query klaim **tanpa bukti** dengan nilai **≥ batas tertentu**, dengan batas dimasukkan lewat parameter `?` (pakai 100.000).
2. Query klaim yang diajukan **lebih dari 30 hari** setelah tanggal biaya (petunjuk: `julianday()`).

Bandingkan hasilnya dengan output `expense_claims.py` di Modul 1.

### ⭐⭐⭐ Latihan 6.4: JOIN dan GROUP BY antar-modul

1. Muat `modules/03-hr/data/employees.csv` dan `leave_requests.csv` sebagai dua tabel. Tulis query `JOIN` yang menampilkan nama karyawan, jumlah pengajuan cuti, dan jumlah yang **approved**.
2. Muat `modules/02-finance/data/budget_vs_actual.csv` dan hitung **total realisasi per departemen** dengan `GROUP BY`. Simpan uang dalam satuan sen.

---

## 📝 Kuis

1. Apa fungsi `PRIMARY KEY`?
2. Mengapa `f"... WHERE department = '{dept}'"` berbahaya? Tulis versi yang aman.
3. Anda menjalankan `INSERT`, lalu program selesai, tetapi datanya tidak ada di file database. Apa yang terlupa?
4. Apa hasil `SELECT 7 / 2` di SQLite? Bagaimana agar hasilnya `3.5`?
5. Apa padanan `GROUP BY` di Excel?

---

## 📌 Ringkasan

- Database = lemari arsip dengan **aturan isi** (`PRIMARY KEY`, `NOT NULL`, `CHECK`).
- SQL: `SELECT → FROM → JOIN → WHERE → GROUP BY → ORDER BY`.
- **Selalu** pakai parameter `?` untuk nilai dari luar. Jangan pernah menggabungkan input ke teks SQL.
- Ingat `commit()`, waspadai pembagian bilangan bulat, dan jangan commit file `.db`.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 6.1**

```sql
SELECT sku, name, ROUND(on_hand / avg_daily_usage, 1) AS days_left
FROM inventory
WHERE on_hand / avg_daily_usage < 5
ORDER BY days_left
```

```
('SKU-006', 'Pallet Wrap', 1.5)
('SKU-004', 'Cardboard Box M', 4.6)
```

Cocok dengan kolom *Days left* di Level 1 (1.5 dan 4.6). `SKU-002` (5.3) tidak masuk karena tidak kurang dari 5. Pembagian di sini aman karena `avg_daily_usage` bertipe `REAL`.

**Latihan 6.2 & 6.3:** lihat [`latihan/kunci/claims_sqlite.py`](latihan/kunci/claims_sqlite.py).

```bash
python training/menengah/latihan/kunci/claims_sqlite.py
```

```
Total klaim per departemen (sebelum aturan):
('Operations', 2, 1800000)
('Finance', 2, 1290000)
('Sales', 2, 770000)
('IT', 2, 185000)

Klaim tanpa bukti dengan nilai minimal Rp100.000:
('C-05', 100000)

Klaim yang diajukan lebih dari 30 hari setelah tanggal biaya:
('C-03', 39)
```

Cek manual Operations: 300.000 + 1.500.000 = **1.800.000**. ✔ Perhatikan: ini total yang **diajukan**. Total yang **dibayar** (1.500.000 untuk Operations di Modul 1) berbeda karena aturan potongan dan penolakan. C-05 dan C-03 cocok dengan status `REJECTED` di output `expense_claims.py`. ✔

**Latihan 6.4:** lihat [`latihan/kunci/sqlite_lanjutan.py`](latihan/kunci/sqlite_lanjutan.py).

```bash
python training/menengah/latihan/kunci/sqlite_lanjutan.py
```

```
Jumlah pengajuan cuti per karyawan (JOIN):
('Budi Santoso', 2, 2)
('Siti Aminah', 2, 1)
('Alex Tan', 2, 1)
('Dewi Lestari', 2, 2)

Total realisasi anggaran per departemen (GROUP BY):
HR              18,000.00
IT              23,500.00
Marketing       57,000.00
Operations      86,500.00
```

Angka realisasi cocok dengan bagian *Totals by department* di output modul 02. ✔ Kunci memakai `LEFT JOIN` agar karyawan yang **belum pernah** mengajukan cuti tetap muncul (dengan 0). Dengan `JOIN` biasa, karyawan seperti itu hilang dari laporan, dan ini kesalahan yang sering terjadi.

**Kuis**
1. Menjadi kunci unik setiap baris; database menolak baris dengan kunci yang sama.
2. Input pengguna bisa mengubah arti query (SQL injection). Versi aman: `conn.execute("SELECT claim_id FROM claims WHERE department = ?", (dept,))`.
3. `conn.commit()`.
4. `3` (pembagian bilangan bulat). Pakai `7 / 2.0` atau `7 * 1.0 / 2`.
5. *Pivot table* (atau `SUMIF`/`COUNTIF` per kelompok).

</details>

---

← [Modul 5](modul-05-linter-formatter.md) | **Berikutnya: [Modul 7: CLAUDE.md →](modul-07-claude-md.md)**
