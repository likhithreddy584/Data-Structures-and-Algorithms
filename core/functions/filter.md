# filter() - Keep Only Matching Items

Filters an iterable by keeping only items where a function returns `True`.

## Basic Example

```python
strings = ["my", "world", "apple", "pear"]

def longer_than_four(s):
    return len(s) > 4

filtered = list(filter(longer_than_four, strings))
print(filtered)
# ['world', 'apple']
```

## Using Lambda

```python
# More concise version
filtered = list(filter(lambda x: len(x) > 4, strings))
print(filtered)
# ['world', 'apple']

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
# [2, 4, 6, 8, 10]
```

**Context**: Each item is passed to the filter function. If the function returns `True`, the item is kept; if `False`, it's removed. This is cleaner than using list comprehensions with conditionals for complex filtering logic.
