# Agar tes di folder kunci/ bisa mengimpor expense_claims.py dari folder latihan/ di atasnya.
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
