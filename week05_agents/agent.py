"""Week 5: function calling and an agent loop with a human approval step.

Test it: pytest week05_agents
Brief:   week05_agents/README.md
"""
import json
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Tool:
    name: str
    description: str
    fn: Callable[..., str]
    needs_approval: bool = False  # e.g. sending an email or issuing a refund


@dataclass
class AgentResult:
    answer: str
    steps: list[dict] = field(default_factory=list)  # {"tool", "args", "result"}


def parse_tool_call(reply: str) -> dict | None:
    """The model replies with either plain text (a final answer) or JSON like
    {"tool": "lookup_order", "args": {"order_id": "A12"}}.

    TODO: return {"tool": str, "args": dict} if the reply is a JSON object with a
    string "tool" (args default to {}); otherwise return None.
    """
    raise NotImplementedError("Week 5: parse_tool_call")


def run_tool(call: dict, tools: dict[str, Tool], approve: Callable[[str, dict], bool]) -> str:
    """TODO:
    - Unknown tool -> return "ERROR: unknown tool <name>" (don't raise: the model can recover).
    - If tool.needs_approval and approve(name, args) is False -> return "DENIED: a human did not approve <name>".
    - Call tool.fn(**args). If it raises, return "ERROR: <message>".
    """
    raise NotImplementedError("Week 5: run_tool")


def run_agent(question: str, tools: dict[str, Tool], llm: Callable[[list[dict]], str],
              approve: Callable[[str, dict], bool], max_steps: int = 5) -> AgentResult:
    """TODO: the loop.
    messages = [system (list the tools and the JSON format), user question]
    repeat up to max_steps:
        reply = llm(messages)
        call = parse_tool_call(reply)
        if call is None: return AgentResult(reply, steps)
        result = run_tool(call, tools, approve); record the step
        append the assistant reply and a user message "TOOL RESULT: <result>"
    If max_steps runs out, return AgentResult("Stopped: too many steps.", steps).
    """
    raise NotImplementedError("Week 5: run_agent")
