import pytest

from week01_setup.hello_llm import SYSTEM_PROMPT, ask, build_messages


def test_messages_have_system_then_user():
    msgs = build_messages("  What is a token?  ")
    assert [m["role"] for m in msgs] == ["system", "user"]
    assert msgs[0]["content"] == SYSTEM_PROMPT
    assert msgs[1]["content"] == "What is a token?"


def test_custom_system_prompt():
    assert build_messages("Hi", system="Reply in Hindi.")[0]["content"] == "Reply in Hindi."


@pytest.mark.parametrize("bad", ["", "   "])
def test_empty_question_rejected(bad):
    with pytest.raises(ValueError):
        build_messages(bad)


def test_ask_uses_the_llm():
    reply = ask("What is RAG?")
    assert reply == reply.strip()
    assert "What is RAG?" in reply  # the mock provider echoes the question
