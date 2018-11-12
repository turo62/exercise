# Finding highest number of a list.

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
length = len(numbers)
max = numbers[0]
i = 1
while i < length:
    if max < numbers[i]:
        max = numbers[i]
        i += 1
    else:
        max = max
        i += 1
print("Maximum of the list is: ", max)
