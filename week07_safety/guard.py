"""Week 7: security guards, PII redaction and cost monitoring.

Test it: pytest week07_safety
Brief:   week07_safety/README.md
"""
import re

INJECTION_PATTERNS = [
    r"ignore (all |any )?(previous|prior|above) (instructions|rules)",
    r"you are now",
    r"reveal (your|the) (system prompt|instructions)",
    r"developer mode",
]


def detect_injection(text: str) -> bool:
    """TODO: True if any INJECTION_PATTERNS regex matches (case-insensitive)."""
    raise NotImplementedError("Week 7: detect_injection")


def redact_pii(text: str) -> str:
    """TODO: replace emails with [EMAIL], Indian mobile numbers (10 digits starting 6-9,
    optionally prefixed by +91 or 91 with an optional space or dash) with [PHONE],
    and 12-digit Aadhaar-style numbers written as 4-4-4 digits (spaces optional) with [ID]."""
    raise NotImplementedError("Week 7: redact_pii")


def estimate_cost(tokens_in: int, tokens_out: int, price_in_per_m: float, price_out_per_m: float) -> float:
    """TODO: cost in USD given prices per million tokens, rounded to 6 decimals."""
    raise NotImplementedError("Week 7: estimate_cost")


def red_team_report(attacks: list[str], respond) -> dict:
    """Run every attack through respond(text) -> str.

    TODO: an attack "leaked" if the response contains "SYSTEM PROMPT:" (our canary).
    Return {"total": n, "leaked": [attacks that leaked], "pass_rate": (n - leaked) / n}.
    """
    raise NotImplementedError("Week 7: red_team_report")
