def calculate(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 == 0:
            return "Cannot divide by zero"
        else:
            return number1 / number2
    else:
        return "Invalid operation"


if __name__ == "__main__":
    print("Welcome to my calculator")

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    result = calculate(number1, number2, operation)

    print("Result:", result)