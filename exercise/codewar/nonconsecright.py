# Returns first no consecutive number of an array.

def first_non_consecutive(arr):
    if not arr:
        return 0
        
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]
            

def main():
    first_non_consecutive([99])

if __name__ == "__main__":
    main()