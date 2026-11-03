# Modul 3: Debugging Bersama AI

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 3](../02-menengah.md#langkah-3-debugging-bersama-ai) |
| **Sesi** | Sesi 2 |
| **Durasi** | 50 menit |
| **Prasyarat** | Modul 2 |
| **File latihan** | [`latihan/data/klaim_rusak.csv`](latihan/data/klaim_rusak.csv), [`latihan/overtime_pay.py`](latihan/overtime_pay.py), [`latihan/test_overtime_pay.py`](latihan/test_overtime_pay.py) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Membaca *traceback* dari bawah ke atas, termasuk traceback berantai.
2. Membedakan 3 sumber masalah: **data**, **kode**, dan **lingkungan**.
3. Menjalankan siklus debugging 5 langkah dan menulis prompt debugging 4 bagian.
4. Menemukan **bug tanpa pesan error** dengan tes dan cek manual.
5. Mengunci perbaikan dengan **tes regresi** agar bug tidak kembali.

---

## 📖 Materi

### A. Membaca traceback: dari bawah ke atas

```
Traceback (most recent call last):
  File ".../expense_claims.py", line 107, in load_claims
    claims.append(parse_claim(row))
  File ".../expense_claims.py", line 94, in parse_claim
    raise ValueError(f"unknown category {row['category']!r}")
ValueError: unknown category 'meals'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  ...
  File ".../expense_claims.py", line 110, in load_claims
    raise ValueError(f"{row['claim_id']}: {error}") from error
ValueError: C-12: unknown category 'meals'
```

1. **Baris paling bawah** = *apa* masalahnya: `ValueError: C-12: unknown category 'meals'`.
2. **Baris `File ... line ...` di atasnya** = *di mana* terjadinya.
3. Ada **dua** traceback? Kalimat *"The above exception was the direct cause..."* berarti error pertama "dibungkus" error kedua yang lebih jelas. Di sini, `load_claims` menambahkan ID klaim `C-12` ke pesan aslinya. Tetap baca **yang paling bawah** dulu.

> 💡 Python 3.11 ke atas menampilkan tanda `~~~~^^^^` di bawah bagian kode yang bermasalah. Python 3.10 tidak. Isinya tetap sama.

### B. Tiga sumber masalah

| Sumber | Ciri | Contoh pesan | Yang diperbaiki |
|--------|------|--------------|-----------------|
| **Data** | Program menolak isi file | `ValueError: C-12: unknown category 'meals'` | File data (setelah dikonfirmasi pemilik data) |
| **Kode** | Hasil salah, atau error di tempat yang "seharusnya aman" | `KeyError`, `TypeError`, atau **tanpa error tapi angkanya salah** | Kode + tes regresi |
| **Lingkungan** | Program bahkan tidak bisa mulai | `ModuleNotFoundError: No module named 'pytest'`, `FileNotFoundError`, `command not found` | `.venv` belum aktif, folder salah, nama file salah ketik |

### C. Error yang paling sering muncul

| Error | Arti sederhana |
|-------|----------------|
| `FileNotFoundError` | File tidak ada di lokasi itu. Cek `pwd` dan nama file |
| `ModuleNotFoundError` | Library tidak ditemukan. Biasanya `.venv` belum aktif |
| `KeyError: 'x'` | Mencari kunci `'x'` di kamus/kolom CSV yang tidak punya kunci itu |
| `ValueError` | Nilainya tidak masuk akal untuk tipe itu, misalnya `int("2,5")` atau tanggal `2026-10-32` |
| `TypeError` | Jenis data salah, misalnya menjumlah teks dengan angka |
| `AssertionError` | Tes gagal: hasil tidak sama dengan yang diharapkan |

### D. Siklus debugging 5 langkah

```
1. REPRODUKSI → 2. BACA → 3. HIPOTESIS → 4. UJI KECIL → 5. PERBAIKI + TES REGRESI
   Bisa diulang?    Pesan error   "Saya duga..."   Ubah satu hal,    Tulis tes yang
                    dari bawah                     lihat hasilnya    menangkap bug ini
```

**Tes regresi** adalah tes yang ditulis **khusus untuk bug yang baru diperbaiki**. Jika suatu hari ada yang tidak sengaja memunculkan bug itu lagi, tes ini langsung gagal.

### E. Template prompt debugging (4 bagian)

```
1. YANG SAYA LAKUKAN: <perintah yang dijalankan>
2. YANG SAYA HARAPKAN: <hasil yang benar>
3. YANG TERJADI: <tempel pesan error LENGKAP atau hasil yang salah>
4. PERMINTAAN: Jelaskan penyebabnya dengan sederhana. Jangan langsung ubah kode;
   beri tahu dulu apakah masalahnya di data, di kode, atau di lingkungan.
```

### F. Jika Claude salah arah

- `Esc`: hentikan Claude di tengah pekerjaan.
- `Esc` dua kali: kembali ke titik percakapan sebelumnya (*rewind*), lalu tulis instruksi yang lebih jelas.
- `git diff` dan `git checkout -- <file>`: lihat dan batalkan perubahan file yang tidak Anda setujui.

### G. Bug paling berbahaya tidak menimbulkan error

Program yang berhenti dengan error **mudah** diketahui. Yang berbahaya adalah program yang **berjalan lancar tetapi angkanya salah**. Penangkalnya: tes kasus tepi (Modul 2) dan cek manual seperti "Cek 3 Baris" di Level 1.

---

## 🛠️ Praktik Terpandu 1: Masalah di Data

Kita bekerja pada **salinan** agar file asli tetap utuh:

```bash
cp training/menengah/latihan/data/klaim_rusak.csv klaim_saya.csv
```

Di Windows PowerShell: `Copy-Item training\menengah\latihan\data\klaim_rusak.csv klaim_saya.csv`.

**1. Reproduksi.**

```bash
python training/menengah/latihan/expense_claims.py klaim_saya.csv
```

Baris terakhir:

```
ValueError: C-12: unknown category 'meals'
```

**2. Baca dan simpulkan.** Klaim `C-12` memakai kategori `meals`, padahal yang dikenal hanya `meal`, `transport`, `lodging`. Masalahnya di **data**, bukan di kode. Program sudah benar karena menolaknya.

**3. Perbaiki satu per satu.** Ubah `meals` menjadi `meal` di `klaim_saya.csv`, lalu jalankan ulang. Muncul error berikutnya:

```
ValueError: C-13: day is out of range for month
```

Tanggal `2026-10-32` tidak ada. **Jangan menebak** tanggal yang benar; dalam pekerjaan nyata, tanyakan ke pemilik data. Untuk latihan ini, anggap pemohon mengonfirmasi tanggalnya `2026-10-31`. Jalankan ulang:

```
ValueError: C-14: expected yes/no, got 'ya'
```

Kolom `receipt` berisi `ya` (Bahasa Indonesia). Ini menarik: **data yang salah, atau program yang terlalu kaku?** Diskusikan di Latihan 3.3. Untuk sekarang, ubah menjadi `yes`.

**4. Hasil akhirnya** harus berjalan tanpa error. Bandingkan dengan kunci Latihan 3.2.

---

## 🛠️ Praktik Terpandu 2: Bug di Kode (Tanpa Pesan Error)

[`latihan/overtime_pay.py`](latihan/overtime_pay.py) menghitung upah lembur. **File ini sengaja berisi satu bug.**

**1. Jalankan programnya.**

```bash
python training/menengah/latihan/overtime_pay.py
```

```
Emp   Date       Hours        Pay
K001  2026-10-05     3    165,000
K002  2026-10-06     1     60,000
K003  2026-10-07     0    -60,000
K004  2026-10-08     4    375,000
```

Tidak ada error. Tetapi lihat `K003`: **0 jam lembur, upahnya minus Rp60.000.** Program "berhasil" dengan hasil yang salah.

**2. Biarkan tes membuktikannya.**

```bash
pytest training/menengah/latihan/test_overtime_pay.py
```

```
..F.                                                                     [100%]
=================================== FAILURES ===================================
_________________________ test_zero_hours_pays_nothing _________________________

    def test_zero_hours_pays_nothing():
>       assert overtime_pay(WAGE, 0) == 0
E       assert -60000 == 0
E        +  where -60000 = overtime_pay(5190000, 0)
```

**3. Minta Claude menjelaskan, bukan langsung memperbaiki:**

```
1. YANG SAYA LAKUKAN: pytest training/menengah/latihan/test_overtime_pay.py
2. YANG SAYA HARAPKAN: semua tes lulus; 0 jam lembur = Rp0
3. YANG TERJADI: test_zero_hours_pays_nothing gagal: assert -60000 == 0
4. PERMINTAAN: Jelaskan baris mana di @training/menengah/latihan/overtime_pay.py
   yang menyebabkan ini dan mengapa. Jangan ubah kode dulu.
```

**4. Uji hipotesis Anda sendiri.** Sebelum membaca jawaban Claude, hitung manual untuk `hours = 0`: berapa nilai `first_hour` dan `next_hours`?

**5. Perbaiki**, lalu jalankan tesnya lagi sampai `4 passed`. Tes `test_zero_hours_pays_nothing` kini menjadi **tes regresi** untuk bug ini.

**6. Kembalikan file** setelah selesai, karena peserta lain dan latihan berikutnya memakai versi yang masih ada bug-nya:

```bash
git checkout training/menengah/latihan/overtime_pay.py
```

---

## 🏋️ Latihan

### ⭐ Latihan 3.1: Data, kode, atau lingkungan?

Tentukan sumber masalah untuk setiap pesan berikut:

1. `ModuleNotFoundError: No module named 'pytest'`
2. `ValueError: INC-1009: unknown priority 'P5'`
3. `FileNotFoundError: [Errno 2] No such file or directory: 'data/klaim.csv'`
4. Laporan menunjukkan sisa cuti 13 hari, padahal jatahnya 12 dan karyawan sudah cuti 2 hari
5. `KeyError: 'amount'` saat membaca CSV yang baru diekspor dari sistem lain

### ⭐⭐ Latihan 3.2: Bersihkan `klaim_saya.csv`

Selesaikan Praktik Terpandu 1 sampai program berjalan tanpa error. Tuliskan **total yang dibayar per departemen**, lalu periksa satu baris secara manual.

### ⭐⭐ Latihan 3.3: `ya` atau `yes`?

Kolom `receipt` berisi `ya`. Ada dua pilihan: perbaiki datanya, atau ubah program agar menerima `ya`/`tidak`. Tulis 2 alasan untuk masing-masing pilihan. Jika memilih mengubah program, tulis prompt yang **meminta tes dulu**.

### ⭐⭐⭐ Latihan 3.4: Bug kedua

Setelah bug 0 jam diperbaiki (Praktik 2, langkah 5), apa hasil `overtime_pay(5_190_000, -1)`? Seharusnya bagaimana? Tulis tesnya dulu, lalu perbaiki kodenya. Bonus: apa yang terjadi jika CSV berisi `2.5` di kolom `hours`, dan bagaimana membuat pesan error-nya menyebut ID karyawan?

---

## 📝 Kuis

1. Traceback berisi dua bagian yang dipisah kalimat *"The above exception was the direct cause of the following exception"*. Bagian mana yang dibaca lebih dulu?
2. Apa itu tes regresi?
3. Mengapa bug di `overtime_pay.py` lebih berbahaya daripada error `C-12: unknown category`?
4. Tanggal di CSV tertulis `2026-10-32`. Mengapa Anda tidak boleh langsung menggantinya dengan `2026-10-31`?

---

## 📌 Ringkasan

- Baca traceback **dari bawah**. Jika berantai, baca yang paling bawah dulu.
- Tentukan sumbernya: **data, kode, atau lingkungan**. Perbaikannya berbeda.
- Siklus: **reproduksi → baca → hipotesis → uji kecil → perbaiki + tes regresi**.
- Minta Claude **menjelaskan dulu**, baru memperbaiki.
- Bug paling berbahaya **tidak** menimbulkan error. Tangkap dengan tes kasus tepi dan cek manual.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 3.1**
1. **Lingkungan**: `.venv` belum aktif atau `pip install -r requirements-dev.txt` belum dijalankan.
2. **Data**: prioritas `P5` tidak dikenal. Tanyakan ke tim IT apakah itu salah ketik atau memang prioritas baru (jika baru, aturan di kode perlu ditambah).
3. **Lingkungan**: Anda menjalankan dari folder yang salah, atau nama filenya salah. Cek dengan `pwd` dan `ls`.
4. **Kode**: tidak ada error, tetapi hasilnya mustahil (sisa > jatah). Jenis bug paling berbahaya.
5. **Data** (format berubah): sistem baru memakai nama kolom lain, misalnya `Amount` atau `nominal`. Sesuaikan pemetaan kolomnya, dan sebaiknya buat pesan error yang menyebut kolom yang hilang.

**Latihan 3.2**

```
Claim  Emp   Category       Amount    Payable  Status
C-11   K001  meal          120,000    120,000  APPROVED
C-12   K002  meal           95,000     95,000  APPROVED
C-13   K003  transport     250,000    250,000  APPROVED
C-14   K004  lodging       900,000    900,000  APPROVED

Payable by department
Sales           120,000
Finance          95,000
IT              250,000
Operations      900,000
TOTAL         1,365,000
```

Cek manual C-13: transport 250.000 ≤ batas 500.000, ada bukti, diajukan 1 hari setelah 31 Oktober → `APPROVED`, dibayar penuh. ✔ Cek total: 120 + 95 + 250 + 900 = **1.365 ribu**. ✔

**Latihan 3.3 (contoh alasan)**
- *Perbaiki data:* aturan format sudah disepakati (`yes`/`no`); program tetap sederhana; kesalahan ketik lain (`yaa`, `iya`) tetap tertangkap.
- *Ubah program:* staf memang mengisi dalam Bahasa Indonesia, jadi masalah ini akan terus berulang; menerima `ya`/`tidak` adalah keputusan yang wajar dan mudah diuji.

Contoh prompt:
```
Di @training/menengah/latihan/expense_claims.py, fungsi parse_yes_no hanya menerima yes/y/no/n.
Staf kami mengisi kolom receipt dalam Bahasa Indonesia.
Tulis dulu tes pytest: "ya" dan "Ya" → True, "tidak" → False, "iya" tetap ditolak dengan ValueError.
Tunjukkan tesnya ke saya. Setelah saya setujui, baru ubah kode seminimal mungkin sampai tes lulus.
```

**Praktik 2 (penyebab bug):** untuk `hours = 0`, `first_hour = min(0, 1) = 0` (benar), tetapi `next_hours = 0 - 1 = -1`. Hasilnya `30.000 × 2 × (−1) = −60.000`. Perbaikan satu baris:

```python
    next_hours = max(hours - 1, 0)
```

**Latihan 3.4:** setelah perbaikan di atas, `overtime_pay(5_190_000, -1)` menghasilkan **−45.000** (`first_hour = min(-1, 1) = -1`). Jam lembur negatif tidak masuk akal, jadi seharusnya ditolak:

```python
def test_negative_hours_is_an_error():
    with pytest.raises(ValueError, match="negative"):
        overtime_pay(WAGE, -1)
```

```python
    if hours < 0:
        raise ValueError(f"overtime hours cannot be negative, got {hours}")
```

Bonus: `int("2.5")` menimbulkan `ValueError: invalid literal for int() with base 10: '2.5'` tanpa menyebut karyawan mana. Bungkus pembacaan baris di `load_entries` dengan `try`/`except ValueError` lalu `raise ValueError(f"{r['employee_id']}: {error}") from error`, seperti di `load_claims`. (Apakah lembur boleh pecahan jam adalah **keputusan bisnis**: tanyakan ke HR dulu.)

**Kuis**
1. Bagian paling bawah (error terakhir), karena itu error yang sudah diberi keterangan paling jelas.
2. Tes yang ditulis untuk bug yang baru diperbaiki, agar bug itu tidak muncul lagi tanpa ketahuan.
3. Karena programnya tetap berjalan dan mencetak angka. Tanpa tes atau cek manual, upah minus bisa lolos ke penggajian.
4. Karena Anda tidak tahu tanggal sebenarnya; bisa saja `2026-10-23` atau `2026-11-02`. Menebak data sama dengan memalsukan data. Tanyakan ke pemilik data.

</details>

---

← [Modul 2](modul-02-pytest.md) | **Berikutnya: [Modul 4: Merencanakan Perubahan Besar →](modul-04-plan-mode.md)**
