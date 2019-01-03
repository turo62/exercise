def black_or_white_key(key_press_count):
    key = ""
    key_press_count = key_press_count % 88
    if key_press_count <5:
        if key_press_count == 2:
            key = "black"
        else:
            key = "white"
    else:
        key_press_count = (key_press_count - 4) % 12
        if key_press_count == 1 or key_press_count == 3 or key_press_count == 6 or key_press_count == 8 or key_press_count == 10:
            key = "black"
        else:
            key = "white"
    return key


def main():
    key = black_or_white_key(2017)
    print(key)


if __name__ == "__main__":
    main()
