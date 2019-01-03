def get_input():
    list1 = []
    word = open("get_oldest.csv", 'r')
    for line in word.readlines():
        list1.append(line.split(","))
    age = []
    pers = ""
    for i in range(len(list1)):
        pers = list1[i]
        age.append([pers[:-3], eval(pers[-2:])]) 
    return age

def find_oldest_person(age):
    Max = ""
    temp = 0
    max_age = 0
    if len(age) == 0:
        return None
    print(age)
    for i in range(len(age)):
        print(type(age[i][1]))
        if int(age[i][1]) > temp:
            temp = age[i][1]
            max_age = age[i]
    Max = max_age[0]
    return Max



def main():
    age = get_input()
    Max = find_oldest_person(age)
    print(Max)


if __name__ == '__main__':
        main()
