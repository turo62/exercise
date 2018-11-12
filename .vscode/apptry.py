try:
    answer = 10/0
    number = int(input("Adj meg egy számot: "))
    print(number)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Téves adatbevitel! Próbálkozz egy számmal!")
