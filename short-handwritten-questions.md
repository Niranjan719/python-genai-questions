# Handwritten Test — 31 Short Python Coding Questions (with concise solutions)

Use these for fast handwritten coding practice. Each question includes a minimal, readable Python solution.

1) Reverse a string
```python
def rev(s):
    return s[::-1]
```

2) Two-sum (return one pair)
```python
def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        if target - v in seen:
            return (seen[target - v], i)
        seen[v] = i
```

3) K most frequent elements
```python
from collections import Counter

def top_k(nums, k):
    return [x for x,_ in Counter(nums).most_common(k)]
```

4) Rotate list right by k
```python
def rotate(nums, k):
    n=len(nums); k%=n
    return nums[-k:]+nums[:-k]
```

5) Length of longest substring without repeat
```python
def longest_sub(s):
    d={}; start=0; best=0
    for i,c in enumerate(s):
        if c in d and d[c]>=start: start=d[c]+1
        d[c]=i; best=max(best,i-start+1)
    return best
```

6) Check palindrome (alnum)
```python
def is_pal(s):
    t=''.join(ch.lower() for ch in s if ch.isalnum())
    return t==t[::-1]
```

7) Merge two sorted arrays (in new array)
```python
def merge(a,b):
    i=j=0; r=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]: r.append(a[i]); i+=1
        else: r.append(b[j]); j+=1
    r.extend(a[i:]); r.extend(b[j:]); return r
```

8) Binary search (index or -1)
```python
def bsearch(a,x):
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==x: return m
        if a[m]<x: lo=m+1
        else: hi=m-1
    return -1
```

9) Check valid parentheses
```python
def valid_paren(s):
    stack=[]; pairs={')':'(',']':'[','}':'{'}
    for c in s:
        if c in '([{': stack.append(c)
        elif c in pairs:
            if not stack or stack.pop()!=pairs[c]: return False
    return not stack
```

10) First non-repeating char
```python
from collections import Counter

def first_unique(s):
    cnt=Counter(s)
    for i,c in enumerate(s):
        if cnt[c]==1: return i
    return -1
```

11) Remove duplicates in-place (sorted array)
```python
def remove_dups(a):
    if not a: return 0
    write=1
    for i in range(1,len(a)):
        if a[i]!=a[i-1]: a[write]=a[i]; write+=1
    return write
```

12) Power(x,n) (fast pow)
```python
def powr(x,n):
    if n<0: x=1/x; n=-n
    res=1
    while n:
        if n&1: res*=x
        x*=x; n>>=1
    return res
```

13) Fibonacci n (iterative)
```python
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
```

14) Count bits (Hamming weight)
```python
def count_bits(x):
    cnt=0
    while x: x &= x-1; cnt+=1
    return cnt
```

15) Check anagram
```python
def is_anagram(a,b):
    from collections import Counter
    return Counter(a)==Counter(b)
```

16) Group anagrams
```python
from collections import defaultdict

def group_anagrams(words):
    d=defaultdict(list)
    for w in words: d[''.join(sorted(w))].append(w)
    return list(d.values())
```

17) Move zeros to end (in-place)
```python
def move_zeros(a):
    write=0
    for v in a:
        if v!=0: a[write]=v; write+=1
    for i in range(write,len(a)): a[i]=0
```

18) Valid palindrome number (no str conversion optional)
```python
def is_pal_num(x):
    if x<0: return False
    s=str(x); return s==s[::-1]
```

19) Find majority element (>n/2)
```python
def majority(nums):
    cand,count=None,0
    for x in nums:
        if count==0: cand=x
        count += 1 if x==cand else -1
    return cand
```

20) Kth largest (quickselect wrapper)
```python
import random

def kth_largest(a,k):
    k=len(a)-k
    def select(l,r):
        pivot=a[random.randint(l,r)]; i=l
        for j in range(l,r+1):
            if a[j]<=pivot: a[i],a[j]=a[j],a[i]; i+=1
        if i-1==k: return a[i-1]
        if i-1>k: return select(l,i-2)
        return select(i,r)
    return select(0,len(a)-1)
```

21) Square root integer (floor)
```python
def isqrt(x):
    lo,hi=0,x
    while lo<=hi:
        m=(lo+hi)//2
        if m*m==x: return m
        if m*m<x: lo=m+1
        else: hi=m-1
    return hi
```

22) Reverse words in a string
```python
def rev_words(s):
    return ' '.join([w for w in s.split()[::-1]])
```

23) URLify (replace spaces with %20 for given true length)
```python
def urlify(s):
    return s.strip().replace(' ','%20')
```

24) Check power of two
```python
def is_pow2(n):
    return n>0 and (n & (n-1))==0
```

25) Find missing number 0..n
```python
def missing(nums):
    n=len(nums)
    total = n*(n+1)//2
    return total - sum(nums)
```

26) Implement FizzBuzz (list output)
```python
def fizzbuzz(n):
    res=[]
    for i in range(1,n+1):
        if i%15==0: res.append('FizzBuzz')
        elif i%3==0: res.append('Fizz')
        elif i%5==0: res.append('Buzz')
        else: res.append(str(i))
    return res
```

27) Transpose matrix
```python
def transpose(mat):
    return [list(row) for row in zip(*mat)]
```

28) Spiral order of matrix
```python
def spiral(mat):
    res=[]
    while mat:
        res+=mat.pop(0)
        if not mat or not mat[0]: break
        mat=[list(x) for x in zip(*mat)][::-1]
    return res
```

29) Check if two intervals overlap
```python
def overlap(a,b):
    return a[0]<=b[1] and b[0]<=a[1]
```

30) Longest common prefix
```python
def lcp(strs):
    if not strs: return ''
    s=min(strs); t=max(strs)
    i=0
    while i<len(s) and s[i]==t[i]: i+=1
    return s[:i]
```

31) Count occurrences of substring (non-overlapping)
```python
def count_sub(s, sub):
    cnt=0; i=0
    while True:
        i=s.find(sub,i)
        if i==-1: break
        cnt+=1; i+=len(sub)
    return cnt
```

32) Merge intervals (list of [start,end])
```python
def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort()
    res=[intervals[0]]
    for s,e in intervals[1:]:
        last_s,last_e=res[-1]
        if s<=last_e: res[-1][1]=max(last_e,e)
        else: res.append([s,e])
    return res
```

33) Validate BST (inorder)
```python
def is_bst(root):
    prev=[None]
    def dfs(n):
        if not n: return True
        if not dfs(n.left): return False
        if prev[0] is not None and n.val<=prev[0]: return False
        prev[0]=n.val
        return dfs(n.right)
    return dfs(root)
```

34) Find LCA in BST
```python
def lca_bst(root,p,q):
    node=root
    while node:
        if p.val<node.val and q.val<node.val: node=node.left
        elif p.val>node.val and q.val>node.val: node=node.right
        else: return node
```

35) Count islands in grid (DFS)
```python
def num_islands(grid):
    if not grid: return 0
    m,n=len(grid),len(grid[0])
    def dfs(i,j):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]=='0': return
        grid[i][j]='0'
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]: dfs(i+di,j+dj)
    cnt=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='1': cnt+=1; dfs(i,j)
    return cnt
```

36) Check power of three
```python
def is_pow3(n):
    if n<1: return False
    while n%3==0: n//=3
    return n==1
```

37) Zigzag conversion (string)
```python
def zigzag(s,rows):
    if rows==1: return s
    rails=['']*rows; r=0; step=1
    for c in s:
        rails[r]+=c
        if r==0: step=1
        if r==rows-1: step=-1
        r+=step
    return ''.join(rails)
```

38) Evaluate RPN
```python
def eval_rpn(tokens):
    st=[]
    for t in tokens:
        if t in '+-*/':
            b=st.pop(); a=st.pop()
            st.append(int(eval(str(a)+t+str(b))))
        else: st.append(int(t))
    return st[0]
```

39) Count trailing zeros in n! (factorial)
```python
def trailing_zeros(n):
    cnt=0
    i=5
    while i<=n:
        cnt+=n//i; i*=5
    return cnt
```

40) Next permutation (in-place)
```python
def next_perm(a):
    n=len(a); i=n-2
    while i>=0 and a[i]>=a[i+1]: i-=1
    if i>=0:
        j=n-1
        while a[j]<=a[i]: j-=1
        a[i],a[j]=a[j],a[i]
    a[i+1:]=reversed(a[i+1:])
```

41) Serialize binary tree (preorder)
```python
def serialize(root):
    res=[]
    def dfs(n):
        if not n: res.append('#'); return
        res.append(str(n.val)); dfs(n.left); dfs(n.right)
    dfs(root); return ','.join(res)
```

42) Deserialize binary tree (preorder)
```python
def deserialize(data):
    vals=iter(data.split(','))
    def dfs():
        v=next(vals)
        if v=='#': return None
        n=Node(int(v)); n.left=dfs(); n.right=dfs(); return n
    return dfs()
```

43) Find duplicates in array (return list)
```python
def find_dups(a):
    seen=set(); dups=[]
    for x in a:
        if x in seen and x not in dups: dups.append(x)
        seen.add(x)
    return dups
```

44) Sum of two linked lists (digits reverse order)
```python
def add_lists(l1,l2):
    carry=0; head=tail=None
    while l1 or l2 or carry:
        s=carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        carry=s//10; node=ListNode(s%10)
        if not head: head=node; tail=node
        else: tail.next=node; tail=node
        l1=l1.next if l1 else None; l2=l2.next if l2 else None
    return head
```

45) Compute GCD (Euclid)
```python
def gcd(a,b):
    while b: a,b=b,a%b
    return a
```

46) Rotate matrix 90 degrees in-place (NxN)
```python
def rotate_matrix(m):
    n=len(m)
    for i in range(n//2):
        for j in range(i,n-1-i):
            tmp=m[i][j]
            m[i][j]=m[n-1-j][i]
            m[n-1-j][i]=m[n-1-i][n-1-j]
            m[n-1-i][n-1-j]=m[j][n-1-i]
            m[j][n-1-i]=tmp
```

47) Find subarray with given sum (positive nums) - sliding window
```python
def subarray_sum(a,target):
    i=0; cur=0
    for j,x in enumerate(a):
        cur+=x
        while cur>target and i<=j: cur-=a[i]; i+=1
        if cur==target: return (i,j)
    return None
```

48) Product of array except self (no division)
```python
def prod_except_self(a):
    n=len(a); res=[1]*n
    left=1
    for i in range(n): res[i]=left; left*=a[i]
    right=1
    for i in range(n-1,-1,-1): res[i]*=right; right*=a[i]
    return res
```

49) Binary tree max depth
```python
def max_depth(root):
    if not root: return 0
    return 1+max(max_depth(root.left), max_depth(root.right))
```

50) Serialize dictionary to query string
```python
def to_qs(d):
    return '&'.join(f"{k}={v}" for k,v in d.items())
```

---
File extended to 50 short questions.
