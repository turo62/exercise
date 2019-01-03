def how_much_i_love_you(nb_petals):

 #List of choices at petal removal.

    list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    length = len(list)

#Returns the right element of list in case nb_petals lower than
# number of items in list.

    if nb_petals <= length:
        output = list[(nb_petals-1)]
#Returns the right element of list in case nb_petals higher than 
# number of items in list.
  
    else:
        if nb_petals > length:   
            c = nb_petals % length
            output = list[c-1]
    return output

def main():
    output = how_much_i_love_you(23)
    print(output)

if __name__ == "__main__":
    main()