# GenAI Interview Preparation Plan

This plan is designed to follow the structure in `instructions.md` and prepare for a realistic EPAM-style interview. It is split into modules, with goals, core topics, hands-on actions, and suggested deliverables.

## Week 1 — Python Foundation

### Goal
Build confidence on Python fundamentals, idioms, and interview-style coding.

### Focus Topics
- OOP, dataclasses, type hints
- Decorators, closures, generators, iterators
- Context managers
- Asyncio, multithreading, multiprocessing, GIL
- Memory management, Pydantic
- List comprehensions, lambdas

### Actions
1. Review and summarize each concept with a one-page note.
2. Solve 3–5 LeetCode-style problems for each topic area:
   - Strings, lists, dictionaries, sets
   - Sliding window, hash maps
   - BFS/DFS, trees, graphs
3. Write a short FastAPI mini-app that uses Pydantic models and background tasks.

### Deliverables
- `python-fundamentals.md`
- A repository folder with solved practice problems and one sample FastAPI service

---

## Week 2 — FastAPI and Backend Patterns

### Goal
Master FastAPI internals and backend design decisions for production apps.

### Focus Topics
- Request lifecycle, DI, middleware
- Auth/JWT/OAuth and security best practices
- Background tasks, async APIs, streaming
- WebSockets, file uploads, exception handling
- Logging, rate limiting

### Actions
1. Draw the FastAPI request lifecycle and DI flow.
2. Build a toy API with:
   - dependency injection
   - JWT auth
   - middleware and exception handlers
   - streaming endpoint and file upload
3. Review performance and concurrency tradeoffs.

### Deliverables
- `fastapi-architecture.md`
- Example code for auth, middleware, and async endpoints

---

## Week 3 — LLM Fundamentals and Prompt Engineering

### Goal
Understand modern transformer internals and prompt strategies.

### Focus Topics
- Transformer architecture, self-attention, multi-head attention
- Positional encoding, decoder-only, encoder-only, encoder-decoder models
- Why GPT works, why BERT differs, why T5 differs
- Zero-shot, few-shot, CoT, ToT, ReAct, function calling, structured output
- Prompt injection, leakage, hallucination, guardrails

### Actions
1. Create a one-page comparison: GPT vs BERT vs T5.
2. Write prompt templates for:
   - summarization
   - instruction following
   - tool calling
3. Design a prompt safety checklist for production.

### Deliverables
- `llm-fundamentals.md`
- `prompt-engineering-cheatsheet.md`

---

## Week 4 — Embeddings and RAG

### Goal
Prepare core RAG concepts, embeddings theory, and retrieval system design.

### Focus Topics
- Embedding vs token vs vector vs sentence/document/chunk embeddings
- Cosine similarity, Euclidean distance, dot product, normalization
- Chunking strategies, hybrid search, parent document retrieval
- Context compression, re-ranking, MMR, semantic vs keyword search
- Lost-in-the-middle, context window, multi-query retrievers

### Actions
1. Build a small RAG prototype with PDF/text chunking and embeddings.
2. Compare vector similarity functions with sample vectors.
3. Document design decisions for a production RAG pipeline.

### Deliverables
- `rag-architecture.md`
- A prototype retrieval script or notebook

---

## Week 5 — Vector DBs and LangChain / LangGraph

### Goal
Master vector DB tradeoffs and the LangChain/LangGraph ecosystem.

### Focus Topics
- FAISS, Pinecone, Weaviate, Chroma, Milvus, Qdrant
- Why not PostgreSQL, ANN basics, metadata filtering, index types
- Persistence and production concerns
- LangChain chains, agents, memory, tools, callbacks, parsers, runnables, streaming
- LangGraph state graph, nodes, edges, routing, checkpointing, memory, interrupts

### Actions
1. Create a comparison matrix for vector databases.
2. Implement a LangChain pipeline using a retriever, chain, and output parser.
3. Explore LangGraph examples for conditional flows and resuming state.

### Deliverables
- `vector-db-comparison.md`
- `langchain-langgraph-notes.md`
- Example code snippets or notebooks

---

## Week 6 — Agentic AI and NLP

### Goal
Deepen agent orchestration knowledge and classical NLP concepts.

### Focus Topics
- Single/multi-agent systems, supervisor/planner/executor/critic agents
- Reflection, planning, task decomposition, tool selection
- NER, POS tagging, tokenization, lemmatization, stemming
- TF-IDF, BM25, text classification, summarization, semantic search

### Actions
1. Design a multi-agent workflow for a realistic use case.
2. Build a simple NLP pipeline for tokenization + NER + summarization.
3. Draft answers for how agent planning and critique improve reliability.

### Deliverables
- `agentic-ai-design.md`
- `nlp-classics.md`
- A small demo pipeline or architecture diagram

---

## Week 7 — MLOps / Cloud / System Design

### Goal
Prepare system design, MLOps practices, and cloud deployment knowledge.

### Focus Topics
- Model registry, prompt versioning, evaluation, tracing, monitoring
- LangSmith, Phoenix, W&B, canary/A-B testing, CI/CD, caching
- Docker, Kubernetes, GKE, Cloud Run, Pub/Sub, Storage, Secret Manager, Vertex AI
- AWS equivalents: Lambda, ECS, EKS, S3, Secrets Manager, SageMaker
- Scalability, latency, security, cost optimization, observability

### Actions
1. Draft architecture for a production AI assistant.
2. Create a deployment checklist for GCP and AWS.
3. Review common system design questions and prepare concise talking points.

### Deliverables
- `mlops-cloud-system-design.md`
- Architecture diagrams for RAG and agentic systems

---

## Week 8 — Mock Interview and Behavioral Prep

### Goal
Practice actual interview flow, coding, architecture, and behavior.

### Focus Topics
- Production issue story, stakeholder communication, ambiguous requirements
- GenAI project end-to-end, latency/cost improvement, mentoring
- Python coding under time pressure
- System design sketching and trade-off explanations

### Actions
1. Do at least one mock interview per week covering:
   - Python coding
   - LLM/RAG architecture
   - System design
   - Behavioral questions
2. Record concise STAR stories for 6 behavioral themes.
3. Review notes and update weak areas.

### Deliverables
- `mock-interview-summary.md`
- A list of candidate answers for high-probability questions

---

## Execution Notes
- Start with the highest-impact modules: Python, FastAPI, RAG, LangChain/LangGraph.
- Keep short written summaries for every module.
- Pair theory with coding or architecture sketches.
- Use the deliverables as a candidate-facing study repository.
- Review weekly and adjust focus to weaker areas.

Good luck. This plan turns `instructions.md` into a concrete interview preparation roadmap.