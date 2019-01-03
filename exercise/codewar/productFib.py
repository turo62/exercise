def productFib(prod):
    num = []
    j = 1
    k = 0
    fib = 0
    while (j + fib) * fib <= prod:  
        fib = j + k
        j = k
        k = fib
    if (j * fib) == prod:
        num.extend((j, fib, True))
        return num
    if (j * fib) < prod:
        k = fib + j
        num.extend((fib, k, False))
        return num


def main():
    num = productFib(12818)
    print(num)

    
if __name__ == '__main__':
    main()