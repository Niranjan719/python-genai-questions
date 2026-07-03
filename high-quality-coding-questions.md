# High-Quality Python Coding Questions for Interview Preparation

This file contains interview-style Python problems with clear descriptions, constraints, sample inputs, sample outputs, and concise example solutions.

## 1) Most Frequent Elements

**Problem:** Given an unsorted list of integers `nums` and an integer `k`, return the `k` most frequent elements in descending order of frequency. If two elements have the same frequency, return the smaller element first.

**Constraints:** `1 <= k <= len(nums)`, `nums` may contain duplicates.

**Sample Input:** `nums = [1, 2, 1, 2, 1, 3, 4, 5, 4, 4]`, `k = 2`

**Sample Output:** `[1, 4]`

**Solution:**
```python
from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    return sorted(counts, key=lambda x: (-counts[x], x))[:k]
```

---

## 2) Unique Pairs with Target Sum

**Problem:** Given a list of integers and a target value, return all unique pairs of numbers that add up to the target. Each pair should be returned in ascending order, and the result can be in any order.

**Sample Input:** `nums = [2, 4, 3, 5, 2, 3, 4, 7, 8, 1]`, `target = 9`

**Sample Output:** `[(1, 8), (2, 7), (4, 5)]`

**Solution:**
```python
def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        comp = target - num
        if comp in seen:
            pairs.add(tuple(sorted((num, comp))))
        seen.add(num)
    return sorted(pairs)
```

---

## 3) Rotate List Right by K Steps

**Problem:** Rotate a list of integers to the right by `k` steps. If `k` is greater than the length of the list, use `k % len(nums)`.

**Sample Input:** `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`

**Sample Output:** `[5, 6, 7, 1, 2, 3, 4]`

**Solution:**
```python
def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n
    return nums[-k:] + nums[:-k]
```

---

## 4) Longest Increasing Subsequence (LIS)

**Problem:** Given a list of integers, find the longest strictly increasing subsequence. Return any valid subsequence with maximum length.

**Sample Input:** `nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]`

**Sample Output:** `[10, 22, 33, 50, 60, 80]`

**Solution:**
```python
def longest_increasing_subsequence(nums):
    if not nums:
        return []
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
    idx = max(range(n), key=lambda i: dp[i])
    lis = []
    while idx != -1:
        lis.append(nums[idx])
        idx = prev[idx]
    return lis[::-1]
```

---

## 5) Longest Substring Without Repeating Characters

**Problem:** Given a string, find the length of the longest substring that contains no duplicate characters.

**Sample Input:** `s = "abcabcbb"`

**Sample Output:** `3`  *(substring: "abc")*

**Solution:**
```python
def length_of_longest_substring(s):
    last_index = {}
    start = 0
    longest = 0
    for i, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= start:
            start = last_index[ch] + 1
        last_index[ch] = i
        longest = max(longest, i - start + 1)
    return longest
```

---

## 6) Word Frequency Count

**Problem:** Given an English sentence, count the frequency of each word, ignoring punctuation and case.

**Sample Input:** `sentence = "Hello, hello! This is a test. This test is simple."`

**Sample Output:** `{'hello': 2, 'this': 2, 'is': 2, 'test': 2, 'a': 1, 'simple': 1}`

**Solution:**
```python
def word_frequency(sentence):
    sentence = ''.join(ch.lower() if ch.isalnum() or ch.isspace() else ' ' for ch in sentence)
    freqs = {}
    for word in sentence.split():
        freqs[word] = freqs.get(word, 0) + 1
    return freqs
```

---

## 7) Merge Overlapping Intervals

**Problem:** Given a list of closed intervals `[start, end]`, merge all overlapping intervals and return a new list of merged intervals.

**Sample Input:** `intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]`

**Sample Output:** `[[1, 6], [8, 10], [15, 18]]`

**Solution:**
```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged
```

---

## 8) Binary Search

**Problem:** Given a sorted list and a target, return the index of the target if found; otherwise, return `-1`.

**Sample Input:** `nums = [1, 2, 4, 5, 7, 9]`, `target = 5`

**Sample Output:** `3`

**Solution:**
```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

---

## 9) Valid Parentheses

**Problem:** Given a string containing only `()[]{}`, determine whether it is valid. The brackets must close in the correct order.

**Sample Input:** `s = "()[]{}"`

**Sample Output:** `True`

**Solution:**
```python
def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

---

## 10) Remove Duplicates from Sorted Array In-Place

**Problem:** Given a sorted list, remove duplicates in-place and return the new length.

**Sample Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`

**Sample Output:** `5`  and `nums[:5] = [0,1,2,3,4]`

**Solution:**
```python
def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

---

## 11) Product of Array Except Self

**Problem:** Return a list where each element is the product of all other elements in the input list. Do not use division.

**Sample Input:** `nums = [1, 2, 3, 4]`

**Sample Output:** `[24, 12, 8, 6]`

**Solution:**
```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result
```

---

## 12) Group Anagrams

**Problem:** Given a list of strings, group anagrams together. Return a list of groups.

**Sample Input:** `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

**Sample Output:** `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

**Solution:**
```python
def group_anagrams(strs):
    buckets = {}
    for s in strs:
        key = ''.join(sorted(s))
        buckets.setdefault(key, []).append(s)
    return list(buckets.values())
```

---

## 13) Evaluate Reverse Polish Notation

**Problem:** Evaluate the value of an arithmetic expression in Reverse Polish Notation.

**Sample Input:** `tokens = ["2", "1", "+", "3", "*"]`

**Sample Output:** `9`

**Solution:**
```python
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            else: stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]
```

---

## 14) Majority Element

**Problem:** Given an array of size `n`, find the element that appears more than `n/2` times. You may assume such element always exists.

**Sample Input:** `nums = [3, 2, 3]`

**Sample Output:** `3`

**Solution:**
```python
def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
```

---

## 15) Count Islands in a Grid

**Problem:** Given a 2D grid of `'1'` (land) and `'0'` (water), count the number of islands. An island is surrounded by water and connected horizontally or vertically.

**Sample Input:**
```
grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
```

**Sample Output:** `3`

**Solution:**
```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
```

---

## 16) Rotate Matrix by 90 Degrees In-Place

**Problem:** Given an `n x n` matrix, rotate it by 90 degrees clockwise in place.

**Sample Input:**
```
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
```

**Sample Output:**
```
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**Solution:**
```python
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp
```

---

## 17) Longest Common Prefix

**Problem:** Write a function to find the longest common prefix string among an array of strings.

**Sample Input:** `strs = ["flower", "flow", "flight"]`

**Sample Output:** `"fl"`

**Solution:**
```python
def longest_common_prefix(strs):
    if not strs:
        return ''
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest
```

---

## 18) Find the First Unique Character

**Problem:** Given a string, return the index of the first non-repeating character. If it does not exist, return `-1`.

**Sample Input:** `s = "loveleetcode"`

**Sample Output:** `2`

**Solution:**
```python
def first_unique_char(s):
    freqs = {}
    for ch in s:
        freqs[ch] = freqs.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freqs[ch] == 1:
            return i
    return -1
```

---

## 19) Find the Missing Number

**Problem:** Given an array containing `n` distinct numbers taken from `0, 1, 2, ..., n`, find the missing number.

**Sample Input:** `nums = [3, 0, 1]`

**Sample Output:** `2`

**Solution:**
```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
```

---

## 20) Find the Maximum Product of Two Numbers

**Problem:** Given a list of integers, return the maximum product of two distinct elements. The list may include negative numbers.

**Sample Input:** `nums = [3, 5, -2, -8, 4]`

**Sample Output:** `40`  *(because -8 * -5 or 8*5, depending on values)*

**Solution:**
```python
def max_product_of_two(nums):
    if len(nums) < 2:
        return None
    nums.sort()
    return max(nums[-1] * nums[-2], nums[0] * nums[1])
```

---

## 21) Fibonacci Number (Iterative)

**Problem:** Return the `n`th Fibonacci number using an iterative method.

**Sample Input:** `n = 6`

**Sample Output:** `8`

**Solution:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

## 22) Power Function Using Fast Exponentiation

**Problem:** Implement `x^n` for integer exponent `n`, handling negative exponents.

**Sample Input:** `x = 2.0`, `n = -2`

**Sample Output:** `0.25`

**Solution:**
```python
def fast_power(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1.0
    while n > 0:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
```

---

## 23) Check Power of Two

**Problem:** Determine whether an integer is a power of two.

**Sample Input:** `n = 16`

**Sample Output:** `True`

**Solution:**
```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

---

## 24) Flatten Nested List Recursively

**Problem:** Given a nested list of integers, flatten it into a single list in order.

**Sample Input:** `nested = [1, [2, [3, 4], 5], 6]`

**Sample Output:** `[1, 2, 3, 4, 5, 6]`

**Solution:**
```python
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```

---

## 25) Count the Number of 1 Bits

**Problem:** Given an integer, return the number of `1` bits it has.

**Sample Input:** `n = 11`  *(binary: `1011`)*

**Sample Output:** `3`

**Solution:**
```python
def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```
