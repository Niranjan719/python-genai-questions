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

## Scenario-Based GenAI and Agentic AI Questions

### Question 9: A client needs a GenAI assistant to summarize financial reports, but the model frequently hallucinates numbers. What would you do?

**Answer:**
- Add retrieval grounding by fetching the relevant document sections before generation.
- Use a prompt that explicitly instructs the model to cite only facts from the provided text.
- Implement a critic or validator agent to check numeric values against the source.
- If needed, use structured data extraction rather than free-form summarization for financial values.

### Question 10: You are building an agentic workflow that extracts customer requests, classifies urgency, and responds automatically. How do you design it?

**Answer:**
- Use a planner agent to decompose the input into intent extraction, urgency classification, and response generation.
- Add a critic agent to verify classification quality and fallback to a safety path if uncertain.
- Keep task-specific nodes separate so each agent or module can be monitored independently.
- Use checkpointing after classification before generating replies to allow audit and retry.

### Question 11: An agent pipeline must interact with multiple tools, and one tool may fail intermittently. How do you handle that?

**Answer:**
- Design retry logic and fallback routes in the workflow graph.
- Add a supervisor or error-handling agent to detect failures and choose alternate tools.
- Use idempotent steps so retries do not produce duplicated side effects.
- Log failure context and expose it to the agent so it can adapt its next action.

### Question 12: A GenAI proof-of-concept works in development but fails in production due to scale. What are the key areas to inspect?

**Answer:**
- Check whether the retriever or embedding index can scale to production data volume.
- Evaluate model latency and whether batching, caching, or smaller models are needed.
- Review workflow orchestration for long-running tasks, retries, and state persistence.
- Validate that prompt length and context windows remain within model limits at scale.

### Question 13: You need to build an agent that performs a multi-step data analysis task and explains its reasoning. What architecture do you use?

**Answer:**
- Use an explicit graph with planner, executor, and critic nodes so reasoning steps are traceable.
- Keep reasoning prompts separate from action prompts to avoid confusion.
- Use a supervisor agent to collect intermediate results and generate a coherent explanation.
- Store intermediate state and decisions so the explanation can be audited later.

### Question 14: A customer asks for a multilingual conversational agent with fallback to human support. How should this be modeled?

**Answer:**
- Use language detection as an initial step in the workflow.
- Route non-English or ambiguous cases to a translation or specialized multilingual agent.
- Add a fallback branch that escalates to human support when confidence is low.
- Track user context and prior messages so handoff is seamless.

### Question 15: A retrieval-augmented agent returns conflicting answers from different documents. How do you handle it?

**Answer:**
- Add a re-ranking or consensus step to prefer higher-confidence, more authoritative sources.
- Use a critic agent to compare retrieved evidence and flag contradictions.
- Present the discrepancy transparently in the response if the conflict cannot be resolved.
- Improve retrieval filtering so unrelated or low-quality documents are excluded.

### Question 16: If asked to improve an agentic system without changing the base model, what options do you consider?

**Answer:**
- Improve prompt engineering and prompt templates to steer behavior more reliably.
- Add retrieval grounding, tool chaining, and better state management.
- Introduce critic or verifier agents to catch errors before they become user-visible.
- Optimize workflow orchestration, retries, and fallback logic instead of the model itself.

### Question 17: Production agents are returning wrong answers. What operational changes would you make?

**Answer:**
- Add monitoring and logging for agent outputs, including failure rates and answer drift.
- Deploy a critic or verification agent that checks responses against trusted sources or business rules.
- Implement a fallback path that routes uncertain or low-confidence results to a safe response or human review.
- Use root cause analysis to determine if the issue is prompt, retrieval, tool input, or data quality.

### Question 18: How do you handle a production DB whose data is continuously changing for a retrieval-augmented agent?

**Answer:**
- Implement incremental re-indexing or near-real-time embedding refresh for changed records.
- Use a data freshness strategy: timestamp metadata, set TTLs, and prioritize recently updated content.
- Add validation to detect stale embeddings and trigger updates when source data changes.
- Combine dynamic retrieval with short-lived caching and fallback to direct database queries for critical cases.

### Question 19: What do you do if an agent frequently returns cached results after the underlying DB has updated?

**Answer:**
- Invalidate or refresh cache entries when the source data changes.
- Use versioning or content hashes on documents to detect stale cache and embeddings.
- Prefer a hybrid approach: serve cached results only when the data is unchanged and otherwise re-run retrieval.
- Monitor cache hit/miss ratios and stale-response incidents so the caching policy can be tuned.

### Question 20: The agent is producing inconsistent answers because source documents are updated often. How do you preserve correctness?

**Answer:**
- Use document provenance metadata so each answer includes the version or timestamp of the source.
- Re-rank retrieved passages by recency and relevance, giving preference to newer trusted content.
- Add a verification step that compares answers against the latest authoritative data.
- Design the prompt to emphasize "answer based only on the most recent source material."

### Question 21: How should you monitor data drift for a GenAI system in production?

**Answer:**
- Track metrics such as answer accuracy, hallucination rate, retrieval relevance, and query distribution shifts.
- Monitor source data changes, embedding quality, and retriever performance over time.
- Set alerts for anomalous behavior, such as sudden drops in validation score or spikes in failed responses.
- Periodically audit agent outputs against human-reviewed cases to detect drift early.
