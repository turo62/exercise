num1 = float(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))
if op == "+":
    print("Result of addition: ", + num1 + num2)
elif op== "-":
    print("Result of substruction: ", + num1 -num2)
elif op == "*":
    print("Result of multiplication: ", + num1 * num2)
elif op == "/":
    print("Result of division: ", + num1 / num2)
else:
    print("Not a valid operator!")

    