# Modul 6: Integrasi Claude API ke Aplikasi Anda

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 6](../03-mahir.md#langkah-6-integrasi-claude-api-ke-aplikasi-anda) |
| **Sesi** | Sesi 6 |
| **Durasi** | 110 menit |
| **Prasyarat** | Modul 4 (rahasia & data pribadi); Level 2 Modul 2 (pytest) |
| **File latihan** | [`latihan/klasifikasi/hybrid_triage.py`](latihan/klasifikasi/hybrid_triage.py), [`latihan/klasifikasi/test_hybrid_triage.py`](latihan/klasifikasi/test_hybrid_triage.py), [`modules/09-customer-service/`](../../modules/09-customer-service/) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Menentukan kapan AI **di dalam** aplikasi bermanfaat, dan kapan aturan biasa sudah cukup.
2. Memanggil Claude API dengan SDK resmi: model, instruksi sistem, pesan, *effort*, dan *fallback*.
3. **Memvalidasi** output AI dan menangani penolakan (`stop_reason == "refusal"`).
4. Menguji kode yang memanggil AI dengan **klien palsu**: cepat, gratis, tanpa internet.
5. Mengelola **API key**, **biaya**, dan **data pribadi** sesuai kebijakan perusahaan dan UU PDP.

---

## 📖 Materi

### A. Dua cara memakai AI

| | AI untuk **menulis** kode (Level 1–3) | AI **di dalam** aplikasi (modul ini) |
|---|---|---|
| Siapa yang memakai | Anda, saat membangun | Aplikasi, setiap kali berjalan |
| Contoh | Claude Code membuat `app.py` | Aplikasi mengirim pesan pelanggan ke Claude untuk dikategorikan |
| Biaya | Langganan/akun Anda | **Per pemakaian** (per token) |
| Risiko utama | Kode salah | Output tidak terduga, biaya, **data pelanggan keluar perusahaan** |

### B. Pola hibrida

Aturan kata kunci di [`ticket_triage.py`](../../modules/09-customer-service/ticket_triage.py) cepat, gratis, dan mudah dijelaskan, tetapi pesan dengan kata-kata tak terduga (atau dalam Bahasa Indonesia) jatuh ke `other`.

```
Pesan masuk → Aturan kata kunci → cocok?  ── ya ──▶ kategori (cepat, gratis)
                                     │
                                    tidak
                                     ▼
                   Samarkan data pribadi → Claude API → validasi → kategori
```

Dengan data contoh modul 09, **6 dari 7 pesan** sudah tertangani aturan. Hanya 1 yang dikirim ke AI.

### C. Anatomi permintaan

Dari [`hybrid_triage.py`](latihan/klasifikasi/hybrid_triage.py):

```python
response = client.beta.messages.create(
    model=MODEL,  # "claude-opus-5-5"
    max_tokens=1024,
    output_config={"effort": "low"},  # klasifikasi sederhana: effort rendah cukup
    betas=["server-side-fallback-2026-07-01"],
    fallbacks="default",  # jika model menolak, API mencoba model cadangan
    system=SYSTEM_PROMPT,
    messages=[{"role": "user", "content": redact(message)}],
)
```

| Parameter | Arti |
|-----------|------|
| `model` | Model yang dipakai. Tulis ID-nya persis; jangan menebak |
| `max_tokens` | Batas panjang jawaban (termasuk "berpikir" model). Terlalu kecil → jawaban terpotong |
| `output_config={"effort": "low"}` | Seberapa dalam model berpikir. Tugas sederhana → `low`: lebih cepat dan hemat |
| `fallbacks="default"` + `betas=[...]` | Jika permintaan ditolak oleh pengaman model, API otomatis mencoba model cadangan |
| `system` | Instruksi tetap: peran, aturan, format jawaban |
| `messages` | Isi yang diproses: di sini, pesan pelanggan yang sudah disamarkan |

### D. Jangan percaya output mentah

```python
if response.stop_reason == "refusal":
    return OTHER
text = next((block.text for block in response.content if block.type == "text"), "")
answer = text.strip().lower().rstrip(".")
return answer if answer in CATEGORIES else OTHER
```

- **`stop_reason`** diperiksa **sebelum** membaca isi. `"refusal"` berarti permintaan ditolak; aplikasi tetap berjalan dengan `other`.
- `response.content` adalah **daftar blok**. Ambil blok bertipe `"text"`.
- Jawaban yang tidak ada di daftar kategori, misalnya *"Kategori: pengiriman, karena..."*, menjadi `other`. Program **tidak pernah** memakai teks AI secara langsung untuk mengambil keputusan.

### E. Uji tanpa memanggil API

`classify_with_claude(message, client)` menerima `client` sebagai **parameter** (*dependency injection*). Di tes, kita memberikan klien palsu:

```python
class FakeClient:
    """Meniru client.beta.messages.create dan mencatat setiap permintaan."""

    def __init__(self, reply="delivery", stop_reason="end_turn"):
        self.requests = []
        self.reply, self.stop_reason = reply, stop_reason
        self.beta = SimpleNamespace(messages=SimpleNamespace(create=self._create))
```

Keuntungannya: tes **cepat, gratis, tanpa internet, tanpa API key**, dan bisa mensimulasikan kasus sulit (jawaban aneh, penolakan) yang jarang terjadi sungguhan. Tes juga memeriksa **apa yang dikirim**: model, effort, dan bahwa data pribadi sudah disamarkan.

### F. API key, biaya, dan data

| Aspek | Aturan |
|-------|--------|
| **API key** | Rahasia. Simpan di environment variable `ANTHROPIC_API_KEY` di **server**. Jangan di kode, frontend, atau Git |
| **Biaya** | Dihitung per token masuk dan keluar; harga berbeda per model (lihat https://www.anthropic.com/pricing). Ukur dari `response.usage` pada sampel nyata sebelum memperkirakan biaya bulanan. Pola hibrida langsung memangkas jumlah panggilan |
| **Data pribadi** | Pesan diproses di server Anthropic. Ikuti kebijakan perusahaan dan UU PDP: kirim **seminimal mungkin**, samarkan identitas (`redact()` mengganti email dan nomor telepon dengan `[EMAIL]`/`[PHONE]`), dan jangan kirim data spesifik (kesehatan, keuangan pribadi) tanpa dasar hukum |
| **Ketersediaan** | API bisa lambat atau gagal. SDK otomatis mengulang beberapa kali; aplikasi harus tetap berfungsi (misalnya kembali ke `other`) jika AI tidak tersedia |

> ⚠️ `redact()` hanya menyamarkan pola yang **mudah dikenali** (email, nomor telepon). Nama, alamat, dan nomor identitas dalam teks bebas tidak tertangkap. Ini mengurangi risiko, tetapi **tidak** menggantikan persetujuan dan kebijakan pemrosesan data.

---

## 🛠️ Praktik Terpandu

**1. Jalankan tes, tanpa API key.** Dari folder utama repositori:

```bash
pytest training/mahir/latihan/klasifikasi -v
```

Hasilnya `9 passed`. Baca nama setiap tes. Tidak ada satu pun yang memanggil API sungguhan.

**2. Baca alurnya.** Di `hybrid_triage.py`, ikuti satu pesan dari `hybrid_category` → `keyword_categorize` → (jika `other`) `classify_with_claude` → `redact` → `parse_category`.

**3. (Opsional, berbayar) Panggil API sungguhan.** Hanya jika perusahaan Anda menyediakan API key untuk latihan:

```bash
pip install anthropic
```

```bash
export ANTHROPIC_API_KEY="isi-dengan-kunci-dari-perusahaan"
```

```bash
python training/mahir/latihan/klasifikasi/hybrid_triage.py
```

Di Windows PowerShell: `$env:ANTHROPIC_API_KEY = "..."`. Format hasilnya:

```
T-001   billing    (rules)
T-002   delivery   (rules)
T-003   technical  (rules)
T-004   account    (rules)
T-005   other      (ai)
T-006   delivery   (rules)
T-007   billing    (rules)
```

Enam baris `(rules)` selalu sama. Kategori baris `(ai)` (`T-005: Do you have a store in Surabaya?`) ditentukan oleh model; `other` adalah jawaban yang masuk akal karena pertanyaan lokasi toko tidak masuk 4 kategori lainnya.

**4. Gabungkan ke aplikasi.** Diskusikan: jika triase ini dipakai di backend aplikasi (Modul 2), di mana `client` dibuat? Jawaban: **sekali** saat aplikasi mulai (di `create_app`), dari environment variable server, lalu dipakai ulang.

---

## 🏋️ Latihan

### ⭐ Latihan 6.1: Perlu AI atau tidak?

Untuk setiap kebutuhan, tentukan: aturan biasa, AI, atau hibrida.
1. Menghitung PPN 11% dari total invoice
2. Mengelompokkan 500 masukan karyawan (teks bebas) per tema
3. Menandai tiket yang berisi kata "urgent"
4. Meringkas isi kontrak 40 halaman untuk tim legal
5. Mengkategorikan pesan pelanggan, sebagian besar dengan pola kata yang mirip

### ⭐⭐ Latihan 6.2: Kata kunci Bahasa Indonesia

Pesan *"Paket saya belum sampai"* selalu jatuh ke AI karena aturan modul 09 hanya mengenal kata Bahasa Inggris. Tambahkan kata kunci Bahasa Indonesia (misalnya `paket`, `pengiriman`, `tagihan`, `kata sandi`) **di salinan** `ticket_triage.py` Anda. Berapa pesan yang masih dikirim ke AI? Mengapa ini penghematan?

### ⭐⭐ Latihan 6.3: Tes untuk jawaban kosong

Tulis tes: jika AI membalas teks kosong, hasilnya `other`. Tulis juga tes: jika AI membalas `"Delivery"` (huruf besar), hasilnya `delivery`.

### ⭐⭐⭐ Latihan 6.4: Saat API gagal

Jika jaringan putus, SDK menimbulkan error setelah mencoba ulang. Ubah `hybrid_category` agar error koneksi atau *rate limit* menghasilkan `("other", "ai-error")`, bukan menghentikan seluruh program. Tulis tesnya dengan klien palsu yang menimbulkan error. Error jenis apa yang **tidak** boleh disembunyikan dengan cara ini?

---

## 📝 Kuis

1. Mengapa `client` dijadikan parameter, bukan dibuat di dalam `classify_with_claude`?
2. Apa yang dilakukan program jika `stop_reason == "refusal"`?
3. Mengapa jawaban AI dicocokkan dengan `CATEGORIES` sebelum dipakai?
4. Sebutkan 2 cara pola hibrida menghemat biaya dan melindungi data.
5. Di mana API key disimpan untuk aplikasi web? Di mana **tidak boleh**?

---

## 📌 Ringkasan

- AI di dalam aplikasi = **biaya per pemakaian + data keluar perusahaan**. Pakai **hibrida**: aturan dulu, AI untuk sisanya.
- Periksa `stop_reason`, ambil blok `text`, **validasi** terhadap daftar yang sah.
- Injeksikan `client`; uji dengan klien palsu. Tes juga memeriksa **apa yang dikirim**.
- API key di environment server; samarkan data pribadi; ukur biaya dari `response.usage`.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 6.1**
1. **Aturan biasa**: rumus pasti; AI hanya menambah biaya dan risiko salah hitung.
2. **AI** (atau hibrida dengan kata kunci untuk tema yang jelas): teks bebas yang beragam.
3. **Aturan biasa**: sudah ada di `is_urgent()` modul 09.
4. **AI**, dengan review manusia. Isi kontrak rahasia: pastikan kebijakan perusahaan mengizinkan.
5. **Hibrida**: aturan untuk pola umum, AI untuk sisanya.

**Latihan 6.2:** dengan kata kunci Bahasa Indonesia, pesan seperti *"Paket saya belum sampai"* tertangani aturan (`delivery`), sehingga tidak ada biaya API, tidak ada data yang keluar, dan hasilnya selalu sama. Dengan data contoh modul 09, tetap hanya `T-005` yang ke AI. Jangan ubah `modules/09-customer-service/` di `main`, karena materi lain mengutip output-nya (efek domino, Level 2 Modul 4).

**Latihan 6.3**
```python
def test_empty_answer_becomes_other():
    client = FakeClient(reply="")
    assert hybrid_category("...", always_other, client) == (OTHER, "ai")


def test_uppercase_answer_is_accepted():
    client = FakeClient(reply="Delivery")
    assert hybrid_category("...", always_other, client) == ("delivery", "ai")
```

**Latihan 6.4 (contoh)**
```python
import anthropic

...
    try:
        return classify_with_claude(message, client), "ai"
    except (anthropic.APIConnectionError, anthropic.RateLimitError, anthropic.InternalServerError):
        return OTHER, "ai-error"
```
Untuk mengujinya tanpa jaringan, buat klien palsu yang `create`-nya menimbulkan error tiruan, dan jadikan daftar error yang ditangkap sebagai parameter atau konstanta agar tes tidak bergantung pada SDK. Error yang **tidak** boleh disembunyikan: `AuthenticationError` (API key salah), `PermissionDeniedError`, dan `BadRequestError` (permintaan salah bentuk). Itu kesalahan konfigurasi atau kode yang harus segera diketahui, bukan gangguan sementara. Catat juga setiap `ai-error` di log agar bisa dipantau.

**Kuis**
1. Agar tes bisa memberikan klien palsu: cepat, gratis, tanpa internet dan API key, serta bisa mensimulasikan kasus sulit.
2. Mengembalikan `other`, sehingga aplikasi tetap berjalan.
3. Model bisa menjawab dengan kalimat, huruf besar, atau kategori yang tidak ada. Program hanya boleh memakai nilai yang sah.
4. (a) Aturan menangani sebagian besar pesan tanpa biaya API; (b) pesan yang tertangani aturan tidak pernah keluar perusahaan; yang dikirim pun disamarkan dulu.
5. Di environment variable server (misalnya `ANTHROPIC_API_KEY`). **Tidak boleh** di kode, frontend, file yang di-commit, atau pesan chat.

</details>

---

← [Modul 5](modul-05-claude-code-lanjutan.md) | **Berikutnya: [Modul 7: Otomatisasi Kualitas dengan CI/CD →](modul-07-ci-cd.md)**
