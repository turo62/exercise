doors = []
for x in range (0, 100):
    doors.append(0)
length = len(doors)
x = 1
i = 0


for y in range(100):
    while i < length:
        if doors[i] == 0:
            doors[i] += 1
            i += x
        else:
            doors[i] -= 1
            i += x
    i = x
    x += 1
i = 0


print("Az alábbiak a nyitott ajtók sorszámai: ", end='')


while i < length:
    if doors[i] == 1:
        print(str(i+1) + ", " , end='')
        i += 1
    else:
        i +=1
