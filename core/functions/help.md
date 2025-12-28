## help() - Built-in Documentation

Access function documentation instantly without leaving your code or searching online.

## Usage

```python
help(print)
# Displays complete documentation for print function

def custom_function(a, b):
    """
    Adds two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b

help(custom_function)
# Displays your custom docstring
```

**Context**: The `help()` function reads docstrings (documentation strings) from any function. This works for built-in functions, library functions, and your own custom functions. It's essential for exploring unfamiliar code or refreshing your memory on function parameters.