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
