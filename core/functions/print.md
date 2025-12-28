# print() - Output with Control

The `print()` function is your first introduction to Python, but it has powerful parameters beyond basic output.

## Basic Usage

```python
name = "Alice"
age = 23
print("My name is", name, "and I am", age, "years old")
# Output: My name is Alice and I am 23 years old
```

## Advanced Parameters

**sep parameter** - Change the separator between arguments:
```python
print("My name is", name, "and I am", age, "years old", sep=" | ")
# Output: My name is | Alice | and I am | 23 | years old

print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry
```

**end parameter** - Control what prints at the end:
```python
print("Hello", end=" | ")
print("World")
# Output: Hello | World (on same line)

# Useful for progress indicators
for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

**Context**: By default, `print()` uses a space as separator and `\n` (newline) as the end character. These parameters give you formatting control without manual string concatenation.