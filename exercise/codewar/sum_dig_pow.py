def sum_dig_pow(a, b):
    num = 0
    num1 = 0
    result = []
    for i in range(a, b + 1):
        num = str(i)
        val = 0
        for j in range(len(num)):
            num1 = int(num[j]) ** (j + 1)
            val += num1
        if int(num) == val:
            result.append(int(num))
    return result




def main():
    result = sum_dig_pow(1, 89)
    print(result)


if __name__ == '__main__':
        main()
