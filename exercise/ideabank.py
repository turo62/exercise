def idea_bank():
    with open("ideabank.txt", "a") as file:
        idea = []
        new_idea = ""
        new_idea2 = ""
        i = 1
        while True:
            new_idea = input("What your new idea? (Enter letter N if finished.): ")
            if new_idea == "N":
                return idea
            elif new_idea != "N":
                new_idea = + new_idea + "\n"
                new_idea2 = str(i) + ". " + new_idea
                file.write(new_idea)
                print(new_idea, "\n")
                idea.append(new_idea2)
                i += 1
    file.close()
    return idea

def main():
    idea = idea_bank()
if __name__ == "__main__":
    main()