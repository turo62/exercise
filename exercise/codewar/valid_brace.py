#Not complete!!!
def validBraces(string):
    length = len(string)
    str1 = 0
    val1 = 0
    for i in range(0, length, 2):
        str1 = string[i] + string[i + 1]
        if str1 == "[]" or str1 == "()" or str1 == "{}":
            val1 = True
        else:
            val1 = False
            break
    return val1





def main():
    val1 = validBraces("(({{[[]]}}))")
    print(val1)

if __name__ == "__main__":
    main()