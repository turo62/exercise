#Works but failed test.
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending' 
    elif arr == sorted(arr)[::-1]:
        return 'yes, descending'
    else:
        return 'no'



def main():
    len = is_sorted_and_how([4, 2, 30])
    print(len)

if __name__ == "__main__":
    main()