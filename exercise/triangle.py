def calc_sides(a, b, c, d, e, f):
    corner_a = [a, b]
    corner_b = [c, d]
    corner_c = [e, f]
    side_a = (abs(corner_a[0] - corner_c[0]) ** 2 + abs(corner_a[1] - corner_c[1]) ** 2) ** (1 / 2)
    side_b = (abs(corner_a[0] - corner_b[0]) ** 2 + abs(corner_a[1] - corner_b[1]) ** 2) ** (1 / 2)
    side_c = (abs(corner_b[0] - corner_c[0]) ** 2 + abs(corner_b[1] - corner_c[1]) ** 2) ** (1 / 2)
    return side_a, side_b, side_c

def calc_area(side_a, side_b, side_c):
    s = (side_a + side_b + side_c) / 2
    area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** (1 / 2)
    area = format(area, " .1f")
    return area


def main():
    side_a, side_b, side_c = calc_sides(0, 0, 0, 3, 5, 0)
    area = calc_area(side_a, side_b, side_c)
    print(area)  


if __name__ == "__main__":
    main()
