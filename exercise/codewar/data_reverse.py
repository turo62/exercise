def data_rev(arr):
    arr_r = ""
    arr_rev = ""
    data_reverse = []
    for i in range(len(arr)): arr_r += str(arr[i])
    j = len(arr_r)
    for i in range(int(len(arr_r) / 8)): 
        arr_rev += (arr_r[(j -8): j])
        j -= 8
    data_reverse = [int(arr_rev)]
    return data_reverse

def main():
    data_reverse = data_rev([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0])
    print(data_reverse)


if __name__ == '__main__':
        main()