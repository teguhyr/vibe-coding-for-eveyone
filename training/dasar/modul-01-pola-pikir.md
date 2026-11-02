# Modul 1: Memahami Vibe Coding & Pola Pikir yang Benar

| | |
|---|---|
| **Langkah di rencana** | [Level 1, Langkah 1](../01-dasar.md#langkah-1-memahami-vibe-coding--pola-pikir-yang-benar) |
| **Sesi** | Sesi 1 |
| **Durasi** | 20 menit |
| **Prasyarat** | Tidak ada |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan apa itu vibe coding dengan kata-kata sendiri.
2. Membedakan peran manusia dan peran AI dalam vibe coding.
3. Menyebutkan 4 keterbatasan AI yang harus selalu diwaspadai.
4. Memetakan pekerjaan berulang di unit kerjanya yang cocok diotomatiskan.

---

## 📖 Materi

### A. Apa itu vibe coding?

**Vibe coding** adalah cara membuat program komputer dengan **menjelaskan keinginan dalam bahasa sehari-hari** kepada asisten AI. AI yang menulis kodenya. Istilah ini dipopulerkan oleh peneliti AI Andrej Karpathy pada awal 2025.

Dulu, untuk membuat alat kecil seperti "rekap otomatis laporan mingguan", Anda harus:
1. belajar bahasa pemrograman berbulan-bulan, atau
2. mengajukan permintaan ke tim IT, lalu menunggu antrean berminggu-minggu.

Sekarang, Anda bisa **menjelaskan kebutuhan Anda ke AI**, lalu dalam hitungan menit mendapatkan program yang bisa dicoba.

### B. Contoh penerapan di setiap fungsi bisnis

| Fungsi | Pekerjaan berulang | Alat yang bisa dibuat |
|--------|-------------------|-----------------------|
| Operasional | Cek stok gudang setiap pagi | Daftar barang yang harus dipesan ulang |
| Keuangan | Bandingkan anggaran vs realisasi | Laporan selisih otomatis |
| HR | Hitung sisa cuti karyawan | Pelacak cuti dengan hari kerja |
| Marketing | Rekap hasil kampanye dari banyak platform | Laporan CTR, CPA, ROAS |
| IT | Pantau tiket helpdesk yang terlambat | Monitor SLA |
| Akuntansi | Cocokkan rekening koran dengan buku besar | Rekonsiliasi bank otomatis |
| Legal | Lacak tenggat perpanjangan kontrak | Daftar kontrak yang harus ditindaklanjuti |
| Pengadaan | Bandingkan penawaran vendor | Skor vendor yang adil dan terdokumentasi |
| Layanan pelanggan | Sortir pesan masuk | Triase otomatis per kategori |
| General Affairs | Cek ruang rapat bentrok | Pendeteksi jadwal ganda |

Semua contoh di atas tersedia sebagai studi kasus di folder [`modules/`](../../modules/).

### C. Pembagian peran: Anda adalah manajer proyek

Bayangkan Claude sebagai **programmer junior yang sangat cepat, rajin, dan sopan, tetapi baru masuk kerja hari ini**. Ia pintar menulis kode, tetapi **tidak tahu** aturan bisnis perusahaan Anda, kecuali Anda menjelaskannya.

| Tugas Anda (manusia) | Tugas AI |
|----------------------|----------|
| Menentukan **masalah apa** yang mau diselesaikan | Menulis kode |
| Menjelaskan **aturan bisnis** dengan jelas | Menjelaskan kode jika ditanya |
| Menyediakan **contoh data** (fiktif) | Menyarankan cara yang lebih baik |
| **Memeriksa hasil**: apakah angkanya benar? | Memperbaiki kode jika diminta |
| Mengambil **keputusan akhir** dan bertanggung jawab | Menjalankan perintah, setelah Anda izinkan |

> 💡 **Prinsip utama:** AI mengerjakan, **manusia bertanggung jawab**. Jika laporan yang dibuat program salah, yang ditanya atasan adalah Anda, bukan AI.

### D. Siklus kerja vibe coding

```
  1. JELASKAN  →  2. AI MEMBUAT  →  3. JALANKAN  →  4. PERIKSA  →  5. PERBAIKI
       ▲                                                              │
       └──────────────────────────────────────────────────────────────┘
```

| Tahap | Yang Anda lakukan | Contoh |
|-------|-------------------|--------|
| 1. Jelaskan | Tulis prompt yang jelas (Modul 5) | "Hitung sisa cuti, hanya hari Senin–Jumat..." |
| 2. AI membuat | Biarkan Claude menulis kode; baca ringkasannya | Claude membuat `leave_tracker.py` |
| 3. Jalankan | Jalankan dengan data contoh | `python leave_tracker.py` |
| 4. Periksa | Cocokkan minimal 3 hasil dengan hitungan manual (Modul 8) | Hitung sisa cuti 1 karyawan dengan kalender |
| 5. Perbaiki | Minta perubahan spesifik | "Tanggal merah 17 Agustus belum dikecualikan" |

**Kisah nyata dari repositori ini:** saat modul IT ([`modules/05-it`](../../modules/05-it/)) dibuat, data contoh awalnya salah: sebuah tiket yang dimaksudkan "terlambat" ternyata baru terbuka 71 jam dari batas 72 jam. **Tahap 4 (periksa)**, lewat tes otomatis, yang menangkap kesalahan itu. Inilah mengapa tahap periksa tidak boleh dilewati.

### E. Empat keterbatasan AI yang wajib Anda ingat

| Keterbatasan | Contoh | Cara mengatasi |
|--------------|--------|----------------|
| **1. Salah paham aturan bisnis** | Anda bilang "lebih dari 10%", AI menganggap tepat 10% juga termasuk | Tulis aturan dengan tegas dan beri contoh angka |
| **2. Kode jalan, tetapi hasilnya salah** | Program tidak error, tetapi menghitung hari kalender, bukan hari kerja | Selalu verifikasi hasil (Modul 8) |
| **3. Terlalu percaya diri** | AI menjelaskan dengan meyakinkan, padahal keliru | Minta AI menunjukkan cara mengecek hasilnya |
| **4. Tidak tahu konteks Anda** | AI tidak tahu tahun fiskal Anda mulai April | Jelaskan konteks di prompt (Modul 5) |

### F. Kapan vibe coding **tidak** cocok?

- ❌ Data asli bersifat pribadi atau rahasia **dan** harus dikirim ke AI (lihat [aturan keamanan data](../README.md#-aturan-emas-keamanan-data-berlaku-di-semua-level))
- ❌ Hasil dipakai untuk keputusan penting (gaji, pajak, hukum) **tanpa** pemeriksaan manusia
- ❌ Sistem inti perusahaan (ERP, sistem pembayaran) yang seharusnya dikelola tim IT
- ✅ Alat bantu kerja pribadi atau tim kecil, dengan data contoh, yang hasilnya bisa diperiksa

---

## 🛠️ Praktik Terpandu: Diskusi 5 Menit

Fasilitator membagi peserta per fungsi (keuangan, HR, dst.). Setiap kelompok menjawab:
1. Pekerjaan apa yang paling **membosankan** dan **berulang** di unit Anda?
2. Berapa jam per bulan habis untuk pekerjaan itu?
3. Kesalahan apa yang paling sering terjadi?

---

## 🏋️ Latihan

### ⭐ Latihan 1.1: Peta pekerjaan berulang

Isi tabel ini dengan **3 pekerjaan berulang** di unit Anda. Simpan baik-baik; tabel ini dipakai di [Proyek Akhir](proyek-akhir.md) dan di Level 2.

| No | Pekerjaan | Seberapa sering? | Waktu per kali | Risiko jika salah (rendah/sedang/tinggi) | Ada data pribadi/rahasia? |
|----|-----------|------------------|----------------|------------------------------------------|---------------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### ⭐⭐ Latihan 1.2: Pilih prioritas

Dari tabel di atas, pilih **satu** pekerjaan yang paling cocok untuk vibe coding pertama Anda. Kriteria pekerjaan yang baik untuk pemula:
- sering dilakukan (mingguan atau harian),
- aturannya jelas dan bisa ditulis,
- hasilnya mudah dicek secara manual,
- bisa dikerjakan dengan data fiktif.

Tuliskan alasan pilihan Anda dalam 2–3 kalimat.

### ⭐⭐⭐ Latihan 1.3: Hitung potensi penghematan

Untuk pekerjaan yang Anda pilih, hitung:
`jam dihemat per bulan = (waktu sekarang − perkiraan waktu dengan alat) × frekuensi per bulan`

Contoh: rekap laporan 2 jam/minggu → dengan alat 15 menit/minggu → hemat (2 − 0,25) × 4 = **7 jam per bulan**.

---

## 📝 Kuis

1. Dalam vibe coding, siapa yang **bertanggung jawab** atas kebenaran hasil program?
   a) AI  b) Tim IT  c) Pengguna yang membuat program  d) Tidak ada
2. Tahap apa yang menangkap kesalahan data contoh di modul IT?
   a) Jelaskan  b) Jalankan  c) Periksa  d) Perbaiki
3. Program berjalan tanpa error. Apakah hasilnya pasti benar? Jelaskan.
4. Sebutkan 2 situasi ketika vibe coding **tidak** cocok dipakai.

---

## 📌 Ringkasan

- Vibe coding = menjelaskan keinginan dalam bahasa sehari-hari; AI menulis kodenya.
- Anda adalah **manajer proyek**; AI adalah **programmer junior** yang cepat tapi bisa salah paham.
- Siklus: **jelaskan → AI membuat → jalankan → periksa → perbaiki**. Tahap periksa tidak boleh dilewati.
- AI mengerjakan, **manusia bertanggung jawab**.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b> (buka setelah mencoba sendiri)</summary>

**Latihan 1.2: contoh jawaban**
> "Saya memilih rekap absensi mingguan karena dilakukan setiap Senin, aturannya jelas (terlambat jika masuk setelah 08.00), dan hasilnya bisa saya cek dengan menghitung 3 karyawan secara manual. Data bisa diganti nama fiktif saat membangun alat."

**Kuis**
1. **c)** Pengguna yang membuat program. AI mengerjakan, manusia bertanggung jawab.
2. **c)** Periksa. Tes otomatis memeriksa hasil dan menemukan tiket yang ternyata belum terlambat.
3. **Tidak.** Program bisa berjalan lancar tetapi memakai aturan yang salah, misalnya menghitung hari kalender, bukan hari kerja. Hasil harus diverifikasi.
4. Contoh: (1) harus mengirim data pribadi asli ke AI; (2) hasil dipakai untuk keputusan penting tanpa pemeriksaan manusia; (3) sistem inti perusahaan yang dikelola tim IT.

</details>

---

← [Daftar Modul](README.md) | **Berikutnya: [Modul 2: Menyiapkan Alat Kerja →](modul-02-menyiapkan-alat.md)**
