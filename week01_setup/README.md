# Week 1: Onboarding and your first LLM call

**Goal:** Set up your workspace, learn the pull-request workflow you'll use every week, and make your first call to a real LLM.

**Your file:** `week01_setup/hello_llm.py`. **Check:** `pytest week01_setup`

## Steps
1. Create your repo from the template and open it in Codespaces.
2. Run `python scripts/progress.py` and read the output.
3. Complete `build_messages()` and `ask()` in `hello_llm.py`.
4. Get a free Gemini or Groq key, set it in `.env`, and run `python -m week01_setup.hello_llm "What is RAG?"`.
5. Branch `week-01-setup`, commit, push, open a pull request.

## Stretch goals
- Add a `--temperature` option and compare three answers at 0.0 and 1.0.
- Time each call and print the latency.

## What your mentor reviews
Clean commits with clear messages, input validation, no secrets committed.

## Submit
Branch `week-01-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.
