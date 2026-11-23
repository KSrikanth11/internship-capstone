# Week 3: Embeddings and semantic search

**Goal:** Build the retrieval layer: split documents into chunks, turn them into vectors and find the most relevant ones for a question.

**Your file:** `week03_search/search.py`. **Check:** `pytest week03_search`

## Steps
1. Complete `chunk_text()`, `cosine()`, `SearchIndex.add()` and `SearchIndex.search()`.
2. Add 5+ real documents of your own to `week03_search/data/` (public FAQs or policies you're allowed to use).
3. Swap the hashed `embed()` for a real embedding model in your own module, keeping the same interface.
4. Compare search results for 10 questions with the toy and the real embeddings.

## Stretch goals
- Save and load the index as JSON so it isn't rebuilt every run.
- Try a vector database such as Chroma or Qdrant.

## What your mentor reviews
Sensible chunk size and overlap, and evidence that real embeddings beat the toy ones.

## Submit
Branch `week-03-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.

## Solutions

Try first: you learn most from getting stuck for a while. Each block opens when you click it.

<details>
<summary>Show solution: <code>chunk_text()</code></summary>

```python
def chunk_text(text: str, size: int = 50, overlap: int = 10) -> list[str]:
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    words = text.split()
    chunks = []
    for i in range(0, len(words), size - overlap):
        chunks.append(" ".join(words[i:i + size]))
        if i + size >= len(words):
            break
    return chunks
```

</details>

<details>
<summary>Show solution: <code>cosine()</code></summary>

```python
def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na, nb = math.sqrt(sum(x * x for x in a)), math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0
```

</details>

<details>
<summary>Show solution: <code>add()</code></summary>

```python
def add(self, text: str, source: str) -> None:
    self.items.append({"id": len(self.items), "text": text, "source": source, "vector": embed(text)})
```

</details>

<details>
<summary>Show solution: <code>search()</code></summary>

```python
def search(self, query: str, k: int = 3) -> list[dict]:
    q = embed(query)
    scored = [{"id": i["id"], "text": i["text"], "source": i["source"], "score": cosine(q, i["vector"])} for i in self.items]
    return sorted(scored, key=lambda h: h["score"], reverse=True)[:k]
```

</details>
