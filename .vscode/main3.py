numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
length = len(numbers)
x = 0
i = 0
while i <= (length-1):
    x = x + numbers[i]
    i += 1
print("Average of the list: ", x / length)
