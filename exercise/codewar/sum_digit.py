def sumDigits(number):
    num_split = [int(digit) for digit in str(abs(number))]
    length = len(num_split)
    sum = 0
    for i in range(length):
        sum = sum + num_split[i]
    return sum

def main():
    sum = sumDigits(-32)
    print(sum)

if __name__ == "__main__":
    main()