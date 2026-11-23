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
