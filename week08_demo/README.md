# Week 8: Documentation, demo day and interviews

**Goal:** Package your work so a recruiter understands it in 3 minutes, and practise explaining it.

**Your file:** `week08_demo/check_docs.py`. **Check:** `pytest week08_demo`

## Steps
1. Complete `docs/PROJECT.md` (every section, no TODOs, 400+ words) until `pytest week08_demo` passes.
2. Record a 3-minute demo video: problem, live demo, architecture, one hard decision.
3. Pin the repo on your GitHub profile and add the project to your resume and LinkedIn.
4. Do the mock interview with your mentor: architecture, trade-offs, what you'd do next.

## Stretch goals
- Write a blog post about one thing you learned.
- Add a short architecture diagram GIF to the README.

## What your mentor reviews
Clarity: could a hiring manager understand and run your project from the docs alone?

## Submit
Branch `week-08-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.

## Solutions

Try first: this one is about explaining your own project.

<details>
<summary>Show solution: an example <code>docs/PROJECT.md</code> outline</summary>

```markdown
## Problem
Students of an ed-tech company wait up to 2 days for answers about refunds, certificates and schedules.
The assistant answers from the official documents in seconds, cites them, and hands risky actions to a human.

## Architecture
React chat UI → FastAPI (/chat, /chat/stream) → guards (injection, PII) → RAG (chunks + embeddings + search)
→ LLM (Gemini free tier) → agent tools (lookup_order, check_course, issue_refund with approval).

## Setup
pip install -r requirements.txt; cp .env.example .env; uvicorn week06_app.api:app --reload; cd frontend && npm run dev

## Evaluation
40 questions (30 answerable, 10 not). v1: 70% correct, 4 hallucinations. v2 (min_score 0.25, few-shot): 87%, 0 hallucinations.

## Security
Injection regex + LLM classifier, PII redaction before the model, approval for refunds. Red team: 20 attacks, 95% blocked.

## Demo
Live app: https://your-app.pages.dev · Video: https://youtu.be/your-video

## What I would do next
Hybrid keyword + vector search; a feedback button feeding the evaluation set; caching common answers to cut cost.
```

Write it in your own words and with your own numbers, at 400+ words.

</details>
