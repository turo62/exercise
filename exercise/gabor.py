# 2018.11.18.
# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


def get_total_count(inventory):
    return sum(inventory.values())


# Displays the inventory.
def display_inventory(inventory):
    print('\n Inventory: \n')
    for key, value in inventory.items():
        print("{} {} \n".format(value, key))
    print('Total number of items: ' + str(get_total_count(inventory)) + '\n')


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order):
    if order == None:
        sorted_inv = list(inventory.items())
    if order == 'count,asc':
        sorted_inv = sorted(list(inventory.items()), key=lambda x: x[1])
    if order == 'count,desc':
        sorted_inv = sorted(list(inventory.items()), reverse=True, key=lambda x: x[1])

    max_len_value = len(str(max(inventory.values())))
    max_len_key = len(max(inventory, key=len))

    # headers
    count_label = 'count'
    item_label = 'item name'
    count_width = 0
    item_width = 0

    if len(count_label) >= max_len_value:
        count_width = len(count_label) + 2
    else:
        count_width = max_len_value + 2

    if len(item_label) >= max_len_key:
        item_width = len(item_label) + 2
    else:
        item_width = max_len_key + 2

    decoriton = (count_width + item_width) * '-' + '--'

    print("\nInventory:\n")
    print(count_label.rjust(count_width), item_label.rjust(item_width))
    print(decoriton + "\n")
    for key, value in sorted_inv:
        print("{} {}\n".format(str(value).rjust(count_width), key.rjust(item_width)))
    print(decoriton + "\n")
    print('Total number of items: ' + str(get_total_count(inventory)) + '\n')


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename):
    with open(filename, "r")as f:
        imported_items = f.read().split(',')
        add_to_inventory(inventory, imported_items)


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename):
    with open(filename, "w")as f:
        total_count = get_total_count(inventory)
        current_count = 0
        for key, value in inventory.items():
            for i in range(value):
                f.write(key)
                current_count += 1
                if current_count != total_count:
                    f.write(",")


def main():
    inventory = {"dagger": 3, "gold coin": 1, "battleaxe": 1}
    display_inventory(inventory)
    dragon_loot = ['gold coin', 'gold coin', 'gold coin', 'ruby']
    order = "count,desc"
    add_to_inventory(inventory, dragon_loot)
    filename = "import_inventory.csv"
    import_inventory(inventory, filename)
    filename = "export_inventory.csv"
    export_inventory(inventory, filename)
    
    print_table(inventory, order)


if __name__ == '__main__':
    main()