import string

def duplicate_count(text):
    lst0 = string.ascii_lowercase + string.digits
    text = text.lower()
    counter = 0
    num = 0
    for i in range(len(lst0)):
        counter = (text.count(lst0[i]))
        if counter > 1:
            num += 1
    return num

def main():
    num = duplicate_count("inDivisidisity")
    print(num)

if __name__ == "__main__":
    main()
