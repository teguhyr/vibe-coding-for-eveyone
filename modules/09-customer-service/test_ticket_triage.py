import csv

from ticket_triage import DEFAULT_DATA, OTHER, categorize, is_urgent, triage


def test_category_with_most_keyword_hits_wins():
    assert categorize("Refund my invoice, the courier was fine") == "billing"


def test_matching_ignores_case():
    assert categorize("PASSWORD RESET") == "account"


def test_whole_words_only():
    assert categorize("Please translate this page") == OTHER  # "late" inside "translate"


def test_multi_word_keyword():
    assert categorize("The scanner is not working") == "technical"


def test_tie_goes_to_first_listed_category():
    assert categorize("The payment page is not working") == "billing"


def test_no_keywords_is_other():
    assert categorize("Do you open on Sundays?") == OTHER


def test_urgency_detection():
    assert is_urgent("Need this ASAP")
    assert not is_urgent("No rush")


def test_sample_data():
    with DEFAULT_DATA.open(newline="", encoding="utf-8") as f:
        results = {t.ticket_id: (t.category, t.urgent) for t in triage(list(csv.DictReader(f)))}
    assert results == {
        "T-001": ("billing", True),
        "T-002": ("delivery", False),
        "T-003": ("technical", False),
        "T-004": ("account", False),
        "T-005": (OTHER, False),
        "T-006": ("delivery", True),
        "T-007": ("billing", False),
    }
