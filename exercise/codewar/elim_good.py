def elimination(arr):
    for x in arr:
        if arr.count(x) == 2:
            return x
def main():
    x = elimination([2, 5, 34, 1, 2, 1])
    print(x)

if __name__ == "__main__":
    main()
    