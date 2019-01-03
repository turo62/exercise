# Simple way of calculating Fibonacci sequence up to the entered serial number.

i = 0
j = 1
k = 0
fib = 0
x = (int(input("Enter a number: "))-1)

n =12
m = 25
while i <= x:
    print("|",( str(i+1) + ":").ljust(n), " |", str(fib).rjust(m), " |")   
    fib = j + k
    j = k
    k = fib
    i += 1
    print("|", "-" * (n + 1), "|", "-" * (m + 1), "|")