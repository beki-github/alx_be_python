def perform_operation(num1, num2, operation):
    """Performs an arithmetic operation on two numbers."""

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Choose +, -, *, or /")
    

def main():
    # User input
    num1_input = input("Enter the first number: ")
    num2_input = input("Enter the second number: ")
    op = input("Enter operation (+, -, *, /): ").strip()

    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
    except ValueError:
        raise ValueError("Inputs must be numeric.")

    # Call required function
    result = perform_operation(num1, num2, op)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()

