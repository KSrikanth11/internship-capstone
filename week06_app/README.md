# Week 6: Full-stack app and deployment

**Goal:** Put everything behind an API with streaming, build a small React chat UI, and deploy it.

**Your file:** `week06_app/api.py`. **Check:** `pytest week06_app`

## Steps
1. Complete `/health`, `/chat` and `/chat/stream`, then run `uvicorn week06_app.api:app --reload` and try `/docs`.
2. Connect `/chat` to your Week 4 RAG answerer.
3. Create `frontend/` with `npm create vite@latest frontend -- --template react` and build a chat screen that streams replies.
4. Deploy the API (Render, Railway or Hugging Face Spaces free tiers) and the frontend (Cloudflare Pages, Vercel or Netlify). Put both URLs in your pull request.

## Stretch goals
- Add a Dockerfile.
- Show citations as clickable chips in the UI.

## What your mentor reviews
A working live URL, input validation, and no keys in the frontend.

## Submit
Branch `week-06-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.
