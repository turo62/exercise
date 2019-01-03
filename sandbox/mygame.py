import mymath

def my_game(num):
    squa_num = mymath.square(num)
    return squa_num

def main():
    squa_num = my_game(17)
    print("this is mygame.")
    print(squa_num)
    #print(mymath.square(17)) (This is with no function called my_game & if__name__...!)

if __name__ == '__main__':
        main()
