"""Week 1: your first LLM call.

Run it:   python -m week01_setup.hello_llm "What is RAG?"
Test it:  pytest week01_setup
Brief:    week01_setup/README.md
"""
import sys

from common.llm import chat

SYSTEM_PROMPT = "You are a concise study assistant for Indian engineering students."


def build_messages(question: str, system: str = SYSTEM_PROMPT) -> list[dict]:
    """Return the chat messages for one question.

    TODO: return a list with a system message (content=system) followed by a
    user message (content=question with surrounding spaces removed).
    Raise ValueError if the question is empty or only spaces.
    """
    raise NotImplementedError("Week 1: build_messages")


def ask(question: str) -> str:
    """TODO: call chat() with build_messages(question) and return the reply without
    leading/trailing whitespace."""
    raise NotImplementedError("Week 1: ask")


if __name__ == "__main__":
    print(ask(" ".join(sys.argv[1:]) or "Explain an LLM in one line."))
