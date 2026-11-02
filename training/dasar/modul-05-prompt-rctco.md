# Modul 5: Rumus Prompt R-C-T-C-O

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 5](../01-dasar.md#langkah-5-rumus-prompt-r-c-t-c-o) |
| **Sesi** | Sesi 1 |
| **Durasi** | 30 menit |
| **Prasyarat** | Modul 4 |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menyebutkan dan menjelaskan 5 bagian prompt R-C-T-C-O.
2. Mengenali bagian yang hilang dari sebuah prompt.
3. Menulis aturan bisnis yang tidak ambigu.
4. Menulis prompt lengkap untuk pekerjaan berulang dari unit kerjanya sendiri.

---

## 📖 Materi

### A. Mengapa prompt penting?

Prompt itu seperti **brief kerja untuk vendor**. Brief yang samar menghasilkan revisi berkali-kali; brief yang jelas menghasilkan pekerjaan yang benar sejak awal.

| Prompt samar | Akibatnya |
|--------------|-----------|
| "buatin program cek budget" | AI menebak nama kolom, aturan, dan format hasil, dan tebakannya sering salah |

### B. Lima bagian R-C-T-C-O

| Huruf | Bagian | Pertanyaan kunci | Tips |
|-------|--------|------------------|------|
| **R** | *Role* (Peran) | AI berperan sebagai siapa, membantu siapa? | Sebutkan juga level Anda: "Saya pemula, jelaskan dengan sederhana" |
| **C** | *Context* (Konteks) | Situasinya apa? Datanya seperti apa? | **Wajib** sebut nama file, nama kolom, dan 2–3 contoh baris (fiktif) |
| **T** | *Task* (Tugas) | Apa persisnya yang harus dibuat? | Satu tugas utama. Pakai kata kerja jelas: hitung, bandingkan, tandai, urutkan |
| **C** | *Constraints* (Batasan) | Aturan apa yang wajib dipatuhi? | Aturan bisnis dengan angka, batas (≥ atau >), kasus khusus (nilai 0, data kosong) |
| **O** | *Output* (Hasil) | Hasilnya seperti apa? | Tabel di layar, file CSV, kolom apa saja, urutan. Minta juga penjelasan cara menjalankan |

### C. Menulis aturan bisnis yang tidak ambigu

Bagian **Constraints** paling sering menjadi sumber kesalahan. Bandingkan:

| ❌ Ambigu | ✅ Jelas |
|----------|---------|
| "Tandai yang over budget" | "Tandai OVER jika realisasi melebihi anggaran **lebih dari** 10%. Tepat 10% masih OK." |
| "Hitung hari cuti" | "Hitung **hari kerja Senin–Jumat**, termasuk tanggal mulai dan selesai, **tidak termasuk** tanggal merah di `holidays.csv`." |
| "Urutkan yang penting dulu" | "Urutkan dari **sisa hari paling sedikit**." |
| "Jangan error" | "Jika anggaran 0, jangan dibagi; tandai **TANPA ANGGARAN**." |

**Trik:** sertakan **satu contoh perhitungan**. *"Contoh: anggaran 50.000, realisasi 58.000 → selisih +8.000, +16% → OVER."* AI hampir tidak mungkin salah paham dengan contoh angka.

### D. Contoh lengkap

```
ROLE: Kamu developer Python yang membantu tim keuangan. Saya pemula; jelaskan kodemu dengan sederhana.

CONTEXT: Saya punya file data/anggaran.csv dengan kolom:
departemen, kategori, anggaran, realisasi
Contoh baris (data fiktif):
Marketing,Iklan Digital,40000000,31000000
HR,Pelatihan,15000000,18000000

TASK: Buat skrip yang menghitung selisih (realisasi - anggaran) dan persentase selisih
untuk setiap baris.

CONSTRAINTS:
- Hanya library standar Python.
- Gunakan Decimal untuk uang, bukan float.
- Tandai "LEBIH" jika selisih > 10%, "KURANG" jika < -10%, selain itu "OK".
  Contoh: anggaran 15.000.000, realisasi 18.000.000 → +20% → LEBIH.
- Jika anggaran 0, jangan error; tandai "TANPA ANGGARAN".

OUTPUT: Tabel di layar: departemen, kategori, anggaran, realisasi, selisih, %, status.
Setelah itu jelaskan cara menjalankan dan cara kerja bagian utamanya.
```

Contoh prompt lain untuk setiap fungsi bisnis ada di bagian **"Step 1: The prompt"** pada README setiap modul di [`modules/`](../../modules/), dan template kosongnya di [`prompt-template.md`](../../modules/00-getting-started/prompt-template.md).

### E. Tujuh kesalahan prompt yang paling umum

1. **Tanpa contoh data:** AI menebak nama kolom.
2. **Aturan tanpa angka:** "yang terlambat", "yang besar".
3. **Batas tidak jelas:** apakah tepat 10% termasuk?
4. **Lupa kasus khusus:** nilai 0, data kosong, tanggal sama.
5. **Terlalu banyak tugas sekaligus:** "buat laporan, grafik, kirim email, dan dashboard".
6. **Tidak menyebut format hasil:** AI memilih sendiri.
7. **Menempel data asli:** **dilarang**. Pakai data fiktif.

### F. Checklist sebelum menekan Enter

- [ ] Ada **R**: peran AI dan level saya
- [ ] Ada **C**: nama file, nama kolom, 2–3 contoh baris **fiktif**
- [ ] Ada **T**: satu tugas utama dengan kata kerja jelas
- [ ] Ada **C**: aturan bisnis dengan angka, batas, dan kasus khusus
- [ ] Ada **O**: bentuk hasil + minta penjelasan
- [ ] **Tidak ada** data pribadi atau rahasia asli

---

## 🛠️ Praktik Terpandu

1. Jalankan `claude` dari folder utama repositori.
2. Kirim **prompt buruk** ini, lalu perhatikan apa yang ditanyakan atau ditebak Claude:

   ```
   buatin program cek budget. tampilkan kodenya saja, jangan buat file.
   ```

3. Ketik `/clear`, lalu kirim **prompt lengkap** dari bagian D, dengan tambahan *"Tampilkan kodenya saja, jangan buat file."* di akhir.
4. Bandingkan kedua hasil. Mana yang lebih sesuai kebutuhan? Mana yang lebih sedikit menebak?

---

## 🏋️ Latihan

### ⭐ Latihan 5.1: Bagian mana yang hilang?

Untuk setiap prompt, sebutkan bagian R-C-T-C-O yang **hilang**:

1. *"Kamu developer Python. Hitung sisa cuti karyawan dan tampilkan dalam tabel."*
2. *"Saya punya kontrak.csv berisi nomor kontrak, vendor, tanggal berakhir. Buat daftar kontrak yang perlu diperpanjang."*
3. *"Kamu developer Python untuk tim marketing. File kampanye.csv berisi nama kampanye, biaya, klik, penjualan. Hitung ROAS tiap kampanye, tampilkan tabel urut dari yang terbaik."*

### ⭐⭐ Latihan 5.2: Perbaiki prompt

Tulis ulang **dua** prompt dari Latihan 5.1 menjadi prompt R-C-T-C-O lengkap. Tambahkan minimal satu aturan dengan contoh angka.

### ⭐⭐⭐ Latihan 5.3: Prompt untuk pekerjaan Anda

Tulis prompt R-C-T-C-O untuk pekerjaan yang Anda pilih di [Latihan 1.2](modul-01-pola-pikir.md#-latihan-12-pilih-prioritas). Periksa dengan checklist di bagian F. Simpan; prompt ini dipakai lagi di [Proyek Akhir](proyek-akhir.md) dan Level 2.

---

## 📝 Kuis

1. Apa kepanjangan R-C-T-C-O?
2. Bagian mana yang paling sering menjadi sumber kesalahan?
3. Mengapa contoh perhitungan dengan angka sangat membantu?
4. Bolehkah menempel 3 baris data gaji asli sebagai contoh di bagian Context? Mengapa?

---

## 📌 Ringkasan

- **R**ole, **C**ontext, **T**ask, **C**onstraints, **O**utput.
- Context **wajib** berisi nama kolom dan contoh baris **fiktif**.
- Constraints: aturan dengan **angka**, **batas** (> atau ≥), **kasus khusus**, dan **satu contoh perhitungan**.
- Periksa dengan checklist sebelum menekan Enter.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 5.1**
1. Hilang **Context** (file dan kolom apa?), **Constraints** (hari kerja? tanggal merah? status apa yang dihitung?). Output hanya disebut "tabel" tanpa kolom.
2. Hilang **Role**, **Constraints** ("perlu diperpanjang" itu kapan? berapa hari sebelum berakhir?), dan **Output**.
3. Hilang **Constraints**: rumus ROAS, perlakuan jika biaya 0, contoh baris data.

**Latihan 5.2: contoh jawaban untuk prompt nomor 2**
```
ROLE: Kamu developer Python yang membantu tim legal. Saya pemula; jelaskan dengan sederhana.

CONTEXT: File data/kontrak.csv (data fiktif) berisi kolom:
nomor_kontrak, vendor, tanggal_berakhir, hari_pemberitahuan, perpanjang_otomatis (ya/tidak)
Contoh: KTR-001,PT Contoh Logistik,2027-01-15,30,ya

TASK: Buat daftar kontrak yang harus ditindaklanjuti.

CONSTRAINTS:
- Hanya library standar Python.
- Tenggat pemberitahuan = tanggal_berakhir - hari_pemberitahuan.
  Contoh: berakhir 2027-01-15, pemberitahuan 30 hari → tenggat 2026-12-16.
- Tandai "SEGERA" jika tenggat dalam 60 hari ke depan (termasuk hari ini),
  "TERLEWAT" jika tenggat sudah lewat tetapi kontrak belum berakhir,
  "BERAKHIR" jika kontrak sudah berakhir.
- Tolak nilai perpanjang_otomatis selain ya/tidak dengan pesan error yang jelas.
- Tanggal "hari ini" bisa diatur lewat opsi --today agar mudah dites.

OUTPUT: Tabel urut dari tenggat terdekat: nomor, vendor, tanggal berakhir, tenggat, status.
Setelah itu jelaskan cara menjalankannya.
```
Bandingkan dengan prompt asli di [`modules/07-legal/README.md`](../../modules/07-legal/README.md).

**Kuis**
1. *Role, Context, Task, Constraints, Output* (Peran, Konteks, Tugas, Batasan, Hasil).
2. **Constraints** (aturan bisnis), karena sering ambigu.
3. Contoh angka menghilangkan tafsiran ganda; AI bisa mencocokkan hasilnya dengan contoh itu.
4. **Tidak boleh.** Data gaji adalah data pribadi yang dilindungi UU PDP. Gunakan angka fiktif dengan format yang sama.

</details>

---

← [Modul 4](modul-04-claude-code-pertama.md) | **Berikutnya: [Modul 6: Membaca Kode Tanpa Takut →](modul-06-membaca-kode.md)**
