# Modul 1: Membaca Anatomi Program Buatan AI

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 1](../02-menengah.md#langkah-1-membaca-anatomi-program-buatan-ai) |
| **Sesi** | Sesi 1 |
| **Durasi** | 35 menit |
| **Prasyarat** | Lulus Level 1 (terutama [Modul 6: Membaca Kode](../dasar/modul-06-membaca-kode.md)) |
| **File latihan** | [`latihan/expense_claims.py`](latihan/expense_claims.py), [`latihan/data/klaim_reimburse.csv`](latihan/data/klaim_reimburse.csv) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menemukan 4 bagian program bisnis: **model data, pembacaan data, aturan bisnis, tampilan**.
2. Menjelaskan arti `@dataclass(frozen=True)`, `@property`, dan "fungsi murni" dengan bahasa sehari-hari.
3. Menentukan bagian mana yang **paling perlu diperiksa** saat AI mengubah program.
4. Menebak hasil aturan bisnis untuk data baru tanpa menjalankan program.

> 💡 Di Level 1 Anda membaca program **baris demi baris**. Di Level 2 Anda membaca **peta**-nya dulu: bagian mana melakukan apa. Programmer berpengalaman juga membaca kode dengan cara ini.

---

## 📖 Materi

### A. Empat bagian program bisnis

```
┌─────────────┐    ┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
│ 1. MODEL    │    │ 2. MEMBACA   │    │ 3. ATURAN BISNIS │    │ 4. TAMPILAN  │
│ DATA        │ →  │ DATA         │ →  │ (logika)         │ →  │ HASIL        │
│ "formulir"  │    │ "input"      │    │ "SOP"            │    │ "laporan"    │
│ @dataclass  │    │ load_*()     │    │ fungsi murni     │    │ main()       │
└─────────────┘    └──────────────┘    └──────────────────┘    └──────────────┘
```

| Bagian | Analogi kantor | Pertanyaan saat memeriksa |
|--------|----------------|---------------------------|
| 1. Model data | Formulir kosong: kolom apa saja yang diisi | Apakah semua kolom penting ada? Tipenya benar (uang, tanggal, teks)? |
| 2. Membaca data | Petugas penerima berkas: menolak formulir yang salah isi | Apakah data yang salah **dihentikan** dengan pesan jelas? |
| 3. Aturan bisnis | SOP: cara memutuskan | Apakah aturannya sama persis dengan SOP? Bagaimana angka **di batas**? |
| 4. Tampilan | Laporan untuk atasan | Apakah kolom dan format mudah dibaca? |

**Bagian 3 paling penting diperiksa**, disusul bagian 2. Kesalahan tampilan terlihat jelas; kesalahan aturan bisnis bisa lolos berbulan-bulan.

### B. Model data: `@dataclass(frozen=True)`

```python
@dataclass(frozen=True)
class Claim:
    claim_id: str
    category: str
    amount: int
    has_receipt: bool
```

- `@dataclass` membuat "formulir" bernama `Claim` dengan kolom-kolom tersebut.
- `frozen=True` berarti **formulir yang sudah diisi tidak bisa dicoret**. Jika ada kode yang mencoba mengubah `claim.amount`, program langsung error. Ini mencegah bug "angka berubah diam-diam di tengah jalan".
- `: str`, `: int`, `: bool` adalah **petunjuk tipe** (*type hints*): teks, bilangan bulat, benar/salah.

### C. `@property`: kolom rumus

```python
    @property
    def days_to_submit(self) -> int:
        return (self.submitted_date - self.expense_date).days
```

Mirip kolom rumus di Excel (`=C2-B2`): nilainya **dihitung dari kolom lain**, bukan diketik. Dipakai seperti kolom biasa: `claim.days_to_submit`. Karena selalu dihitung ulang, nilainya tidak mungkin "ketinggalan" dari data aslinya.

### D. Fungsi murni: kalkulator yang jujur

**Fungsi murni** hanya memakai input yang diberikan, lalu mengembalikan hasil. Ia **tidak** membaca file, tidak mencetak ke layar, dan tidak bergantung pada jam komputer.

| Fungsi murni ✅ | Bukan fungsi murni ❌ |
|-----------------|----------------------|
| `review_claim(claim)`: dari satu klaim → keputusan | `main()`: membaca file, mencetak tabel |
| `working_days(start, end, holidays)` | Fungsi yang memakai `date.today()` di dalamnya |

Mengapa penting? Fungsi murni **mudah diuji** (Modul 2): input sama → hasil selalu sama. Itu sebabnya modul `05-it` dan `07-legal` menerima `--now` / `--today` dari luar, bukan membaca jam komputer di dalam aturan bisnisnya.

### E. Pembacaan data: penjaga pintu

Fungsi `load_*()` mengubah baris CSV (semuanya teks) menjadi model data, sekaligus **memvalidasi**:

```python
if claim.category not in CATEGORY_LIMITS:
    raise ValueError(f"unknown category {row['category']!r}")
```

Aturan di semua modul repositori ini: data yang salah **tidak pernah dilewati diam-diam**. Program berhenti dan menyebut ID baris yang salah.

### F. Tampilan: `main()` dan `argparse`

`main()` merangkai semuanya: baca argumen, panggil `load_*()`, jalankan aturan, cetak tabel. `argparse` membuat "tombol pengaturan" program. Lihat daftar tombolnya dengan `--help`:

```bash
python modules/05-it/ticket_sla.py --help
```

### G. Konstanta: aturan bisnis yang ditulis sebagai data

```python
CATEGORY_LIMITS = {"meal": 150_000, "transport": 500_000, "lodging": 1_200_000}
MAX_SUBMIT_DAYS = 30
```

Nama berhuruf **KAPITAL** adalah konstanta: angka kebijakan yang dikumpulkan di bagian atas file. Jika kebijakan berubah (misalnya batas makan naik), cukup ubah satu baris di sini. Konstanta adalah bagian dari **aturan bisnis**, jadi ikut diperiksa.

---

## 🛠️ Praktik Terpandu

**1. Peta modul HR.** Buka [`modules/03-hr/leave_tracker.py`](../../modules/03-hr/leave_tracker.py) dan cocokkan dengan tabel ini:

| Bagian | Di file ini |
|--------|-------------|
| 1. Model data | `class Employee`, `class LeaveRequest`, `class Balance` |
| 2. Membaca data | `load_employees`, `load_requests`, `load_holidays` |
| 3. Aturan bisnis | `working_days`, `calculate_balances` (+ konstanta `VALID_STATUSES`) |
| 4. Tampilan | `main` |

Perhatikan `Balance.remaining`: sebuah `@property` (sisa cuti = jatah − terpakai).

**2. Minta Claude menjelaskan bagian terpenting.** Jalankan `claude` dari folder utama repositori:

```
Jelaskan fungsi working_days di @modules/03-hr/leave_tracker.py baris per baris.
Lalu beri 3 contoh tanggal yang hasilnya mungkin mengejutkan orang HR.
```

**3. Tebak sebelum memeriksa.** Berapa hari kerja dari **Jumat 30 Oktober 2026** sampai **Selasa 3 November 2026**? Tulis jawaban Anda, lalu cari tes `test_weekend_is_not_counted` di [`test_leave_tracker.py`](../../modules/03-hr/test_leave_tracker.py).

**4. Jalankan program latihan Level 2.** Program ini dipakai di beberapa modul berikutnya:

```bash
python training/menengah/latihan/expense_claims.py
```

```
Claim  Emp   Category       Amount    Payable  Status
C-01   K001  meal          120,000    120,000  APPROVED
C-02   K001  transport     650,000    500,000  PARTIAL
C-03   K002  meal           90,000          0  REJECTED: late
C-04   K002  lodging     1,200,000  1,200,000  APPROVED
C-05   K003  transport     100,000          0  REJECTED: no receipt
C-06   K003  meal           85,000     85,000  APPROVED
C-07   K004  transport     300,000    300,000  APPROVED
C-08   K004  lodging     1,500,000  1,200,000  PARTIAL

Payable by department
Sales           620,000
Finance       1,200,000
IT               85,000
Operations    1,500,000
TOTAL         3,405,000
```

Baca *docstring* (teks pembuka di antara `"""`) di bagian atas [`expense_claims.py`](latihan/expense_claims.py). Di sana tertulis 4 aturan bisnis dan **urutan** pemeriksaannya.

> 💡 Di dalam `.venv` yang aktif, `python` dan `python3` sama saja. Materi Level 2 memakai `python`.

---

## 🏋️ Latihan

### ⭐ Latihan 1.1: Peta `expense_claims.py`

Isi tabel 4 bagian untuk [`latihan/expense_claims.py`](latihan/expense_claims.py). Sebutkan juga konstanta mana yang termasuk aturan bisnis.

### ⭐⭐ Latihan 1.2: Tebak keputusan

Tanpa menjalankan program, tentukan **status** dan **jumlah dibayar** untuk 3 klaim baru:

| Klaim | Kategori | Jumlah | Bukti | Diajukan setelah |
|-------|----------|--------|-------|------------------|
| a | meal | 160.000 | ada | 2 hari |
| b | transport | 120.000 | **tidak ada** | 31 hari |
| c | lodging | 1.200.000 | ada | 30 hari |

### ⭐⭐ Latihan 1.3: Urutan aturan

Di `review_claim`, aturan "terlambat" diperiksa **sebelum** aturan "tanpa bukti". Jika urutannya dibalik, apa yang berubah untuk klaim **b** di Latihan 1.2? Apakah jumlah dibayarnya berubah? Mengapa perbedaan ini tetap penting bagi karyawan dan tim keuangan?

### ⭐⭐⭐ Latihan 1.4: Anatomi modul lain

Pilih modul sesuai fungsi Anda (misalnya [`05-it/ticket_sla.py`](../../modules/05-it/ticket_sla.py)). Isi tabel 4 bagian, lalu jawab: di baris mana data yang salah dihentikan, dan apa bunyi pesan error-nya?

---

## 📝 Kuis

1. Sebutkan 4 bagian program bisnis. Bagian mana yang paling penting diperiksa?
2. Apa akibat `frozen=True` pada sebuah `@dataclass`?
3. Mengapa `review_claim` disebut fungsi murni, sedangkan `main` tidak?
4. Kebijakan batas klaim makan naik menjadi Rp175.000. Baris mana yang Anda ubah?

---

## 📌 Ringkasan

- Baca **peta** program dulu: model data → membaca data → aturan bisnis → tampilan.
- Periksa paling teliti **aturan bisnis** (termasuk konstanta) dan **validasi input**.
- `@property` = kolom rumus; `frozen=True` = formulir yang tidak bisa dicoret.
- Fungsi murni mudah diuji, jadi aturan bisnis sebaiknya ditulis sebagai fungsi murni.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 1.1**

| Bagian | Di `expense_claims.py` |
|--------|------------------------|
| 1. Model data | `class Claim` (dengan `@property days_to_submit`), `class Decision` |
| 2. Membaca data | `load_claims`, `parse_claim`, `parse_yes_no` |
| 3. Aturan bisnis | `review_claim`, `payable_by_department` |
| 4. Tampilan | `main` |

Konstanta aturan bisnis: `CATEGORY_LIMITS`, `MAX_SUBMIT_DAYS`, `RECEIPT_REQUIRED_FROM`. (`APPROVED`, `PARTIAL`, dan seterusnya adalah label status.)

**Latihan 1.2**
- **a)** `PARTIAL`, dibayar **150.000** (batas meal), karena 160.000 > 150.000.
- **b)** `REJECTED: late`, dibayar **0**. Aturan terlambat (31 > 30 hari) diperiksa lebih dulu.
- **c)** `APPROVED`, dibayar **1.200.000**. Tepat 30 hari masih tepat waktu (`> 30` baru terlambat), dan tepat di batas lodging masih dibayar penuh (`> limit` baru dipotong).

**Latihan 1.3:** statusnya menjadi `REJECTED: no receipt`, jumlah dibayar tetap 0. Perbedaannya ada pada **alasan**: karyawan akan mengira cukup melampirkan bukti lalu mengajukan ulang, padahal klaimnya tetap akan ditolak karena terlambat. Laporan ke tim keuangan juga salah menghitung "berapa klaim ditolak karena terlambat". Urutan aturan adalah keputusan bisnis, jadi harus tertulis di prompt dan di docstring.

**Latihan 1.4 (contoh `ticket_sla.py`)**

| Bagian | Di file ini |
|--------|-------------|
| 1. Model data | `class Ticket` (dengan `@property is_open`) |
| 2. Membaca data | `load_tickets` |
| 3. Aturan bisnis | `hours_elapsed`, `is_breached`, `compliance_by_priority` + konstanta `SLA_HOURS` |
| 4. Tampilan | `main` (dengan argumen `--now`) |

Data salah dihentikan di `load_tickets`: `raise ValueError(f"{r['ticket_id']}: unknown priority {r['priority']!r}")`, misalnya `INC-9: unknown priority 'P9'`.

**Kuis**
1. Model data, membaca data, aturan bisnis, tampilan. Paling penting: **aturan bisnis**.
2. Isi objek tidak bisa diubah setelah dibuat; mencoba mengubahnya menimbulkan error.
3. `review_claim` hanya memakai input dan mengembalikan hasil. `main` membaca file dan mencetak ke layar.
4. `CATEGORY_LIMITS` di bagian atas file: ubah `"meal": 150_000` menjadi `"meal": 175_000`. Jangan lupa: tes dan contoh output yang bergantung pada angka itu juga perlu dicek (Modul 2 dan 4).

</details>

---

← [Daftar Modul](README.md) | **Berikutnya: [Modul 2: Tes Otomatis dengan pytest →](modul-02-pytest.md)**
