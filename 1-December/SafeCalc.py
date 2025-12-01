def safe_calculator(a, b, operator):
    try:
        a = float(a)
        b = float(b)
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return "Error: Division by zero is not allowed."
            return a / b
        else:
            return f"Error: Invalid operator '{operator}'. Use +, -, *, or /."
    except ValueError:
        return "Error: Inputs must be numeric."
    except Exception as e:
        return f"Unexpected error: {e}"

print(safe_calculator("10", "5", "+"))
print(safe_calculator("10", "abc", "*"))
print(safe_calculator("10", "0", "/"))
print(safe_calculator("10", "5", "^"))
