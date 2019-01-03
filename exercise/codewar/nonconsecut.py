# Returns the first non consecutive number of an array
# Bad solution!!!!!!!!!!
def first_non_consecutive(arr):
    num = 0
    length = len(arr)
    for i in range(1, length):
        print(arr.index(arr[i -1]))
        if (abs(arr[i] - arr[i - 1])) > 1 and (length - 1) != 0:
            num = arr[i]
            break
        elif (abs(arr[i] - arr[i - 1])) == 1 or (length - 1) == 0:
            num = None
                   
    return num

def main():
    num = first_non_consecutive([99])
    print(num)

if __name__ == "__main__":
    main()