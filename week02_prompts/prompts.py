"""Week 2: prompt templates, structured JSON output and an evaluation set.

Test it: pytest week02_prompts
Brief:   week02_prompts/README.md
"""
import json
from typing import Callable

TICKET_PROMPT = """You classify support tickets for an ed-tech company.
Return ONLY JSON: {{"category": one of {categories}, "urgent": true|false}}

Ticket: {ticket}"""

CATEGORIES = ["payment", "technical", "course-content", "other"]


def render_prompt(template: str, **values) -> str:
    """TODO: fill the template with values using str.format.
    Raise KeyError naming the missing field if a placeholder has no value."""
    raise NotImplementedError("Week 2: render_prompt")


def parse_json_reply(text: str, required: tuple[str, ...] = ("category", "urgent")) -> dict:
    """Models often wrap JSON in ```json fences or add a sentence before it.

    TODO: take the text between the first "{" and the last "}", json.loads it and
    check every key in `required` is present. Raise ValueError if there is no
    JSON object, it does not parse, or a key is missing.
    """
    raise NotImplementedError("Week 2: parse_json_reply")


def run_eval(cases: list[dict], classify: Callable[[str], dict]) -> dict:
    """Each case is {"ticket": str, "expected": str}.

    TODO: call classify(ticket) for each case and compare result["category"]
    with case["expected"]. A classify() that raises counts as wrong.
    Return {"total": n, "correct": k, "accuracy": k / n (0.0 when n == 0),
            "failures": [tickets that were wrong]}.
    """
    raise NotImplementedError("Week 2: run_eval")
