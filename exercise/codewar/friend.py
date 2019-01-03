def friend(x):
    length = []
    len1 = []
    for i in range(len(x)):
        length.append(len(x[i]))
    for j in range(len(length)):
        if length[j] == 4:
            len1.append(x[j])    
    return len1

def main():
    len1 = friend(["Ryan", "Kieran", "Mark",])
    print(len1)

if __name__ == "__main__":
    main()
