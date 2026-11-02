from inventory_reorder import DEFAULT_DATA, Item, items_to_reorder, load_items


def make_item(sku: str, on_hand: int, usage: float = 2.0, lead: int = 5, safety: int = 10) -> Item:
    return Item(sku, sku, on_hand, usage, lead, safety)


def test_reorder_point_is_usage_times_lead_time_plus_safety_stock():
    assert make_item("A", on_hand=0).reorder_point == 20  # 2 * 5 + 10


def test_item_exactly_at_reorder_point_is_due():
    assert items_to_reorder([make_item("A", on_hand=20)]) == [make_item("A", on_hand=20)]


def test_item_above_reorder_point_is_not_due():
    assert items_to_reorder([make_item("A", on_hand=21)]) == []


def test_most_urgent_item_comes_first():
    slow = make_item("SLOW", on_hand=10, usage=1)  # 10 days of cover
    fast = make_item("FAST", on_hand=10, usage=5)  # 2 days of cover
    assert [i.sku for i in items_to_reorder([slow, fast])] == ["FAST", "SLOW"]


def test_zero_usage_does_not_divide_by_zero():
    assert make_item("A", on_hand=5, usage=0).days_of_cover == float("inf")


def test_sample_data():
    due = items_to_reorder(load_items(DEFAULT_DATA))
    assert [i.sku for i in due] == ["SKU-006", "SKU-004", "SKU-002"]
