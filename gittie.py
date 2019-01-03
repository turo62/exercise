def introduce():
    print("Akármit is nyomtathatok! :)")

introduce()


def joke():
    szam = input("nyomj egy szamot, leginkabb az 1-t")
    if szam == '1':
        print("kacaghatsz")
    else:
        print('miért nem nyomtal 1-t?')
joke()

def add():
    a = 3
    b = 5
    c = a + b
    return c

print(add())

def shout():
    print("Anything.")
