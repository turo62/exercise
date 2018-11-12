import random

colo = []
col = open("colors.txt", 'r')
for line in col.readlines():
    colo.append(line.strip())

col_t = []
col1 = open("sent_col.txt", 'r')
for line in col1.readlines():
    col_t.append(line.strip())

noun = []
noun1 = open("sent_noun.txt", 'r')
for line in noun1.readlines():
    noun.append(line.strip())

cel = []
cel1 = open("sent_cel.txt", 'r')
for line in cel1.readlines():
    cel.append(line.strip())

def rand_col():
        number_of_samples = 1
        random_color = random.choice(col_t)
        return random_color

def rand_noun():
        number_of_samples = 1
        random_items = random.choice(noun)
        return random_items

def rand_cel():
        number_of_samples = 1
        random_cel = random.choice(cel)
        return random_cel

def get_input(colo):
        color = input("Enter a color: ")
        x = False
        while not x:
                if color in colo:
                        x = True
                else:
                        print("Undefined color")
                        color = input("Enter a color: ")
        return color

def forw():
    color = get_input(colo)
    plural_noun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity: ")
    print(rand_col() + " " + color)
    print(plural_noun + " " + rand_noun())
    print(rand_cel() + " " + celebrity)

def main():
        forw()

if __name__ == '__main__':
        main()

