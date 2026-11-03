# Vibe Coding: From Zero to Hero

**Materi pelatihan berbahasa Indonesia** untuk siapa saja (staf operasional, keuangan, HR, marketing, IT, akuntansi, legal, dan fungsi pendukung lainnya) yang ingin membangun alat kerja dan aplikasi sendiri dengan bantuan AI (Claude Code).

Anda **tidak perlu latar belakang pemrograman**. Yang Anda butuhkan: paham masalah di pekerjaan Anda, mau mencoba, dan disiplin memeriksa hasil.

---

## Peta Perjalanan

```
 ZERO                                                               HERO
  │                                                                   │
  ▼                                                                   ▼
┌──────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
│  LEVEL 1: DASAR  │──▶│  LEVEL 2: MENENGAH   │──▶│  LEVEL 3: MAHIR      │
│  "Saya bisa      │   │  "Saya bisa membuat  │   │  "Saya bisa membuat  │
│   menjalankan &  │   │   alat yang benar,   │   │   aplikasi untuk tim │
│   mengubah skrip"│   │   teruji & rapi"     │   │   & mengajari orang" │
└──────────────────┘   └──────────────────────┘   └──────────────────────┘
   ± 12 jam              ± 25 jam                    ± 45 jam
   (2 minggu)            (4 minggu)                  (6–8 minggu)
```

| Level | File | Anda akan bisa... | Proyek akhir |
|-------|------|-------------------|--------------|
| 🟢 **Dasar** | [01-dasar.md](01-dasar.md) + [📘 materi modul](dasar/README.md) | Menyiapkan alat, menulis prompt yang baik, menjalankan & memodifikasi skrip, memverifikasi hasil, menyimpan versi dengan Git | Memodifikasi modul Operasional dengan prompt sendiri |
| 🟡 **Menengah** | [02-menengah.md](02-menengah.md) + [📘 materi modul](menengah/README.md) | Membaca kode buatan AI, menulis & menjalankan tes, debugging, memakai database SQL, membuat `CLAUDE.md`, bekerja dengan branch | Alat otomatisasi dari pekerjaan Anda sendiri, lengkap dengan tes |
| 🔴 **Mahir** | [03-mahir.md](03-mahir.md) + [📘 materi modul](mahir/README.md) | Membangun aplikasi web (API + database + tampilan), mengamankan aplikasi, memakai fitur lanjutan Claude Code, mengintegrasikan Claude API, CI/CD, deploy, menjadi *AI champion* di kantor | Aplikasi web multi-pengguna untuk satu proses bisnis |

---

## Cara Menggunakan Materi Ini

1. **Ikuti urutan.** Setiap langkah dibangun di atas langkah sebelumnya. Jangan melompat ke level Mahir sebelum lulus checklist level Dasar dan Menengah.
2. **Praktik, bukan hanya membaca.** Setiap langkah punya bagian **🛠️ Praktik**. Kerjakan di komputer Anda.
3. **Gunakan modul studi kasus.** Folder [`../modules/`](../modules/) berisi 10 studi kasus per fungsi bisnis. Materi ini akan sering merujuk ke sana.
4. **Cek checklist kelulusan** di akhir setiap level. Jika semua tercentang, lanjut ke level berikutnya.
5. **Belajar berkelompok lebih efektif.** Satu sesi mingguan 2 jam + latihan mandiri adalah ritme yang baik.

### Struktur setiap langkah

| Bagian | Isi |
|--------|-----|
| 🎯 **Tujuan** | Apa yang akan Anda kuasai |
| 📖 **Konsep** | Penjelasan singkat dengan analogi sehari-hari |
| 🛠️ **Praktik** | Perintah, prompt, atau kode yang Anda jalankan sendiri |
| ⚠️ **Kesalahan umum** | Jebakan yang sering dialami pemula |
| ✅ **Cek pemahaman** | Pertanyaan atau latihan singkat |

---

## Modul Studi Kasus per Fungsi Bisnis

| Fungsi | Modul | Dipakai di level |
|--------|-------|------------------|
| Operasional | [01-operations](../modules/01-operations/) | Dasar |
| Keuangan | [02-finance](../modules/02-finance/) | Dasar |
| SDM / HR | [03-hr](../modules/03-hr/) | Menengah |
| Marketing | [04-marketing](../modules/04-marketing/) | Menengah |
| IT | [05-it](../modules/05-it/) | Menengah |
| Akuntansi | [06-accounting](../modules/06-accounting/) | Menengah |
| Legal | [07-legal](../modules/07-legal/) | Menengah |
| Pengadaan | [08-procurement](../modules/08-procurement/) | Mahir |
| Layanan Pelanggan | [09-customer-service](../modules/09-customer-service/) | Mahir |
| General Affairs | [10-general-affairs](../modules/10-general-affairs/) | Mahir |

---

## 🔒 Aturan Emas Keamanan Data (berlaku di semua level)

> **Jangan pernah** menempelkan data pribadi atau rahasia asli ke alat AI mana pun, termasuk data karyawan, KTP/NIK, NPWP, gaji, rekening bank, data kesehatan, data pelanggan, atau isi kontrak rahasia.
>
> Data seperti ini dilindungi oleh **UU Pelindungan Data Pribadi (UU PDP No. 27 Tahun 2022)** dan, untuk data warga Uni Eropa, **GDPR**. Pelanggaran dapat berakibat sanksi bagi perusahaan dan individu.
>
> **Cara aman:** bangun dan uji alat dengan **data contoh (sintetis/buatan)**, lalu jalankan alat yang sudah jadi pada data asli **di komputer Anda sendiri**, tanpa mengirim data itu ke AI.

---

## Glosarium Singkat

| Istilah | Arti sederhana |
|---------|----------------|
| **Vibe coding** | Membuat perangkat lunak dengan menjelaskan keinginan dalam bahasa sehari-hari ke AI, lalu memeriksa dan memperbaiki hasilnya |
| **Prompt** | Instruksi yang Anda tulis untuk AI |
| **Skrip** | File berisi kode program yang bisa dijalankan, mis. `inventory_reorder.py` |
| **Terminal / CLI** | Jendela untuk mengetik perintah ke komputer |
| **Claude Code** | Asisten AI dari Anthropic yang bisa membaca, menulis, dan menjalankan kode di proyek Anda |
| **CSV** | File tabel sederhana (bisa dibuka di Excel), kolom dipisah koma |
| **Bug** | Kesalahan pada program |
| **Tes (test)** | Kode kecil yang otomatis memeriksa apakah program bekerja benar |
| **Git / commit** | Alat untuk menyimpan "foto" versi pekerjaan Anda; *commit* = satu foto |
| **Branch** | "Cabang" pekerjaan terpisah agar eksperimen tidak merusak versi utama |
| **Database / SQL** | Tempat menyimpan data terstruktur / bahasa untuk mengambil data darinya |
| **API** | "Pintu" agar satu program bisa meminta data atau layanan dari program lain |
| **Deploy** | Memasang aplikasi agar bisa dipakai orang lain |
| **CI/CD** | Pemeriksaan & pemasangan otomatis setiap kali kode berubah |

---

**Siap? Mulai dari [Level 1: Dasar →](01-dasar.md)**
