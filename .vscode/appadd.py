add_todo = open("todo1.txt", "a+")
add_todo.write(input("Enter an item: ", "\n"))
add_todo.close()
add_todo = open("todo1.txt", "r")
print(add_todo.read())
