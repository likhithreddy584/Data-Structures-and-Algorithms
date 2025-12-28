# map() - Apply Function to All Items

Applies a function to every item in an iterable (list, tuple, string, etc.) without manual loops.

## Basic Example

```python
strings = ["my", "world", "apple", "pear"]

# Get length of each string
lengths = list(map(len, strings))
print(lengths)
# [2, 5, 5, 4]
```

## Using Lambda Functions

```python
# Add 's' to each string
pluralized = list(map(lambda x: x + "s", strings))
print(pluralized)
# ['mys', 'worlds', 'apples', 'pears']

# Square all numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# [1, 4, 9, 16, 25]
```

## Using Custom Functions

```python
def add_suffix(string):
    return string + "s"

result = list(map(add_suffix, strings))
```

**Context**: `map()` is more concise and often faster than manual loops. It returns a map object (iterator), so wrap it in `list()` to see all results immediately.
