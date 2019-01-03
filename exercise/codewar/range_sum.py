def f(n):
    if isinstance(n, int) == False or n <= 0: 
        return None
    a =   range(n+1)
    if isinstance(n, int):
        return sum(range(n + 1))

def main():
    sum = f(25)
    print(sum)

if __name__ == "__main__":
    main()