// Kunci Modul 3: komponen pemesanan dengan tombol Hapus di setiap baris.
// Pasangan backend: endpoint DELETE /api/bookings/<id> dari latihan Modul 2.
import { useEffect, useState, type FormEvent } from "react";

type Booking = {
  id: number;
  room: string;
  booked_by: string;
  start_at: string;
  end_at: string;
};

export default function BookingApp() {
  const [bookings, setBookings] = useState<Booking[]>([]);
  const [message, setMessage] = useState("");

  async function loadBookings() {
    const response = await fetch("/api/bookings");
    if (!response.ok) {
      setMessage("Gagal memuat daftar booking. Apakah backend sudah berjalan?");
      return;
    }
    setBookings(await response.json());
  }

  useEffect(() => {
    loadBookings();
  }, []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const formElement = event.currentTarget; // simpan sebelum await: React mengosongkannya setelahnya
    const form = new FormData(formElement);
    const response = await fetch("/api/bookings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(Object.fromEntries(form)),
    });
    const result = await response.json();
    if (response.ok) {
      setMessage(`Booking #${result.id} berhasil disimpan.`);
      formElement.reset();
      loadBookings();
    } else {
      setMessage(result.error); // React otomatis meng-escape teks, aman dari XSS
    }
  }

  async function handleDelete(booking: Booking) {
    // Konfirmasi dulu: menghapus tidak bisa dibatalkan.
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

  return (
    <main>
      <h1>Pemesanan Ruang Rapat</h1>

      <form onSubmit={handleSubmit}>
        <label>
          Ruang
          <select name="room" required>
            <option>Merapi</option>
            <option>Bromo</option>
            <option>Rinjani</option>
          </select>
        </label>
        <label>
          Tim pemesan
          <input name="booked_by" required />
        </label>
        <label>
          Mulai
          <input name="start_at" type="datetime-local" required />
        </label>
        <label>
          Selesai
          <input name="end_at" type="datetime-local" required />
        </label>
        <button type="submit">Pesan</button>
      </form>

      <p role="status">{message}</p>

      <table>
        <thead>
          <tr>
            <th>Ruang</th>
            <th>Tim</th>
            <th>Mulai</th>
            <th>Selesai</th>
            <th>Aksi</th>
          </tr>
        </thead>
        <tbody>
          {bookings.map((b) => (
            <tr key={b.id}>
              <td>{b.room}</td>
              <td>{b.booked_by}</td>
              <td>{b.start_at}</td>
              <td>{b.end_at}</td>
              <td>
                {/* aria-label menyebut barisnya, agar pembaca layar tidak hanya mendengar "Hapus" */}
                <button type="button" onClick={() => handleDelete(b)} aria-label={`Hapus booking ${b.room} ${b.start_at}`}>
                  Hapus
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
