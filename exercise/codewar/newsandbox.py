def diamond(n):
    j = 1
    k = n
    diam1 = []
    if n % 2 == 0 or n != abs(n):
        return "null"
    else:
        for j in range(1, n + 2, 2):
            print((j * "*").center(n))
        for k in range(n - 2, 0, -2):
            print((k * "*").center(n))
        return diam1



def main():
    diam1 = diamond(10)
    print(diam1)


if __name__ == "__main__":
    main()