# Modul 2: Tes Otomatis dengan pytest

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 2](../02-menengah.md#langkah-2-tes-otomatis-dengan-pytest) |
| **Sesi** | Sesi 1 |
| **Durasi** | 70 menit |
| **Prasyarat** | Modul 1 |
| **File latihan** | [`latihan/test_expense_claims.py`](latihan/test_expense_claims.py), [`latihan/expense_claims.py`](latihan/expense_claims.py) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjalankan tes untuk seluruh repositori, satu folder, satu file, atau satu tes.
2. Membaca tes: **siapkan → jalankan → periksa**.
3. Menemukan dan menulis tes **kasus tepi** (nilai di batas, nol, data salah).
4. Memakai `pytest.raises` untuk menguji bahwa data salah ditolak.
5. Menerapkan teknik **"tes dulu"**: tes gagal (merah) → ubah kode → tes lulus (hijau).

---

## 📖 Materi

### A. Tes = daftar periksa yang dijalankan komputer

Tes adalah kalimat "jika input X, hasilnya harus Y" yang ditulis sebagai kode. Komputer memeriksa **semua** kalimat itu dalam hitungan detik, setiap kali kode berubah. Seperti auditor yang tidak pernah lelah memeriksa ulang seluruh laporan.

### B. Anatomi satu tes

```python
def test_claim_above_limit_is_capped():
    decision = review_claim(claim(category="transport", amount=650_000))  # siapkan + jalankan
    assert (decision.status, decision.payable) == (PARTIAL, 500_000)  # periksa
```

| Bagian | Arti |
|--------|------|
| `def test_...` | pytest otomatis menjalankan setiap fungsi yang namanya diawali `test_` di file `test_*.py` |
| Nama tes | Ditulis seperti **aturan bisnis**: "klaim di atas batas dipotong" |
| `claim(...)` | Fungsi pembantu yang membuat klaim contoh; hanya bagian yang penting untuk tes ini yang diisi |
| `assert` | "Pastikan bahwa...". Jika salah, tes **gagal** dan pytest menunjukkan nilai yang sebenarnya |

### C. Menjalankan tes

| Perintah | Menjalankan |
|----------|-------------|
| `pytest` | Semua tes di folder `modules/` (diatur di `pyproject.toml`) |
| `pytest modules/03-hr` | Satu modul |
| `pytest modules/03-hr -v` | Satu modul, dengan nama setiap tes |
| `pytest training/menengah/latihan/test_expense_claims.py` | Satu file |
| `pytest training/menengah/latihan/test_expense_claims.py::test_late_claim_is_rejected` | Satu tes |
| `pytest -k late` | Tes yang namanya mengandung kata `late` |

Titik `.` = lulus, `F` = gagal (*failed*), `E` = error saat menyiapkan tes.

### D. Kasus tepi: tempat bug bersembunyi

Untuk setiap aturan dengan angka batas, uji **tiga titik**: tepat di batas, satu langkah di bawah, satu langkah di atas.

| Aturan | Tepat di batas | Di bawah | Di atas |
|--------|----------------|----------|---------|
| Terlambat jika > 30 hari | 30 hari → tepat waktu | 29 hari | 31 hari → terlambat |
| Bukti wajib jika ≥ Rp100.000 | 100.000 → wajib | 99.999 → tidak wajib | 100.001 |
| Dipotong jika > batas lodging | 1.200.000 → penuh | 1.199.999 | 1.200.001 → dipotong |

Kasus tepi lain yang sering terlupa: **nol** (0 jam lembur, anggaran 0), **kosong** (file tanpa baris), **urutan aturan** (dua aturan berlaku sekaligus), dan **data salah**.

### E. Menguji bahwa data salah ditolak: `pytest.raises`

```python
def test_unknown_employee_is_an_error():
    request = LeaveRequest("E9", date(2026, 11, 2), date(2026, 11, 2), "approved")
    with pytest.raises(ValueError, match="E9"):
        calculate_balances([], [request])
```

Artinya: "kode di dalam blok `with` **harus** menimbulkan `ValueError` yang pesannya memuat `E9`". Jika tidak ada error, tes gagal. `match=` memastikan pesan error menyebut baris yang salah.

### F. `test_sample_data`: foto hasil yang benar

Setiap modul punya tes `test_sample_data` yang mengunci hasil **persis** dari CSV contoh. Jika seseorang mengubah aturan dan hasil ikut berubah, tes ini gagal, dan Anda **dipaksa** memutuskan: perubahan ini disengaja atau tidak?

### G. Teknik "tes dulu" (*test-first*)

```
  1. MERAH              2. HIJAU               3. RAPIKAN
  Tulis tes untuk  ──▶  Ubah kode seminimal ──▶ Rapikan kode,
  aturan baru.          mungkin sampai tes      tes tetap hijau.
  Tes GAGAL.            LULUS.
```

Tes yang gagal di langkah 1 membuktikan dua hal: tesnya benar-benar menguji sesuatu, dan aturan itu memang belum ada.

### H. Aturan emas: jangan ubah tes agar lulus

Jika tes gagal setelah AI mengubah kode, tanyakan: **kodenya yang salah, atau aturan bisnisnya memang berubah?** Tes yang ditulis dari aturan bisnis yang benar **tidak boleh** diubah demi lulus. Jika Claude mengusulkan mengubah tes, minta alasannya dulu.

---

## 🛠️ Praktik Terpandu

**1. Jalankan semua tes.** Dari folder utama repositori:

```bash
pytest
```

Semua tes harus lulus. Lalu lihat nama tes modul HR:

```bash
pytest modules/03-hr -v
```

Baca nama-namanya. Apakah Anda bisa menebak aturan bisnisnya hanya dari nama tes?

**2. Lihat tes gagal dengan sengaja.**
1. Di `modules/01-operations/data/inventory.csv`, ubah stok `SKU-001` dari `120` menjadi `90`.
2. Jalankan `pytest modules/01-operations`. Hasilnya memuat:

   ```
   >       assert [i.sku for i in due] == ["SKU-006", "SKU-004", "SKU-002"]
   E       AssertionError: assert ['SKU-006', '...2', 'SKU-001'] == ['SKU-006', '...4', 'SKU-002']
   E         
   E         Left contains one more item: 'SKU-001'
   ```

   Sisi kiri (*Left*) adalah hasil sebenarnya, sisi kanan adalah yang diharapkan tes. Kini ada satu barang tambahan, `SKU-001`.
3. Kembalikan datanya:

   ```bash
   git checkout modules/01-operations/data/inventory.csv
   ```

**3. Jalankan tes latihan.**

```bash
pytest training/menengah/latihan/test_expense_claims.py -v
```

Tiga tes lulus. Tetapi tidak ada satu pun yang menguji **batas** (tepat 30 hari, tepat Rp100.000, tepat di batas kategori).

**4. Tulis tes kasus tepi pertama bersama-sama.** Tambahkan di akhir [`test_expense_claims.py`](latihan/test_expense_claims.py):

```python
def test_submitted_exactly_30_days_later_is_still_on_time():
    assert review_claim(claim(days_late=30)).status == APPROVED
```

Jalankan lagi file tesnya: kini 4 tes lulus.

**5. Minta Claude mencari kasus tepi lain:**

```
Lihat @training/menengah/latihan/expense_claims.py dan tesnya.
Daftar kasus tepi apa yang belum diuji? Tulis dalam bentuk tabel:
aturan, input, hasil yang diharapkan. JANGAN tulis kodenya dulu.
```

Bandingkan daftar Claude dengan tabel di bagian D. Pilih yang benar-benar sesuai aturan bisnis, baru minta Claude menuliskan tesnya.

---

## 🏋️ Latihan

Semua latihan menambah tes di [`latihan/test_expense_claims.py`](latihan/test_expense_claims.py). **Jangan ubah `expense_claims.py`**, kecuali di Latihan 2.5.

### ⭐ Latihan 2.1: Jalankan satu tes

Jalankan **hanya** tes `test_late_claim_is_rejected`, lalu jalankan semua tes yang namanya mengandung kata `limit`. Berapa tes yang berjalan di masing-masing perintah?

### ⭐⭐ Latihan 2.2: Batas waktu dan batas kategori

Tulis tes untuk: (a) diajukan 31 hari kemudian → terlambat; (b) lodging tepat 1.200.000 → dibayar penuh; (c) lodging 1.200.001 → dipotong menjadi 1.200.000.

### ⭐⭐ Latihan 2.3: Bukti dan urutan aturan

Tulis tes untuk: (a) 100.000 tanpa bukti → ditolak; (b) 99.999 tanpa bukti → disetujui; (c) klaim 200.000, tanpa bukti, **dan** terlambat 40 hari → statusnya `REJECTED: late` (aturan terlambat menang).

### ⭐⭐⭐ Latihan 2.4: Data salah dan foto hasil

1. Tulis tes dengan `pytest.raises` yang membuktikan bahwa `load_claims` menolak kategori `meals` dan pesan error-nya menyebut ID klaim. Petunjuk: tes boleh membuat file CSV sementara dengan parameter `tmp_path` (lihat `test_unknown_priority_is_rejected` di [`modules/05-it/test_ticket_sla.py`](../../modules/05-it/test_ticket_sla.py)).
2. Tulis `test_sample_data` yang mengunci status 8 klaim dan total per departemen dari CSV contoh.

### ⭐⭐⭐ Latihan 2.5: Tes dulu, kode kemudian

Tim keuangan menambah kategori **`parking`** dengan batas **Rp50.000**.
1. Tulis tesnya **dulu**: parkir 60.000 → `PARTIAL`, dibayar 50.000. Jalankan. Tes harus **gagal**. Catat error-nya.
2. Ubah `expense_claims.py` seminimal mungkin sampai tes lulus.
3. Jalankan semua tes di file itu. Semua harus lulus.
4. Kembalikan `expense_claims.py` ke versi asli (`git checkout training/menengah/latihan/expense_claims.py`), karena modul berikutnya memakai versi aslinya. Simpan tes Anda.

---

## 📝 Kuis

1. Apa arti `.`, `F`, dan `E` di hasil pytest?
2. Aturan: "diskon jika belanja ≥ Rp500.000". Sebutkan 3 nilai yang sebaiknya diuji.
3. Untuk apa parameter `match=` di `pytest.raises`?
4. Tes `test_sample_data` gagal setelah Claude mengubah kode. Apa yang Anda lakukan pertama kali?
5. Mengapa dalam teknik "tes dulu" tes **harus gagal** sebelum kode diubah?

---

## 📌 Ringkasan

- Tes = aturan bisnis yang diperiksa komputer: **siapkan → jalankan → periksa**.
- Uji **tiga titik** di setiap batas: tepat di batas, di bawah, di atas. Jangan lupa nol, kosong, dan data salah.
- `pytest.raises(..., match=...)` membuktikan data salah ditolak dengan pesan yang jelas.
- **Tes dulu:** merah → hijau → rapikan.
- Tes yang benar **tidak boleh** diubah hanya agar lulus.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

Kunci lengkap Latihan 2.2–2.4 ada di [`latihan/kunci/test_expense_claims_kunci.py`](latihan/kunci/test_expense_claims_kunci.py). Jalankan:

```bash
pytest training/menengah/latihan/kunci -v
```

Hasilnya: `11 passed` (4 dari 11 tes berasal dari satu tes berparameter yang menguji 4 jenis data salah).

**Latihan 2.1**

```bash
pytest training/menengah/latihan/test_expense_claims.py::test_late_claim_is_rejected
```

→ `1 passed`.

```bash
pytest training/menengah/latihan/test_expense_claims.py -k limit
```

→ `1 passed, 2 deselected` (hanya `test_claim_above_limit_is_capped`). Jika Anda sudah menambah tes lain yang namanya mengandung `limit`, jumlahnya ikut bertambah.

**Latihan 2.2 & 2.3 (cuplikan)**

```python
def test_submitted_31_days_later_is_late():
    assert review_claim(claim(days_late=31)).status == REJECTED_LATE


def test_exactly_at_limit_is_paid_in_full():
    decision = review_claim(claim(category="lodging", amount=1_200_000))
    assert (decision.status, decision.payable) == (APPROVED, 1_200_000)


def test_receipt_is_required_from_exactly_100_000():
    assert review_claim(claim(amount=100_000, receipt=False)).status == REJECTED_NO_RECEIPT
    assert review_claim(claim(amount=99_999, receipt=False)).status == APPROVED


def test_late_rule_wins_over_missing_receipt():
    decision = review_claim(claim(amount=200_000, days_late=40, receipt=False))
    assert decision.status == REJECTED_LATE
```

Jangan lupa menambah `REJECTED_NO_RECEIPT` ke baris `from expense_claims import ...`. Jika lupa, pytest menampilkan `NameError: name 'REJECTED_NO_RECEIPT' is not defined`.

**Latihan 2.4:** lihat `test_bad_rows_name_the_claim_id` dan `test_sample_data` di file kunci. Hasil yang dikunci:

```python
{"Sales": 620_000, "Finance": 1_200_000, "IT": 85_000, "Operations": 1_500_000}
```

**Latihan 2.5**

```python
def test_parking_is_capped_at_50_000():
    decision = review_claim(claim(category="parking", amount=60_000))
    assert (decision.status, decision.payable) == (PARTIAL, 50_000)
```

Sebelum kode diubah, tes gagal dengan:

```
>       limit = CATEGORY_LIMITS[claim.category]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       KeyError: 'parking'
```

Perubahan minimal: tambahkan `"parking": 50_000` ke `CATEGORY_LIMITS`. Tidak perlu menyentuh bagian lain, karena `parse_claim` memvalidasi kategori dari kamus yang sama.

**Kuis**
1. `.` lulus. `F` gagal: `assert` salah atau kode di dalam tes menimbulkan error (seperti `KeyError` di Latihan 2.5). `E` error saat **menyiapkan** tes, sebelum isi tesnya berjalan.
2. 499.999 (tidak diskon), 500.000 (diskon, tepat di batas), 500.001 (diskon).
3. Memastikan **pesan** error memuat teks tertentu, misalnya ID baris yang salah.
4. Baca selisih *Left* vs *Right*, lalu tanyakan: apakah perubahan hasil ini **disengaja**? Jika tidak, kodenya yang salah. Jika ya (aturan bisnis berubah), perbarui tes **dan** contoh output di README.
5. Untuk membuktikan bahwa tes benar-benar menguji aturan baru. Tes yang langsung lulus mungkin tidak menguji apa pun.

</details>

---

← [Modul 1](modul-01-anatomi-program.md) | **Berikutnya: [Modul 3: Debugging Bersama AI →](modul-03-debugging.md)**
