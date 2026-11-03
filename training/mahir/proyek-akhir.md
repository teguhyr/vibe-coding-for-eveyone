# 🏆 Proyek Akhir (Capstone) Level 3: Aplikasi Web untuk Tim

| | |
|---|---|
| **Rencana training** | [Proyek Akhir (Capstone) Level 3](../03-mahir.md#-proyek-akhir-capstone-level-3) |
| **Sesi** | Perencanaan **Sesi 9** → klinik **Sesi 10–11** → demo **Sesi 12** |
| **Durasi** | ± 23 jam (Sesi 9–12 + ± 15 jam mandiri, termasuk uji coba dengan pengguna) |
| **Prasyarat** | Modul 1–10 selesai |

## 🎯 Tujuan

Membangun **aplikasi web multi-pengguna** untuk satu proses bisnis nyata, dari ide sampai siap dipakai tim: aman, teruji, terdokumentasi, bisa dijalankan orang lain, dan **benar-benar dicoba pengguna**.

---

## 📋 Brief Proyek

**Pilih satu tema** (atau usulkan sendiri, dengan persetujuan fasilitator):

| Fungsi | Ide aplikasi | Modul dasar |
|--------|--------------|-------------|
| HR | Pengajuan & persetujuan cuti online (karyawan → atasan → HR) | [03-hr](../../modules/03-hr/) |
| Keuangan | Pengajuan & persetujuan anggaran per departemen | [02-finance](../../modules/02-finance/) |
| Pengadaan | Portal perbandingan penawaran vendor dengan skor otomatis | [08-procurement](../../modules/08-procurement/) |
| Layanan Pelanggan | Dashboard tiket dengan triase hibrida (aturan + Claude API) | [09-customer-service](../../modules/09-customer-service/) |
| Legal | Register kontrak dengan pengingat tenggat otomatis | [07-legal](../../modules/07-legal/) |
| General Affairs | Pemesanan ruang rapat lengkap dengan login dan peran admin | [10-general-affairs](../../modules/10-general-affairs/) |

**Batas ukuran:** satu proses bisnis, 2 peran, 3–6 endpoint utama. Lebih baik kecil dan matang daripada besar dan setengah jadi.

### 10 hal wajib

| # | Wajib | Modul | Bukti |
|---|-------|-------|-------|
| 1 | **ADR**: mengapa aplikasi web, bukan solusi lain | 9 | `docs/adr/001-*.md` |
| 2 | **Backend API** dengan database, validasi, dan aturan bisnis | 2 | `backend/` + tes |
| 3 | **Frontend** yang mudah dipakai dan aksesibel | 3 | `frontend/`, label & `role="status"` |
| 4 | **Login dan minimal 2 peran** dengan hak akses berbeda | 4 | Tes 401/403 |
| 5 | **Tes otomatis** untuk aturan bisnis, validasi, hak akses, dan keamanan | 2, 4 | `pytest` hijau |
| 6 | **Hasil `/security-review`** yang temuannya sudah ditindaklanjuti | 4 | `docs/security-review.md` |
| 7 | **CI** yang hijau | 7 | Tab Actions + branch protection |
| 8 | **Dockerfile** dan panduan deploy | 8 | `Dockerfile`, bagian *Deploy* di README |
| 9 | **README** untuk pengguna dan pengembang, serta **`CLAUDE.md`** proyek | Level 2 Modul 7 | Orang lain bisa menjalankan aplikasi hanya dari README |
| 10 | **Demo** 15 menit ke calon pengguna + umpan balik minimal **3 orang** | 10 | `docs/umpan-balik.md` |

---

## 🪜 Langkah Pengerjaan

### Sesi 9: Perencanaan

1. **Lima pertanyaan wajib** (Modul 9) untuk tema Anda. Tulis angkanya.
2. **ADR 001** (Modul 9).
3. **Rancangan endpoint** (Modul 1, Latihan 1.3): metode, alamat, peran yang boleh, kode status berhasil/gagal.
4. **Daftar tes** sebelum kode, minimal:

   | Kategori | Contoh |
   |----------|--------|
   | Aturan bisnis | Bentrok ditolak; berurutan boleh; sisa cuti tidak boleh minus |
   | Validasi | Data tidak lengkap → 400; tanggal terbalik → 400 |
   | Autentikasi | Tanpa login → 401; kata sandi salah → 401 dengan pesan yang sama |
   | Otorisasi | Staf mengubah data orang lain → 403; admin boleh |
   | Keamanan | Input SQL injection tidak berbahaya; kata sandi tidak disimpan polos; aplikasi menolak jalan tanpa `SECRET_KEY` |

5. **Data sintetis** untuk demo (Level 2 Modul 9). Tidak ada data asli.
6. Repositori + branch + `CLAUDE.md` awal.

### Sesi 10: Backend dan tes

Plan Mode → tes dulu → implementasi → `pytest` + ruff → commit kecil-kecil. Pasang CI (Modul 7) **sejak awal**, bukan di akhir.

### Sesi 11: Frontend, keamanan, Docker

1. Frontend dengan form login dan tampilan untuk setiap peran.
2. `/security-review` + subagent `reviewer-keamanan` (Modul 5). Catat setiap temuan dan tindakannya di `docs/security-review.md`:

   ```
   | # | Temuan | Tingkat | Tindakan | Tes | Status |
   |---|--------|---------|----------|-----|--------|
   ```

3. `Dockerfile`, `.dockerignore`, `.env.example`, dan bagian *Deploy* di README.
4. **Uji "orang lain":** minta rekan meng-clone repositori dan menjalankan aplikasi **hanya** dengan README. Catat setiap kali ia bertanya, lalu perbaiki README-nya.

### Mandiri: uji coba pengguna

Demo ke minimal **3 calon pengguna nyata** (dengan data sintetis). Untuk setiap orang, catat:

```
Nama/peran      : (boleh disamarkan: "Staf GA 1")
Tugas yang dicoba: (misalnya: memesan ruang, membatalkan pesanan)
Berhasil tanpa bantuan? : ya / tidak, di langkah mana macet
Yang disukai    :
Yang membingungkan :
Akan memakai?   : ya / mungkin / tidak, alasannya
```

Perbaiki 1–2 masalah terbesar sebelum Sesi 12.

### Sesi 12: Demo

---

## 🎤 Demo (Sesi 12, 15 menit per peserta)

1. **Masalah & ADR** (2 menit): mengapa aplikasi web, berapa biaya masalahnya sekarang.
2. **Demo sebagai 2 peran** (4 menit): alur utama, satu aturan bisnis ditolak, satu akses yang ditolak (403).
3. **Bukti kualitas** (3 menit): `pytest -v`, CI hijau di GitHub, ringkasan `security-review.md`.
4. **Deploy** (2 menit): jalankan dengan Docker, atau tunjukkan langkah README.
5. **Umpan balik pengguna** (2 menit): apa yang Anda ubah berdasarkan masukan mereka.
6. **Dampak & perawatan** (1 menit): hemat jam/bulan, kesalahan yang dicegah, siapa penerusnya.
7. **Tanya jawab** (1 menit).

---

## 📊 Rubrik Penilaian

| Kriteria | 1 — Belum | 2 — Cukup | 3 — Baik | 4 — Sangat baik |
|----------|-----------|-----------|----------|-----------------|
| **Masalah & ADR** *(wajib)* | Tidak ada ADR | ADR tanpa pilihan lain | ADR lengkap dengan ≥ 3 pilihan dan konsekuensi | + angka nyata dan penerus yang sudah setuju |
| **Backend & aturan bisnis** *(wajib)* | Aturan salah | Benar untuk kasus normal | Benar termasuk batas; validasi 400 | + kode status tepat untuk setiap kasus gagal |
| **Login & hak akses** *(wajib)* | Tidak ada | Login tanpa peran | 2 peran, dicek di backend, teruji 401/403 | + kata sandi ter-hash, sesi aman, SSO dipertimbangkan |
| **Tes & CI** *(wajib)* | Tes gagal / tidak ada CI | Tes ada, CI belum | Tes aturan + validasi + hak akses + keamanan; CI hijau | + branch protection; tes ditulis lebih dulu (terlihat di riwayat) |
| **Keamanan & data** *(wajib)* | Ada rahasia/data asli di repositori | Temuan tinggi masih terbuka | Tidak ada temuan tinggi terbuka; tidak ada rahasia/data asli | + setiap temuan punya tes; data pribadi diminimalkan |
| **Frontend & aksesibilitas** | Tidak bisa dipakai | Berfungsi, sulit dipakai | Mudah dipakai, label & pesan status | + diuji dengan keyboard saja; pesan error jelas |
| **Deploy & dokumentasi** | Tidak bisa dijalankan orang lain | Bisa dengan bantuan | Bisa hanya dari README; Dockerfile berjalan | + backup, log, dan daftar periksa rilis |
| **Pengguna & dampak** *(wajib)* | Belum dicoba pengguna | 1–2 pengguna | ≥ 3 pengguna, umpan balik tercatat | + perubahan berdasarkan umpan balik dan dampak terukur |

**Lulus:** semua kriteria **wajib** minimal skor **3**, dan semua [kriteria lulus di rencana training](../03-mahir.md#-proyek-akhir-capstone-level-3) terpenuhi.

---

<details>
<summary>🔑 <b>Contoh Referensi untuk Fasilitator: Pemesanan Ruang Rapat</b></summary>

Materi Level 3 sudah membangun sebagian besar tema General Affairs. Gunakan sebagai contoh saat menjelaskan brief, **bukan** untuk disalin peserta (peserta yang memilih tema ini harus menambahkan fitur yang belum ada, misalnya pemesanan berulang mingguan, kapasitas ruang, atau ekspor kalender).

| # | Wajib | Ada di |
|---|-------|--------|
| 1 | ADR | [`latihan/kunci/adr/001-aplikasi-ruang-rapat.md`](latihan/kunci/adr/001-aplikasi-ruang-rapat.md) |
| 2 | Backend | [`latihan/kunci/backend-lengkap/booking_api.py`](latihan/kunci/backend-lengkap/booking_api.py) |
| 3 | Frontend | [`latihan/kunci/frontend/BookingApp.tsx`](latihan/kunci/frontend/BookingApp.tsx) (belum ada form login) |
| 4 | Login + 2 peran | `booking_api.py`: `staff` dan `admin` |
| 5 | Tes | [`test_booking_api.py`](latihan/kunci/backend-lengkap/test_booking_api.py): 14 tes (aturan, validasi, 401/403, injection, hash, `SECRET_KEY`) |
| 6 | Security review | Latihan 4.2–4.3 |
| 7 | CI | [`latihan/ci/ci.yml`](latihan/ci/ci.yml) (job `backend`) |
| 8 | Docker | [`latihan/ruang-rapat/backend/Dockerfile`](latihan/ruang-rapat/backend/Dockerfile) + Latihan 8.3 |
| 9 | README & `CLAUDE.md` | Belum ada: tugas peserta |
| 10 | Demo & umpan balik | Tugas peserta |

**Kesalahan umum peserta di capstone:**
- **Proyek terlalu besar** (5 peran, 20 endpoint). Arahkan kembali ke satu alur utama.
- **Hak akses hanya di frontend** (tombol disembunyikan, tetapi endpoint tetap terbuka). Minta peserta membuktikan dengan `curl`.
- **CI baru dipasang di hari terakhir**, sehingga banyak masalah menumpuk.
- **README hanya untuk diri sendiri.** Uji "orang lain" di Sesi 11 hampir selalu menemukan langkah yang terlupa (membuat pengguna pertama, mengisi `.env`).
- **Data demo berisi data asli** rekan kerja. Periksa sebelum demo.
- **Umpan balik pengguna hanya basa-basi.** Minta pengguna mencoba tugas sendiri, tanpa dipandu, dan catat di mana mereka macet.

</details>

---

← [Modul 10](modul-10-ai-champion.md) | **Berikutnya: [Evaluasi →](evaluasi.md)**
