# 🧑‍🏫 Panduan Fasilitator — Level 3: Mahir

Panduan ini untuk **trainer/fasilitator** yang membawakan [Paket Materi Level 3](README.md). Isinya: persiapan, rundown menit demi menit, tips mengajar, dan solusi masalah yang sering muncul.

---

## 1. Ringkasan Pelatihan

| | |
|---|---|
| **Format** | 12 sesi tatap muka × 2 jam dalam 6 minggu (2 sesi per minggu) + ± 21 jam mandiri (latihan + capstone). Sediakan cadangan 1–2 minggu untuk uji coba pengguna |
| **Ukuran kelas** | Ideal 6–12 peserta. Rasio 1 fasilitator + 1 asisten per 6 peserta (banyak masalah instalasi dan debugging individual) |
| **Peserta** | Lulusan [Level 2](../menengah/evaluasi.md#-kriteria-kelulusan-level-2) |
| **Fasilitator** | Pernah membangun dan men-deploy aplikasi web; memahami OWASP dasar; sudah menjalankan semua praktik di paket ini |
| **Hasil** | Peserta lulus [kriteria kelulusan Level 3](evaluasi.md#-kriteria-kelulusan-level-3-hero) |

---

## 2. Persiapan

### H-14: Koordinasi dengan IT dan keamanan

Level 3 membutuhkan lebih banyak izin daripada level sebelumnya. Pastikan **tertulis**:
- [ ] Izin memasang **Node.js LTS** dan **Docker Desktop** (lisensi Docker Desktop untuk perusahaan besar perlu dicek tim IT) di laptop peserta.
- [ ] Akses jaringan ke `pypi.org`, `registry.npmjs.org`, `github.com`, `hub.docker.com`, dan `claude.ai`.
- [ ] Repositori GitHub (atau sistem setara) untuk setiap peserta, dengan GitHub Actions aktif.
- [ ] **Keputusan tentang Claude API** (Modul 6): apakah ada API key latihan dari perusahaan, berapa batas biayanya, dan siapa yang memegang key. Jika tidak ada, Modul 6 tetap bisa dijalankan penuh dengan tes klien palsu; langkah 3 (panggilan sungguhan) dilewati.
- [ ] Persetujuan tim IT/keamanan untuk **uji coba capstone** dengan pengguna (di laptop peserta atau server uji internal, dengan data sintetis).

### H-7: Undangan & prasyarat

- [ ] Kirim undangan berisi jadwal 12 sesi dan tautan ke [Daftar Modul](README.md).
- [ ] Minta peserta memasang Node.js LTS dan Docker, lalu mengirim hasil `node --version`, `npm --version`, `docker --version`, dan `docker run hello-world`.
- [ ] Minta peserta memikirkan **tema capstone** dari daftar di [Proyek Akhir](proyek-akhir.md).

### H-1: Persiapan fasilitator

Jalankan dari folder utama repositori (dengan `.venv` aktif):

```bash
pip install -r requirements-dev.txt -r training/mahir/latihan/ruang-rapat/backend/requirements.txt
```

```bash
pytest training/mahir/latihan/ruang-rapat/backend
```

```bash
pytest training/mahir/latihan/kunci/backend-lengkap
```

```bash
pytest training/mahir/latihan/klasifikasi
```

Hasil yang benar: `6 passed`, `14 passed`, `9 passed`. Jalankan ketiganya **terpisah** (dua folder pertama sama-sama berisi file dengan nama yang bisa bentrok jika digabung dengan proyek peserta).

- [ ] Jalankan semua praktik terpandu Modul 1–10, termasuk membuat proyek React (Modul 3) dan `docker build` (Modul 8) di laptop presentasi.
- [ ] Siapkan **lembar pre-test** ([Evaluasi](evaluasi.md)).
- [ ] Perbesar ukuran huruf terminal, VS Code, dan browser (minimal 18pt) untuk proyektor.

---

## 3. Rundown Sesi

Setiap sesi 120 menit. Pola umum: 5 menit tanya jawab tugas mandiri, materi + praktik, 5 menit penutup dan tugas mandiri.

### Minggu 1

#### Sesi 1: Arsitektur & HTTP

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:10 | Pembukaan + **pre-test** | [Evaluasi](evaluasi.md) | Tekankan: pre-test tidak dinilai |
| 0:10–1:55 | Arsitektur 3 lapis & HTTP | [Modul 1](modul-01-arsitektur-3-lapis.md) | Momen penting: `curl` mengirim permintaan **tanpa** frontend → aturan harus di backend. Latihan 1.3 (rancang endpoint cuti) dikerjakan berpasangan |
| 1:55–2:00 | Penutup | — | Tugas: Latihan 1.4 |

#### Sesi 2: API Flask

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab | — | |
| 0:05–1:55 | API Flask + SQLite | [Modul 2](modul-02-api-flask.md) | Peserta membangun di `projects/ruang-rapat` dengan Plan Mode, lalu membandingkan dengan contoh jadi. Latihan 2.2 (DELETE, tes dulu) di kelas |
| 1:55–2:00 | Penutup | — | Tugas: Latihan 2.3, 2.4 |

### Minggu 2

#### Sesi 3: React

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab | — | Cek semua peserta punya Node.js; yang belum, berpasangan |
| 0:05–1:55 | Frontend React | [Modul 3](modul-03-react.md) | `npm install` bisa lama di Wi-Fi kelas: minta peserta menjalankan langkah 1 **sebelum** sesi. Tunjukkan tab Network di DevTools |
| 1:55–2:00 | Penutup | — | Tugas: Latihan 3.3, 3.4 |

#### Sesi 4: Keamanan

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab | — | Ingatkan aturan etika: serangan hanya ke aplikasi latihan sendiri |
| 0:05–1:55 | OWASP, login, peran | [Modul 4](modul-04-keamanan-owasp.md) | Latihan 4.2 (temukan celah) sebagai lomba kelompok, 15 menit. Bahas temuan bersama sebelum kunci dibuka |
| 1:55–2:00 | Penutup | — | Tugas: Latihan 4.3, 4.4 |

### Minggu 3

#### Sesi 5: Claude Code lanjutan

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab | — | |
| 0:05–1:55 | Command, skill, subagent, hooks, permissions, headless | [Modul 5](modul-05-claude-code-lanjutan.md) | Kerjakan di proyek **peserta**, bukan di repositori pelatihan. Cek versi Claude Code peserta (`claude --version`); fitur bisa berbeda antarversi |
| 1:55–2:00 | Penutup | — | Tugas: Latihan 5.2, 5.4 |

#### Sesi 6: Claude API

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab | — | |
| 0:05–1:55 | Integrasi Claude API | [Modul 6](modul-06-claude-api.md) | Mulai dari tes klien palsu (tanpa biaya). Panggilan sungguhan hanya dengan API key dari perusahaan, **didemokan fasilitator** jika key tidak dibagikan ke peserta. Tekankan diskusi data pribadi |
| 1:55–2:00 | Penutup | — | Tugas: Latihan 6.2, 6.4. Pilih tema capstone |

### Minggu 4

#### Sesi 7: CI/CD & Docker

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab | — | |
| 0:05–0:55 | CI/CD | [Modul 7](modul-07-ci-cd.md) | Run pertama GitHub Actions butuh 1–2 menit: sambil menunggu, bahas anatomi YAML |
| 0:55–1:55 | Docker | [Modul 8](modul-08-docker.md) | Unduh image `python:3.12-slim` bisa lama: minta peserta menjalankan `docker pull python:3.12-slim` **sebelum** sesi |
| 1:55–2:00 | Penutup | — | Tugas: Latihan 7.2, 8.3 |

#### Sesi 8: Arsitek & AI Champion

| Waktu | Kegiatan | Materi | Catatan fasilitator |
|-------|----------|--------|---------------------|
| 0:00–0:05 | Tanya jawab | — | |
| 0:05–0:55 | Berpikir seperti arsitek | [Modul 9](modul-09-arsitek.md) | Latihan 9.1 sebagai diskusi kelas. Tanyakan "siapa yang merawat?" untuk setiap ide capstone |
| 0:55–1:55 | AI Champion | [Modul 10](modul-10-ai-champion.md) | Jika memungkinkan, undang perwakilan legal/IT 15 menit untuk mendengar draf kebijakan AI peserta |
| 1:55–2:00 | Penutup | — | Tugas: ADR capstone (draf) |

### Minggu 5

#### Sesi 9: Capstone — Perencanaan

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:15 | Brief, 10 hal wajib, rubrik | Tunjukkan [contoh referensi](proyek-akhir.md) dan tegaskan batas ukuran |
| 0:15–1:00 | Lima pertanyaan + ADR | Periksa: ada penerus? ada data pribadi? |
| 1:00–1:45 | Rancangan endpoint + daftar tes | Setiap peserta minimal 1 tes per kategori (aturan, validasi, 401, 403, keamanan) |
| 1:45–1:55 | Tukar rencana berpasangan | Cari satu celah hak akses di rancangan pasangan |
| 1:55–2:00 | Penutup | Tugas: backend + tes + CI terpasang |

#### Sesi 10: Capstone — Klinik backend

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:10 | Masalah umum | Kumpulkan dan jawab untuk seluruh kelas |
| 0:10–1:50 | Klinik | Prioritaskan peserta yang CI-nya belum hijau atau belum punya tes hak akses |
| 1:50–2:00 | Cek kemajuan | Setiap peserta menunjukkan `pytest` + tab Actions |

### Minggu 6

#### Sesi 11: Capstone — Frontend, keamanan, Docker

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:10 | Masalah umum | |
| 0:10–1:10 | Frontend + `/security-review` | Setiap temuan tinggi harus punya tindakan sebelum Sesi 12 |
| 1:10–1:45 | Uji "orang lain" | Peserta bertukar repositori: jalankan aplikasi rekan **hanya** dari README. Catat setiap pertanyaan |
| 1:45–2:00 | Persiapan demo & uji pengguna | Ingatkan: 3 pengguna nyata sebelum Sesi 12, data sintetis |

#### Sesi 12: Demo & Kelulusan

| Waktu | Kegiatan | Catatan fasilitator |
|-------|----------|---------------------|
| 0:00–0:05 | Pembukaan | Urutan demo diundi |
| 0:05–1:35 | Demo capstone (15 menit/peserta) | Untuk kelas > 6 orang, bagi menjadi 2 ruang paralel. Nilai dengan rubrik. Undang calon pengguna dan perwakilan IT bila memungkinkan |
| 1:35–1:45 | **Post-test** | Soal sama dengan pre-test |
| 1:45–1:55 | Penilaian diri & umpan balik | Bagian B & C di [Evaluasi](evaluasi.md) |
| 1:55–2:00 | Penutupan | Umumkan kelulusan; minta setiap lulusan menjadwalkan workshop Level 1 pertamanya |

### Rekap waktu

| | Jam |
|---|---|
| 12 sesi tatap muka × 2 jam | 24 |
| Latihan mandiri (latihan ⭐⭐–⭐⭐⭐ setiap modul) | ± 6 |
| Capstone mandiri (implementasi, README, uji coba 3 pengguna) | ± 15 |
| **Total** | **± 45** |

---

## 4. Tips Mengajar

1. **Biarkan peserta membangun sendiri, lalu membandingkan.** Folder `latihan/` adalah pembanding, bukan untuk disalin. Kode buatan Claude untuk setiap peserta akan berbeda; nilai **perilaku** dan tesnya.
2. **"Buktikan dengan `curl`."** Setiap kali peserta bilang "sudah aman karena tombolnya disembunyikan", minta ia mengirim permintaan langsung ke backend.
3. **Keamanan sebagai kebiasaan, bukan modul.** Setelah Modul 4, tanyakan "401 atau 403?" dan "di mana rahasianya disimpan?" di setiap sesi.
4. **Tunjukkan bug AI yang nyata.** Bug `event.currentTarget` setelah `await` (Modul 3) dan `SELECT *` yang ikut mengirim kolom kata sandi (Modul 4) adalah contoh yang mudah diingat.
5. **Jaga ukuran capstone.** Penyebab utama tidak lulus adalah proyek terlalu besar. Satu alur, 2 peran, 3–6 endpoint.
6. **Tegakkan aturan data.** Capstone memakai masalah nyata, tetapi datanya **harus** sintetis. Periksa repositori dan data demo setiap peserta.
7. **Libatkan IT sejak awal.** Peserta Level 3 membuat aplikasi yang bisa dipakai orang lain. Hubungan baik dengan tim IT menentukan apakah aplikasi itu boleh dipakai.

---

## 5. Masalah Umum & Solusi

| Masalah | Solusi cepat |
|---------|--------------|
| `ModuleNotFoundError: No module named 'flask'` | `.venv` belum aktif, atau `pip install -r .../backend/requirements.txt` belum dijalankan |
| `Address already in use` (port 5000/5173/8000) | Server lama masih berjalan. Hentikan dengan `Ctrl+C` di terminalnya, atau pakai port lain. Di macOS, port 5000 kadang dipakai *AirPlay Receiver*: matikan di System Settings atau jalankan Flask di port lain |
| Browser: error koneksi atau `502` saat memuat data | Backend belum berjalan. Kedua server (Flask dan Vite) harus aktif |
| `npm` tidak dikenal | Node.js belum terpasang atau terminal belum dibuka ulang setelah instalasi |
| `pytest` mengumpulkan tes dari dua `test_app.py` dan gagal impor | Dua folder dengan nama file yang sama dijalankan dalam satu perintah. Jalankan per folder |
| `RuntimeError: Set the FLASK_SECRET_KEY environment variable` | Disengaja (Modul 4). Set variabelnya di terminal yang sama dengan server |
| Login berhasil di `curl`, tetapi permintaan berikutnya 401 | Cookie tidak dikirim. Pakai `-c cookies.txt` saat login dan `-b cookies.txt` sesudahnya |
| Docker: `Cannot connect to the Docker daemon` | Docker Desktop belum dijalankan |
| CI merah, lokal hijau | Dependensi tidak tercatat di requirements, atau file belum di-commit. Lihat [Latihan 7.3](modul-07-ci-cd.md#-latihan-73-kenapa-merah-di-ci-hijau-di-laptop) |
| Peserta tidak punya API key Claude | Modul 6 tetap lengkap dengan tes klien palsu. Fasilitator mendemokan panggilan sungguhan |
| Fitur Claude Code berbeda dari materi | Cek `claude --version` dan dokumentasi terbaru; perbarui Claude Code. Laporkan perbedaannya agar materi diperbarui |

---

## 6. Penilaian & Sertifikat

- Rekap skor pre-test, post-test, dan rubrik capstone setiap peserta.
- **Lulus Level 3 ("Hero"):** post-test ≥ 12/15, capstone lulus, checklist "Hero" lengkap (2 item boleh menyusul paling lambat 1 bulan, lihat [kriteria](evaluasi.md#-kriteria-kelulusan-level-3-hero)).
- Peserta yang belum lulus: beri kesempatan memperbaiki capstone dalam 3 minggu.
- Laporkan ke manajemen: kenaikan skor pre→post test, jumlah lulusan, **daftar aplikasi capstone** dengan dampak terukur dan status persetujuan IT, serta **jadwal workshop Level 1** yang akan dibawakan para lulusan. Inilah efek berganda dari program ini.

---

← [Daftar Modul](README.md)
