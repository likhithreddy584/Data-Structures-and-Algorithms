#  What is Time Complexity?

**Time complexity** measures how the runtime of an algorithm grows as the input size increases. It's not about exact seconds, but about the **pattern of growth**.

## Real-World Analogy

Imagine you're looking for a book:
- **Linear search**: Check every book one by one (slow for many books)
- **Binary search**: If books are sorted, open middle book, eliminate half (fast!)

```python
import time

def linear_search(arr, target):
    """Check every element one by one"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """Divide and conquer on sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Let's compare with a large sorted array
large_array = list(range(1000000))
target = 999999

# Linear search timing
start = time.time()
linear_search(large_array, target)
linear_time = time.time() - start

# Binary search timing
start = time.time()
binary_search(large_array, target)
binary_time = time.time() - start

print(f"Linear search: {linear_time:.6f} seconds")
print(f"Binary search: {binary_time:.6f} seconds")
print(f"Binary search is {linear_time/binary_time:.0f}x faster!")
```
