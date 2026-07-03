# Week 6 — Agentic AI and NLP Interview Questions and Answers

This file includes coding questions, answers, and interview Q&A for Week 6: agentic AI and NLP fundamentals.

## Coding Question 1: Simple task decomposition helper

**Problem:** Given a task string, split it into subtasks by keywords.

**Answer:**
```python
from typing import List


def split_task(task: str) -> List[str]:
    return [part.strip() for part in task.split("and") if part.strip()]

print(split_task("Read the document and summarize key points and propose next steps"))
# ['Read the document', 'summarize key points', 'propose next steps']
```

## Coding Question 2: Rule-based entity extractor

**Problem:** Extract capitalized words as name entities from text.

**Answer:**
```python
import re
from typing import List


def extract_entities(text: str) -> List[str]:
    return re.findall(r"\b[A-Z][a-z]+\b", text)

print(extract_entities("Alice met Bob in New York."))
# ['Alice', 'Bob', 'New', 'York']
```

## Coding Question 3: Simple TF-IDF vectorizer for a small corpus

**Problem:** Compute TF-IDF scores for each term in a tiny corpus.

**Answer:**
```python
import math
from collections import Counter
from typing import List, Dict


def compute_tfidf(corpus: List[str]) -> List[Dict[str, float]]:
    docs = [Counter(doc.split()) for doc in corpus]
    df = Counter(term for doc in docs for term in doc)
    n = len(corpus)
    tfidf_docs = []
    for doc in docs:
        doc_tfidf = {}
        for term, count in doc.items():
            tf = count / sum(doc.values())
            idf = math.log((n + 1) / (df[term] + 1)) + 1
            doc_tfidf[term] = tf * idf
        tfidf_docs.append(doc_tfidf)
    return tfidf_docs

print(compute_tfidf(["ai is good", "ai is powerful"]))
```

## Coding Question 4: Simple summarization prompt generator

**Problem:** Build a prompt that asks for a concise summary of text.

**Answer:**
```python
from typing import List


def summary_prompt(text: str) -> str:
    return (
        "You are an assistant. Summarize the following text in one short paragraph:\n\n"
        f"{text}\n\n"
        "Summary:"
    )

print(summary_prompt("The model learns from many examples and generalizes to unseen text."))
```

## Coding Question 5: Simple NLP pipeline stub

**Problem:** Implement a pipeline that tokenizes, lowercases, and removes stopwords.

**Answer:**
```python
from typing import List


STOPWORDS = {"the", "is", "and", "a", "of"}


def preprocess(text: str) -> List[str]:
    tokens = text.lower().split()
    return [token for token in tokens if token not in STOPWORDS]

print(preprocess("The AI model is a system of learning."))
# ['ai', 'model', 'system', 'learning.']
```

## Interview Questions

### Question 1: What is a supervisor agent?

**Answer:**
- A supervisor agent oversees other agents and makes high-level decisions.
- It can assign tasks, validate outputs, and handle exceptions.
- Use it when multiple agents need coordination and quality control.
- It improves reliability in complex workflows.

### Question 2: What is a planner agent?

**Answer:**
- A planner agent decomposes a goal into smaller tasks.
- It selects the order and dependencies for execution.
- It is useful for multi-step, structured problems.
- It can feed subtasks to executor agents or tools.

### Question 3: What is a critic agent?

**Answer:**
- A critic agent evaluates outputs and checks for errors or quality problems.
- It can reject, request revision, or approve results.
- It adds a validation layer to agent workflows.
- It is useful for improving accuracy and reducing hallucinations.

### Question 4: How does task decomposition help in agent systems?

**Answer:**
- Decomposition breaks large goals into manageable subtasks.
- It enables parallelism and clearer reasoning.
- It reduces model complexity for each step.
- It also makes debugging and recovery easier.

### Question 5: What is tokenization?

**Answer:**
- Tokenization splits text into tokens, such as words or subwords.
- It is the first step in most NLP and LLM pipelines.
- The tokenization strategy affects model input length and semantics.
- Common methods include whitespace, wordpiece, and byte-pair encoding.

### Question 6: What is lemmatization vs stemming?

**Answer:**
- Stemming trims words to a root form, often crudely (e.g. `running` -> `run`).
- Lemmatization returns the canonical base form using linguistic rules.
- Lemmatization is usually more accurate but slower.
- Use stemming for speed and lemmatization for better semantic quality.

### Question 7: When should you use TF-IDF vs embeddings?

**Answer:**
- TF-IDF is useful for sparse, keyword-based retrieval and classical text search.
- Embeddings are better for semantic search and meaning-based retrieval.
- TF-IDF works well for exact-match, domain-specific queries.
- Use embeddings when intent and similarity matter more than term frequency.

### Question 8: What is BM25?

**Answer:**
- BM25 is a ranking function for keyword-based retrieval.
- It improves on TF-IDF by normalizing term frequency and document length.
- It is widely used in search engines for relevance scoring.
- It is a good hybrid retrieval baseline with embeddings.
