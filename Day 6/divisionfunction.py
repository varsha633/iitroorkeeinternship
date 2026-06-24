def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

# Examples
print(safe_divide(10, 2))
print(safe_divide(10, 0))
