from pathlib import Path

import pytest

from week03_search.search import SearchIndex, chunk_text
from week04_rag import rag

DOCS = Path(__file__).parents[1] / "week03_search" / "data"
HITS = [{"id": 0, "text": "Refunds within 7 days.", "source": "refund-policy.md", "score": 0.8},
        {"id": 4, "text": "Certificates have QR codes.", "source": "certificates.md", "score": 0.4}]


@pytest.fixture
def index():
    idx = SearchIndex()
    for path in sorted(DOCS.glob("*.md")):
        for chunk in chunk_text(path.read_text(encoding="utf-8"), 40, 8):
            idx.add(chunk, path.name)
    return idx


def test_build_context():
    assert rag.build_context(HITS) == "[1] (refund-policy.md) Refunds within 7 days.\n[2] (certificates.md) Certificates have QR codes."


def test_extract_citations():
    assert rag.extract_citations("Yes [2]. Also [1] and again [2], not [7].", 3) == [2, 1]
    assert rag.extract_citations("No citations.", 3) == []


def test_answer_with_citations(index, monkeypatch):
    seen = {}

    def fake_chat(messages, **kw):
        seen["messages"] = messages
        return "You have 7 days to ask for a refund [1]."

    monkeypatch.setattr(rag, "chat", fake_chat)
    result = rag.answer("How many days do I have to ask for a refund?", index)
    assert result["found"] is True
    assert result["citations"] == [{"n": 1, "source": "refund-policy.md"}]
    assert seen["messages"][0] == {"role": "system", "content": rag.SYSTEM}
    assert "[1] (refund-policy.md)" in seen["messages"][1]["content"]
    assert seen["messages"][1]["content"].endswith("Question: How many days do I have to ask for a refund?")


def test_not_found_skips_llm(index, monkeypatch):
    monkeypatch.setattr(rag, "chat", lambda *a, **k: pytest.fail("LLM must not be called"))
    result = rag.answer("best biryani in Hyderabad", index)
    assert result == {"answer": rag.NOT_FOUND, "citations": [], "found": False}


def test_model_says_not_found(index, monkeypatch):
    monkeypatch.setattr(rag, "chat", lambda *a, **k: rag.NOT_FOUND)
    assert rag.answer("refund for certificate fees", index)["found"] is False
