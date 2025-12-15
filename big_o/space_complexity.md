
# What is Space Complexity?

**Space complexity** measures how much additional memory an algorithm needs as input size grows.

## Types of Space Usage

1. **Input space**: Memory for the input (we usually don't count this)
2. **Auxiliary space**: Extra memory the algorithm uses (this is what we measure)

```python
def sum_iterative(n):
    """
    Space Complexity: O(1) - constant space
    Only uses a single variable 'total'
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_recursive(n):
    """
    Space Complexity: O(n) - linear space
    Each recursive call adds a frame to the call stack
    """
    if n <= 0:
        return 0
    return n + sum_recursive(n - 1)

# Example with visualization
def demonstrate_space():
    n = 5
    
    print("Iterative approach:")
    print(f"Result: {sum_iterative(n)}")
    print("Stack depth: 1 (constant)\n")
    
    print("Recursive approach:")
    print(f"Result: {sum_recursive(n)}")
    print(f"Stack depth: {n} (grows with input)")

demonstrate_space()
```

### Space Complexity Example: Creating Arrays

```python
def create_2d_array(n):
    """
    Space Complexity: O(n²)
    Creates an n x n matrix
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        matrix.append(row)
    return matrix

# For n=3, creates 3x3 = 9 elements
# For n=100, creates 100x100 = 10,000 elements
# Space grows quadratically!

small_matrix = create_2d_array(3)
print(f"3x3 matrix has {len(small_matrix) * len(small_matrix[0])} elements")

large_matrix = create_2d_array(100)
print(f"100x100 matrix has {len(large_matrix) * len(large_matrix[0])} elements")
```