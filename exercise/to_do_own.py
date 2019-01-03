def add():
    new_item = input("Add an item: ")
    mark = "-"
    if new_item != "":
        with open("to_do.txt", "a") as f:
            f.write(mark + "\t" + new_item + "\n")
        print("\n", "Item added.")
    else:
        return new_item


def list():
    lst = []
    with open("to_do.txt", "r") as f:
        items = f.readlines()
    for item in items:
        item = item.rstrip("\n")
        lst.append(item.split("\t"))
    print("You saved the following to-do items:")
    for i in range(len(lst)):
        print(4 * " " + str(i + 1) + ". " + "[" + lst[i][0] + "]   " + lst[i][1])
    return lst


def mark():
    lst = list()
    mark = input("Which one you want to mark as completed: ")
    lst[int(mark) - 1][0] = "x"
    print(lst[(int(mark) - 1)][1], " is completed.")
    with open("to_do.txt", "w") as f:
        for i in range(len(lst)):
            f.write(lst[i][0] + "\t" + lst[i][1] + "\n")


def archive():
    lst = list()
    with open("to_do.txt", "w") as f:
        for i in range(len(lst)):
            if lst[i][0] != "x":
                f.write(lst[i][0] + "\t" + lst[i][1] + "\n")
    print("All completed tasks got deleted.")

def specify_command():
    specify = input("Please specify a command [list, add, mark, archive]: ")
    if specify == "add":
        add()
    elif specify == "list":
        list()
    elif specify == "mark":
        mark()
    elif specify == "archive":
        archive()


def main():
    specify_command()


if __name__ == "__main__":
    main()