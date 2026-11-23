# Agentic AI & LLM Engineering Internship: capstone starter

The starter repository for the [Aiprojects4U Learning Solutions](https://aiprojects4u.com/internships/agentic-ai-llm-engineering-remote-internship) remote internship. Over 8 weeks you build one real product, a **support assistant for an ed-tech company**, piece by piece: prompts, semantic search, RAG with citations, an agent with tools and human approval, a full-stack app, security and evaluation.

Every week has a brief, starter code with `TODO`s, and automatic tests that pass only when the task is done.

## Start in 2 minutes (no installs)
1. Click **Use this template → Create a new repository** (make it public: it's your portfolio).
2. In your new repo: **Code → Codespaces → Create codespace**. Python and every package install themselves.
3. In the terminal: `python scripts/progress.py`. You'll see 8 empty boxes. Your job is to tick them.

Prefer your own laptop? Python 3.11+, then:
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## LLM access: free, no card needed
Tests always use an offline mock, so you never need a key to pass them. To talk to a real model, pick one in `.env`:

| `LLM_PROVIDER` | Get access | Notes |
|---|---|---|
| `gemini` | Free key at aistudio.google.com/apikey | Generous free tier; good default |
| `groq` | Free key at console.groq.com/keys | Very fast open models (Llama) |
| `ollama` | Install from ollama.com, run `ollama pull llama3.2` | Fully offline on your laptop |
| `mock` | Nothing | Deterministic replies for tests |

Never commit `.env`. It is already in `.gitignore`.

## The 8 weeks
| Week | Folder | You build | Check |
|---|---|---|---|
| 1 | `week01_setup` | Git workflow and your first LLM call | `pytest week01_setup` |
| 2 | `week02_prompts` | Prompt templates, JSON output, an evaluation set | `pytest week02_prompts` |
| 3 | `week03_search` | Chunking, embeddings and semantic search | `pytest week03_search` |
| 4 | `week04_rag` | RAG answers with citations and an honest "not found" | `pytest week04_rag` |
| 5 | `week05_agents` | Function calling, an agent loop, human approval | `pytest week05_agents` |
| 6 | `week06_app` | FastAPI backend, streaming chat, React frontend, deploy | `pytest week06_app` |
| 7 | `week07_safety` | Injection guard, PII redaction, red teaming, cost | `pytest week07_safety` |
| 8 | `week08_demo` | Documentation, demo video, interview prep | `pytest week08_demo` |

Each folder's `README.md` is that week's brief: goal, steps, stretch goals and what the mentor reviews.

## How each week works
1. `git checkout -b week-03-search` (the branch name **must** start with `week-NN`).
2. Read the brief, fill in the `TODO`s, run the week's tests until they pass.
3. Push and open a pull request into `main`. The template asks a few questions; answer them honestly.
4. **Automatic checks** run that week's tests on your pull request. Green means the code works; your mentor then reviews design, clarity and your answers.
5. Paste the pull request link in the weekly submission form on the site. Merge after the mentor approves.

Stuck? Ask in **Help & Support** on aiprojects4u.com/support (choose "Doubt"). Share your error and what you tried, never your API key.

## Rules that keep it fair
- Write your own code. Using AI assistants is allowed (it's an AI internship!), but you must be able to explain every line in the weekly review.
- Don't copy another intern's solution. Reviews include a short live walkthrough.
- Don't edit the `test_*.py` files to make them pass. You may add your own tests.

## Completion criteria (for the certificate)
All 8 weeks green and reviewed, a deployed app, a 3-minute demo video, `docs/PROJECT.md` complete, and the final demo-day review.

Licensed under the MIT License. © Aiprojects4U Learning Solutions.
