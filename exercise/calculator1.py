
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')


    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    # Addition.
    if operation == "+":
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    # Substraction.
    elif operation == "-":
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    # Multiplication
    elif operation == "*":
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    # Division.
    elif operation == "/":
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print("You have not typed a valid operator. Please, run the program again!")
    again()    

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if calc_again.upper() == "Y":
        calculate()
    elif calc_again.upper() == "N":
        print("See you later!")
    else:
        again()

calculate()