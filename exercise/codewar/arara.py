# Returns arara translation of a number. Wrong solution.
def count_arara(n):
    val = ""
    temp = 0
    temp2 = 0
    empty = " "
    dict = {1 : "anane",
            2 : "adak",
            3 : "adak anane",
            4 : "adak adak",
            5 : "adak adak anane",
            6 : "adak adak adak",
            7 : "adak adak adak anane",
            8 : "adak adak adak adak"
        }
    if n > 8:
        temp = n // 8
        val = (dict.get(8) * temp + " ")
        val = val + (dict.get(n % 2)
    if n <= 8:
        val = dict.get(n)
        
    return val




def main():
    val = count_arara(5)
    print(val)

if __name__ == "__main__":
    main()