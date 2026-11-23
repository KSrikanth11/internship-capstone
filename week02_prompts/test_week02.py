import pytest

from week02_prompts.prompts import CATEGORIES, TICKET_PROMPT, parse_json_reply, render_prompt, run_eval


def test_render_fills_placeholders():
    text = render_prompt(TICKET_PROMPT, categories=CATEGORIES, ticket="UPI payment failed")
    assert "UPI payment failed" in text
    assert '{"category"' in text  # escaped braces survive


def test_render_missing_value():
    with pytest.raises(KeyError):
        render_prompt(TICKET_PROMPT, categories=CATEGORIES)


@pytest.mark.parametrize("reply", [
    '{"category": "payment", "urgent": true}',
    '```json\n{"category": "payment", "urgent": true}\n```',
    'Sure! Here is the JSON: {"category": "payment", "urgent": true} Hope it helps.',
])
def test_parse_json_variants(reply):
    assert parse_json_reply(reply) == {"category": "payment", "urgent": True}


@pytest.mark.parametrize("reply", ["no json here", '{"category": "payment"}', '{"category": "payment", "urgent": }'])
def test_parse_json_errors(reply):
    with pytest.raises(ValueError):
        parse_json_reply(reply)


def test_run_eval_counts_and_handles_errors():
    cases = [
        {"ticket": "Refund not received", "expected": "payment"},
        {"ticket": "Video does not load", "expected": "technical"},
        {"ticket": "crash me", "expected": "other"},
    ]

    def classify(ticket):
        if ticket == "crash me":
            raise ValueError("bad JSON")
        return {"category": "payment", "urgent": False}

    report = run_eval(cases, classify)
    assert report["total"] == 3 and report["correct"] == 1
    assert report["accuracy"] == pytest.approx(1 / 3)
    assert report["failures"] == ["Video does not load", "crash me"]
    assert run_eval([], classify)["accuracy"] == 0.0
