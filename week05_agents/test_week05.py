import json

from week05_agents.agent import Tool, parse_tool_call, run_agent, run_tool

ORDERS = {"A12": "paid, course: GenAI Beginners"}
refunds = []
TOOLS = {
    "lookup_order": Tool("lookup_order", "Look up an order", lambda order_id: ORDERS.get(order_id, "not found")),
    "issue_refund": Tool("issue_refund", "Refund an order", lambda order_id: refunds.append(order_id) or "refunded", needs_approval=True),
    "broken": Tool("broken", "Always fails", lambda: 1 / 0),
}


def test_parse_tool_call():
    assert parse_tool_call('{"tool": "lookup_order", "args": {"order_id": "A12"}}') == {"tool": "lookup_order", "args": {"order_id": "A12"}}
    assert parse_tool_call('{"tool": "broken"}') == {"tool": "broken", "args": {}}
    assert parse_tool_call("Your order is paid.") is None
    assert parse_tool_call('{"answer": 1}') is None
    assert parse_tool_call("[1, 2]") is None


def test_run_tool_rules():
    yes, no = (lambda n, a: True), (lambda n, a: False)
    assert run_tool({"tool": "lookup_order", "args": {"order_id": "A12"}}, TOOLS, no) == ORDERS["A12"]
    assert run_tool({"tool": "nope", "args": {}}, TOOLS, yes) == "ERROR: unknown tool nope"
    refunds.clear()
    assert run_tool({"tool": "issue_refund", "args": {"order_id": "A12"}}, TOOLS, no).startswith("DENIED")
    assert refunds == []
    assert run_tool({"tool": "issue_refund", "args": {"order_id": "A12"}}, TOOLS, yes) == "refunded"
    assert run_tool({"tool": "broken", "args": {}}, TOOLS, yes).startswith("ERROR:")


def test_agent_loop_uses_tool_results():
    script = iter([json.dumps({"tool": "lookup_order", "args": {"order_id": "A12"}}), "Order A12 is paid."])
    seen = []

    def llm(messages):
        seen.append([m["content"] for m in messages])
        return next(script)

    result = run_agent("Is order A12 paid?", TOOLS, llm, approve=lambda n, a: True)
    assert result.answer == "Order A12 is paid."
    assert result.steps == [{"tool": "lookup_order", "args": {"order_id": "A12"}, "result": ORDERS["A12"]}]
    assert seen[1][-1] == f"TOOL RESULT: {ORDERS['A12']}"


def test_agent_stops_after_max_steps():
    result = run_agent("loop", TOOLS, lambda m: '{"tool": "lookup_order", "args": {"order_id": "X"}}',
                       approve=lambda n, a: True, max_steps=3)
    assert result.answer == "Stopped: too many steps." and len(result.steps) == 3
