def top_25(n):
    lst =[]
    item = 100
    i = 0
    while item <= n:
        lst.append(item)
        item += 1
    lst.reverse()
    for item in lst:
        if item % 7 == 0 or item % 9 == 0:
            if i < 25 :
                print(item)
                i += 1              
    return lst

def main():
    lst = top_25(999)

if __name__ == '__main__':
        main() 
        