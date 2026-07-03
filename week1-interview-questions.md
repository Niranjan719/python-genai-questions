# Week 1 — Python Interview Questions and Answers

This file includes coding questions, answers, and interview Q&A for Week 1: Python fundamentals.

## Coding Question 1: Decorator with optional arguments

**Problem:** Write a decorator `retry` that retries a function up to `n` times when it raises an exception.

**Answer:**
```python
from functools import wraps
import time


def retry(max_attempts=3, delay=0.1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


@retry(max_attempts=4, delay=0.2)
def unstable_operation(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    return x * 2

print(unstable_operation(2))
```

## Coding Question 2: Generator to flatten nested lists

**Problem:** Implement `flatten(nested_list)` as a generator that yields values from arbitrarily nested lists.

**Answer:**
```python
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, 3], [4, [5, 6], []], 7])))
# [1, 2, 3, 4, 5, 6, 7]
```

## Coding Question 3: Custom context manager for timing

**Problem:** Create a context manager `timing(label)` that prints elapsed time.

**Answer:**
```python
import time


class timing:
    def __init__(self, label="block"):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        elapsed = time.perf_counter() - self.start
        print(f"{self.label} elapsed={elapsed:.4f}s")


with timing("example"):
    total = sum(range(1000000))
```

## Coding Question 4: Async producer-consumer with queue

**Problem:** Use `asyncio` to implement producer and consumer tasks sharing an `asyncio.Queue`.

**Answer:**
```python
import asyncio


async def producer(queue):
    for i in range(5):
        await asyncio.sleep(0.1)
        await queue.put(i)
        print(f"produced {i}")
    await queue.put(None)


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"consumed {item}")
    print("consumer done")


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
```

## Coding Question 5: BFS on a graph using adjacency list

**Problem:** Given a graph as a dict, return BFS traversal from a start node.

**Answer:**
```python
from collections import deque


def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
print(bfs(graph, "A"))
# ['A', 'B', 'C', 'D', 'E', 'F']
```

## Interview Questions

### Question 1: Explain Python's GIL

**Answer:**
- Python’s Global Interpreter Lock ensures only one thread executes Python bytecode at a time in CPython.
- It simplifies memory management and prevents race conditions in native object access.
- It limits CPU-bound threading performance, so use multiprocessing or native extensions for parallel CPU work.
- I/O-bound tasks still benefit from threading because the GIL is released during blocking I/O operations.

### Question 2: When should you use `multiprocessing` vs `threading`?

**Answer:**
- Use `threading` for I/O-bound workloads where tasks spend most time waiting on network, disk, or database calls.
- Use `multiprocessing` for CPU-bound workloads that need multiple CPUs, because it spawns separate processes and bypasses the GIL.
- Keep in mind `multiprocessing` has higher overhead for startup and data sharing.

### Question 3: How do decorators work?

**Answer:**
- A decorator takes a function and returns a wrapper function with additional behavior.
- The wrapper has the same signature and can run code before and after calling the original function.
- Use `functools.wraps` to preserve metadata like `__name__` and `__doc__`.
- They are useful for cross-cutting concerns like logging, caching, retries, auth, and metrics.

### Question 4: What is a generator and when should you use one?

**Answer:**
- A generator is a function that uses `yield` to produce values lazily.
- It avoids building large intermediate lists and is memory-efficient for streams of data.
- Use generators for pipelines, file processing, tree traversal, and infinite sequences.
- A generator preserves state across yields and can be composed with `yield from`.

### Question 5: Explain `@dataclass` and its benefits

**Answer:**
- `@dataclass` automatically generates `__init__`, `__repr__`, `__eq__`, and other methods for classes.
- It reduces boilerplate for data containers and improves readability.
- Use `field(default_factory=...)` for mutable defaults.
- It works well with type hints and can integrate with serialization or validation libraries.
