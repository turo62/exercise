# "A" and "T" are complements of each other, as "C" and "G"

def DNA_strand(dna):
    output = ""
    for i in range(0,len(dna)):
        if dna[i]=="A":
            output += "T"
        if dna[i]=="T":
            output += "A"
        if dna[i]=="C" :
            output += "G"
        if dna[i]=="G" :
            output += "C"
    return output

def main():
    output = DNA_strand("GATCTC")
    print(output)

if __name__ == "__main__":
    main()
