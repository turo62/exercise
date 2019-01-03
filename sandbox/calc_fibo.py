import fibo

def fib_calc(a, b):
    fib = fibo.fib
    fib2 = fibo.fib2
    num1 = fib(a)
    num2 = fib2(b)
    return num1, num2



def main():
    num1, num2 = fib_calc(1000, 500)
    print(num1)
    print(num2)

    
if __name__ == '__main__':
    main()