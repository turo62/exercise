# Net best practice.
def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);

def main():
    len = divisors(24)
    print(len)

if __name__ == "__main__":
    main()

# Mine.
def divisors(n):
    div_num = 0
    for i in range(1, n+1):
        if (n % i) ==0:
            div_num += 1
    return div_num

def main():
    div_num = divisors(24)
    print(div_num)

if __name__ == "__main__":
    main()