# Mine.
def find_longest(arr):
    len2 = []
    len1 = 0
    for i in range(len(arr)):
        len2. append(str(arr[i]))
    len1 = int(max(len2, key = len))
    print(type(len1))
    #return len1
# Best practice on net.
def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))



def main():
    max = find_longest([1, 200, 100000])
    print(max)

if __name__ == "__main__":
    main()