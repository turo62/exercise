import os
import justtry2
# Import with root folder/

    def menu():
        answer = ""
    while answer != "x":
        os.system("clear")
        print("multiply(1)")
        print("sum(2)")
        print("spec_sum(3)")
        print("exit x")
        answer = input("Choose one: ")
        if answer == "1":
            print(multiply(5))
        elif answer == "2":
            print(sum(5))
        elif answer == "3":
            print(justtry2.spec_sum(75))
        elif answer != "x":
            print("Wrong option!")
        print("Press enter to continue.")
        input()


def multiply(n):
    sum = 1
    for i in range(1, n + 1) :
        sum = sum * i
    return sum

def sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def main():
    exit = True
    x = 0
    # While always boolean.
    while exit:
        try:
            x = input("Type a number :")
            x = int(x)
            if x > 30:
                print("Wrong input!")
            else:
                exit = False
        except:
            print("Wrong input!")
    s = sum(x)
    print(s)



if __name__ == "__main__":
    #main()
    menu()
    #c = justtry2.add(5, 4)
    #print(c)
    #justtry2.bubble_sort([2, 24, 8, 11, 1, 6])
    #print(justtry2.matrix_op([[2, 3, 5], [3, 5, 5], [4, 2, 6]], 0))
