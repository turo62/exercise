def sort_by_length(arr):
    new_list = sorted(arr,key=len) # To generate reverse list from longest to shortest type ", reverse = True".
    return new_list



def main():
    new_list = sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"])
    print(new_list)

if __name__ == "__main__":
    main()