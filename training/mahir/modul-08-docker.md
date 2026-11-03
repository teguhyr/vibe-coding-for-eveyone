# Modul 8: Deploy dengan Docker

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 8](../03-mahir.md#langkah-8-deploy-dengan-docker) |
| **Sesi** | Sesi 7 |
| **Durasi** | 60 menit |
| **Prasyarat** | Modul 2 (backend), Modul 4 (rahasia); **Docker Desktop** atau Docker Engine terpasang (`docker --version`) |
| **File latihan** | [`latihan/ruang-rapat/backend/Dockerfile`](latihan/ruang-rapat/backend/Dockerfile), [`.dockerignore`](latihan/ruang-rapat/backend/.dockerignore) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menjelaskan **image**, **container**, **volume**, dan **port** dengan analogi.
2. Membaca dan menulis `Dockerfile` untuk API Flask dengan server produksi **gunicorn**.
3. Membangun dan menjalankan container, dengan data yang **tetap ada** setelah container diganti.
4. Memberikan rahasia lewat environment variable, bukan lewat image.
5. Menyiapkan hal operasional dasar: **backup**, **log**, dan daftar periksa sebelum rilis.

> ⚠️ Men-deploy aplikasi ke server kantor atau ke internet **wajib** mengikuti kebijakan tim IT/keamanan. Modul ini melatih proses di komputer Anda sendiri.

---

## 📖 Materi

### A. Docker = kontainer pengiriman

| Istilah | Analogi | Arti |
|---------|---------|------|
| **Image** | Cetakan / resep paket | Aplikasi + Python + library, dibekukan menjadi satu paket. Dibuat dari `Dockerfile` |
| **Container** | Paket yang sedang dikirim/dipakai | Image yang sedang berjalan. Bisa dihentikan, dihapus, dan dibuat ulang dari image yang sama |
| **Volume** | Gudang di luar paket | Tempat data yang harus **bertahan** walau container dihapus (database!) |
| **Port** | Pintu | `-p 8000:8000` menghubungkan pintu komputer Anda ke pintu container |

Hasilnya: "di laptop saya jalan" juga berarti "di server jalan", karena isi paketnya sama persis.

### B. Server pengembangan vs produksi

| `python app.py` (pengembangan) | `gunicorn` (produksi) |
|-------------------------------|-----------------------|
| Mencetak peringatan *"Do not use it in a production deployment"* | Dirancang untuk banyak pengguna sekaligus |
| `debug=True`: konsol debug bisa **menjalankan kode** (Modul 4) | Tanpa debug |
| Memuat ulang otomatis saat kode berubah | Stabil, bisa menjalankan beberapa *worker* |

### C. `Dockerfile` baris demi baris

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Simpan database di volume agar data tidak hilang saat kontainer diganti
VOLUME /app/data
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app('/app/data/bookings.db')"]
```

| Baris | Arti |
|-------|------|
| `FROM python:3.12-slim` | Mulai dari image Python resmi versi ringan |
| `WORKDIR /app` | Folder kerja di dalam container |
| `COPY requirements.txt .` lalu `RUN pip install ...` | Pasang library **dulu**. Docker menyimpan hasil langkah ini (*cache*); selama `requirements.txt` tidak berubah, build berikutnya jauh lebih cepat |
| `COPY app.py .` | Baru salin kode. Hanya file yang dibutuhkan, bukan seluruh folder |
| `VOLUME /app/data` | Folder data ditandai sebagai volume |
| `ENV PYTHONUNBUFFERED=1` | Log Python langsung tampil, tidak tertahan |
| `EXPOSE 8000` | Dokumentasi: aplikasi mendengarkan di port 8000 |
| `CMD [...]` | Perintah saat container mulai. `app:create_app('/app/data/bookings.db')` = panggil `create_app` dari `app.py` dengan lokasi database di volume (pola `create_app` dari Modul 2) |

**`.dockerignore`** ([contoh](latihan/ruang-rapat/backend/.dockerignore)) mencegah file lokal (`*.db`, `.env`, cache) ikut terbawa ke image, mirip `.gitignore`.

### D. Rahasia: saat menjalankan, bukan di image

Image bisa disalin dan dibagikan, jadi **jangan** pernah `COPY .env` atau menulis `ENV FLASK_SECRET_KEY=...` di `Dockerfile`. Berikan rahasia saat container dijalankan:

```bash
docker run -e FLASK_SECRET_KEY="..." ...
```

atau dengan file yang tidak di-commit: `docker run --env-file .env ...`.

### E. Data, backup, dan log

- **Volume** menyimpan `bookings.db` di luar container. Hapus container → data tetap ada. Hapus **volume** → data hilang. Hati-hati dengan `docker volume rm`.
- **Backup:** SQLite punya fungsi backup bawaan yang aman walau aplikasi sedang berjalan:

  ```python
  import sqlite3

  src = sqlite3.connect("bookings.db")
  dst = sqlite3.connect("backup-2026-11-03.db")
  with dst:
      src.backup(dst)
  ```

  Jadwalkan setiap hari, simpan di lokasi lain, dan **uji pemulihannya** sesekali. Backup yang tidak pernah dicoba dipulihkan belum tentu bisa dipakai.
- **Log:** `docker logs <nama-container>` menampilkan output aplikasi. Catat error, tetapi jangan mencatat kata sandi, token, atau data pribadi.

### F. Frontend

`npm run build` di folder `frontend` menghasilkan file statis di `frontend/dist/` (HTML, CSS, JS). File ini bisa disajikan oleh web server mana pun, misalnya Nginx, yang juga meneruskan `/api/...` ke container backend (perannya sama dengan proxy Vite saat pengembangan). Konfigurasi ini biasanya disiapkan bersama tim IT.

---

## 🛠️ Praktik Terpandu

**1. Build image** (dari folder `projects/ruang-rapat/backend`, atau `training/mahir/latihan/ruang-rapat/backend` untuk contoh jadi):

```bash
docker build -t ruang-rapat-api .
```

**2. Jalankan container** dengan volume bernama `ruang-rapat-data`:

```bash
docker run -d --name ruang-rapat -p 8000:8000 -v ruang-rapat-data:/app/data ruang-rapat-api
```

`-d` = berjalan di latar belakang, `--name` = nama container.

**3. Uji** (perhatikan port **8000**, bukan 5000):

```bash
curl -X POST http://127.0.0.1:8000/api/bookings -H "Content-Type: application/json" -d @booking.json
```

Pakai file `booking.json` dari Modul 1. Balasannya `201` berisi booking baru.

**4. Lihat log:**

```bash
docker logs ruang-rapat
```

Baris seperti `Booting worker with pid` menunjukkan gunicorn berjalan.

**5. Buktikan data bertahan.** Hapus container, buat yang baru dari image yang sama, lalu ambil daftar booking:

```bash
docker rm -f ruang-rapat
```

```bash
docker run -d --name ruang-rapat -p 8000:8000 -v ruang-rapat-data:/app/data ruang-rapat-api
```

```bash
curl http://127.0.0.1:8000/api/bookings
```

Booking dari langkah 3 **masih ada**, karena tersimpan di volume.

**6. Bersihkan** setelah latihan:

```bash
docker rm -f ruang-rapat
```

```bash
docker volume rm ruang-rapat-data
```

---

## 🏋️ Latihan

### ⭐ Latihan 8.1: Image, container, atau volume?

1. Paket berisi Python 3.12, Flask, dan `app.py` yang siap dijalankan
2. Tempat `bookings.db` disimpan
3. Aplikasi yang sedang berjalan dan melayani permintaan di port 8000

### ⭐⭐ Latihan 8.2: Tanpa volume

Jalankan container **tanpa** `-v ruang-rapat-data:/app/data`, buat booking, hapus container, buat ulang. Apa yang terjadi pada data? Mengapa?

### ⭐⭐ Latihan 8.3: Backend lengkap di Docker

Buat `Dockerfile` untuk [`kunci/backend-lengkap/booking_api.py`](latihan/kunci/backend-lengkap/booking_api.py). Apa yang berbeda di baris `COPY` dan `CMD`? Bagaimana memberikan `FLASK_SECRET_KEY`, dan bagaimana membuat pengguna pertama?

### ⭐⭐⭐ Latihan 8.4: Daftar periksa rilis

Isi daftar periksa di [Langkah 8 rencana training](../03-mahir.md#langkah-8-deploy-dengan-docker) untuk aplikasi Anda. Untuk setiap butir yang belum terpenuhi, tulis tindakan, penanggung jawab, dan tenggatnya.

---

## 📝 Kuis

1. Mengapa `COPY requirements.txt` dan `RUN pip install` ditulis **sebelum** `COPY app.py`?
2. Mengapa produksi memakai gunicorn, bukan `python app.py`?
3. Container dihapus. Apakah data di volume ikut hilang?
4. Mengapa rahasia tidak boleh ditulis di `Dockerfile`?
5. Kapan terakhir kali backup Anda **diuji dipulihkan**? Mengapa pertanyaan ini penting?

---

## 📌 Ringkasan

- **Image** = paket, **container** = paket yang berjalan, **volume** = gudang data di luar paket.
- Produksi: **gunicorn**, tanpa `debug`; `create_app(db_path)` menunjuk ke volume.
- Rahasia diberikan saat `docker run` (`-e` / `--env-file`), **tidak pernah** di image.
- Operasional: backup harian yang **diuji**, log tanpa data pribadi, persetujuan tim IT.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 8.1:** (1) image; (2) volume; (3) container.

**Latihan 8.2:** data **hilang**. Tanpa volume, `bookings.db` tersimpan di lapisan tulis container itu sendiri, yang ikut terhapus bersama container. (Catatan: karena `Dockerfile` memakai `VOLUME /app/data`, Docker otomatis membuat volume **anonim** tanpa nama. Volume itu tidak dipakai ulang oleh container baru, jadi data tetap tidak terlihat.)

**Latihan 8.3 (contoh)**
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY booking_api.py .

VOLUME /app/data
ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "booking_api:create_app('/app/data/bookings.db')"]
```
`requirements.txt` sama dengan backend contoh (Flask sudah menyertakan `werkzeug.security`). Jalankan dengan rahasia dari file yang tidak di-commit:
```bash
docker run -d --name ruang-rapat -p 8000:8000 --env-file .env -v ruang-rapat-data:/app/data ruang-rapat-api-lengkap
```
Pengguna pertama dibuat dengan menjalankan perintah `add-user` **di dalam** container yang sedang berjalan, dengan kata sandi lewat environment:
```bash
docker exec -e NEW_USER_PASSWORD="..." ruang-rapat python booking_api.py --db /app/data/bookings.db add-user admin admin
```
Tanpa `FLASK_SECRET_KEY`, gunicorn gagal memulai dengan `RuntimeError: Set the FLASK_SECRET_KEY environment variable`. Itu disengaja (Modul 4).

**Latihan 8.4:** yang dinilai: setiap butir punya status yang jujur, dan butir yang belum terpenuhi punya rencana konkret. Butir "tim IT/keamanan sudah meninjau" tidak boleh dicentang sendiri.

**Kuis**
1. Agar Docker bisa memakai ulang *cache* langkah instalasi. Jika hanya `app.py` yang berubah, library tidak perlu dipasang ulang, sehingga build jauh lebih cepat.
2. Server pengembangan tidak dirancang untuk banyak pengguna, dan mode debug-nya berbahaya. Gunicorn adalah server produksi tanpa debug.
3. Tidak. Volume terpisah dari container. Data hanya hilang jika volume-nya dihapus.
4. Image bisa disalin, dibagikan, dan diunggah ke registry. Siapa pun yang punya image bisa membaca isinya, termasuk rahasia.
5. Backup yang belum pernah diuji mungkin rusak, tidak lengkap, atau tidak bisa dipulihkan. Anda baru tahu saat benar-benar membutuhkannya.

</details>

---

← [Modul 7](modul-07-ci-cd.md) | **Berikutnya: [Modul 9: Berpikir Seperti Arsitek →](modul-09-arsitek.md)**
