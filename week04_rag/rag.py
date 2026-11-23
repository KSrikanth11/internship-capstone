"""Week 4: a RAG answerer with citations and an honest "not found".

Test it: pytest week04_rag
Brief:   week04_rag/README.md
"""
import re

from common.llm import chat
from week03_search.search import SearchIndex

NOT_FOUND = "I couldn't find this in the documents."

SYSTEM = (
    "Answer ONLY from the numbered sources. Cite sources like [1] or [2] after each claim. "
    f"If the sources don't contain the answer, reply exactly: {NOT_FOUND}"
)


def build_context(hits: list[dict]) -> str:
    """TODO: number the hits from 1, one per line: "[1] (refund-policy.md) <text>"."""
    raise NotImplementedError("Week 4: build_context")


def extract_citations(reply: str, n_sources: int) -> list[int]:
    """TODO: find every [n] in the reply. Return the unique numbers in order of first
    appearance, keeping only 1 <= n <= n_sources (models sometimes invent [7])."""
    raise NotImplementedError("Week 4: extract_citations")


def answer(question: str, index: SearchIndex, k: int = 3, min_score: float = 0.2) -> dict:
    """Return {"answer": str, "citations": [{"n", "source"}], "found": bool}.

    TODO:
      1. hits = index.search(question, k)
      2. If there are no hits or the best score is below min_score, return
         {"answer": NOT_FOUND, "citations": [], "found": False} WITHOUT calling the LLM.
      3. Otherwise call chat() with SYSTEM as the system message and a user message
         "Sources:\n<build_context(hits)>\n\nQuestion: <question>".
      4. Map extract_citations(reply, len(hits)) to {"n": n, "source": hits[n-1]["source"]}.
      5. found is False if the reply contains NOT_FOUND.
    """
    raise NotImplementedError("Week 4: answer")
