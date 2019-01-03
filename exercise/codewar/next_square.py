def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

def main():
    next_square = find_next_square(121)
    print(next_square)

if __name__ == "__main__":
    main()