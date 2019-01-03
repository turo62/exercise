def reverse_words(text):
    words = text.split(" ")
    newWords = [word[::-1] for word in words]
    newtext = " ".join(newWords) 
    return newtext

def main():
    newtext = reverse_words('The quick brown fox jumps over the lazy dog.')
    print(newtext)

if __name__ == "__main__":
    main()