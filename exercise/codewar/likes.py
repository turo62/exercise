#Not complete!!!
def likes(names):
    length = len(names)
    some = ""
    num = length - 2
    if length > 3:
        some += (names[0] + ", "  + names[1] +  "and" + num + " like this.")
    return some




def main():
    some = likes(("Mary", "Rob", "Jacob", "Kitty"))
    print(some)

if __name__ == "__main__":
    main()