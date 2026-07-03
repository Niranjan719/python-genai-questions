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

## Transformer, Fine-tuning, and RAG Interview Questions

### Question 1: What is the Transformer architecture and why is it important?

**Answer:**
- Transformer is a neural architecture built around self-attention, which computes relationships between all input tokens in parallel.
- It replaces recurrence and convolutions, enabling much better scaling for long-range dependencies.
- Transformers are the foundation for modern language models because they support pretraining on massive corpora and efficient fine-tuning.
- Key components are multi-head attention, feed-forward networks, residual connections, and layer normalization.

### Question 2: How do encoder-only, decoder-only, and encoder-decoder Transformers differ?

**Answer:**
- Encoder-only models like BERT process the full input bidirectionally and are best for understanding tasks such as classification and extraction.
- Decoder-only models like GPT generate text autoregressively, predicting the next token from left-to-right context.
- Encoder-decoder models like T5 and BART use an encoder to build a representation of the source and a decoder to generate output, making them ideal for sequence-to-sequence tasks like translation and summarization.

### Question 3: What role does positional encoding play in Transformers?

**Answer:**
- Since self-attention has no inherent notion of token order, positional encoding injects sequence position information into token embeddings.
- Common options are sinusoidal encodings and learned position embeddings.
- Positional encoding allows the model to distinguish "first word" from "last word" and capture relative order.
- For long sequences, relative positional encodings or rotary embeddings can improve generalization.

### Question 4: Explain the encoder-decoder attention mechanism.

**Answer:**
- In encoder-decoder models, the decoder attends to encoder outputs using cross-attention.
- The decoder's queries come from earlier decoder layers, while keys and values come from encoded source representations.
- This allows the generated output to condition on the full source context.
- Cross-attention is what makes translation, summarization, and RAG-style generation work effectively.

### Question 5: What are the main fine-tuning strategies for large language models?

**Answer:**
- Full fine-tuning updates all model parameters and is simple but expensive in memory and compute.
- Head-only fine-tuning changes only the task-specific output layer, which is efficient but may underfit.
- Parameter-efficient methods like LoRA, adapters, and prompt tuning keep most weights frozen and learn a small set of extra parameters.
- Choice depends on model size, dataset size, deployment constraints, and whether you need to preserve the base model for multiple tasks.

### Question 6: How does Retrieval-Augmented Generation (RAG) use embeddings?

**Answer:**
- RAG uses embeddings to encode documents and queries into the same vector space for semantic search.
- A retriever finds the most relevant documents based on embedding similarity.
- Those retrieved chunks are then passed to a generator for answer synthesis.
- Embeddings make RAG robust to paraphrasing and allow it to fetch domain-specific knowledge beyond the model's weights.

### Question 7: What differences exist between embedding models and generation models?

**Answer:**
- Embedding models are optimized to produce dense vector representations for similarity, retrieval, classification, or clustering.
- Generation models are optimized to produce fluent token sequences for text completion, conversation, or summarization.
- Embedding models usually output a fixed-length vector, while generation models output token probabilities over a vocabulary.
- In a RAG pipeline, embedding models are used for retrieval and generation models are used for response construction.

### Question 8: Which hyperparameters matter most when training or fine-tuning Transformers?

**Answer:**
- Learning rate is the single most important hyperparameter; too high causes divergence and too low slows learning.
- Batch size affects optimization stability and generalization; larger batches often need learning rate scaling.
- Sequence length determines context capacity and memory usage.
- Model depth, number of attention heads, hidden dimension, and dropout control model capacity and regularization.
- Warmup steps, weight decay, and gradient clipping are also critical in practice.

### Question 9: How should you choose a learning rate schedule for Transformer fine-tuning?

**Answer:**
- Use a small initial learning rate because pretrained models can be sensitive to large updates.
- A linear warmup followed by cosine or linear decay is a common pattern.
- Warmup helps the optimizer stabilize before reaching the target rate.
- For small datasets, shorter training with early stopping is safer than aggressive schedules.

### Question 10: What common issues arise with RAG and how do you mitigate them?

**Answer:**
- Hallucination: use better retriever quality, evidence grounding, and prompt constraints.
- Irrelevant retrieval: improve embeddings, tune similarity thresholds, or add re-ranking.
- Context window overflow: chunk documents and limit retrieved tokens.
- Refreshing stale knowledge: update the retriever corpus and re-embed documents regularly.
