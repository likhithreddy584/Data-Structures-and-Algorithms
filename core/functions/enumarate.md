## 8. enumerate() - Get Index and Value

Provides both the index and value when looping through an iterable, eliminating the need for manual index tracking.

### Without enumerate (old way)
```python
tasks = ["Write code", "Test code", "Deploy code"]

for index in range(len(tasks)):
    print(f"{index + 1}. {tasks[index]}")
# 1. Write code
# 2. Test code
# 3. Deploy code
```

### With enumerate (better way)
```python
for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")
# Same output, cleaner code
```

### See the Structure
```python
print(list(enumerate(tasks)))
# [(0, 'Write code'), (1, 'Test code'), (2, 'Deploy code')]
```

### Custom Start Index
```python
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")
# Starts counting from 1 instead of 0
```

**Context**: `enumerate()` returns tuples of (index, value) pairs. This is much cleaner than manually tracking indices with `range(len(...))` and makes your code more Pythonic.
