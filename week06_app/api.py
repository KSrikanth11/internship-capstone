"""Week 6: the backend of your full-stack app (FastAPI).

Run it:  uvicorn week06_app.api:app --reload   then open http://127.0.0.1:8000/docs
Test it: pytest week06_app
Brief:   week06_app/README.md (the React frontend lives in your own frontend/ folder)
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from common.llm import chat

app = FastAPI(title="Capstone assistant API")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    history: list[dict] = []


@app.get("/health")
def health():
    """TODO: return {"status": "ok"}."""
    raise HTTPException(501, "Week 6: /health")


@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    """TODO: build messages = req.history (keep only the last 10, and only roles
    "user"/"assistant") + the new user message, call chat(messages) and return
    {"reply": reply}. Reject a message that is only whitespace with HTTP 422."""
    raise HTTPException(501, "Week 6: /chat")


@app.post("/chat/stream")
def chat_stream(req: ChatRequest):
    """TODO: stream the reply word by word as plain text, e.g.
    StreamingResponse((w + " " for w in reply.split()), media_type="text/plain")."""
    raise HTTPException(501, "Week 6: /chat/stream")
