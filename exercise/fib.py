# Simple way of calculating Fibonacci sequence up to the entered serial number.

i = 0
j = 1
k = 0
fib = 0
x = (int(input("Enter a number: "))-1)


while i <= x:
    print((str(i+1) + ":").ljust(5), str(fib).rjust(25))   
    fib = j + k
    j = k
    k = fib
    i += 1

