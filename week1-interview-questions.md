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

## Additional Coding Questions

### Q1: K most frequent elements

Problem: You are given a list of unsorted integers. Write a Python function that returns the k most frequent elements in descending order of frequency.

The implementation below follows your original logic: build a frequency dict, convert to list, sort by frequency descending, and return the top-k keys. The example prints both inputs and outputs.

```python
def most_frequest_nums(nums, k):
    empty_dict = {}
    for num in nums:
        empty_dict[num] = empty_dict.get(num, 0) + 1
    work_list = list(empty_dict.items())
    work_list.sort(key=lambda x: x[1], reverse=True)
    print("Frequency list (value, count):", work_list)
    answer_list = []
    for item in work_list[:k]:
        answer_list.append(item[0])
    return answer_list

# Inputs
list1 = [1, 2, 1, 2, 1, 3, 4, 5, 4, 4]
k = 2

# Run
ans = most_frequest_nums(list1, k)
print("Input:", list1)
print("k:", k)
print("Output:", ans)  # Expected: [1, 4]
```

### Q2: All unique pairs summing to target

Problem: Given a list of integers and a target sum, return all unique pairs of elements that add up to the target.

```python
def find_pairs(nums, target):
    pairs = set()
    seen = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return pairs

# Example usage:
nums = [2, 4, 3, 5, 2, 3, 4, 7, 8, 1]
target = 9
print(find_pairs(nums, target))  # {(1, 8), (2, 7), (4, 5)}
```

### Q3: Rotate list to the right by k steps

Problem: Write a function that rotates a list to the right by k steps.

```python
def rotate_list(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    if k == 0:
        return nums
    return nums[-k:] + nums[:-k]

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate_list(nums, k))  # [5,6,7,1,2,3,4]
```

### Q4: Longest Increasing Subsequence (LIS)

Problem: Given a list of integers, write a function to find the longest increasing subsequence.

```python
def longest_increasing_subsequence(nums):
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    max_index = dp.index(max_length)

    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]

    return lis[::-1]

nums = [10,22,9,33,21,50,41,60,80]
print(longest_increasing_subsequence(nums))  # example output
```

### Q5: Intersection of two lists

Problem: Write a function to find the intersection of two lists.

```python
def intersection_of_lists(list1, list2):
    return list(set(list1).intersection(set(list2)))

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
print(intersection_of_lists(list1, list2))  # [4,5] (order may vary)
```

### Q6: Longest substring without repeating characters

Problem: Given a string, find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

s = "abcabcbb"
print(length_of_longest_substring(s))  # 3
```

### Q7: Palindrome check

Problem: Write a function to check if a string is a palindrome.

```python
def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    return s == s[::-1]

print(is_palindrome("Racecar"))  # True
```

### Q8: Maximum product of two distinct elements

Problem: Given a list of integers, write a function to find the maximum product of two distinct elements.

```python
def max_product_of_two(nums):
    if len(nums) < 2:
        return None
    # Handle negatives as well: consider two smallest (most negative) values
    nums_sorted = sorted(nums)
    return max(nums_sorted[-1] * nums_sorted[-2], nums_sorted[0] * nums_sorted[1])

nums = [3,5,1,7,9]
print(max_product_of_two(nums))  # 63
```
