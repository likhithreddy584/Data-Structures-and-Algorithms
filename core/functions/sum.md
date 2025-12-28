## 6. sum() - Add Numbers Together

Calculates the sum of all numeric values in an iterable.

### Basic Usage
```python
numbers = {1, 2, 3, 4, 5, 10.5, 9, 6}
total = sum(numbers)
print(total)
# 35.5
```

### With Start Value
```python
# Start summing from 10
total = sum(numbers, 10)
print(total)
# 45.5

# Start from negative value
total = sum(numbers, -10)
print(total)
# 25.5
```

**Context**: The optional `start` parameter adds an initial value to the sum. This is useful for offsetting calculations or accumulating values across multiple operations. All items must be numeric (int or float).

---