def black_or_white_key(key_press_count):
    key = ""
    if (key_press_count - 1) % 88 % 12 in [1, 4, 6, 9, 11]:
        key = "black" 
    else:
        key = "white"
    return key


def main():
    key = black_or_white_key(12)
    print(key)


if __name__ == "__main__":
    main()