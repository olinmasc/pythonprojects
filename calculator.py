operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        result = "Error: Division by zero"
    print(result)
else:
    result = "Error: Invalid operator"
    print(result)
