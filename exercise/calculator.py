import string

def inputs():
    oper = ""
    x = int(input("Enter a number (or a letter to exit): "))
    oper = input("Enter an operand: ")
    y = int(input("Enter a number: "))
     
    if oper == "+":
        add(x, y)
    elif oper == "-":
        subs(x, y)
    elif oper == "*":
        mult(x, y)
    else:
        div_num(x, y)

def add(x, y):
    print(x + y)
    inputs()

def subs(x, y):
    print(x - y)
    inputs()

def mult(x, y):
    print(x * y)
    inputs()

def div_num(x, y):
    print(x / y)
    inputs()

def main():
    inputs()

if __name__ == "__main__":
    main()