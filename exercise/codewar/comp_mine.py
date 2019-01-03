def compSame(array1, array2):
    nums1 = array1
    nums2 = array2
    counter = 0
    if len(array1) == 0 or len(array2) == 0:
        return False
    for num1 in nums1:
        for num2 in nums2:
            if num1 ** 2 == num2:
                counter += 1
                nums2.remove(num2)
    if counter == len(nums1):
        print(counter)
        return True
    else:
        return False


def main():
    array1 = [121, 144, 19, 161, 19, 144, 19, 11] 
    array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    compSame(array1, array2)


if __name__ == "__main__":
    main()