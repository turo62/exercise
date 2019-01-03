import array

def find_uniq(arr):
    num = max(arr)
    counter = arr.count(num)
    if counter == 1:
        unique = num
    else:
        unique = min(arr)
    return unique

def main():
    unique = find_uniq([ 0, 0, 0.55, 0, 0 ])
    print(unique)

if __name__ == "__main__":
    main()