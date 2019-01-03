def rom_dict(number):
        rom_dict= {1000 : "M",
                900 : "CM",
                500 : "D",
                400 : "CD",
                100 : "C",
                90 : "XC",
                50 : "L",
                40 : "XL",
                10 : "X",
                9 : "IX",
                5 : "V",
                4 : "IV",
                1 : "I"
        }
        
        rom_num = ""
        for k, v in rom_dict.items():
                while number >= k:
                        rom_num += v
                        number -= k
        return rom_num

def main():
        number = int(input("Enter a number: "))
        rom_num = rom_dict(number)
        print(rom_num)
        

if __name__ == "__main__":
    main()