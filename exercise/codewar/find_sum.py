def find(n):
    sum_f = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_f += i
    return sum_f


def main():
    sum_f = find(10)
    print(sum_f)

if __name__ == "__main__":
    main()