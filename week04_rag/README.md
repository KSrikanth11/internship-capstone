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

## Solutions

Try first: you learn most from getting stuck for a while. Each block opens when you click it.

<details>
<summary>Show solution: <code>build_context()</code></summary>

```python
def build_context(hits: list[dict]) -> str:
    return "\n".join(f"[{n}] ({h['source']}) {h['text']}" for n, h in enumerate(hits, 1))
```

</details>

<details>
<summary>Show solution: <code>extract_citations()</code></summary>

```python
def extract_citations(reply: str, n_sources: int) -> list[int]:
    out = []
    for m in re.findall(r"\[(\d+)\]", reply):
        n = int(m)
        if 1 <= n <= n_sources and n not in out:
            out.append(n)
    return out
```

</details>

<details>
<summary>Show solution: <code>answer()</code></summary>

```python
def answer(question: str, index: SearchIndex, k: int = 3, min_score: float = 0.2) -> dict:
    hits = index.search(question, k)
    if not hits or hits[0]["score"] < min_score:
        return {"answer": NOT_FOUND, "citations": [], "found": False}
    reply = chat([{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": f"Sources:\n{build_context(hits)}\n\nQuestion: {question}"}])
    cites = [{"n": n, "source": hits[n - 1]["source"]} for n in extract_citations(reply, len(hits))]
    return {"answer": reply, "citations": cites, "found": NOT_FOUND not in reply}
```

</details>
