def balance(left, right):
    val = ((left.count('!') * 2) + (left.count('?') * 3)) - ((right.count('!') * 2) + (right.count('?') * 3))
    return 'Right' if val < 0 else 'Left' if val > 0 else 'Balance'