import string


def import_high_scores():
    scores = []
    with open("high_score.txt", "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split(",")
            scores.append(line)
    print(len(scores))
    return scores


def print_high_scores(scores):
    for score in scores:
        print((score[0]).ljust(20), "| ", (score[1]).ljust(10), "| ", (score[2]).ljust(3), "| ", (score[3]).ljust(3), "| ", (score[4]).ljust(18))


def main():
    scores = import_high_scores()
    print_high_scores(scores)


if __name__ == "__main__":
        main()
