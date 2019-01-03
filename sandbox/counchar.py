# Counts number of characters of text entered by user.
# To be clean coded. There are too many duplicates.

def get_input():
    length = 0
    word = input("Enter something: ")
    if len(word) == 0:
        print("Not a valid input!")
        word = input("Enter something: ")
        length = len(word)
    else:
        length = len(word)
    return word, length

word, length = get_input()

print(word, "has ", length, " characters.")
