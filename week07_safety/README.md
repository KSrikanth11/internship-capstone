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
