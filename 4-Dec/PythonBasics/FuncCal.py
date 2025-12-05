
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

print("Choose operation: add, subtract, multiply, divide")
operation = input("Operation: ").lower()
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if operation == "add":
    print("Result:", add(x, y))
elif operation == "subtract":
    print("Result:", subtract(x, y))
elif operation == "multiply":
    print("Result:", multiply(x, y))
elif operation == "divide":
    print("Result:", divide(x, y))
else:
    print("Invalid operation")
