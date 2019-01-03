import string


def high(x):
    alphabet = string.ascii_lowercase
    str_split = x.split(" ")
    new_x = []
    for word in str_split:
        sum = 0
        for i in range(len(word)):
            sum += alphabet.index(word[i]) + 1
            new_x.append(sum)
    word = str_split[new_x.index(max(new_x))]
    return word


def main():
    word = high('vypxfynv rluxlqnfvh')
    print(word)


if __name__ == "__main__":
    main()