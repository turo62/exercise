def get_sum(a, b):
    c = 0
    sum = 0
    
    if b > a:
        c = b
        b = a
        a = c
    for i in range(b, (a + 1)):
        sum = sum + i
        i += 1
    if a == b:
        sum = a
    return sum

def main():
    sum = get_sum(-5, 15)
    print(sum)

if __name__ == "__main__":
    main()
