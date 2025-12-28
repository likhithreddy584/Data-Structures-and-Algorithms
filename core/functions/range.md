# range() - Generate Number Sequences

Creates sequences of numbers, commonly used in for loops but also useful for generating numeric lists.

## Syntax Patterns

**One argument** (stop only):
```python
list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Starts at 0, stops before 10
```

**Two arguments** (start, stop):
```python
list(range(2, 10))
# [2, 3, 4, 5, 6, 7, 8, 9]
# Starts at 2, stops before 10
```

**Three arguments** (start, stop, step):
```python
list(range(2, 10, 2))
# [2, 4, 6, 8]
# Starts at 2, stops before 10, increments by 2

# Negative step for countdown
list(range(10, -10, -2))
# [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
```

**Context**: `range()` returns an iterator (not a list), which is memory-efficient for loops. Convert to `list()` only when you need to see or manipulate all values at once.