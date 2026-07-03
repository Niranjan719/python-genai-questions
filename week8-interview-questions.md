# Week 8 — Mock Interview and Behavioral Prep Interview Questions and Answers

This file includes coding questions, mock interview prompts, and behavioral preparation for Week 8.

## Coding Question 1: Whiteboard-style code review helper

**Problem:** Return the first failing test from a list of results.

**Answer:**
```python
from typing import List, Dict, Optional


def first_failing_test(results: List[Dict[str, str]]) -> Optional[str]:
    for result in results:
        if result["status"] == "fail":
            return result["name"]
    return None

print(first_failing_test([
    {"name": "test_a", "status": "pass"},
    {"name": "test_b", "status": "fail"},
]))
# test_b
```

## Coding Question 2: Identify bottleneck in latency data

**Problem:** Choose the highest latency component from a dict.

**Answer:**
```python
from typing import Dict


def largest_latency(components: Dict[str, float]) -> str:
    return max(components, key=components.get)

print(largest_latency({"db": 120, "model": 280, "cache": 30}))
# model
```

## Coding Question 3: Build a STAR summary string

**Problem:** Format a STAR story from fields.

**Answer:**
```python
from typing import Dict


def build_star(story: Dict[str, str]) -> str:
    return (
        f"Situation: {story['situation']}\n"
        f"Task: {story['task']}\n"
        f"Action: {story['action']}\n"
        f"Result: {story['result']}"
    )

print(build_star({
    "situation": "We had a latency spike.",
    "task": "Identify root cause.",
    "action": "Analyzed logs and optimized queries.",
    "result": "Latency dropped by 40%."
}))
```

## Coding Question 4: Convert behavioral notes into bullet list

**Problem:** Convert a list of phrase strings into a joined bullet markdown string.

**Answer:**
```python
from typing import List


def bullets(items: List[str]) -> str:
    return "\n".join(f"- {item}" for item in items)

print(bullets(["Led a cross-functional team", "Improved reliability"]))
```

## Coding Question 5: Mock interview question randomizer

**Problem:** Pick a random question from a list.

**Answer:**
```python
import random
from typing import List


def pick_question(questions: List[str]) -> str:
    return random.choice(questions)

print(pick_question(["Explain RAG.", "Describe your hardest bug."]))
```

## Interview Questions

### Question 1: Tell me about a production issue you resolved.

**Answer structure:**
- Situation: Describe the issue clearly.
- Task: What was your responsibility?
- Action: What steps did you take?
- Result: What improved and by how much?

### Question 2: Describe a difficult stakeholder conversation.

**Answer structure:**
- Situation: Explain the conflict or ambiguity.
- Task: What needed alignment?
- Action: How did you communicate trade-offs?
- Result: What was agreed and what changed?

### Question 3: How do you handle ambiguous requirements?

**Answer:**
- Clarify assumptions with stakeholders.
- Break the problem into smaller hypotheses.
- Prototype quickly and validate.
- Iterate based on feedback.

### Question 4: How do you improve latency or reduce cost?

**Answer:**
- Measure baseline performance and cost.
- Identify hotspots and model inefficiencies.
- Apply caching, batching, smaller models, and async design.
- Validate impact with metrics.

### Question 5: Describe a GenAI project you led end-to-end.

**Answer:**
- Explain the problem, stakeholders, and value.
- Summarize architecture, data flow, and model choice.
- Highlight challenges and how you overcame them.
- Share the final outcome and what you learned.

### Question 6: How do you mentor junior engineers?

**Answer:**
- Provide clear feedback and pair programming.
- Encourage ownership and ask guiding questions.
- Share best practices and review their work.
- Help them build confidence through small wins.

### Question 7: What is your approach to mock interviews?

**Answer:**
- Practice coding problems with time pressure.
- Review design questions and explain trade-offs aloud.
- Use STAR stories for behavioral questions.
- Reflect on mistakes and iterate.

### Question 8: What are your strongest GenAI topics?

**Answer:**
- Identify your highest-confidence areas, e.g. RAG, LangChain, architecture.
- Explain how your experience maps to the role.
- Mention the areas you are actively strengthening.
- Show readiness to learn and adapt.
