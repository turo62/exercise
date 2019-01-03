# Mine.
def vowel_indices(word):
    i = 0
    result = []
    vowels = ["y", "a", "e", "i", "o", "u"]
    word = word.lower()
    for letter in word:
        i += 1
        if letter in vowels:
            result.append(i)
    return result

def main():
    result = vowel_indices("YoMama")
    print(result)

if __name__ == "__main__":
    main()

# Net best practice.
def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']