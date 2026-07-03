# Week 5 — Vector DBs and LangChain / LangGraph Interview Questions and Answers

This file includes coding questions, answers, and interview Q&A for Week 5: vector databases, LangChain, and LangGraph.

## Coding Question 1: Build a vector DB comparison table

**Problem:** Create a simple dict of vector DB features.

**Answer:**
```python
vector_db_comparison = {
    "FAISS": {"type": "local", "ann": True, "metadata": "limited"},
    "Pinecone": {"type": "managed", "ann": True, "metadata": "rich"},
    "Weaviate": {"type": "managed", "ann": True, "metadata": "rich"},
    "Chroma": {"type": "local", "ann": False, "metadata": "good"},
}

print(vector_db_comparison["Pinecone"])
```

## Coding Question 2: Simple metadata filter for search results

**Problem:** Filter a list of documents by metadata key/value.

**Answer:**
```python
from typing import List, Dict


def filter_documents(docs: List[Dict], metadata_key: str, metadata_value) -> List[Dict]:
    return [doc for doc in docs if doc.get("metadata", {}).get(metadata_key) == metadata_value]


docs = [
    {"id": 1, "metadata": {"source": "pdf"}},
    {"id": 2, "metadata": {"source": "web"}},
]
print(filter_documents(docs, "source", "pdf"))
```

## Coding Question 3: LangChain-like simple chain runner

**Problem:** Implement a minimal chain that calls two functions sequentially.

**Answer:**
```python
from typing import Callable, Any, List


class SimpleChain:
    def __init__(self, steps: List[Callable[[Any], Any]]):
        self.steps = steps

    def run(self, input_data):
        result = input_data
        for step in self.steps:
            result = step(result)
        return result


def step1(text):
    return text.upper()


def step2(text):
    return f"Processed: {text}"

chain = SimpleChain([step1, step2])
print(chain.run("hello"))
```

## Coding Question 4: LangGraph-style state transition function

**Problem:** Define a node transition map and a simple router.

**Answer:**
```python
from typing import Dict, Callable


State = str
Transition = Dict[State, State]


transitions: Transition = {
    "start": "validate",
    "validate": "execute",
    "execute": "complete",
}


def route(state: State) -> State:
    return transitions.get(state, "error")

print(route("start"))
print(route("validate"))
```

## Coding Question 5: Example LangChain tool wrapper

**Problem:** Create a simple tool that wraps a callable and logs input.

**Answer:**
```python
from typing import Callable, Any


class Tool:
    def __init__(self, name: str, func: Callable[[Any], Any]):
        self.name = name
        self.func = func

    def run(self, input_data):
        print(f"Running tool {self.name} with input: {input_data}")
        return self.func(input_data)


def uppercase(text: str) -> str:
    return text.upper()

tool = Tool("upper", uppercase)
print(tool.run("hello"))
```

## Interview Questions

### Question 1: Why not use PostgreSQL for vector search?

**Answer:**
- PostgreSQL can do basic vector search but lacks optimized ANN indexes and scale.
- Dedicated vector DBs provide faster similarity search and better index structures.
- They also offer persistence, true distance metrics, and metadata filtering tailored for embeddings.
- Use PostgreSQL only for small or hybrid workloads when simplicity outweighs performance.

### Question 2: What is ANN and why is it useful?

**Answer:**
- ANN stands for Approximate Nearest Neighbor.
- It finds vectors that are close enough, trading a bit of accuracy for much faster search.
- Useful for large embedding collections where exact nearest neighbor search is too slow.
- Most production vector DBs use ANN to scale similarity search.

### Question 3: How do you choose between FAISS, Pinecone, Weaviate, Chroma?

**Answer:**
- Use FAISS for local, offline, high-performance search without managed service overhead.
- Use Pinecone for managed production workloads with simple API-based scaling.
- Use Weaviate when you need schema-based metadata, graph semantics, and hybrid search.
- Use Chroma for lightweight local development or small-scale prototypes.

### Question 4: What are LangChain chains and agents?

**Answer:**
- Chains are sequences of steps that process input and produce output.
- Agents are models that choose tools or actions dynamically based on the prompt.
- Chains are good for deterministic pipelines; agents are useful for open-ended tasks.
- Both can be combined for retrieval, reasoning, and tool orchestration.

### Question 5: What is LangGraph and when is it better than LangChain?

**Answer:**
- LangGraph represents orchestration as nodes and edges with conditional routing.
- It is better when you need stateful flows, branching logic, checkpointing, or resumability.
- LangChain is often simpler for linear or agent-based flows.
- Use LangGraph for complex workflows where execution order depends on runtime signals.

### Question 6: What is a state graph?

**Answer:**
- A state graph is a directed graph of nodes representing processing steps.
- Edges define valid transitions and may include conditional rules.
- It allows explicit modeling of workflow state and error handling.
- Useful for long-running, interruptible, or multi-agent processes.

### Question 7: How do you handle metadata in vector search?

**Answer:**
- Store metadata alongside vectors for filtering, provenance, and retrieval quality.
- Use metadata filters to narrow search results by domain, source, date, or type.
- Combine semantic ranking with metadata constraints for hybrid retrieval.
- Keep metadata keys consistent and searchable across your ingestion pipeline.

### Question 8: What is checkpointing in LangGraph?

**Answer:**
- Checkpointing saves workflow state at defined points.
- It allows resuming from a node after failure or interruption.
- It improves reliability in multi-step or long-running pipelines.
- Use checkpoints for retry, debugging, and auditability.
