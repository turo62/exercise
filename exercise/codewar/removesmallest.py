def remove_smallest(numbers):
    list = numbers
    if list == [] or len(list) == 1:
        list = []

    else:   
        b = list.index(min(list))
        del list[b]
    return list

def main():
    list = remove_smallest([158])
    print(list)

if __name__ == "__main__":
    main()