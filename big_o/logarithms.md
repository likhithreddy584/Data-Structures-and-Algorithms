# Understanding Logarithms

Before diving into Big O notation, we need to understand logarithms because they appear frequently in algorithm analysis.

## What is a Logarithm?

A logarithm answers the question: "To what power must we raise a base to get a certain number?"

**log₂(8) = 3** means "2 raised to what power equals 8?" Answer: 3, because 2³ = 8

## Why Logarithms Matter in Programming

Logarithms appear when you repeatedly divide something in half (or by any constant factor).

```python
# Example: How many times can we divide 16 by 2 until we reach 1?
def count_divisions(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
        print(f"Step {count}: n = {n}")
    return count

result = count_divisions(16)
print(f"\nTotal divisions: {result}")
# Output shows 4 divisions: log₂(16) = 4
```

**Output:**
```
Step 1: n = 8
Step 2: n = 4
Step 3: n = 2
Step 4: n = 1

Total divisions: 4
```