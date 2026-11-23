from week08_demo.check_docs import PROJECT_MD, problems


def test_project_doc_is_complete():
    issues = problems(PROJECT_MD.read_text(encoding="utf-8"))
    assert not issues, "docs/PROJECT.md: " + "; ".join(issues)
