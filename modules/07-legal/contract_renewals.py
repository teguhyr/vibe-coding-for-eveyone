"""Legal: contract renewal and notice deadline tracker.

Many contracts require written notice a number of days *before* they end if you
want to cancel or renegotiate. Miss that deadline and an auto-renewing contract
renews for another term. This tool lists contracts that need action soon.

This is a tracking aid, not legal advice. Always check the contract wording.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "contracts.csv"
DEFAULT_WINDOW_DAYS = 60

EXPIRED = "EXPIRED"
NOTICE_PASSED = "NOTICE PERIOD PASSED"
ACT_NOW = "ACT NOW"
OK = "OK"


@dataclass(frozen=True)
class Contract:
    contract_id: str
    counterparty: str
    contract_type: str
    end_date: date
    notice_days: int
    auto_renew: bool

    @property
    def notice_deadline(self) -> date:
        return self.end_date - timedelta(days=self.notice_days)


def contract_status(contract: Contract, today: date, window_days: int = DEFAULT_WINDOW_DAYS) -> str:
    if contract.end_date < today:
        return EXPIRED
    if contract.notice_deadline < today:
        return NOTICE_PASSED
    if contract.notice_deadline <= today + timedelta(days=window_days):
        return ACT_NOW
    return OK


def contracts_needing_attention(
    contracts: list[Contract], today: date, window_days: int = DEFAULT_WINDOW_DAYS
) -> list[tuple[Contract, str]]:
    flagged = [(c, contract_status(c, today, window_days)) for c in contracts]
    flagged = [(c, s) for c, s in flagged if s != OK]
    return sorted(flagged, key=lambda pair: pair[0].notice_deadline)


def parse_yes_no(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"yes", "y", "true"}:
        return True
    if normalized in {"no", "n", "false"}:
        return False
    raise ValueError(f"Expected yes/no, got {value!r}")


def load_contracts(path: Path) -> list[Contract]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            Contract(
                r["contract_id"],
                r["counterparty"],
                r["contract_type"],
                date.fromisoformat(r["end_date"]),
                int(r["notice_days"]),
                parse_yes_no(r["auto_renew"]),
            )
            for r in csv.DictReader(f)
        ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Contract renewal and notice deadline tracker.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    parser.add_argument("--window", type=int, default=DEFAULT_WINDOW_DAYS)
    args = parser.parse_args()

    flagged = contracts_needing_attention(load_contracts(args.csv_file), args.today, args.window)
    print(f"Contracts needing attention as of {args.today} (window: {args.window} days)")
    if not flagged:
        print("Nothing due.")
        return
    print(f"{'ID':<8} {'Counterparty':<25} {'Ends':<10}  {'Notice by':<10}  {'Auto':<4}  Status")
    for c, status in flagged:
        auto = "yes" if c.auto_renew else "no"
        print(
            f"{c.contract_id:<8} {c.counterparty:<25} {c.end_date}  {c.notice_deadline}  "
            f"{auto:<4}  {status}"
        )


if __name__ == "__main__":
    main()
