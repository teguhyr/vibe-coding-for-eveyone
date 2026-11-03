# Contoh konfigurasi Claude Code (Modul 5)

Folder ini **sengaja tidak bernama `.claude/`**, agar contoh di sini tidak aktif di repositori pelatihan.
Untuk memakainya di proyek Anda sendiri, salin isinya ke folder `.claude/` di akar proyek:

```
.claude/
├── commands/cek-kualitas.md          → /cek-kualitas
├── skills/laporan-bulanan/SKILL.md   → dipakai Claude saat relevan, atau /laporan-bulanan
├── agents/reviewer-keamanan.md       → subagent reviewer keamanan
├── hooks/protect_data.py             → contoh hook PreToolUse (Latihan 5.4)
└── settings.json                     → permissions + hook
```

Format fitur Claude Code berkembang cepat. Cocokkan dengan dokumentasi terbaru di https://code.claude.com/docs sebelum dipakai tim.
