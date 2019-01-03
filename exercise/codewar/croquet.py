def openOrSenior(data):
    res = []
    for i in data:
      if i[0] >= 55 and i[1] > 7:
        res.append("Senior")
      else:
        res.append("Open")
    return res

def get_input():
    data = []
    print("Type in data of new membership")
    age = int(input("Enter the age: "))
    handycap = int(input("Enter the handycap level: "))
    data.append([age, handycap])
    return data

def main():
    data = get_input()
    res = openOrSenior(data)
    print(res)   

if __name__ == "__main__":
    main()