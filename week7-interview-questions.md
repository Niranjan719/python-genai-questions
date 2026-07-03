# Week 7 — MLOps / Cloud / System Design Interview Questions and Answers

This file includes coding questions, answers, and interview Q&A for Week 7: MLOps, cloud deployment, and system design.

## Coding Question 1: Simple deployment checklist generator

**Problem:** Create a function that returns a deployment checklist for GCP or AWS.

**Answer:**
```python
from typing import List


def deployment_checklist(provider: str) -> List[str]:
    base = ["use HTTPS", "secure secrets", "enable logging"]
    if provider.lower() == "gcp":
        return base + ["use GKE or Cloud Run", "store secrets in Secret Manager", "use Pub/Sub for events"]
    if provider.lower() == "aws":
        return base + ["use ECS/EKS or Lambda", "store secrets in Secrets Manager", "use S3 and SNS/SQS"]
    raise ValueError("Unknown provider")

print(deployment_checklist("gcp"))
```

## Coding Question 2: Format a model evaluation report

**Problem:** Build a report from evaluation metrics.

**Answer:**
```python
from typing import Dict


def format_evaluation(metrics: Dict[str, float]) -> str:
    lines = [f"{name}: {value:.4f}" for name, value in metrics.items()]
    return "\n".join(lines)

print(format_evaluation({"accuracy": 0.92, "f1": 0.87}))
```

## Coding Question 3: Compute simple cost per request

**Problem:** Calculate total cost for a model based on request volume and per-request cost.

**Answer:**
```python
from typing import List, Dict


def cost_estimate(requests: int, cost_per_request: float, overhead: float = 0.0) -> float:
    return requests * cost_per_request + overhead

print(cost_estimate(10000, 0.0005, overhead=50.0))
```

## Coding Question 4: Schedule retraining based on drift signal

**Problem:** Return `True` when drift metrics exceed thresholds.

**Answer:**
```python
from typing import Dict


def should_retrain(metrics: Dict[str, float], thresholds: Dict[str, float]) -> bool:
    return any(metrics.get(name, 0.0) > thresholds.get(name, float("inf")) for name in thresholds)

print(should_retrain({"precision": 0.7, "recall": 0.6}, {"precision": 0.75}))
```

## Coding Question 5: Build a simple service health summary

**Problem:** Summarize service health from status flags.

**Answer:**
```python
from typing import Dict


def health_summary(status: Dict[str, bool]) -> str:
    unhealthy = [name for name, healthy in status.items() if not healthy]
    if not unhealthy:
        return "All systems healthy"
    return f"Unhealthy: {', '.join(unhealthy)}"

print(health_summary({"db": True, "api": False, "cache": True}))
```

## Interview Questions

### Question 1: What is prompt versioning?

**Answer:**
- Prompt versioning tracks changes to prompts just like code.
- It helps compare behavior, reproduce results, and rollback bad prompts.
- Use Git, ML metadata stores, or prompt registry tools.
- It is important for model governance and evaluation.

### Question 2: What is model registry and why is it important?

**Answer:**
- A model registry stores model versions, metadata, and deployment status.
- It enables reproducibility, auditability, and controlled rollouts.
- It supports staged promotion from dev to prod.
- It is essential for managing multiple model variants and governance.

### Question 3: How do you monitor LLM applications?

**Answer:**
- Monitor latency, error rates, request volume, and throughput.
- Track prompt usage, token cost, and output quality.
- Log unexpected outputs, hallucinations, and security incidents.
- Use observability tools with dashboards and alerts.

### Question 4: How do you reduce LLM costs by 70%?

**Answer:**
- Use shorter prompts and compress context.
- Cache responses for repeated queries.
- Choose cheaper or smaller models when accuracy allows.
- Batch requests, use retrieval augmentation, and prune unnecessary calls.

### Question 5: What is canary deployment?

**Answer:**
- Canary deployment rolls out a new version to a small subset of users first.
- It allows monitoring and validation before full production release.
- If issues occur, rollback is easier.
- It reduces risk for model updates and infrastructure changes.

### Question 6: What is A/B testing for ML systems?

**Answer:**
- A/B testing compares two variants with live traffic.
- It measures impact on metrics like accuracy, engagement, or cost.
- It helps choose the best model or prompt with data.
- Use proper traffic splitting and statistical analysis.

### Question 7: How do you secure AI systems in cloud deployment?

**Answer:**
- Use IAM to restrict access to services and secrets.
- Encrypt data in transit and at rest.
- Protect APIs with auth, rate limiting, and WAF.
- Isolate workloads with VPCs, private endpoints, and service accounts.

### Question 8: What are common system design trade-offs for GenAI services?

**Answer:**
- Latency vs accuracy: larger models produce better results but slower responses.
- Cost vs quality: more expensive models and infrastructure improve experience.
- Scalability vs complexity: distributed systems scale but require more orchestration.
- Observability vs performance: extensive logging can add overhead but improves diagnosis.
