# 📝 Evaluasi Level 3: Pre-test, Post-test & Umpan Balik

| | |
|---|---|
| **Kapan** | **Pre-test:** 10 menit pertama Sesi 1. **Post-test:** Sesi 12, setelah demo |
| **Durasi** | 10 menit |
| **Tujuan** | Mengukur peningkatan pemahaman peserta dan memperbaiki pelatihan berikutnya |

Pre-test dan post-test memakai **soal yang sama**. Peserta **tidak** diberi kunci jawaban setelah pre-test.

---

## Bagian A: Soal Pilihan Ganda (15 soal)

**1.** Aturan "booking tidak boleh bentrok" paling tepat ditegakkan di...
- a) Frontend saja
- b) Backend (frontend boleh ikut memeriksa demi kenyamanan)
- c) Database saja, tanpa pesan error
- d) Dokumentasi pengguna

**2.** API membalas `500` saat pengguna mengirim tanggal dengan format salah. Seharusnya...
- a) `200`
- b) `404`
- c) `500` sudah benar
- d) `400`, dengan pesan yang jelas

**3.** Keuntungan utama pola `create_app(db_path)` adalah...
- a) Tes bisa memakai database sementara sehingga data asli tidak tersentuh
- b) Aplikasi berjalan lebih cepat
- c) Tidak perlu SQL
- d) Otomatis aman dari XSS

**4.** Booking A 09:00–10:00 sudah ada. Booking B di ruang yang sama, 10:00–11:00, menurut rumus `start_a < end_b AND start_b < end_a`...
- a) Bentrok
- b) Tergantung siapa yang memesan
- c) Tidak bentrok
- d) Error

**5.** Dalam React, mengapa `event.currentTarget` disimpan ke variabel **sebelum** `await`?
- a) Agar lebih cepat
- b) Setelah `await`, React mengosongkannya menjadi `null`
- c) Agar aman dari SQL injection
- d) Tidak ada alasan khusus

**6.** Cara menampilkan komentar pengguna yang aman dari XSS di React adalah...
- a) `<div dangerouslySetInnerHTML={{ __html: komentar }} />`
- b) Menggabungkan komentar ke string HTML
- c) Menyimpan komentar di `localStorage`
- d) `<div>{komentar}</div>`

**7.** Pengguna sudah login sebagai staf, lalu mencoba menghapus booking milik orang lain. Kode status yang tepat adalah...
- a) `403`
- b) `401`
- c) `404`
- d) `409`

**8.** Kata sandi pengguna sebaiknya disimpan sebagai...
- a) Teks biasa, agar mudah dipulihkan
- b) Di file `.env`
- c) Hash, lalu dicocokkan dengan fungsi pemeriksa hash
- d) Di kode frontend

**9.** Aturan "kode harus selalu dirapikan setiap kali Claude mengubah file" paling tepat dipasang sebagai...
- a) Kalimat di `CLAUDE.md`
- b) Hook `PostToolUse`
- c) Skill
- d) Komentar di kode

**10.** Subagent reviewer keamanan diberi `tools: Read, Grep, Glob`. Alasannya...
- a) Agar lebih pintar
- b) Wajib untuk semua subagent
- c) Agar bisa menjalankan semua perintah
- d) Hak akses minimum: ia cukup membaca, tidak perlu mengubah file

**11.** Saat memakai Claude API di dalam aplikasi, output model sebaiknya...
- a) Divalidasi terhadap daftar nilai yang sah sebelum dipakai
- b) Langsung dipakai apa adanya
- c) Disimpan tanpa diperiksa
- d) Ditampilkan sebagai HTML

**12.** API key Claude untuk aplikasi web disimpan di...
- a) Kode React agar praktis
- b) File workflow CI
- c) Environment variable di server
- d) `CLAUDE.md`

**13.** CI menunjukkan `ModuleNotFoundError: No module named 'flask'`, padahal di laptop lulus. Penyebab paling mungkin...
- a) GitHub sedang rusak
- b) Tesnya salah
- c) Python di CI terlalu baru
- d) `flask` tidak tercatat di file requirements yang dipasang oleh workflow

**14.** Container Docker dihapus lalu dibuat ulang. Data booking tetap ada jika...
- a) Database disimpan di volume
- b) Image dibuat ulang
- c) Memakai `debug=True`
- d) Tidak mungkin

**15.** Pertanyaan arsitektur yang paling sering terlupa, dan menyebabkan "aplikasi bayangan", adalah...
- a) Bahasa pemrograman apa?
- b) Warna tema apa?
- c) Siapa yang merawat aplikasi ini setelah pembuatnya pindah tugas?
- d) Berapa jumlah endpoint?

---

## Bagian B: Penilaian Diri (isi sebelum & sesudah)

Beri skor 1–5 (1 = sama sekali tidak bisa, 5 = sangat yakin bisa):

| Kemampuan | Sebelum | Sesudah |
|-----------|---------|---------|
| Menjelaskan arsitektur 3 lapis dan membaca permintaan/balasan HTTP | | |
| Membangun API Flask + SQLite dengan tes | | |
| Membangun frontend React yang terhubung ke API dan aksesibel | | |
| Mencegah SQL injection, XSS, kebocoran rahasia, dan hak akses yang rusak | | |
| Menambahkan login dan peran, dan mengujinya | | |
| Memakai command, skill, subagent, hooks, dan permissions Claude Code | | |
| Mengintegrasikan Claude API dengan aman (validasi, biaya, data pribadi) | | |
| Memasang CI dan branch protection | | |
| Mengemas dan menjalankan aplikasi dengan Docker | | |
| Menulis ADR dan memilih solusi paling sederhana yang cukup | | |
| Mengajar rekan dan mengusulkan kebijakan AI | | |

---

## Bagian C: Umpan Balik Pelatihan (Sesi 12)

1. Modul mana yang **paling bermanfaat**? Mengapa?
2. Modul mana yang **paling sulit**? Bagian mana yang perlu dijelaskan lebih baik?
3. Apakah durasi pelatihan: terlalu cepat / pas / terlalu lambat?
4. Apakah aplikasi capstone Anda akan dipakai tim? Jika belum, apa hambatannya (teknis, persetujuan IT, pengguna)?
5. Siapa 2 rekan pertama yang akan Anda ajari, dan kapan?
6. Saran untuk fasilitator:

---

## ✅ Kriteria Kelulusan Level 3 ("Hero")

Peserta dinyatakan **lulus Level 3** jika:
- [ ] Skor post-test **≥ 12 dari 15** (80%)
- [ ] Capstone lulus (semua kriteria wajib skor ≥ 3, lihat [rubrik](proyek-akhir.md#-rubrik-penilaian))
- [ ] Semua item [Checklist "Hero"](../03-mahir.md#-checklist-hero) tercentang. Dua item yang butuh waktu lebih lama ("sudah mengajari rekan kerja" dan "capstone dipakai orang lain") boleh diselesaikan **paling lambat 1 bulan** setelah pelatihan, dengan bukti ke fasilitator

---

<details>
<summary>🔑 <b>Kunci Jawaban (untuk fasilitator)</b></summary>

| No | Jawaban | Modul | No | Jawaban | Modul |
|----|---------|-------|----|---------|-------|
| 1 | b | 1 | 9 | b | 5 |
| 2 | d | 1 | 10 | d | 5 |
| 3 | a | 2 | 11 | a | 6 |
| 4 | c | 2 | 12 | c | 6 |
| 5 | b | 3 | 13 | d | 7 |
| 6 | d | 3, 4 | 14 | a | 8 |
| 7 | a | 4 | 15 | c | 9 |
| 8 | c | 4 | | | |

Jika banyak peserta salah pada soal yang sama, ulas kembali modul terkait di awal sesi berikutnya.

</details>

---

← [Proyek Akhir](proyek-akhir.md) | [Daftar Modul](README.md) | **Untuk fasilitator: [Panduan Fasilitator →](panduan-fasilitator.md)**
