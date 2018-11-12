# Sorting list of numbers entered by the user.


def get_input():
    numbers = [int(x) for x in input("Type in series of numbers with whitespaces. Push enter when complete!:").split()]
    N = len(numbers)
    return N, numbers


def sort_nums(N, numbers):

    for i in range(N):
        j = 0
        while j <= N - 2:
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
            else:
                j = j+1
    return numbers


def main():
    N, numbers = get_input()
    print(numbers)
    sort_nums(N, numbers)
    numbers = sort_nums(N, numbers)
    print(sort_nums(N, numbers))


if __name__ == '__main__':
    main()
