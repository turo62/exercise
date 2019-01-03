# Returns multiples of an integer up to given limit.
def find_multiples(integer, limit):
    print(arr(range(integer, limit+1, integer)))
    return arr(range(integer, limit+1, integer))

def main():
    find_multiples(5, 25)

if __name__ == "__main__":
    main()
