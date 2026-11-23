# Week 2: Prompt engineering, JSON output and evaluation

**Goal:** Turn free-text support tickets into reliable structured JSON, and measure how often your prompt is right.

**Your file:** `week02_prompts/prompts.py`. **Check:** `pytest week02_prompts`

## Steps
1. Complete `render_prompt()`, `parse_json_reply()` and `run_eval()`.
2. Write 20 realistic tickets with expected categories in `week02_prompts/eval_set.json`.
3. Wire a real `classify()` that calls `chat()` and parses the JSON. Run your evaluation.
4. Improve the prompt (few-shot examples, clearer rules) and run it again. Record both scores in your pull request.

## Stretch goals
- Retry once when the JSON doesn't parse, with the error fed back to the model.
- Compare two providers on the same evaluation set.

## What your mentor reviews
An honest evaluation set, a before/after score, and robust parsing.

## Submit
Branch `week-02-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.

## Solutions

Try first: you learn most from getting stuck for a while. Each block opens when you click it.

<details>
<summary>Show solution: <code>render_prompt()</code></summary>

```python
def render_prompt(template: str, **values) -> str:
    return template.format(**values)
```

</details>

<details>
<summary>Show solution: <code>parse_json_reply()</code></summary>

```python
def parse_json_reply(text: str, required: tuple[str, ...] = ("category", "urgent")) -> dict:
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end < start:
        raise ValueError("no JSON object")
    try:
        data = json.loads(text[start:end + 1])
    except json.JSONDecodeError as err:
        raise ValueError(str(err)) from err
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(f"missing {missing}")
    return data
```

</details>

<details>
<summary>Show solution: <code>run_eval()</code></summary>

```python
def run_eval(cases: list[dict], classify: Callable[[str], dict]) -> dict:
    failures = []
    for case in cases:
        try:
            ok = classify(case["ticket"]).get("category") == case["expected"]
        except Exception:
            ok = False
        if not ok:
            failures.append(case["ticket"])
    n = len(cases)
    return {"total": n, "correct": n - len(failures), "accuracy": (n - len(failures)) / n if n else 0.0, "failures": failures}
```

</details>
