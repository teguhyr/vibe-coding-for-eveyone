# Modul 5: Fitur Lanjutan Claude Code

| | |
|---|---|
| **Langkah di rencana** | [Level 3, Langkah 5](../03-mahir.md#langkah-5-fitur-lanjutan-claude-code) |
| **Sesi** | Sesi 5 |
| **Durasi** | 110 menit |
| **Prasyarat** | Level 2 Modul 7 (`CLAUDE.md`) dan Modul 9 (data aman) |
| **File latihan** | [`latihan/contoh-claude/`](latihan/contoh-claude/) (command, skill, subagent, settings, hook) |

## 🎯 Tujuan Pembelajaran

Setelah modul ini, peserta mampu:
1. Memilih fitur yang tepat: **custom command**, **skill**, **subagent**, **hooks**, **permissions**, **MCP**, atau **mode headless**.
2. Membuat custom command dan skill yang bisa dibagikan ke tim lewat Git.
3. Membuat subagent dengan **alat terbatas**, misalnya reviewer yang hanya boleh membaca.
4. Menulis aturan izin (`allow`/`deny`) dan hook yang **menegakkan** aturan, bukan sekadar mengingatkan.
5. Menjalankan Claude Code dari skrip dengan `claude -p`.

> 💡 Fitur Claude Code berkembang cepat. Format di modul ini sesuai dengan rencana training; sebelum dipakai tim, cocokkan dengan dokumentasi terbaru di https://code.claude.com/docs.

---

## 📖 Materi

### A. Peta fitur

| Fitur | Analogi | Lokasi | Kapan dipakai |
|-------|---------|--------|---------------|
| **`CLAUDE.md`** | SOP proyek | Akar proyek | Selalu dibaca. Fakta dan aturan proyek (Level 2) |
| **Custom command** | Tombol pintas | `.claude/commands/<nama>.md` | Prompt yang **Anda** panggil berulang kali: `/cek-kualitas` |
| **Skill** | Buku resep khusus | `.claude/skills/<nama>/SKILL.md` | Prosedur yang Claude pakai **saat relevan**, berdasarkan `description` |
| **Subagent** | Spesialis yang dipanggil untuk satu tugas | `.claude/agents/<nama>.md` | Tugas terfokus dengan konteks dan alat sendiri: reviewer keamanan |
| **Permissions** | Daftar izin akses gedung | `.claude/settings.json` | Perintah yang boleh tanpa bertanya, dan yang **dilarang** |
| **Hooks** | Satpam otomatis | `.claude/settings.json` | "**Setiap kali** X terjadi, jalankan Y", dijamin, tidak bergantung ingatan AI |
| **MCP server** | Kabel ke sistem lain | `claude mcp add ...` | Menghubungkan Claude ke database, Jira, Google Drive, dan lainnya |
| **Mode headless** | Karyawan yang bekerja dari jadwal | `claude -p "..."` | Otomatisasi, skrip, dan CI |

**Prinsip memilih:**
- Ingin Claude **tahu** sesuatu? → `CLAUDE.md`.
- Ingin **Anda** bisa memanggil prompt dengan cepat? → custom command.
- Ingin Claude **memakai prosedur** saat situasinya cocok? → skill.
- Ingin sesuatu **pasti terjadi** atau **pasti dicegah**? → hooks dan permissions. Instruksi di `CLAUDE.md` bisa terlewat; hook tidak.

### B. Custom command dan skill

[`commands/cek-kualitas.md`](latihan/contoh-claude/commands/cek-kualitas.md): isinya adalah prompt biasa. `$ARGUMENTS` diganti dengan teks yang Anda ketik setelah nama perintah: `/cek-kualitas modul keuangan`.

[`skills/laporan-bulanan/SKILL.md`](latihan/contoh-claude/skills/laporan-bulanan/SKILL.md): bagian di antara `---` (*frontmatter*) berisi `name` dan `description`. **`description` adalah bagian terpenting**: Claude membacanya untuk memutuskan kapan skill dipakai. Tulis **kapan** skill dipakai ("Gunakan saat pengguna meminta laporan bulanan..."), bukan hanya apa isinya.

> 💡 Di versi Claude Code terbaru, custom command dan skill makin menyatu: keduanya bisa dipanggil sebagai `/nama`. Bedanya, skill juga bisa dipakai Claude secara otomatis saat relevan, dan bisa menyertakan file pendukung di foldernya.

### C. Subagent

[`agents/reviewer-keamanan.md`](latihan/contoh-claude/agents/reviewer-keamanan.md) memakai `tools: Read, Grep, Glob`: reviewer ini **hanya bisa membaca**, tidak bisa mengubah file atau menjalankan perintah. Prinsip **hak akses minimum** (*least privilege*) yang sama dengan Modul 4.

Panggil dengan bahasa biasa: *"Pakai subagent reviewer-keamanan untuk meninjau perubahan di branch ini."* Subagent bekerja di konteksnya sendiri, lalu mengembalikan ringkasan, sehingga percakapan utama tetap bersih.

### D. Permissions

[`settings.json`](latihan/contoh-claude/settings.json):

```json
"permissions": {
  "allow": ["Bash(pytest:*)", "Bash(ruff check:*)", "Bash(ruff format:*)"],
  "deny": ["Read(./private/**)", "Read(./.env)"]
}
```

- `allow`: boleh dijalankan **tanpa bertanya**. Hanya untuk perintah yang aman dan sering.
- `deny`: **dilarang**, bahkan jika diminta.
- Selain itu: Claude bertanya dulu, seperti biasa.

> ⚠️ Jangan pernah `Bash(*)` di `allow`. Itu sama dengan memberi kunci semua ruangan, termasuk perintah yang menghapus file atau mengirim data keluar.

### E. Hooks

```json
"hooks": {
  "PostToolUse": [
    {
      "matcher": "Edit|Write",
      "hooks": [{ "type": "command", "command": "ruff format ." }]
    }
  ]
}
```

| Bagian | Arti |
|--------|------|
| `PostToolUse` | Kapan: **setelah** Claude memakai sebuah alat. Ada juga `PreToolUse` (**sebelum**, bisa memblokir) dan peristiwa lain |
| `matcher: "Edit\|Write"` | Hanya untuk alat Edit atau Write |
| `command` | Perintah terminal yang dijalankan |

Hook `PreToolUse` bisa **memblokir**: Claude Code mengirim detail pemanggilan alat sebagai JSON ke *stdin* perintah hook, dan jika perintah itu keluar dengan **exit code 2**, pemanggilan dibatalkan dan pesan di *stderr* dikirim ke Claude sebagai alasan. Contohnya [`hooks/protect_data.py`](latihan/contoh-claude/hooks/protect_data.py) menolak Edit/Write ke folder `private/`, file `.env`, `.xlsx`, `.xls`, dan `.db`.

### F. MCP dan mode headless

- **MCP server** menghubungkan Claude ke sistem lain. Contoh bentuk perintahnya: `claude mcp add <nama> -- <perintah server>`. Lihat daftar server yang terpasang dengan `claude mcp list`. **Hati-hati:** setiap server MCP membuka akses ke sistem dan datanya. Pasang hanya server resmi/tepercaya yang disetujui tim IT, dan pikirkan data apa yang bisa terbaca (UU PDP).
- **Mode headless** (`claude -p "..."`) menjalankan satu permintaan tanpa sesi interaktif, lalu mencetak hasilnya. Cocok untuk skrip terjadwal atau CI. Aturan izin di `settings.json` tetap berlaku; perintah yang tidak diizinkan tidak akan dijalankan.

---

## 🛠️ Praktik Terpandu

Kerjakan di proyek Anda sendiri (misalnya `~/proyek-reimburse` dari Level 2, atau `projects/ruang-rapat`). **Jangan** menyalin ke folder utama repositori pelatihan, karena repositori ini punya `CLAUDE.md` dan aturannya sendiri.

**1. Salin contoh konfigurasi** ke folder `.claude/` proyek Anda:

```bash
mkdir -p .claude
```

```bash
cp -r <repo-pelatihan>/training/mahir/latihan/contoh-claude/commands <repo-pelatihan>/training/mahir/latihan/contoh-claude/skills <repo-pelatihan>/training/mahir/latihan/contoh-claude/agents .claude/
```

```bash
cp <repo-pelatihan>/training/mahir/latihan/contoh-claude/settings.json .claude/
```

Ganti `<repo-pelatihan>` dengan lokasi repositori pelatihan Anda. Di Windows PowerShell, pakai `Copy-Item -Recurse`.

**2. Coba custom command.** Jalankan `claude`, lalu ketik:

```
/cek-kualitas fokus pada tes yang gagal
```

**3. Coba skill.** Jika proyek Anda bukan repositori pelatihan, ubah langkah 1 di `SKILL.md` ke laporan milik proyek Anda. Lalu tanya dengan bahasa biasa, **tanpa** menyebut nama skill: *"Tolong buatkan rekap anggaran bulan ini."* Apakah Claude memakai skill-nya?

**4. Coba subagent.**

```
Pakai subagent reviewer-keamanan untuk meninjau semua file Python di proyek ini.
```

Perhatikan: reviewer tidak mengubah file apa pun.

**5. Uji izin `deny`.** Buat `private/rahasia.csv` berisi satu baris palsu, lalu minta Claude membacanya. Claude harus menolak.

**6. Uji hook.** Edit sebuah file Python dengan bantuan Claude dan buat spasi berantakan. Setelah Claude menyimpan, hook menjalankan `ruff format .`, dan file otomatis rapi.

**7. Coba mode headless** di terminal biasa:

```bash
claude -p "Jalankan pytest dan ringkas hasilnya dalam 3 baris"
```

**8. Bagikan ke tim.** Commit `.claude/commands`, `.claude/skills`, `.claude/agents`, dan `.claude/settings.json`, agar semua anggota tim memakai SOP yang sama.

---

## 🏋️ Latihan

### ⭐ Latihan 5.1: Pilih fiturnya

Fitur apa yang paling tepat untuk setiap kebutuhan?
1. "Claude harus tahu bahwa tahun fiskal kami mulai 1 April."
2. "Saya sering mengetik prompt panjang yang sama untuk membuat catatan rilis."
3. "Kode **harus selalu** dirapikan setiap kali Claude mengubah file."
4. "Claude tidak boleh membaca folder `data_karyawan/`, apa pun alasannya."
5. "Setiap Senin pagi, ringkasan hasil tes dikirim otomatis."
6. "Saat ada yang meminta laporan rekonsiliasi, ikuti langkah-langkah baku tim akuntansi."

### ⭐⭐ Latihan 5.2: Command untuk pekerjaan Anda

Buat satu custom command untuk prompt yang paling sering Anda ketik ke Claude. Pakai `$ARGUMENTS`. Commit dan minta satu rekan mencobanya.

### ⭐⭐ Latihan 5.3: Perbaiki `description`

Skill dengan `description: Skill laporan.` jarang dipakai Claude. Tulis ulang agar Claude tahu **kapan** memakainya.

### ⭐⭐⭐ Latihan 5.4: Hook penjaga data

Pasang [`hooks/protect_data.py`](latihan/contoh-claude/hooks/protect_data.py) sebagai hook `PreToolUse` untuk `Edit|Write`. Uji dulu di terminal **tanpa** Claude, dengan mengirim JSON palsu ke stdin. Lalu uji lewat Claude: minta Claude membuat `private/coba.csv`.

---

## 📝 Kuis

1. Apa beda custom command dan skill?
2. Mengapa aturan "selalu rapikan kode" lebih baik dipasang sebagai hook daripada ditulis di `CLAUDE.md`?
3. Apa arti `tools: Read, Grep, Glob` pada subagent reviewer, dan mengapa itu baik?
4. Mengapa `Bash(*)` di daftar `allow` berbahaya?
5. Apa yang terjadi jika hook `PreToolUse` keluar dengan exit code 2?

---

## 📌 Ringkasan

- `CLAUDE.md` = yang Claude **tahu**; command = pintasan **Anda**; skill = prosedur yang Claude pakai **saat relevan**; subagent = **spesialis** dengan alat terbatas.
- Hooks dan permissions **menegakkan** aturan; instruksi teks hanya **meminta**.
- Izinkan seminimal mungkin; larang akses ke data rahasia; uji setiap aturan.
- Simpan konfigurasi tim di `.claude/` dan bagikan lewat Git.

---

<details>
<summary>🔑 <b>Kunci Jawaban</b></summary>

**Latihan 5.1**
1. `CLAUDE.md`
2. Custom command (misalnya `/catatan-rilis`)
3. Hook `PostToolUse` dengan matcher `Edit|Write`
4. Permission `deny`: `"Read(./data_karyawan/**)"`, ditambah hook `PreToolUse` untuk Edit/Write ke folder itu, dan `.gitignore`. Pertahanan berlapis.
5. Mode headless (`claude -p`) yang dijalankan penjadwal (cron, Task Scheduler, atau CI terjadwal)
6. Skill dengan `description` yang menyebut "rekonsiliasi"

**Latihan 5.2 (contoh)** `.claude/commands/catatan-rilis.md`:
```markdown
Buat catatan rilis dari commit sejak tag terakhir (git log <tag-terakhir>..HEAD).
Kelompokkan: Fitur baru, Perbaikan, Lainnya. Bahasa Indonesia, untuk pengguna non-teknis.
Jangan sebut nama file atau istilah teknis. Versi rilis: $ARGUMENTS
```

**Latihan 5.3 (contoh)**
```
description: Membuat laporan rekonsiliasi bank bulanan dari data/bank_statement.csv dan data/ledger.csv. Gunakan saat pengguna meminta rekonsiliasi, pencocokan bank vs buku besar, atau laporan selisih bank.
```

**Latihan 5.4:** tambahkan di `settings.json` (ganti jalur ke lokasi file hook Anda):

```json
"PreToolUse": [
  {
    "matcher": "Edit|Write",
    "hooks": [{ "type": "command", "command": "python .claude/hooks/protect_data.py" }]
  }
]
```

Uji tanpa Claude (macOS/Linux):

```bash
echo '{"tool_name": "Write", "tool_input": {"file_path": "private/coba.csv"}}' | python .claude/hooks/protect_data.py
```

```
Diblokir: private/coba.csv adalah data asli/rahasia. Gunakan data sintetis.
```

`echo $?` menampilkan `2`. Untuk `{"file_path": "data/contoh.csv"}`, tidak ada pesan dan exit code `0`. Skrip ini sudah diuji untuk folder `private/`, file `.env`, `.xlsx`, dan file biasa. Menguji hook di luar Claude dulu adalah kebiasaan yang baik: hook yang rusak bisa memblokir **semua** pekerjaan.

**Kuis**
1. Command dipanggil oleh **Anda** (`/nama`). Skill juga bisa dipakai Claude **otomatis** saat situasinya cocok dengan `description`, dan bisa membawa file pendukung.
2. Instruksi di `CLAUDE.md` bisa terlewat; hook **selalu** dijalankan oleh Claude Code setiap kali peristiwanya terjadi.
3. Subagent hanya boleh membaca dan mencari, tidak bisa mengubah file atau menjalankan perintah. Hak akses minimum mengurangi risiko jika ia salah langkah.
4. Claude boleh menjalankan **perintah terminal apa pun** tanpa bertanya, termasuk yang menghapus file atau mengirim data ke luar.
5. Pemanggilan alat itu **dibatalkan**, dan pesan di stderr dikirim ke Claude sebagai alasan penolakan.

</details>

---

← [Modul 4](modul-04-keamanan-owasp.md) | **Berikutnya: [Modul 6: Integrasi Claude API →](modul-06-claude-api.md)**
