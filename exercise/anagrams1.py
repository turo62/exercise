def anagrams(filename):
    words1 = []
    words = open(filename, "r")
    for line in words.readlines():
        words1.append(line.strip())
    length = len(words1)
    for word in words1:
        for j in range(length):
            wordso1 = "".join(sorted(word))
            wordso2 = "".join(sorted(words1[j]))
            word3 = word
            word4 = words1[j]
            if wordso1 == wordso2 and word3 != word4:
                print(word3, word4)
                j += 1
            else:
                j += 1

def main():
    anagrams("anagrams.csv")

if __name__ == "__main__":
    main()