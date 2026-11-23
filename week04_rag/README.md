# Week 4: RAG with citations and an honest "not found"

**Goal:** Answer questions only from your documents, cite the sources, and refuse instead of guessing.

**Your file:** `week04_rag/rag.py`. **Check:** `pytest week04_rag`

## Steps
1. Complete `build_context()`, `extract_citations()` and `answer()`.
2. Tune `min_score` with 10 answerable and 5 unanswerable questions.
3. Run with a real model and check every citation actually supports the claim.

## Stretch goals
- Show the cited chunk text under each answer.
- Measure groundedness: what fraction of answers cite at least one correct source?

## What your mentor reviews
No hallucinated answers on unanswerable questions, and correct citations.

## Submit
Branch `week-04-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.
