import sys


def printing_from_commandline():
    if sys.argv[1] == "--print":
        ideas_to_list()


def delete_row():
    if sys.argv[1] == "--del" and len(sys.argv[2]) >= 1:
        num = int(sys.argv[2])
    with open ("ideabank.txt", "r") as file:
        remove = file.readlines()
    with open ("ideabank.txt", "w") as write_file:
        for index, row in enumerate(remove):
            if index != (num - 1):
                write_file.write(row)
    ideas_to_list()


def get_input():
    ideas = []
    new_idea = ""
    while True:
        new_idea = input("What your new idea? (Enter letter N if finished.): ")
        if new_idea == "N":
            return ideas
        elif new_idea != "N":
            ideas.append(new_idea)
    return ideas


def save_ideas(ideas):
    length = len(ideas)
    if length >0:
        with open("ideabank.txt", "a") as file:
            for idea in ideas:
                file.write(idea + "\n")
    file.close()


def ideas_to_list():
    idea_b = []
    idea_f = open("ideabank.txt", 'r')
    for line in idea_f.readlines():
        idea_b.append(line.strip())
    i = 0
    print("Your ideabank:")
    for idea in idea_b:
        i += 1
        print(str(i) + ". " + idea + "\n")
    idea_f.close()


def main():
        if len(sys.argv) > 2:
                delete_row()
        if len(sys.argv) > 1:
                printing_from_commandline()
        else:
                ideas = get_input()
                save_ideas(ideas)
                ideas_to_list()



if __name__ == "__main__":
    main()