def square_digits(num):
    str1 = str(num)
    length = len(str1)
    val1 =""
    
    for i in range(length):
        val2= 0
        val2 = int(str1[i])
        val2 = str(val2 ** 2)
        val1 += val2
    val1 = int(val1)
    return val1




def main():
    val1 = square_digits(54221)
    print(val1)

if __name__ == "__main__":
    main()