file = open("employee.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("employee.txt", "w")
file.write("Some new text")
file.close()

file = open("employee.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()