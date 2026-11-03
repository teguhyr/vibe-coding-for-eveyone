# Modul 9: Berpikir Seperti Arsitek

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 9](../03-mahir.md#langkah-9-berpikir-seperti-arsitek) |
| **Sesi** | Sesi 8 |
| **Durasi** | 50 menit |
| **Prasyarat** | Modul 1–8 |
| **File latihan** | [`latihan/kunci/adr/001-aplikasi-ruang-rapat.md`](latihan/kunci/adr/001-aplikasi-ruang-rapat.md) (contoh ADR) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Memilih **solusi paling sederhana yang cukup**: spreadsheet, skrip, aplikasi, atau proyek tim IT.
2. Mengajukan **5 pertanyaan wajib** sebelum membangun.
3. Menimbang biaya **membangun** dan biaya **merawat**, termasuk risiko "aplikasi bayangan" (*shadow IT*).
4. Menulis **Architecture Decision Record (ADR)** satu halaman.

---

## 📖 Materi

### A. Tangga solusi

| Kebutuhan | Solusi paling sederhana | Tanda harus naik tangga |
|-----------|-------------------------|------------------------|
| Satu orang, sesekali, data kecil | Rumus Excel / Google Sheets | Rumus makin rumit, sering salah tempel |
| Satu orang, rutin, aturan rumit | **Skrip Python** (Level 1–2) | Orang lain ikut butuh, data harus dibagikan |
| Beberapa orang, data bersama, perlu riwayat & hak akses | **Aplikasi web + database** (Level 3) | Ratusan pengguna, data kritis, harus selalu menyala |
| Ribuan pengguna, kritis bagi bisnis, regulasi ketat | Proyek tim IT dengan arsitektur penuh | — |

Naik satu anak tangga menambah **kemampuan**, tetapi juga **biaya perawatan**: server, keamanan, backup, pembaruan, dan orang yang memahami kodenya. Selalu tanyakan: *"Apakah anak tangga di bawahnya sudah cukup?"*

> 💡 Sebelum membangun, cek dulu: apakah sistem yang **sudah ada** di kantor (ERP, HRIS, kalender email, helpdesk) sudah punya fiturnya? Mengaktifkan fitur yang ada hampir selalu lebih murah daripada membangun.

### B. Lima pertanyaan wajib

1. **Masalahnya apa**, dan berapa biayanya sekarang (jam kerja, kesalahan, risiko)?
2. **Siapa penggunanya**, berapa orang, dan seberapa sering?
3. **Data apa** yang disimpan? Ada data pribadi? (UU PDP)
4. **Apa jadinya jika aplikasi mati** satu hari? Satu minggu?
5. **Siapa yang merawat** aplikasi ini setelah Anda pindah tugas?

Pertanyaan 5 paling sering terlupa. Aplikasi buatan karyawan yang dipakai banyak orang tetapi tidak diketahui tim IT dan tidak punya penerus disebut **aplikasi bayangan** (*shadow IT*). Risikonya: berhenti total saat pembuatnya cuti atau resign, tidak pernah diperbarui keamanannya, dan datanya tidak ikut kebijakan perusahaan.

### C. Biaya total, bukan hanya biaya membangun

| Biaya | Contoh |
|-------|--------|
| Membangun | Waktu Anda, dibantu AI: beberapa hari |
| Menjalankan | Server, domain, biaya Claude API per pemakaian |
| Merawat | Pembaruan library, perbaikan bug, menyesuaikan aturan bisnis yang berubah |
| Mendukung pengguna | Menjawab pertanyaan, melatih pengguna baru |
| Risiko | Data bocor, aplikasi mati saat dibutuhkan |

Vibe coding membuat biaya **membangun** turun drastis. Biaya **merawat** tidak ikut turun sebanyak itu. Karena itu keputusan arsitektur makin penting, bukan makin tidak penting.

### D. ADR: catatan keputusan

**Architecture Decision Record** adalah catatan satu halaman tentang **satu** keputusan penting:

| Bagian | Isi |
|--------|-----|
| **Konteks** | Masalah, angka, batasan saat ini |
| **Pilihan yang dipertimbangkan** | Minimal 3, termasuk yang paling sederhana dan "tidak membangun apa pun" |
| **Keputusan** | Pilihan yang diambil |
| **Alasan** | Mengapa pilihan itu, dikaitkan dengan konteks |
| **Konsekuensi** | Apa yang harus dirawat, risiko yang diterima, kapan keputusan ditinjau ulang |

Contoh lengkap: [`001-aplikasi-ruang-rapat.md`](latihan/kunci/adr/001-aplikasi-ruang-rapat.md). ADR tidak diubah setelah diterima; jika keputusan berubah, tulis ADR baru yang menggantikannya. Dengan begitu riwayat **mengapa** tetap terlihat.

---

## 🛠️ Praktik Terpandu

**1. Baca contoh ADR** di [`latihan/kunci/adr/001-aplikasi-ruang-rapat.md`](latihan/kunci/adr/001-aplikasi-ruang-rapat.md). Temukan jawaban untuk kelima pertanyaan wajib di dalamnya.

**2. Tulis ADR untuk proyek capstone Anda** dengan bantuan Claude:

```
Bantu saya menulis Architecture Decision Record (ADR) untuk <aplikasi saya>.
Konteks: <masalah, jumlah pengguna, data yang disimpan, biaya saat ini>.
Bagian: konteks, pilihan yang dipertimbangkan (minimal: spreadsheet, skrip,
fitur sistem yang sudah ada, aplikasi web), keputusan, alasan, konsekuensi
(perawatan, risiko, kapan ditinjau ulang). Maksimal 1 halaman, Bahasa Indonesia.
Tanyakan dulu informasi yang belum saya berikan; jangan mengarang angka.
```

**3. Periksa drafnya.** Semua angka harus dari Anda, bukan karangan AI. Hapus kalimat yang terlalu umum.

**4. Simpan** sebagai `docs/adr/001-<nama>.md` di repositori proyek, lalu commit.

---

## 🏋️ Latihan

### ⭐ Latihan 9.1: Anak tangga yang tepat

Tentukan solusi paling sederhana yang cukup:
1. Seorang staf keuangan menghitung denda keterlambatan untuk 20 invoice setiap bulan.
2. 40 karyawan mengajukan pinjaman koperasi; pengurus perlu menyetujui dan melihat riwayat.
3. HR ingin karyawan mengisi survei kepuasan setahun sekali.
4. Tim legal (3 orang) mencatat 60 kontrak dan butuh pengingat tenggat.
5. Seluruh perusahaan (2.000 orang) butuh sistem absensi dengan sidik jari.

### ⭐⭐ Latihan 9.2: Lima pertanyaan

Jawab kelima pertanyaan wajib untuk proyek capstone Anda. Untuk pertanyaan 5, tulis nama penerus atau pemilik cadangan yang **sudah setuju**.

### ⭐⭐⭐ Latihan 9.3: ADR kedua

Tulis ADR untuk satu keputusan **teknis** di capstone Anda, misalnya "SQLite atau PostgreSQL?", "login sendiri atau SSO kantor?", atau "panggil Claude API untuk semua pesan atau hibrida?". Minta satu rekan membacanya dan menyebutkan satu pilihan yang belum Anda pertimbangkan.

---

## 📝 Kuis

1. Apa arti "solusi paling sederhana yang cukup"?
2. Pertanyaan wajib mana yang paling sering terlupa, dan apa akibatnya?
3. Mengapa vibe coding membuat keputusan arsitektur **lebih** penting?
4. Mengapa ADR menuliskan pilihan yang **tidak** diambil?
5. Keputusan di ADR 001 berubah setahun kemudian. Apa yang Anda lakukan dengan file ADR 001?

---

## 📌 Ringkasan

- Naik tangga solusi hanya jika anak tangga di bawahnya **terbukti tidak cukup**. Cek sistem yang sudah ada dulu.
- Lima pertanyaan: masalah & biaya, pengguna, data (UU PDP), dampak jika mati, **siapa yang merawat**.
- Hitung biaya total: membangun + menjalankan + merawat + mendukung + risiko.
- Tulis keputusan penting sebagai **ADR**: konteks, pilihan, keputusan, alasan, konsekuensi.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 9.1**
1. **Spreadsheet** (atau skrip kecil jika aturannya rumit). Satu orang, data kecil.
2. **Aplikasi web**: banyak pengguna, persetujuan, riwayat, hak akses. Tetapi cek dulu apakah sistem koperasi/ERP yang ada sudah punya fitur ini.
3. **Formulir survei** yang sudah tersedia (misalnya Microsoft Forms/Google Forms yang disetujui perusahaan). Tidak perlu membangun.
4. **Skrip** seperti modul 07 (dijalankan berkala) atau spreadsheet bersama + pengingat kalender (Level 2 Modul 10 Kasus 5). Aplikasi web baru layak jika penggunanya bertambah atau butuh alur persetujuan.
5. **Proyek tim IT / sistem resmi**: ribuan pengguna, perangkat keras, data biometrik (data pribadi **spesifik** menurut UU PDP). Bukan proyek vibe coding perorangan.

**Latihan 9.2:** yang dinilai: angka nyata (bukan perkiraan kosong), data pribadi diidentifikasi, dampak jika mati dijawab jujur, dan ada penerus yang sudah setuju.

**Latihan 9.3 (contoh pilihan yang sering terlupa):** "SQLite atau PostgreSQL?" → pilihan ketiga: database yang **sudah dikelola** tim IT. "Login sendiri atau SSO?" → pilihan: tidak ada login, aplikasi hanya bisa diakses dari jaringan kantor (lalu diskusikan mengapa itu tidak cukup untuk hak akses per pengguna).

**Kuis**
1. Pilih solusi dengan kemampuan cukup untuk kebutuhan saat ini, dengan biaya perawatan paling rendah.
2. "Siapa yang merawat?" Akibatnya aplikasi bayangan: berhenti saat pembuatnya pergi, tidak diperbarui, datanya di luar kebijakan.
3. Membangun jadi murah dan cepat, sehingga mudah membuat terlalu banyak aplikasi yang semuanya harus dirawat. Yang mahal kini adalah perawatan dan risiko.
4. Agar pembaca berikutnya tahu pilihan lain sudah dipertimbangkan, dan mengapa ditolak. Ini mencegah diskusi yang sama terulang.
5. Biarkan isinya. Ubah statusnya menjadi "Digantikan oleh ADR 00X", lalu tulis ADR baru dengan konteks dan keputusan yang baru.

</details>

---

← [Modul 8](modul-08-docker.md) | **Berikutnya: [Modul 10: Menjadi AI Champion →](modul-10-ai-champion.md)**
