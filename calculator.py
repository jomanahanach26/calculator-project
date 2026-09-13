print("Welcome to my calculator")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")
if operation == "+":
    result = number1 + number2
    print("Result:", result)
elif operation == "-":
    result = number1 - number2
    print("Result:", result)
elif operation == "*":
    result = number1 * number2
    print("Result:", result)
elif operation == "/":
    if number2 == 0:
        print("Cannot divide by zero")
    else:
        result = number1 / number2
        print("Result:", result)