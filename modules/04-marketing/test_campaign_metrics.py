import pytest
from campaign_metrics import DEFAULT_DATA, Campaign, load_campaigns, needs_review, rank_by_roas


def campaign(name="C", spend=100.0, impressions=1000, clicks=50, conversions=5, revenue=400.0):
    return Campaign(name, "Test", spend, impressions, clicks, conversions, revenue)


def test_metric_formulas():
    c = campaign()
    assert c.ctr == pytest.approx(0.05)
    assert c.cpc == pytest.approx(2.0)
    assert c.cpa == pytest.approx(20.0)
    assert c.roas == pytest.approx(4.0)


def test_zero_denominators_give_none_instead_of_crashing():
    c = campaign(spend=0, impressions=0, clicks=0, conversions=0, revenue=0)
    assert (c.ctr, c.cpc, c.cpa, c.roas) == (None, None, None, None)


def test_ranking_puts_best_roas_first_and_unknown_last():
    low, high, unknown = (
        campaign("LOW", revenue=50),
        campaign("HIGH", revenue=900),
        campaign("NA", spend=0),
    )
    assert [c.name for c in rank_by_roas([unknown, low, high])] == ["HIGH", "LOW", "NA"]


def test_needs_review_below_target_only():
    assert needs_review(campaign(revenue=150))  # ROAS 1.5
    assert not needs_review(campaign(revenue=200))  # ROAS 2.0 meets target
    assert not needs_review(campaign(spend=0))


def test_sample_data():
    ranked = rank_by_roas(load_campaigns(DEFAULT_DATA))
    assert [c.name for c in ranked][:3] == ["Email Newsletter", "Search Brand", "Ramadan Promo"]
    assert [c.name for c in ranked if needs_review(c)] == [
        "Display Retarget",
        "Influencer Trial",
        "City Billboard",
    ]
