# Week 5: Function calling and agents with approval

**Goal:** Give the assistant tools (look up an order, check a course, issue a refund) and make sure risky tools need a human's yes.

**Your file:** `week05_agents/agent.py`. **Check:** `pytest week05_agents`

## Steps
1. Complete `parse_tool_call()`, `run_tool()` and `run_agent()`.
2. Write three tools of your own; at least one must need approval.
3. Connect `run_agent()` to `chat()` and test 5 multi-step questions with a real model.
4. Log every step so a mentor can follow what the agent did.

## Stretch goals
- Use your provider's native function-calling API instead of JSON-in-text.
- Add a per-conversation budget of tool calls.

## What your mentor reviews
Safe defaults: unknown tools, errors and denials never crash the loop.

## Submit
Branch `week-05-...`, open a pull request into `main`, fill in the template, and paste its link in the weekly submission form.

## Solutions

Try first: you learn most from getting stuck for a while. Each block opens when you click it.

<details>
<summary>Show solution: <code>parse_tool_call()</code></summary>

```python
def parse_tool_call(reply: str) -> dict | None:
    try:
        data = json.loads(reply)
    except (json.JSONDecodeError, TypeError):
        return None
    if not isinstance(data, dict) or not isinstance(data.get("tool"), str):
        return None
    return {"tool": data["tool"], "args": data.get("args") or {}}
```

</details>

<details>
<summary>Show solution: <code>run_tool()</code></summary>

```python
def run_tool(call: dict, tools: dict[str, Tool], approve: Callable[[str, dict], bool]) -> str:
    name, args = call["tool"], call.get("args", {})
    tool = tools.get(name)
    if tool is None:
        return f"ERROR: unknown tool {name}"
    if tool.needs_approval and not approve(name, args):
        return f"DENIED: a human did not approve {name}"
    try:
        return str(tool.fn(**args))
    except Exception as err:
        return f"ERROR: {err}"
```

</details>

<details>
<summary>Show solution: <code>run_agent()</code></summary>

```python
def run_agent(question: str, tools: dict[str, Tool], llm: Callable[[list[dict]], str],
              approve: Callable[[str, dict], bool], max_steps: int = 5) -> AgentResult:
    tool_list = "\n".join(f"- {t.name}: {t.description}" for t in tools.values())
    messages = [{"role": "system", "content": f"Tools:\n{tool_list}\nCall one as JSON {{\"tool\": name, \"args\": {{}}}} or answer in text."},
                {"role": "user", "content": question}]
    steps = []
    for _ in range(max_steps):
        reply = llm(messages)
        call = parse_tool_call(reply)
        if call is None:
            return AgentResult(reply, steps)
        result = run_tool(call, tools, approve)
        steps.append({"tool": call["tool"], "args": call["args"], "result": result})
        messages += [{"role": "assistant", "content": reply}, {"role": "user", "content": f"TOOL RESULT: {result}"}]
    return AgentResult("Stopped: too many steps.", steps)
```

</details>
