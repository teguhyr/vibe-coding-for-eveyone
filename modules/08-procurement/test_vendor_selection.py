import pytest
from vendor_selection import (
    DEFAULT_DATA,
    Quote,
    group_by_item,
    load_quotes,
    normalize,
    score_quotes,
)


def quote(vendor: str, price: float, lead: int, quality: float) -> Quote:
    return Quote("Item", vendor, price, lead, quality)


def test_normalize_lower_is_better():
    assert normalize(100, [100, 200], higher_is_better=False) == 1.0
    assert normalize(200, [100, 200], higher_is_better=False) == 0.0
    assert normalize(150, [100, 200], higher_is_better=False) == 0.5


def test_normalize_all_equal_does_not_divide_by_zero():
    assert normalize(5, [5, 5], higher_is_better=True) == 1.0


def test_vendor_best_on_everything_scores_one():
    best, worst = quote("BEST", 100, 2, 5), quote("WORST", 200, 9, 3)
    ranked = score_quotes([worst, best])
    assert ranked[0] == (best, pytest.approx(1.0))
    assert ranked[1] == (worst, pytest.approx(0.0))


def test_weights_must_add_up_to_one():
    with pytest.raises(ValueError):
        score_quotes([quote("A", 1, 1, 1)], {"price": 0.5, "lead_time": 0.5, "quality": 0.5})


def test_sample_data():
    groups = group_by_item(load_quotes(DEFAULT_DATA))
    winners = {item: score_quotes(qs)[0] for item, qs in groups.items()}
    assert {item: q.vendor for item, (q, _) in winners.items()} == {
        "Office Chair": "Vendor B",
        "Laptop": "Vendor D",
        "Toner Cartridge": "Vendor B",
    }
    assert winners["Office Chair"][1] == pytest.approx(0.6)
