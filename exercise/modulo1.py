# Finding the top 25 three-digit natural numbers divisible by 7 or by 9.

i = 1

for number in range(1000, 100, -1):
    while i <= 25:
        if number % 7 == 0 or number % 9 == 0:
            print(number)
            number -= 1
            i += 1
        else:
            number -=1
