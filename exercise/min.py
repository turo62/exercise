# Finding lowest number of a list.

numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
length = len(numbers)
min = numbers[0]
i = 1
while i < length:
    if min > numbers[i]:
        min = numbers[i]
        i += 1
    else:
        min = min
        i += 1
print("Minimum of the list is: ", min)
