def row_sum_odd_numbers(n):
    sum_odd = sum(range((n * (n - 1) + 1),(n * (n +1)), 2))
    return sum_odd

def main():
    sum_odd = row_sum_odd_numbers(4)
    print(sum_odd)

if __name__ == "__main__":
    main()