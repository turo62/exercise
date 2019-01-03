def sorting_nums(numbers):
        print(numbers)
        N = len(numbers)
        for i in range(N):
                for j in range(N - 1):
                        if numbers[j] > numbers[j + 1]:
                                temp = numbers[j + 1]
                                numbers[j + 1] = numbers[j]
                                numbers[j] = temp
                        else:
                                j += 1
        return numbers


def main():
    numbers = sorting_nums([1, 2, 56, 32, 51, 2, 8, 92, 15])
    print(numbers)

if __name__ == "__main__":
    main()
