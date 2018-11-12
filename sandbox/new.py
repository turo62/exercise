colo = []
col = open("colors.txt", 'r')
for line in col.readlines():
    colo.append(line.strip())

def main():
    search_l()

def search_l():
    color = input("Enter a color: ")
    i = 0
    length = len(colo)
    if colo.count(color) > 0:
        print(colo.count(color))
        while i < length:
            if colo[i] == color:
                plural_noun = input("Enter a plural noun: ")
                celebrity = input("Enter a celebrity: ")
                print("Roses are " + color)
                print(plural_noun + " are blue.")
                print("I love " + celebrity)
            else:
                i += 1
            
search_l()
