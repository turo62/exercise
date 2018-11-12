todo_file = open("/home/turoczi/Dokumentumok/python/todolist.txt", "a+")
todo_file.write("\n" + input("Enter new task: "))
todo_file.close()