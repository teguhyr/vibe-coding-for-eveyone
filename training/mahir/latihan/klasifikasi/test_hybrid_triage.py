# Tes Modul 6 dengan klien palsu: cepat, gratis, tanpa internet, tanpa API key.
from types import SimpleNamespace

from hybrid_triage import (
    MODEL,
    OTHER,
    hybrid_category,
    load_keyword_categorize,
    parse_category,
    redact,
)


class FakeClient:
    """Meniru client.beta.messages.create dan mencatat setiap permintaan."""

    def __init__(self, reply="delivery", stop_reason="end_turn"):
        self.requests = []
        self.reply, self.stop_reason = reply, stop_reason
        self.beta = SimpleNamespace(messages=SimpleNamespace(create=self._create))

    def _create(self, **kwargs):
        self.requests.append(kwargs)
        content = [SimpleNamespace(type="text", text=self.reply)]
        return SimpleNamespace(stop_reason=self.stop_reason, content=content)


def always_other(_message: str) -> str:
    return OTHER


def test_rules_first_so_no_api_call():
    client = FakeClient()
    assert hybrid_category("refund please", lambda _m: "billing", client) == ("billing", "rules")
    assert client.requests == []


def test_ai_only_when_rules_say_other():
    client = FakeClient(reply="delivery")
    assert hybrid_category("Paket saya belum sampai", always_other, client) == ("delivery", "ai")
    assert len(client.requests) == 1


def test_request_uses_expected_model_and_settings():
    client = FakeClient()
    hybrid_category("Paket saya belum sampai", always_other, client)
    request = client.requests[0]
    assert request["model"] == MODEL
    assert request["output_config"] == {"effort": "low"}
    assert request["fallbacks"] == "default"


def test_unexpected_ai_answer_becomes_other():
    client = FakeClient(reply="Kategori: pengiriman, karena paketnya terlambat")
    assert hybrid_category("Paket saya belum sampai", always_other, client) == (OTHER, "ai")


def test_refusal_becomes_other():
    client = FakeClient(reply="", stop_reason="refusal")
    assert hybrid_category("...", always_other, client) == (OTHER, "ai")


def test_parse_category_tolerates_case_and_period():
    assert parse_category(" Billing.\n") == "billing"


def test_personal_data_is_redacted_before_sending():
    client = FakeClient()
    message = "Hubungi saya di budi@contoh.co.id atau 0812-3456-7890, paket belum sampai"
    hybrid_category(message, always_other, client)
    sent = client.requests[0]["messages"][0]["content"]
    assert "budi@contoh.co.id" not in sent and "0812-3456-7890" not in sent
    assert sent == "Hubungi saya di [EMAIL] atau [PHONE], paket belum sampai"


def test_redact_international_format():
    assert redact("WA +62 812 3456 7890 ya") == "WA [PHONE] ya"


def test_keyword_rules_from_module_09_are_used():
    categorize = load_keyword_categorize()
    assert categorize("I was charged twice on my last invoice") == "billing"
    assert categorize("Paket saya belum sampai") == OTHER  # Bahasa Indonesia: aturan tidak kenal
