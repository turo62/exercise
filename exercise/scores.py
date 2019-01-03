import string


def import_high_scores():
    scores = []
    time = []
    with open("high_score.txt", "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split(",")
            scores.append(line)
    if len(scores) > 10:
        for i in range(len(scores)):
            time.append(int(scores[i][2]))
    while len(scores) > 10:
        del scores[time.index(max(time))]
    open("high_score.txt", "w").close()
    for i in range(len(scores)):
        score = scores[i][0] + "," + scores[i][1] + "," + scores[i][2] + "," + scores[i][3] + "," + scores[i][4]
        update_scores(score)
    return scores


def update_scores(score):
    with open("high_score.txt", "a") as f:
        f.write(score + "\n")


def print_high_scores(scores):
    for score in scores:
        print((score[0]).ljust(20), "| ", (score[1]).ljust(10), "| ", (score[2]).ljust(3), "| ", (score[3]).ljust(3), "| ", (score[4]).ljust(18))


def main_w():
    scores = import_high_scores()
    print_high_scores(scores)


if __name__ == "__main_w__":
        main_w()
