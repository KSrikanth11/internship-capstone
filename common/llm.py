"""A tiny LLM client that works with free tiers, so no paid key is ever needed.

Providers (set LLM_PROVIDER in your .env):
  gemini  Google AI Studio free tier      GEMINI_API_KEY
  groq    Groq free tier (OpenAI-style)    GROQ_API_KEY
  ollama  open models on your own machine  (no key; run `ollama serve`)
  mock    offline, deterministic replies   (used by the automatic tests)

Usage:
    from common.llm import chat
    reply = chat([{"role": "system", "content": "Be brief."}, {"role": "user", "content": "Hi"}])
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Callable

Message = dict  # {"role": "system"|"user"|"assistant", "content": str}


class LLMError(RuntimeError):
    """Raised when a provider call fails for good (after retries)."""


class RateLimitError(LLMError):
    """HTTP 429: wait and retry."""


def _load_dotenv(path: str = ".env") -> None:
    if not os.path.exists(path):
        return
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _post(url: str, payload: dict, headers: dict, timeout: float = 60) -> dict:
    request = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as err:
        body = err.read().decode(errors="replace")[:300]
        if err.code == 429:
            raise RateLimitError(f"429 rate limited: {body}") from err
        raise LLMError(f"HTTP {err.code}: {body}") from err
    except urllib.error.URLError as err:
        raise LLMError(f"Network error: {err.reason}") from err


# ------------------------------------------------------------------ providers

def _gemini(messages: list[Message], temperature: float, max_tokens: int) -> str:
    key = os.environ.get("GEMINI_API_KEY", "")
    if not key:
        raise LLMError("Set GEMINI_API_KEY in .env (free at https://aistudio.google.com/apikey).")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
    system = "\n".join(m["content"] for m in messages if m["role"] == "system")
    contents = [{"role": "model" if m["role"] == "assistant" else "user", "parts": [{"text": m["content"]}]} for m in messages if m["role"] != "system"]
    payload = {"contents": contents, "generationConfig": {"temperature": temperature, "maxOutputTokens": max_tokens}}
    if system:
        payload["systemInstruction"] = {"parts": [{"text": system}]}
    data = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}", payload, {})
    return data["candidates"][0]["content"]["parts"][0]["text"]


def _groq(messages: list[Message], temperature: float, max_tokens: int) -> str:
    key = os.environ.get("GROQ_API_KEY", "")
    if not key:
        raise LLMError("Set GROQ_API_KEY in .env (free at https://console.groq.com/keys).")
    model = os.environ.get("GROQ_MODEL", "llama-3.1-8b-instant")
    data = _post("https://api.groq.com/openai/v1/chat/completions",
                 {"model": model, "messages": messages, "temperature": temperature, "max_tokens": max_tokens},
                 {"Authorization": f"Bearer {key}"})
    return data["choices"][0]["message"]["content"]


def _ollama(messages: list[Message], temperature: float, max_tokens: int) -> str:
    model = os.environ.get("OLLAMA_MODEL", "llama3.2")
    base = os.environ.get("OLLAMA_URL", "http://localhost:11434")
    data = _post(f"{base}/api/chat", {"model": model, "messages": messages, "stream": False,
                                      "options": {"temperature": temperature, "num_predict": max_tokens}}, {})
    return data["message"]["content"]


def _mock(messages: list[Message], temperature: float, max_tokens: int) -> str:
    """Deterministic offline replies, so tests and CI never need a key or network."""
    last = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
    system = " ".join(m["content"] for m in messages if m["role"] == "system").lower()
    if "json" in system:
        return json.dumps({"answer": f"Mock answer to: {last[:60]}", "confidence": 0.5})
    return f"Mock reply to: {last[:80]}"


PROVIDERS: dict[str, Callable[[list[Message], float, int], str]] = {
    "gemini": _gemini, "groq": _groq, "ollama": _ollama, "mock": _mock,
}


def chat(messages: list[Message], temperature: float = 0.3, max_tokens: int = 512,
         provider: str | None = None, retries: int = 3) -> str:
    """Send a chat request with retries and exponential backoff on rate limits."""
    _load_dotenv()
    name = (provider or os.environ.get("LLM_PROVIDER", "mock")).lower()
    if name not in PROVIDERS:
        raise LLMError(f"Unknown LLM_PROVIDER '{name}'. Use one of: {', '.join(PROVIDERS)}.")
    for attempt in range(retries + 1):
        try:
            return PROVIDERS[name](messages, temperature, max_tokens)
        except RateLimitError:
            if attempt == retries:
                raise
            time.sleep(2 ** attempt)
    raise LLMError("unreachable")
