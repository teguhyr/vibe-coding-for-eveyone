"""Latihan Modul 6: triase pesan pelanggan secara hibrida.

1. Coba aturan kata kunci dari modules/09-customer-service (cepat, gratis, mudah dijelaskan).
2. Hanya jika hasilnya "other", tanya Claude API.
3. Jawaban AI selalu divalidasi: di luar daftar kategori -> "other".
Sebelum dikirim ke API, email dan nomor telepon disamarkan (UU PDP: minimisasi data).
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]
KEYWORD_MODULE = REPO_ROOT / "modules" / "09-customer-service" / "ticket_triage.py"
DEFAULT_DATA = KEYWORD_MODULE.parent / "data" / "messages.csv"

CATEGORIES = ("billing", "delivery", "technical", "account", "other")
OTHER = "other"
MODEL = "claude-opus-5-5"
SYSTEM_PROMPT = (
    "You classify customer service messages for an Indonesian company. "
    "Messages may be in English or Bahasa Indonesia. "
    f"Reply with exactly one word from this list: {', '.join(CATEGORIES)}."
)

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
# Nomor Indonesia: 08xx atau +62/62, boleh dipisah spasi atau tanda hubung.
PHONE = re.compile(r"(?:\+62|62|0)[\s-]?8[\d\s-]{7,13}\d")


def redact(message: str) -> str:
    """Samarkan data pribadi yang mudah dikenali sebelum teks keluar dari perusahaan."""
    return PHONE.sub("[PHONE]", EMAIL.sub("[EMAIL]", message))


def parse_category(text: str) -> str:
    answer = text.strip().lower().rstrip(".")
    return answer if answer in CATEGORIES else OTHER  # jangan percaya output mentah


def classify_with_claude(message: str, client: Any) -> str:
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=1024,
        output_config={"effort": "low"},  # klasifikasi sederhana: effort rendah cukup
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",  # jika model menolak, API mencoba model cadangan
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": redact(message)}],
    )
    if response.stop_reason == "refusal":
        return OTHER
    text = next((block.text for block in response.content if block.type == "text"), "")
    return parse_category(text)


def hybrid_category(
    message: str, keyword_categorize: Callable[[str], str], client: Any
) -> tuple[str, str]:
    """Return (category, source). source is "rules" or "ai"."""
    category = keyword_categorize(message)
    if category != OTHER:
        return category, "rules"
    return classify_with_claude(message, client), "ai"


def load_keyword_categorize() -> Callable[[str], str]:
    # Modul-modul di repositori ini sengaja tidak saling impor; muat file-nya langsung.
    name = "module09_ticket_triage"  # nama unik agar tidak bentrok dengan impor lain
    spec = importlib.util.spec_from_file_location(name, KEYWORD_MODULE)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {KEYWORD_MODULE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module  # @dataclass membutuhkan modulnya terdaftar di sys.modules
    spec.loader.exec_module(module)
    return module.categorize


def main() -> None:
    parser = argparse.ArgumentParser(description="Hybrid customer message triage.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    import anthropic  # diimpor di sini agar tes tidak membutuhkan SDK maupun API key

    client = anthropic.Anthropic()  # membaca ANTHROPIC_API_KEY dari environment
    categorize = load_keyword_categorize()
    with args.csv_file.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            category, source = hybrid_category(row["message"], categorize, client)
            print(f"{row['ticket_id']:<7} {category:<10} ({source})")


if __name__ == "__main__":
    main()
