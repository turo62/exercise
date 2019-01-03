def find_nb(n):
#My solution.
    sum = 0
    num = 0
    if ((n ** 0.5) - int(n ** 0.5)) == 0:
        for i in range(int(n ** 0.5)):
            if sum < n ** 0.5:
                num += 1
                sum += num
        #return num
    else:
        num = -1
    #return num

# The right one found on net.
    num = int((2*n**0.5)**0.5)
    if (num*(num+1)//2)**2 != n: return -1
    return num

def main():
    num = find_nb(1071225)
    print(num)

if __name__ == "__main__":
    main()