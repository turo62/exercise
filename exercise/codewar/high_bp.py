def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


def main():
    word = high('vypxfynv rluxlqnfvh')
    print(word)


if __name__ == "__main__":
    main()