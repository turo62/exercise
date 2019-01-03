def sort_array(source_array):
    odds = []
    i = 0
    array = []
    array1 = []
    if source_array == []:
        return source_array
    for num in source_array:
        if num % 2 == 1 and num != 0:
            odds.append(num)
            num = "a"
            array.append(num)
        elif num% 2 ==0:
            array.append(num)
    odds = sorted(odds)
    for num in array:
        if num == 'a':
            array1.append(odds[i])
            odds.remove(odds[i])
        elif num % 2 ==0:
            array1.append(num)
    return array1


def main():
    array1 = sort_array([5, 3, 2, 8, 1, 4])


if __name__ == "__main__":
    main()