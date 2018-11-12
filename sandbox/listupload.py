colo = []
col = open("colors.txt", 'r')
for line in col.readlines():
    colo.append([line])
    for i in line.split(","):
        colo[-1].append(i)
print(colo)