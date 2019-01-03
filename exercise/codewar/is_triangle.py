# Returns whether given numbers can build a triangle.
def is_triangle(a, b, c):
    list = [a, b, c]
    for i in range(3):
        n = 0
        for j in range(3):
            if list[j] > list[i]:
                tmp = list[j]
                list[j] = list[i]
                list[i] = tmp
    if list[2] < (list[0] + list[1]):
        n = True
    else:
        n = False
    return n


def main():
    n = is_triangle(1, 1 ,2)
    print(n)

if __name__ == "__main__":
    main()