#Cpied in three solutions of the problem.
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1

def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1

def mxdiflg(a1, a2):
    if not (a1 and a2): return -1
    l1 = list(map(len, a1))
    l2 = list(map(len, a2))
    return max((max(l1)-min(l2)), (max(l2)-min(l1)))

#And this was mine. :(
def mxdiflg(a1, a2):
    length = len(a1)
    length1 = len(a2)
    if (length == 0) or (length1 == 0):
        max_diff = -1
        return max_diff
    min_a1 = len(min(a1, key = len))
    max_a1 = len(max(a1, key = len))
    min_a2 = len(min(a2, key = len))
    max_a2 = len(max(a2, key = len))
    if (max_a2 - min_a1) > (max_a1 - min_a2):
        max_diff = (max_a2 - min_a1)
    else:
        max_diff = (max_a1 - min_a2)
    return max_diff

def main():
    max_diff = mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"], [])
    print(max_diff)

if __name__ == "__main__":
    main()