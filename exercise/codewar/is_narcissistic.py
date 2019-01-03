def is_narcissistic(i):
    nums = str(i)
    num_i = 0
    for num in nums:
        num_i += int(num) ** len(nums)
    if i == num_i:
        return True
    else:
        return False