nums = []
for i in range(101):
    nums.append(1)


for j in range(1, 101):
    for i in range(1, 101, j):
        if nums[i] == 1:
            nums[i] = 0
        elif nums[i] == 0:
            nums[i] = 1


print(nums)