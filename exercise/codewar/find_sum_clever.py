def find(n):
    return sum(e for e in range(1, n+1) if e % 3 == 0 or e % 5 == 0)


def main():
    sum = find(10)
    print(sum)

if __name__ == "__main__":
    main()