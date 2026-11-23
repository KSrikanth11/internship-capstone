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
