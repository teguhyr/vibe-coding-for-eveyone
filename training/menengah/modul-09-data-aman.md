# Modul 9: Data Asli dengan Aman

| | |
|---|---|
| **Langkah di rencana** | [Level 2, Langkah 9](../02-menengah.md#langkah-9-data-asli-dengan-aman) |
| **Sesi** | Sesi 4 |
| **Durasi** | 30 menit |
| **Prasyarat** | Modul 7 (`CLAUDE.md`) |
| **File latihan** | [`modules/03-hr/data/`](../../modules/03-hr/data/) (data sintetis), [`.gitignore`](../../.gitignore) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menerapkan pola **"bangun dengan data palsu, jalankan dengan data asli"**.
2. Mengelompokkan kolom data: aman, perlu dianonimkan, atau tidak boleh dipakai sama sekali.
3. Membuat data sintetis dan menganonimkan data dengan 4 teknik.
4. Memasang **pertahanan berlapis**: folder `private/`, `.gitignore`, larangan di `CLAUDE.md`, dan aturan izin Claude Code.
5. Mengetahui langkah yang harus diambil jika data terlanjur terkirim.

> ⚠️ Modul ini **tidak** menggantikan kebijakan perlindungan data perusahaan Anda. Jika ragu, tanyakan ke petugas pelindungan data (DPO), tim legal, atau tim keamanan informasi.

---

## 📖 Materi

### A. Pola "bangun dengan data palsu, jalankan dengan data asli"

```
   ┌──────────────────────────────┐           ┌──────────────────────────────┐
   │  TAHAP BANGUN (bersama AI)   │           │  TAHAP PAKAI (tanpa AI)      │
   │  • Data sintetis/contoh      │  ──────▶  │  • Data asli                 │
   │  • Prompt, kode, tes         │           │  • Di komputer Anda sendiri  │
   │  • Boleh dibagikan           │           │  • Hasil tidak dikirim ke AI │
   └──────────────────────────────┘           └──────────────────────────────┘
```

AI hanya perlu tahu **bentuk** data (nama kolom, format, contoh nilai palsu), bukan **isi** data asli. Program yang sudah teruji dengan data palsu bisa dijalankan pada data asli **tanpa** AI.

### B. Data yang wajib dilindungi (UU PDP No. 27/2022)

| Kategori | Contoh |
|----------|--------|
| Data pribadi umum | Nama lengkap, jenis kelamin, kewarganegaraan, agama, status perkawinan, atau gabungan data yang bisa mengenali seseorang (nama + alamat + tanggal lahir) |
| Nomor identitas | KTP/NIK, NPWP, paspor, BPJS, nomor karyawan yang bisa dicocokkan ke orang |
| Data pribadi spesifik | Kesehatan, biometrik, genetika, catatan kejahatan, data anak, **data keuangan pribadi** (gaji, rekening, nomor kartu) |
| Rahasia perusahaan | Isi kontrak, harga negosiasi, strategi, kata sandi, API key |

Data pribadi **spesifik** berisiko paling tinggi. Kebocorannya bisa menimbulkan sanksi bagi perusahaan dan kerugian besar bagi orangnya. Untuk data warga Uni Eropa, berlaku juga **GDPR**.

### C. Empat teknik mengurangi risiko

| Teknik | Cara | Contoh |
|--------|------|--------|
| **Sintetis** | Buat data palsu dengan bentuk yang sama | AI membuat 30 karyawan fiktif |
| **Minimisasi** | Pakai hanya kolom yang dibutuhkan | Program cuti tidak butuh NIK, gaji, alamat: buang kolomnya |
| **Pseudonimisasi** | Ganti identitas dengan kode | `Budi Santoso` → `K-001` |
| **Generalisasi / acak** | Kurangi detail, geser angka | Tanggal lahir → tahun lahir; gaji → rentang; angka ± acak |

> ⚠️ Data yang di-pseudonimkan **masih data pribadi** jika ada tabel kunci yang bisa mengembalikan `K-001` ke `Budi Santoso`, atau jika gabungan kolomnya masih bisa mengenali orang (misalnya satu-satunya manajer wanita di cabang Medan). Untuk dikirim ke AI, **data sintetis** adalah pilihan teraman.

### D. Pertahanan berlapis

Jangan bergantung pada satu pengaman saja. Pasang beberapa lapis:

| Lapis | Melindungi dari | Cara |
|-------|-----------------|------|
| 1. Folder terpisah | Tercampur dengan data contoh | Simpan data asli di `private/` |
| 2. `.gitignore` | Ikut ter-commit ke Git | Repositori ini sudah memblokir `private/`, `*.xlsx`, `*.xls`, `*.db`, `.env` |
| 3. `CLAUDE.md` | Claude membacanya karena tidak tahu | "Jangan pernah membaca folder `private/`" |
| 4. Aturan izin Claude Code | Claude membaca walau ada instruksi | Aturan `deny` di `.claude/settings.json` (lihat Latihan 9.4) |
| 5. Kebiasaan Anda | Semua hal di atas gagal | Jalankan alat jadi di **terminal biasa**, jangan tempel hasilnya ke AI |

### E. Jika data terlanjur terkirim atau ter-commit

1. **Berhenti.** Jangan lanjutkan percakapan dengan data itu.
2. **Laporkan** ke atasan dan DPO/tim keamanan sesuai prosedur perusahaan. Jangan disembunyikan; UU PDP mewajibkan penanganan kegagalan pelindungan data dengan cepat.
3. **Rahasia (kata sandi, API key) dianggap bocor:** segera **ganti (rotate)**. Menghapus commit saja tidak cukup, karena salinannya mungkin sudah ada di tempat lain.
4. **Perbaiki prosesnya** agar tidak terulang (tambah lapis pertahanan di bagian D).

---

## 🛠️ Praktik Terpandu

**1. Siapkan folder "data asli" (latihan).** Kita berpura-pura data sintetis modul HR adalah data asli bulan Oktober:

```bash
mkdir -p private/hr_oktober
```

```bash
cp modules/03-hr/data/*.csv private/hr_oktober/
```

Di Windows PowerShell: `New-Item -ItemType Directory -Force private\hr_oktober` lalu `Copy-Item modules\03-hr\data\*.csv private\hr_oktober\`.

**2. Pastikan Git mengabaikannya.**

```bash
git status
```

Folder `private/` **tidak** muncul. Buktikan aturan mana yang memblokirnya:

```bash
git check-ignore -v private/hr_oktober/employees.csv
```

```
.gitignore:10:private/	private/hr_oktober/employees.csv
```

Artinya: baris ke-10 di `.gitignore` (`private/`) memblokir file ini.

**3. Jalankan alat jadi di terminal biasa**, bukan lewat percakapan dengan Claude:

```bash
python modules/03-hr/leave_tracker.py --data-dir private/hr_oktober
```

Hasilnya tampil di layar Anda saja. Tidak ada yang terkirim ke AI.

**4. Minta data sintetis dengan menyebut struktur, bukan isi.**

```
Buat file CSV berisi 30 baris data karyawan FIKTIF dengan kolom:
employee_id, name, department, annual_entitlement.
employee_id berformat E001-E030. department hanya: Operations, Finance, IT, Marketing.
annual_entitlement 12 atau 15. Pakai nama Indonesia yang umum dan jelas fiktif.
Jangan pakai data orang nyata. Simpan sebagai data/karyawan_sintetis.csv.
```

**5. Bersihkan latihan.**

```bash
rm -r private/hr_oktober
```

Di Windows PowerShell: `Remove-Item -Recurse private\hr_oktober`.

---

## 🏋️ Latihan

### ⭐ Latihan 9.1: Kelompokkan kolom

Sebuah ekspor HR berisi kolom berikut. Untuk membuat **laporan sisa cuti**, kelompokkan setiap kolom: **pakai**, **pakai setelah di-pseudonimkan**, atau **buang**.

`nik`, `nama_lengkap`, `departemen`, `tanggal_lahir`, `alamat_rumah`, `jatah_cuti`, `tanggal_mulai_cuti`, `tanggal_selesai_cuti`, `status_cuti`, `diagnosis_sakit`, `nomor_rekening`, `gaji_pokok`

### ⭐⭐ Latihan 9.2: Data sintetis lembur

Tulis prompt untuk membuat data sintetis yang cocok dengan [`latihan/data/lembur_oktober.csv`](latihan/data/lembur_oktober.csv) (kolom `employee_id,date,monthly_wage,hours`), 20 baris, **termasuk kasus tepi** yang berguna untuk tes.

### ⭐⭐ Latihan 9.3: Aman atau tidak?

Untuk setiap situasi, jawab **aman** atau **tidak aman**, beserta alasannya:

1. Menempel 5 baris data gaji asli ke Claude "karena cuma contoh".
2. Menempel **nama kolom** dan 2 baris **fiktif** dengan format yang sama dengan data asli.
3. Menjalankan `python leave_tracker.py --data-dir private/...` di terminal, lalu menempel **tabel hasilnya** ke Claude untuk "dibuatkan ringkasan".
4. Menempel pesan error `ValueError: Unknown leave status 'aproved' for E002` ke Claude.
5. Menyimpan `data_asli.xlsx` di folder `modules/03-hr/data/`.

### ⭐⭐⭐ Latihan 9.4: Kunci folder `private/` untuk Claude

Di `~/proyek-reimburse` (Modul 7), buat file `.claude/settings.json` yang **melarang** Claude membaca folder `private/`. Buat file `private/rahasia.csv` berisi satu baris palsu, lalu minta Claude membacanya. Apa yang terjadi? Mengapa lapis ini tetap tidak boleh menjadi satu-satunya pengaman?

---

## 📝 Kuis

1. Apa yang dikirim ke AI pada tahap "bangun"? Apa yang **tidak**?
2. Sebutkan 3 contoh data pribadi spesifik menurut UU PDP.
3. Mengapa data yang di-pseudonimkan masih bisa dianggap data pribadi?
4. Perintah apa yang membuktikan sebuah file diabaikan Git, dan oleh aturan mana?
5. API key terlanjur ter-commit dan ter-push. Apa langkah terpenting?

---

## 📌 Ringkasan

- **Bangun dengan data palsu, jalankan dengan data asli**, di komputer sendiri, tanpa AI.
- Lindungi data pribadi umum, nomor identitas, data **spesifik** (kesehatan, keuangan pribadi, dan lainnya), serta rahasia perusahaan.
- Kurangi risiko: **sintetis**, minimisasi, pseudonimisasi, generalisasi.
- Pasang **pertahanan berlapis**: `private/` + `.gitignore` + `CLAUDE.md` + aturan izin + kebiasaan.
- Jika terlanjur bocor: berhenti, **laporkan**, ganti rahasia, perbaiki proses.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 9.1**

| Kelompok | Kolom |
|----------|-------|
| **Pakai** | `departemen`, `jatah_cuti`, `tanggal_mulai_cuti`, `tanggal_selesai_cuti`, `status_cuti` |
| **Pakai setelah di-pseudonimkan** | `nama_lengkap` (atau `nik`) → ganti dengan kode `K-001`. Pilih **satu** pengenal saja; laporan cukup memakai kode |
| **Buang** | `tanggal_lahir`, `alamat_rumah`, `diagnosis_sakit` (data kesehatan = data spesifik), `nomor_rekening`, `gaji_pokok` (data keuangan pribadi = data spesifik), dan `nik` jika sudah memakai kode |

Prinsipnya **minimisasi**: laporan sisa cuti tidak butuh gaji, alamat, atau diagnosis.

**Latihan 9.2 (contoh)**
```
Buat CSV 20 baris data lembur FIKTIF dengan kolom employee_id,date,monthly_wage,hours.
employee_id K001-K010 (fiktif). date di bulan Oktober 2026, format YYYY-MM-DD.
monthly_wage antara 4.000.000 dan 12.000.000, sebagian dipilih agar upah per jam bulat
(kelipatan 173, misalnya 5.190.000 dan 6.920.000).
hours bilangan bulat 0-4. Sertakan kasus tepi: 0 jam, tepat 1 jam, tepat 4 jam (batas maksimal).
Jangan pakai data orang nyata.
```
Kasus "5 jam" atau "jam negatif" lebih baik diuji di **tes** (`pytest.raises`), bukan di CSV contoh, karena CSV contoh harus bisa dijalankan sampai selesai.

**Latihan 9.3**
1. **Tidak aman.** Gaji adalah data keuangan pribadi (spesifik). "Cuma 5 baris" tetap pelanggaran.
2. **Aman.** Struktur + data fiktif sudah cukup bagi AI.
3. **Tidak aman.** Hasil dari data asli **juga** data pribadi (nama, sisa cuti per orang). Buat ringkasannya sendiri, atau minta Claude menambahkan fitur ringkasan ke **program**, lalu jalankan programnya pada data asli.
4. **Hati-hati.** Pesan error bisa memuat ID atau nilai dari data asli. Di sini hanya kode `E002` dan salah ketik status, biasanya dapat diterima. Jika pesan error memuat nama, NIK, atau nominal, samarkan dulu (`E002` → `EXXX`).
5. **Tidak aman.** Folder `data/` hanya untuk data sintetis. (File `.xlsx` memang diblokir `.gitignore`, tetapi Claude tetap bisa membacanya saat bekerja di folder itu.)

**Latihan 9.4**
```json
{
  "permissions": {
    "deny": ["Read(./private/**)"]
  }
}
```
Saat diminta membaca `private/rahasia.csv`, Claude Code menolak karena aturan `deny`. Mengapa tidak cukup: aturan ini hanya berlaku di proyek yang punya file tersebut, bisa terhapus atau salah tulis, dan tidak melindungi dari Anda sendiri yang menempelkan data ke percakapan. Karena itu tetap dipasang **bersama** `.gitignore`, `CLAUDE.md`, dan kebiasaan yang benar. Jika ingin aturan ini berlaku untuk seluruh tim, commit `.claude/settings.json` ke repositori.

**Kuis**
1. Dikirim: struktur data, data sintetis, prompt, kode, tes. **Tidak** dikirim: data asli dan hasil olahan data asli.
2. Pilih tiga dari: kesehatan, biometrik, genetika, catatan kejahatan, data anak, data keuangan pribadi.
3. Karena masih bisa dikembalikan ke orangnya, lewat tabel kunci atau gabungan kolom lain yang unik.
4. `git check-ignore -v <file>`, yang menampilkan file `.gitignore`, nomor baris, dan aturannya.
5. **Ganti (rotate)** API key-nya segera dan laporkan. Menghapus commit tidak membuat key yang bocor aman lagi.

</details>

---

← [Modul 8](modul-08-branch-review.md) | **Berikutnya: [Modul 10: Studi Kasus Lintas Fungsi →](modul-10-studi-kasus-lintas-fungsi.md)**
