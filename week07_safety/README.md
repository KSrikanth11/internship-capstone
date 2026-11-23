# Week 7: Security, red teaming and cost

**Goal:** Harden the assistant: block prompt injection, redact personal data before it reaches the model, red-team it and track cost.

**Your file:** `week07_safety/guard.py`. **Check:** `pytest week07_safety`

## Steps
1. Complete `detect_injection()`, `redact_pii()`, `estimate_cost()` and `red_team_report()`.
2. Put the guards in front of `/chat`.
3. Write 20 attacks (injection, data leaks, off-topic) and report your pass rate before and after the guards.
4. Log tokens and cost per request, and show a simple daily total.

## Stretch goals
- Use an LLM-based classifier as a second guard layer.
- Build a small evaluation dashboard page.

## What your mentor reviews
A real red-team set, layered defences and honest numbers.

## Submit
Branch `week-07-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.

## Solutions

Try first: you learn most from getting stuck for a while. Each block opens when you click it.

<details>
<summary>Show solution: <code>detect_injection()</code></summary>

```python
def detect_injection(text: str) -> bool:
    return any(re.search(p, text, re.I) for p in INJECTION_PATTERNS)
```

</details>

<details>
<summary>Show solution: <code>redact_pii()</code></summary>

```python
def redact_pii(text: str) -> str:
    text = re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[EMAIL]", text)
    text = re.sub(r"\b\d{4}\s?\d{4}\s?\d{4}\b", "[ID]", text)
    return re.sub(r"(?:\+?91[ -]?)?\b[6-9]\d{9}\b", "[PHONE]", text)
```

</details>

<details>
<summary>Show solution: <code>estimate_cost()</code></summary>

```python
def estimate_cost(tokens_in: int, tokens_out: int, price_in_per_m: float, price_out_per_m: float) -> float:
    return round(tokens_in / 1e6 * price_in_per_m + tokens_out / 1e6 * price_out_per_m, 6)
```

</details>

<details>
<summary>Show solution: <code>red_team_report()</code></summary>

```python
def red_team_report(attacks: list[str], respond) -> dict:
    leaked = [a for a in attacks if "SYSTEM PROMPT:" in respond(a)]
    n = len(attacks)
    return {"total": n, "leaked": leaked, "pass_rate": (n - len(leaked)) / n if n else 1.0}
```

</details>
