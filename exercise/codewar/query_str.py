#Not complete!!!
from operator import itemgetter

def get_key(data):
    key1 = []
    val1 = []
    list1 = ""
    str2 =""
    str3 = ""
    for key in data.keys():
        key1.append(key)
    length = len(key1)
    val1 = itemgetter(*key1)(data)
    for i in range(len(key1)):
        for j in range(len(val1)):
            list1.join(key1[i])
            list1.join("=")
            list1.join(val1[j]
    print(list1)      
    return lst



def main():
    lst = get_key({ "bar": [2, 4], "foo": [1, 3] })
    print(lst)

if __name__ == "__main__":
    main()
