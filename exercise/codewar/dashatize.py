#Not complete!!!
def dashatize(num):
    num1 = str(num)
    new_num = []
    while i < len(num1):
        if int(num1[i]) % 2 != 0 and int(num1[i + 1]) % 2 !=0:
            new_num.append[("-" + num1[i])]
        if int(num1[i]) % 2 != 0 and int(num1[i + 1]) % 2 == 0:
            new_num.append[("-" + num1[i] + "-" )]
        else:
            new_num.append[num1[i]]
        return new_num



def main():
    new_num = dashatize(974302)
    print(new_num)

if __name__ == "__main__":
    main()