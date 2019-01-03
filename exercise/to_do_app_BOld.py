# To do list app
# 2018.10.25

'''
With your group, write an application in Python that keeps your to-dos in one place. It should support the following features:

listing tasks
adding a new task
marking a task as completed
archive (deleting all complete tasks)
'''
import sys


def add_item_to_the_lsit():
    new_item = input(str("\n" + "Add an item: "))
    if new_item != "":
        with open("item_list.txt","a") as open_file:
            open_file.write(new_item + "\n" + "not completed" + "\n")
        print("\n" + "Item added.")
    else:
        return new_item


def print_the_list():
    with open("item_list.txt","r") as open_file:
        items = open_file.readlines()
        print("\n" + "You saved the following to-do items:" + "\n")
        for i in range(0, len(items), 2):
                if items[i + 1].strip() == "marked":
                    print("\t" + str(int((i) / 2 + 1)) + ". " + "[X]", items[i].strip())
                else:
                    print("\t" + str(int((i) / 2 + 1)) + ". " + "[ ]", items[i].strip()) 


def mark_the_completed_task():
    print_the_list()
    user_choose = int(input("\n" + "Which one you want to mark as completed: "))
    with open("item_list.txt","r+") as open_file:
        items = open_file.readlines()
    switch_marked_file(user_choose, items)


def switch_marked_file(user_choose, items):
    if user_choose <= len(items) / 2:
        items[(user_choose - 1) * 2 + 1] = "marked\n"
        with open("item_list.txt", "w+") as writefile:
            for item in items:
                writefile.write(item)
        print("\n" + items[(user_choose - 1) * 2].strip() + " is completed")


def delet_the_completed_task_from_the_list():
    with open("item_list.txt","r+") as open_file:
        items = open_file.readlines()
    with open("item_list.txt", "w+") as removefile:
        for i in range(1,len(items),2):
            if items[i] != "marked" + "\n":
                removefile.write(items[i - 1])
                removefile.write("not completed" + "\n")
    print("\n" + "All completed tasks got deleted.")


def specifying_command():
    ask_for_commad = input("\n" + "Please specify a command [list, add, mark, archive]: ")
    if ask_for_commad == "add":
            add_item_to_the_lsit()
    elif ask_for_commad == "list":
            print_the_list()
    elif ask_for_commad == "mark":
            mark_the_completed_task()
    elif ask_for_commad == "archive":
            delet_the_completed_task_from_the_list()            


def main():
    specifying_command()


if __name__ == '__main__':
        main()
