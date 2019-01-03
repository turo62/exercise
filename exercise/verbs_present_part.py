def present_part(verbs_str):
    vowels = ["a", "e", "i", "o", "u"]
    exceptions = ["be", "see", "flee", "knee"]
    length = len(exceptions)
    verbs = verbs_str.split()
    for verb in verbs:
        if (verb[-2] + verb[-1]) == "ie":
            verb = verb[:-2]
            print(verb + "ying")
        elif verb[-1] == "e":
            for i in range(length):
                if verb != exceptions[i]:
                    i += 1
            verb = verb[:-1]
            print(verb + "ing")
        elif verb[-2] in vowels and verb[-1] not in vowels and verb[-3] not in vowels:
            verb += verb[-1]
            print(verb + "ing")
        else:
            print(verb + "ing")

def main():
    present_part("amaze tie work set run ruin shop waste die lie")

if __name__ == "__main__":
    main()
