# zip() - Combine Multiple Iterables

Combines multiple iterables element-by-element into tuples, automatically handling length mismatches.

## Without zip (manual way)

```python
names = ["Alice", "Bob", "Charlie", "Tim"]
ages = [30, 25, 35]

for i in range(min(len(names), len(ages))):
    print(f"{names[i]} is {ages[i]} years old")
```

## With zip (elegant way)

```python
names = ["Alice", "Bob", "Charlie", "Tim"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Alice is 30 years old
# Bob is 25 years old
# Charlie is 35 years old
# (Tim is excluded - no corresponding age)
```

## Multiple Iterables

```python
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
genders = ["female", "male", "male"]

combined = list(zip(names, ages, genders))
print(combined)
# [('Alice', 30, 'female'), ('Bob', 25, 'male'), ('Charlie', 35, 'male')]

for name, age, gender in zip(names, ages, genders):
    print(f"{name} is {age} years old and is {gender}")
```

**Context**: `zip()` stops at the shortest iterable's length, preventing index errors. It's perfect for parallel iteration over related data stored in separate lists.
