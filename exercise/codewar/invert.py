def invert(lst):
    inv1 = []
    length = len(lst)
    val = 0
    for i in range(length):
        val = lst[i] * -1
        inv1.append(val)
    return inv1

def main():
    inv1 = invert([1,-2,3,-4,5])
    print(inv1)

if __name__ == "__main__":
    main()