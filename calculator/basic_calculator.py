# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def calculate(operation, num1, num2):
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    else:
        return "Invalid operation"

# This function is not easily testable due to its reliance on user input/output
def run_calculator():
    while True:
        operation = input("Enter operation (+, -, *, /) or 'exit' to quit: ")

        if operation == "exit":
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = calculate(operation, num1, num2)
        print("The result is:", result)

def main():
    run_calculator()

if __name__ == "__main__":
    main()