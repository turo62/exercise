
# Checks anagrams of words in a list imported from external file.
# Do not forget copying the file to the same folder!


def get_input():
    words1= []
    word = open("anagrams.csv", 'r')
    for line in word.readlines():
        words1.append(line.strip())
        N = len(words1)
    return words1, N

def anagr(words1, N):
    for i in range(N):
        j = 0
        while j <= N - 2:
            a = sorted(words1[i])
            b = "".join(a)
            c = sorted(words1[j+1])
            d = "".join(c)
            e = words1[i]
            f = words1[j+1]
            if b == d and e != f:
                print(e, f)
                j += 1
            else:
                j += 1
    return words1


def main():
       words1, N = get_input()
       anagr(words1, N)


if __name__ == '__main__':
        main()
