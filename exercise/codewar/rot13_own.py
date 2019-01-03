import string


def rot13(message):
    chars = string.ascii_lowercase
    chars1 = string.ascii_uppercase
    new_mess = ""
    for char in message:
        if char in chars:
            if chars.index(char) < 12:
                new_mess += chars[chars.index(char) + 13]
            else:
                new_mess += chars[chars.index(char) - 13]
        elif char in chars1:
            if chars1.index(char) < 12:
                new_mess += chars1[chars1.index(char) + 13]
            else:
                new_mess += chars1[chars1.index(char) - 13]
        else:
            new_mess += char
    return new_mess



           
def main():
    new_mess = rot13("Test")
    print(new_mess)


if __name__ == "__main__":
    main()