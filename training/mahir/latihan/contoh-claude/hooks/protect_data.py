"""Contoh hook PreToolUse (Modul 5): tolak Edit/Write ke file data asli.

Claude Code mengirim detail pemanggilan alat sebagai JSON lewat stdin.
Exit code 2 = blokir pemanggilan itu; pesan di stderr dikirim balik ke Claude sebagai alasan.
"""

import json
import sys
from pathlib import PurePath

PROTECTED_DIRS = {"private", "data_asli"}
PROTECTED_NAMES = {".env"}
PROTECTED_SUFFIXES = {".xlsx", ".xls", ".db"}


def is_protected(file_path: str) -> bool:
    path = PurePath(file_path)
    in_protected_dir = bool(PROTECTED_DIRS & set(path.parts))
    return in_protected_dir or path.name in PROTECTED_NAMES or path.suffix in PROTECTED_SUFFIXES


def main() -> int:
    event = json.load(sys.stdin)
    file_path = event.get("tool_input", {}).get("file_path", "")
    if file_path and is_protected(file_path):
        print(
            f"Diblokir: {file_path} adalah data asli/rahasia. Gunakan data sintetis.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
