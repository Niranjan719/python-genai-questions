# Week 3 — LLM Fundamentals and Prompt Engineering Interview Questions and Answers

This file includes coding questions, answers, and interview Q&A for Week 3: LLM fundamentals and prompt engineering.

## Coding Question 1: Simple token frequency counter

**Problem:** Count token frequencies in text using whitespace tokenization, ignoring punctuation.

**Answer:**
```python
import re
from collections import Counter


def token_counts(text: str):
    tokens = re.findall(r"\b\w+\b", text.lower())
    return Counter(tokens)


print(token_counts("AI systems, AI pipelines, and AI interviews."))
# Counter({'ai': 3, 'systems': 1, 'pipelines': 1, 'and': 1, 'interviews': 1})
```

## Coding Question 2: Compare cosine similarity of two vectors

**Problem:** Implement cosine similarity for two numeric vectors.

**Answer:**
```python
import math
from typing import Sequence


def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


print(cosine_similarity([1, 2, 3], [1, 2, 3]))
# 1.0
```

## Coding Question 3: Prompt template builder

**Problem:** Build a small prompt templating helper for structured instructions.

**Answer:**
```python
from string import Template


def build_prompt(template: str, **kwargs) -> str:
    return Template(template).substitute(kwargs)


template = (
    "You are an assistant.\n"
    "Translate the following text into $language:\n"
    "$text"
)

print(build_prompt(template, language="French", text="Hello world"))
```

## Coding Question 4: Simple few-shot prompt generator

**Problem:** Create a function that generates a few-shot prompt with examples.

**Answer:**
```python
from typing import List, Dict


def generate_few_shot_prompt(task: str, examples: List[Dict[str, str]], query: str) -> str:
    prompt = ["You are an assistant that helps with the following task:", task, "\nExamples:"]
    for example in examples:
        prompt.append(f"Input: {example['input']}\nOutput: {example['output']}\n")
    prompt.append(f"Input: {query}\nOutput:")
    return "\n".join(prompt)


examples = [
    {"input": "Add 1 and 2", "output": "3"},
    {"input": "Add 5 and 7", "output": "12"}
]
print(generate_few_shot_prompt("Add numbers", examples, "Add 10 and 20"))
```

## Coding Question 5: Simple hallucinatory response filter

**Problem:** Detect if a model response contains unsupported claims by checking required evidence tokens.

**Answer:**
```python
from typing import List


def contains_evidence(response: str, required_terms: List[str]) -> bool:
    text = response.lower()
    return all(term.lower() in text for term in required_terms)

print(contains_evidence("The source says 42 is the answer.", ["source", "42"]))
# True
```

## Interview Questions

### Question 1: What is an embedding?

**Answer:**
- An embedding maps text to a numeric vector in a high-dimensional space.
- It encodes semantic meaning so similar text has nearby vectors.
- Embeddings are used for search, clustering, classification, and retrieval.
- Token embeddings represent tokens, while sentence/document embeddings represent larger text units.

### Question 2: Explain cosine similarity vs Euclidean distance.

**Answer:**
- Cosine similarity measures angle between vectors and is invariant to magnitude.
- Euclidean distance measures straight-line distance and is sensitive to vector length.
- Cosine is often better for text embeddings because we care about semantic direction.
- Normalize embeddings to compare similarity more consistently.

### Question 3: Why does GPT work?

**Answer:**
- GPT is a decoder-only transformer trained on next-token prediction.
- Self-attention lets it condition on all previous context efficiently.
- Large-scale pretraining on web-scale text helps generalize to many tasks.
- Prompting guides the model, and the transformer architecture enables flexible reasoning.

### Question 4: How does BERT differ from GPT?

**Answer:**
- BERT is an encoder-only model trained with masked language modeling.
- It is bidirectional and excels at understanding tasks like classification and QA.
- GPT is unidirectional and optimized for generation.
- BERT is usually fine-tuned for downstream tasks, while GPT is often prompted.

### Question 5: What is prompt injection and how do you guard against it?

**Answer:**
- Prompt injection occurs when adversarial text in input manipulates model behavior.
- Guardrails include input validation, explicit instructions, and tool access controls.
- Use sanitization, role separation, and a strict prompt template.
- Avoid blindly appending untrusted text to the core prompt.

### Question 6: What is zero-shot vs few-shot prompting?

**Answer:**
- Zero-shot prompting gives the model a task instruction without examples.
- Few-shot prompting includes examples of input/output pairs.
- Few-shot can improve accuracy by teaching the model format and expectations.
- Zero-shot is useful when examples are unavailable or prompt length is limited.

### Question 7: Explain Chain of Thought (CoT)

**Answer:**
- Chain of Thought encourages the model to generate intermediate reasoning steps.
- It improves performance on complex reasoning and multi-step tasks.
- You can prompt with examples that show step-by-step thinking.
- CoT is especially useful for math, logic, and explanation-heavy tasks.

### Question 8: What is a structured output prompt?

**Answer:**
- A structured output prompt asks the model to respond in a fixed format like JSON.
- It makes parsing results deterministic and safer for automation.
- Include an explicit schema, field names, and example output.
- Validate the model’s response and fallback if formatting fails.
