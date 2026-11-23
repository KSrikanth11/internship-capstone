from pathlib import Path

import pytest

from week03_search.search import SearchIndex, chunk_text, cosine, embed

DOCS = Path(__file__).parent / "data"


def test_chunk_overlap():
    words = " ".join(str(i) for i in range(10))
    assert chunk_text(words, size=4, overlap=1) == ["0 1 2 3", "3 4 5 6", "6 7 8 9"]


def test_chunk_edge_cases():
    assert chunk_text("", 4, 1) == []
    assert chunk_text("one two", 4, 1) == ["one two"]
    with pytest.raises(ValueError):
        chunk_text("a b c", 3, 3)


def test_cosine():
    assert cosine([1, 0], [1, 0]) == pytest.approx(1.0)
    assert cosine([1, 0], [0, 1]) == pytest.approx(0.0)
    assert cosine([0, 0], [1, 1]) == 0.0
    assert cosine(embed("refund policy"), embed("refund policy")) == pytest.approx(1.0)


def test_search_finds_the_right_document():
    index = SearchIndex()
    for path in sorted(DOCS.glob("*.md")):
        for chunk in chunk_text(path.read_text(encoding="utf-8"), size=40, overlap=8):
            index.add(chunk, path.name)
    hits = index.search("how many days do I have to ask for a refund", k=3)
    assert len(hits) == 3
    assert hits[0]["source"] == "refund-policy.md"
    assert hits[0]["score"] >= hits[1]["score"] >= hits[2]["score"]
    assert set(hits[0]) >= {"id", "text", "source", "score"}
    assert index.search("certificate verification QR", k=1)[0]["source"] == "certificates.md"
