import string

def alphabet_position(text):
    char_list = string.ascii_lowercase
    text = text.lower()
    length = len(text)
    strings = ""
    for i in range(0, length):
        if text[i] not in char_list or text[i] == " ":
            i += 1
        elif text[i] in char_list:
            strings = strings + str((char_list.index(text[i])+1)) + " "
    return strings

def main():
    strings = alphabet_position("The narwhal bacons at midnight.")
    print(strings)

if __name__ == "__main__":
    main()
