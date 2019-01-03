def wave(str):
    new_str = []
    for i in range(len(str)):
        if str[i] == " ":
            i += 1
        else:
            new_str.append(''.join([str[:i], str[i].upper(), str[i + 1:]]))
    return new_str


def main():
    new_str = wave("two words")
    print(new_str)


if __name__ == "__main__":
    main()