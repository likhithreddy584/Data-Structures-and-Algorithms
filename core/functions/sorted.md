# sorted() - Sort Any Iterable

Returns a sorted list from any iterable, with options for reverse order and custom sorting logic.

## Basic Sorting

```python
numbers = [5, 2, 8, 1, 9, 3]
sorted_nums = sorted(numbers)
print(sorted_nums)
# [1, 2, 3, 5, 8, 9]
```

## Reverse Order

```python
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)
# [9, 8, 5, 3, 2, 1]
```

## Custom Sorting with Key

```python
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Sort by age in reverse
sorted_desc = sorted(people, key=lambda person: person["age"], reverse=True)
print(sorted_desc)
# [{'name': 'Charlie', 'age': 35}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
```

**Context**: The `key` parameter is powerful - it takes a function that extracts a comparison value from each item. The sorting is based on what this function returns, not the items themselves.
