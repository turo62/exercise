def spec_sum(n):
    x = 0
    for i in range(65, n, 3):
        x += i
    return x

def add(a, b):
    return a + b

# Print the incoming list in ascending order.
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                tmp = list[j]
                list[j] = list[i]
                list[i] = tmp
    print(list, len(list))


def matrix_op(m, n):
    sum = 0
    for i in range(len(m)):
        sum = sum + m[i][n]
    return sum

