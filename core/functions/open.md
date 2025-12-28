# open() - File Operations

Opens files for reading, writing, or appending, with proper resource management using context managers.

## Writing to a File (W mode)

```python
# Overwrites file if it exists
with open("test.txt", "w") as file:
    file.write("Hello World\n")
    file.write("My name is Tim")
# File automatically closed after this block
```

## Reading from a File (R mode)

```python
with open("test.txt", "r") as file:
    text = file.read()
    print(text)
# Hello World
# My name is Tim
```

## Appending to a File (A mode)

```python
# Adds to end without overwriting
with open("test.txt", "a") as file:
    file.write("\nNew addition")
```

## File Modes

- **"r"** - Read (default mode)
- **"w"** - Write (creates new or overwrites existing)
- **"a"** - Append (adds to end of existing file)
- **"r+"** - Read and write
- **"w+"** - Write and read (overwrites)
- **"a+"** - Append and read

## Why Use Context Managers?

```python
# DON'T DO THIS (manual close)
file = open("test.txt", "w")
file.write("Hello")
file.close()  # Easy to forget!

# DO THIS (automatic close)
with open("test.txt", "w") as file:
    file.write("Hello")
# File automatically closed, even if error occurs
```

**Context**: The `with` statement creates a context manager that guarantees the file is properly closed, even if an exception occurs. This prevents memory leaks and file corruption. Always use `with` for file operations.