# Week 4 — Embeddings and RAG Interview Questions and Answers

This file includes coding questions, answers, and interview Q&A for Week 4: embeddings, similarity, and RAG design.

## Coding Question 1: Normalize a vector

**Problem:** Implement a function that normalizes a numeric vector to unit length.

**Answer:**
```python
import math
from typing import Sequence, List


def normalize(vector: Sequence[float]) -> List[float]:
    norm = math.sqrt(sum(x * x for x in vector))
    if norm == 0:
        return [0.0 for _ in vector]
    return [x / norm for x in vector]

print(normalize([3, 4]))
# [0.6, 0.8]
```

## Coding Question 2: Compute cosine similarity and Euclidean distance

**Problem:** Write functions for cosine similarity and Euclidean distance.

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


def euclidean_distance(a: Sequence[float], b: Sequence[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

print(cosine_similarity([1, 0], [0, 1]))
print(euclidean_distance([1, 0], [0, 1]))
```

## Coding Question 3: Chunk text into overlapping spans

**Problem:** Implement text chunking with overlap.

**Answer:**
```python
from typing import List


def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    tokens = text.split()
    if chunk_size <= 0 or overlap >= chunk_size:
        raise ValueError("Invalid chunk_size or overlap")

    chunks = []
    start = 0
    while start < len(tokens):
        end = start + chunk_size
        chunks.append(" ".join(tokens[start:end]))
        if end >= len(tokens):
            break
        start += chunk_size - overlap
    return chunks

print(chunk_text("This is a sample text for chunking and retrieval testing.", 5, 2))
```

## Coding Question 4: Simple nearest neighbor search

**Problem:** Given vectors and a query, return the top k closest items by cosine similarity.

**Answer:**
```python
from heapq import nlargest
from typing import List, Tuple


def top_k_similar(query, vectors, k=3):
    scores = [(cosine_similarity(query, vec), idx) for idx, vec in enumerate(vectors)]
    return [idx for _, idx in nlargest(k, scores)]


vectors = [[1, 0], [0, 1], [1, 1]]
print(top_k_similar([1, 0], vectors, k=2))
# [0, 2]
```

## Coding Question 5: Build a simple RAG retrieval prompt

**Problem:** Given retrieved document chunks and a query, create a prompt that includes context and instructions.

**Answer:**
```python
from typing import List


def build_rag_prompt(query: str, chunks: List[str]) -> str:
    context = "\n\n".join(f"Chunk {i+1}: {chunk}" for i, chunk in enumerate(chunks))
    return (
        "You are a document assistant. Use the context below to answer the question.\n\n"
        f"{context}\n\n"
        f"Question: {query}\n"
        "Answer concisely based on the context."
    )

print(build_rag_prompt("What is RAG?", ["RAG combines retrieval and generation.", "It uses embeddings and vector search."]))
```

## Interview Questions

### Question 1: What is an embedding?

**Answer:**
- An embedding is a numeric vector representation of text.
- It captures semantic relationships so similar text maps to nearby vectors.
- Embeddings support search, clustering, ranking, and retrieval.

### Question 2: What is the difference between token, sentence, and document embeddings?

**Answer:**
- Token embeddings represent individual tokens or words.
- Sentence embeddings represent the meaning of a full sentence.
- Document embeddings represent the meaning of an entire document or chunk.
- Use larger embeddings for broader context and smaller embeddings for fine-grained matching.

### Question 3: Why use cosine similarity for text embeddings?

**Answer:**
- Cosine similarity measures direction rather than magnitude.
- It is robust when vector length varies due to text length.
- It often better reflects semantic similarity in embedding spaces.
- Normalize embeddings to compare cosine values directly.

### Question 4: What is chunking and why is overlap important?

**Answer:**
- Chunking splits long documents into smaller pieces for embedding and retrieval.
- Overlap preserves context between adjacent chunks.
- It helps reduce information loss at chunk boundaries.
- Choose chunk size and overlap based on document structure and model context window.

### Question 5: What is RAG and when should you use it?

**Answer:**
- RAG stands for Retrieval-Augmented Generation.
- It retrieves relevant context from external documents and passes it to a generator.
- Use RAG when your model needs up-to-date or domain-specific knowledge not stored in weights.
- It improves factuality and reduces hallucinations for knowledge-heavy tasks.

### Question 6: What is hybrid search?

**Answer:**
- Hybrid search combines semantic vector search with traditional keyword search.
- It improves recall by using both relevance and exact matches.
- Useful when queries contain important exact terms or entities.
- Many vector DBs support hybrid filtering with metadata and text expressions.

### Question 7: What is maximum marginal relevance (MMR)?

**Answer:**
- MMR balances relevance and diversity in retrieval.
- It selects documents that are relevant to the query while avoiding redundancy.
- It is useful when you want varied supporting evidence.
- MMR helps reduce repeated or overly similar results.

### Question 8: What is the "lost in the middle" problem?

**Answer:**
- It occurs when long context spans exceed the model’s effective attention capacity.
- Earlier or later context becomes less influential in the final output.
- It can happen with long prompt context or many document chunks.
- Mitigation techniques include reranking, context compression, chunk pruning, and retrieval augmentation.
