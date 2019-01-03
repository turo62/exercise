def iq_test(numbers):
    list1 = []
    nums = ""
    nums = (numbers.split())
    for i in range(0,len(nums)):
        list1.append(int(nums[i]))
    even_nums = []
    odd_nums = []
    odd = 0
    even = 0
    num = 0
    for x in list1:    
        if x % 2 == 0:     
            even_nums.append(x)
            even = list1.index(x)
        else:       
            odd_nums.append(x)
            odd = list1.index(x)
    if len(even_nums) > len(odd_nums):
        num = odd + 1
        return num
    else:
        num = even + 1
        return num
        
def main():
    num = iq_test("1 2 2")
    print(num) 

if __name__ == '__main__':
    main()