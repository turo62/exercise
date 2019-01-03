import string


def is_pangram(s):
    L   =   []
    s = s.lower()
    s = s.split(" ")
    sentence = "".join(s)
    for letter in sentence:
        if letter in string.ascii_lowercase:
            if letter not in L:
                L.append(letter)
    if len(L)  == 26:
        return True
    else:
        return False


def main():
    is_pangram("This isn't a pangram! is not a pangram.")


if __name__ == "__main__":
        main()