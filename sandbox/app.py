def new_table():
    n = 4
    m = 3
    b = [[" "] * m] * n
    return b

def add_task():
    n = 1
    m = 3
    a = [[" "] * m] * n
    a[0] [2] = input("Add a task: ")
    return a

def ins_new_line():
    b = new_table()
    a = add_task()
    c = b.append(a)
    return c

def main():
    ins_new_line()

if __name__ == '__main__':
    main()

print(ins_new_line())