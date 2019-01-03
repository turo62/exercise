def two_sum(numbers, target):
    b = 0
    arr = []
    for i in range(len(numbers)):
        if (target / numbers[i] - target // numbers[i] == 0) and  b < 3:
            arr.append(i)
            b += 1
    return arr




def main():
    arr = two_sum([2,2,3], 4)
    print(arr)

if __name__ == "__main__":
    main()

def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]

def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], i]
        d[num] = i