def lowest_product(input):
    lst_nums = list(input)
    prod_lst = []
    product = 0
    if len(input) < 4:
        return "Number is too small"
    else:
        for i in range(len(lst_nums) - 3):
            prod_lst.append((int(lst_nums[i]) * int(lst_nums[i + 1]) * int(lst_nums[i + 2]) * int(lst_nums[i + 3])))
        product = min(prod_lst) 
    return product


def main():
    product = lowest_product("1234111")
    print(product)


if __name__ == "__main__":
    main()