"""Week 3: chunking, embeddings and semantic search.

The tests use a tiny offline "embedding" (hashed bag of words) so they run anywhere.
In your project, swap embed() for a real model (for example Gemini's free
text-embedding endpoint or sentence-transformers) and keep the same interface.

Test it: pytest week03_search
Brief:   week03_search/README.md
"""
import hashlib
import math
import re

DIM = 256


def chunk_text(text: str, size: int = 50, overlap: int = 10) -> list[str]:
    """Split text into chunks of `size` words, each overlapping the previous by `overlap` words.

    TODO: split on whitespace; step = size - overlap; stop once a chunk reaches
    the last word. Return [] for empty text. Raise ValueError if overlap >= size.
    Example: 10 words, size=4, overlap=1 -> words 0-3, 3-6, 6-9.
    """
    raise NotImplementedError("Week 3: chunk_text")


def embed(text: str) -> list[float]:
    """Hashed bag-of-words vector, normalised to length 1 (already done for you)."""
    vec = [0.0] * DIM
    for word in re.findall(r"[a-z0-9]+", text.lower()):
        vec[int(hashlib.md5(word.encode()).hexdigest(), 16) % DIM] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def cosine(a: list[float], b: list[float]) -> float:
    """TODO: cosine similarity = dot(a, b) / (|a| * |b|). Return 0.0 if either vector is all zeros."""
    raise NotImplementedError("Week 3: cosine")


class SearchIndex:
    def __init__(self):
        self.items: list[dict] = []  # {"id", "text", "source", "vector"}

    def add(self, text: str, source: str) -> None:
        """TODO: store the chunk with an id (its position, starting at 0), its source and embed(text)."""
        raise NotImplementedError("Week 3: SearchIndex.add")

    def search(self, query: str, k: int = 3) -> list[dict]:
        """TODO: return the top-k items as {"id", "text", "source", "score"}, best first."""
        raise NotImplementedError("Week 3: SearchIndex.search")
