def get_input():
        nums = input("Enter numbers with whitespaces in between. Press enter when ready.: ").split()
        numbers = []
        for num in nums:
                numbers.append(int(num))
        return numbers
        
def sorting_nums(numbers):
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
        numbers = get_input()
        print(numbers)
        sorting_nums(numbers)
        numbers = sorting_nums(numbers)
        print(numbers)

if __name__ == "__main__":
    main()
