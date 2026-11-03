# Modul 3: Membangun Tampilan dengan React

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 3](../03-mahir.md#langkah-3-membangun-tampilan-dengan-react) |
| **Sesi** | Sesi 3 |
| **Durasi** | 110 menit |
| **Prasyarat** | Modul 2 (backend berjalan); **Node.js LTS** terpasang (`node --version` menampilkan v22 atau lebih baru) |
| **File latihan** | [`latihan/kunci/frontend/BookingApp.tsx`](latihan/kunci/frontend/BookingApp.tsx) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Membuat proyek React + TypeScript dengan Vite dan menghubungkannya ke API Flask lewat *proxy*.
2. Menjelaskan **komponen**, **state** (`useState`), dan **efek** (`useEffect`).
3. Mengirim form ke API dan menampilkan hasil maupun pesan error dari backend.
4. Menulis tampilan yang **aksesibel** (label, `role="status"`, tombol yang jelas).
5. Mengenali bug React yang sering dibuat AI: memakai `event.currentTarget` setelah `await`.

---

## 📖 Materi

### A. Komponen = balok LEGO

Tampilan dipecah menjadi **komponen**: fungsi yang mengembalikan HTML-seperti (JSX).

```tsx
function Salam({ nama }: { nama: string }) {
  return <p>Halo, {nama}!</p>;
}
```

`{ nama }` adalah **props**: data yang diberikan dari luar, seperti isian formulir. `{nama}` di dalam JSX menampilkan nilainya **sebagai teks**.

### B. State: data yang membuat tampilan berubah

```tsx
const [bookings, setBookings] = useState<Booking[]>([]);
```

- `bookings` = nilai sekarang (awalnya daftar kosong).
- `setBookings(baru)` = ganti nilainya. React **otomatis menggambar ulang** bagian yang berubah.

Analogi: papan jadwal di lobi. Anda tidak menghapus dan menulis ulang seluruh papan; cukup ganti kartu jadwalnya, dan papan langsung menampilkan yang baru.

> ⚠️ Jangan mengubah state langsung (`bookings.push(...)`). Selalu lewat `setBookings(...)`, atau React tidak tahu ada perubahan.

### C. Efek: "lakukan ini setelah tampil"

```tsx
useEffect(() => {
  loadBookings();
}, []);
```

Muat data **sekali** saat komponen pertama kali tampil. `[]` di akhir = "tidak bergantung pada apa pun, jadi jangan diulang".

### D. Form, `fetch`, dan `await`

```tsx
async function handleSubmit(event: FormEvent<HTMLFormElement>) {
  event.preventDefault();                 // jangan muat ulang halaman
  const formElement = event.currentTarget; // simpan SEBELUM await
  const form = new FormData(formElement);
  const response = await fetch("/api/bookings", { method: "POST", ... });
  ...
  formElement.reset();
}
```

`fetch` mengirim permintaan HTTP dari browser, persis seperti `curl` di Modul 1. `await` menunggu balasannya.

**Bug yang sering dibuat AI:** setelah `await`, React mengosongkan `event.currentTarget` menjadi `null`. Kode `event.currentTarget.reset()` setelah `await` akan error: `Cannot read properties of null (reading 'reset')`. Solusinya: simpan ke variabel **sebelum** `await`.

### E. Proxy: satu alamat untuk dua server

Saat pengembangan, React berjalan di `http://localhost:5173` dan Flask di `http://127.0.0.1:5000`. Konfigurasi *proxy* di `vite.config.ts` meneruskan setiap permintaan `/api/...` dari 5173 ke 5000, sehingga kode frontend cukup menulis `fetch("/api/bookings")`.

### F. Keamanan dan aksesibilitas bawaan

| Praktik | Mengapa |
|---------|---------|
| Tampilkan teks dengan `{message}` | React otomatis meng-*escape* teks, sehingga `<script>` dari pengguna tampil sebagai tulisan, bukan dijalankan (aman dari **XSS**, Modul 4) |
| Setiap input dibungkus `<label>` | Pembaca layar (*screen reader*) menyebut nama kolomnya; mengklik label memfokuskan input |
| Pesan memakai `role="status"` | Pesan "berhasil"/"bentrok" diumumkan otomatis oleh pembaca layar |
| Tombol punya teks yang jelas | "Hapus booking Merapi 09:00", bukan hanya ikon tempat sampah |
| **Jangan** menaruh rahasia di kode frontend | Semua kode frontend bisa dilihat siapa pun lewat browser (*View Source*, DevTools) |

---

## 🛠️ Praktik Terpandu

Ikuti langkah 1–5 di [Langkah 3 rencana training](../03-mahir.md#langkah-3-membangun-tampilan-dengan-react) di folder `projects/ruang-rapat`. Catatan tambahan:

**1. Buat proyek.**

```bash
npm create vite@latest frontend -- --template react-ts
```

Jika ditanya pertanyaan tambahan (misalnya ingin langsung menjalankan), pilih tidak; kita akan menjalankannya sendiri. Lalu:

```bash
cd frontend
```

```bash
npm install
```

**2. Atur proxy, buat `src/BookingApp.tsx`, dan ganti `src/App.tsx`** persis seperti di rencana training.

**3. Pastikan kodenya lolos pemeriksaan tipe dan bisa di-*build*:**

```bash
npm run build
```

Jika ada error TypeScript, tempelkan **seluruh** pesannya ke Claude dengan template debugging Level 2.

**4. Jalankan keduanya.** Terminal 1 (folder `backend`): `python app.py`. Terminal 2 (folder `frontend`):

```bash
npm run dev
```

Buka http://localhost:5173.

**5. Uji 3 skenario** dan catat apa yang tampil:

| Skenario | Yang diharapkan |
|----------|-----------------|
| Pesan Merapi 3 Nov 09:00–10:00 | `Booking #1 berhasil disimpan.` dan baris baru di tabel |
| Pesan yang sama sekali lagi | `Bentrok dengan booking #1` (tabel tidak bertambah) |
| Hentikan backend (`Ctrl+C`), lalu muat ulang halaman | Tabel kosong; buka DevTools (`F12`) → tab *Console* dan *Network* untuk melihat error-nya |

**6. Lihat lalu lintasnya.** Di DevTools → tab **Network**, klik permintaan `bookings`. Lihat *Headers* (metode, kode status) dan *Response* (JSON). Ini adalah HTTP yang sama dengan `curl` di Modul 1.

---

## 🏋️ Latihan

### ⭐ Latihan 3.1: Ruang baru

Tambahkan ruang `Semeru` ke pilihan. Apakah backend menerimanya? (Petunjuk: lihat Latihan 2.4.) Mengapa daftar ruang **sebaiknya** diambil dari backend, misalnya `GET /api/rooms`, dan tidak ditulis di dua tempat?

### ⭐⭐ Latihan 3.2: Tombol Hapus

Tambahkan tombol **Hapus** di setiap baris tabel, memakai endpoint `DELETE` dari Latihan 2.2. Minta konfirmasi sebelum menghapus, dan tampilkan pesan hasilnya di `role="status"`.

### ⭐⭐ Latihan 3.3: Pesan saat backend mati

Saat backend tidak berjalan, halaman diam saja. Tampilkan pesan yang jelas, misalnya *"Gagal memuat daftar booking. Apakah backend sudah berjalan?"*

### ⭐⭐⭐ Latihan 3.4: Validasi di dua tempat

Tambahkan pemeriksaan di frontend: jika jam selesai ≤ jam mulai, tampilkan pesan **tanpa** mengirim ke backend. Lalu buktikan dengan `curl` bahwa backend **tetap** menolak data itu. Jelaskan mengapa pemeriksaan di frontend saja tidak cukup.

---

## 📝 Kuis

1. Apa beda **props** dan **state**?
2. Apa arti `[]` di akhir `useEffect(() => { ... }, [])`?
3. Mengapa `const formElement = event.currentTarget` harus ditulis **sebelum** `await`?
4. Mengapa `<p>{message}</p>` aman dari XSS, sedangkan `dangerouslySetInnerHTML` tidak?
5. Seorang rekan ingin menaruh API key Claude di kode React agar "lebih praktis". Apa jawaban Anda?

---

## 📌 Ringkasan

- React = **komponen** + **state**; ubah state lewat setter, dan tampilan ikut berubah.
- `useEffect(..., [])` untuk memuat data sekali; `fetch` + `await` untuk bicara dengan API.
- Simpan `event.currentTarget` **sebelum** `await`.
- Teks lewat `{...}` otomatis aman dari XSS; label dan `role="status"` membuat tampilan aksesibel.
- Frontend bisa dilihat dan dilewati siapa pun: **tanpa rahasia, dan validasi tetap di backend**.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 3.1:** backend contoh (`latihan/ruang-rapat/backend/app.py`) menerima nama ruang apa pun, jadi `Semeru` diterima. Backend lengkap di kunci (dengan `ROOMS`) akan menolaknya dengan 400. Jika daftar ruang ditulis di frontend **dan** backend, keduanya bisa tidak sinkron: frontend menawarkan ruang yang ditolak backend, atau sebaliknya. Satu sumber kebenaran (*single source of truth*) di backend, misalnya `GET /api/rooms`, mencegah hal ini.

**Latihan 3.2 & 3.3:** lihat [`latihan/kunci/frontend/BookingApp.tsx`](latihan/kunci/frontend/BookingApp.tsx). Kunci ini sudah diuji: `npm run build` lulus, lalu diuji di browser (Playwright) terhadap backend dengan endpoint `DELETE`: simpan → `Booking #1 berhasil disimpan.`, simpan ulang → `Bentrok dengan booking #1`, hapus → `Booking #1 dihapus.` dan tabel kosong, tanpa error di browser. Inti tambahannya:

```tsx
async function handleDelete(booking: Booking) {
  if (!window.confirm(`Hapus booking ${booking.room} oleh ${booking.booked_by}?`)) {
    return;
  }
  const response = await fetch(`/api/bookings/${booking.id}`, { method: "DELETE" });
  if (response.ok) {
    setMessage(`Booking #${booking.id} dihapus.`);
    loadBookings();
  } else {
    const result = await response.json();
    setMessage(result.error);
  }
}
```

Perhatikan: balasan `204` **tidak punya isi**, jadi `response.json()` hanya dipanggil saat gagal. Memanggil `response.json()` pada balasan 204 akan error. Tombolnya memakai `type="button"` (agar tidak ikut mengirim form) dan `aria-label` yang menyebut barisnya.

Untuk Latihan 3.3, `loadBookings()` memeriksa `response.ok`. Catatan: jika backend mati total, saat pengembangan proxy Vite membalas `502 Bad Gateway`, sehingga `response.ok` bernilai `false` dan pesannya tampil (sudah diuji di browser). Untuk penanganan yang lebih lengkap, bungkus `fetch` dengan `try`/`catch` agar error jaringan juga tertangkap.

**Latihan 3.4 (contoh):**
```tsx
const start = String(form.get("start_at"));
const end = String(form.get("end_at"));
if (end <= start) {
  setMessage("Jam selesai harus setelah jam mulai.");
  return;
}
```
Nilai `datetime-local` berformat `YYYY-MM-DDTHH:MM`, jadi perbandingan teks aman (alasan yang sama dengan normalisasi di Modul 2). Pemeriksaan ini hanya untuk **kenyamanan** pengguna. Siapa pun bisa mengirim permintaan langsung dengan `curl` tanpa melewati React, jadi backend tetap harus menolak (dan memang menolak dengan 400).

**Kuis**
1. Props = data yang diberikan dari luar komponen (seperti parameter fungsi). State = data milik komponen yang bisa berubah dan memicu gambar ulang.
2. Efek hanya dijalankan sekali, setelah komponen pertama kali tampil.
3. Setelah `await`, React mengosongkan `event.currentTarget` menjadi `null`, sehingga `.reset()` akan error.
4. `{message}` ditampilkan sebagai **teks** (di-escape). `dangerouslySetInnerHTML` memasukkan teks sebagai **HTML**, sehingga `<script>` atau `<img onerror=...>` bisa dijalankan.
5. Tidak boleh. Kode frontend bisa dibaca siapa pun di browser, jadi key-nya bocor. Panggil Claude API dari **backend**, dan simpan key di environment variable server (Modul 6).

</details>

---

← [Modul 2](modul-02-api-flask.md) | **Berikutnya: [Modul 4: Keamanan Aplikasi (OWASP) →](modul-04-keamanan-owasp.md)**
