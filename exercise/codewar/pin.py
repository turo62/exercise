import string

def validate_pin(pin):
    length = len(pin)
    nums = string.digits
    if length == 4 or length == 6:
        for i in range(length):
            if pin[i] not in nums:
                number = False
                break
            else:
                number = True
    else:
        number = False
        
    return number

def main():
    number = validate_pin("5957")
    print(number)

if __name__ == "__main__":
    main()