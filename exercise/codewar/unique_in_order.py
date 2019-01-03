def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

def main():
    result = unique_in_order('AAAABBBCCDAABBB')
    print(result)

if __name__ == "__main__":
    main()