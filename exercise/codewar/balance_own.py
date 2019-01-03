def balance(left, right):
    str1 = (left, right)
    bal1 = []
    for str_a in str1:
        sum = 0
        for char in str_a:
            if char == "!":
                sum += 2
            elif char == "?":
                sum += 3
        bal1.append(sum)
    if bal1[0] > bal1[1]:
        return  "Left"
    elif bal1[1] > bal1[0]:
        return  "Right"
    elif bal1[0] == bal1[1]:
        return  "Balance"




def main():
    bal_1 = balance("!??", "?!!")
    print(bal_1)


if __name__ == "__main__":
    main()