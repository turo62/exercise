def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "a, á, e, é, i, í, ó, ö, ő, u, ú, ü, ű":
            if letter.isupper():
                translation = translation + "B"
            else:
                translation = translation + "b"

        else:
            translation = translation + letter
    return translation

print(translate(input("Adj egy mondatot: ")))