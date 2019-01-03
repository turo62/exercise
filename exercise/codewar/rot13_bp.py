# Did not work locally. Test accepted.
import string
from string import maketrans, lowercase as lc, uppercase as uc

def rot13(message):
    tran = maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
    return message.translate(tran)
           
def main():
    new_mess = rot13("Test")
    print(new_mess)


if __name__ == "__main__":
    main()