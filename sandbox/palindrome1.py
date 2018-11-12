string = input("Enter a text with no punctuation mark: ")
string = string.replace(" ","")
string = string.lower()
string2 = string[::-1]
print(string2)
if string == string2:
    print("True")
else:
    print("False")