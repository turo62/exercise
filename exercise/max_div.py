def common_div(num1, num2):
    numh=num1
    divs = []
    if num2 < num1:
        numh = num2
    for i in range(1, numh):
        if num1 % i == 0 and num2 % i == 0:
            divs.append(i)
    print(max(divs))
    print(divs)
    return max(divs)

def main():
    common_div(120, 80)

if __name__ == "__main__":
    main()
