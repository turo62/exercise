# Returns duplicate number if any or none.
# Wrong solution. 
def elimination(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i + 1]:
            n = arr[i]
            break
        else:
            n = None
    return n

def main():
    n = elimination([2, 5, 34, 5, 22])
    print(n)

if __name__ == "__main__":
    main()