# Write a function called find_oldest_person that

# takes a CSV filename as its parameter
# reads and processes the CSV file
# and returns the oldest person's name.
# If there are multiple people with the same age in the file it doesn't matter which one is returned by the function.

# The CSV file is structured as follows

# Joe,10
# Mary,18
# Ma,x28
# Create simple CSV files to test your own method.

# Calling your function with the filename of such a file should result in 'Max' as he's the oldest.

def find_oldest_person(filename):

    with open(filename, "r") as f:
        name_list = f.readlines()
    if len(name_list) == 0:
        return None
    list_of_names = []
    with open(filename, "r") as f:
        for i in f.readlines():
            i = i.strip("\n")
            i = i.split(",")
            list_of_names.append(i)
    oldest_person = ""
    max = 0
    for row in list_of_names:
        if max < int(row[1]):
            max = int(row[1])
            oldest_person = row[0]

    return oldest_person


def main():
    print(find_oldest_person("people.csv"))

if __name__ == "__main__":
    main()
