import random
import string
import sys
import os
import time
from time import gmtime, strftime
import scores


def rand_capital():
    cap_and_countries = []
    with open("countries-and-capitals.txt", "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            line = line.split(" | ")
            cap_and_countries.append(line)
    cap_and_country = random.choice(cap_and_countries)
    return cap_and_country


def life_points(capital, country):
    points = len(capital) - capital.count(" ") + 2
    guesses = []
    with open("guesses.txt", "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            guesses.append(line)
    if len(guesses) > 0:
        print("Not in word: ", end="")
        for guess in guesses:
            if guess not in capital or list(guess) != capital:
                print(guess, " ", end="")
                if len(guess) == 1:
                    points -= 1
                elif len(guess) > 1:
                    points -= 2
        if points <= 0:
            looser(country)
        elif points > 0:
            print("\n", "You have " + str(points) + " life points.")
    elif len(guesses) == 0:
        print("You have " + str(points) + " life points.")
    return guesses


def get_input():
    guess = input("Enter a letter or the whole word: ")
    guess = guess.upper()
    return guess


def check_guess(capital, guesses, start):
    cap1 = list(len(capital) * "_")
    if len(guesses[-1]) > 1:
        if list(guesses[-1]) == capital:
            winner(guesses, start, capital)
    elif len(guesses[-1]) == 1:
        for i in range(len(capital)):
            if capital[i] in guesses:
                cap1[i] = capital[i]
        if cap1 == capital:
            winner(guesses, start, capital)
        return cap1


def update_guesses(guesses):
    with open("guesses.txt", "a") as f:
        f.write(guesses[-1] + "\n")


def clear_guesses():
    with open("guesses.txt", "w") as f:
        f.write("")


def winner(guesses, start, capital):
    print("\n", "Congratulations! You won!")
    end = int(time.time())
    cap2 = "".join(capital)
    name = input("Enter your name: ")
    score = name + "," + str(strftime("%d. %m. %Y %H:%M", gmtime())) + "," + str(end - start) + "," + str(len(guesses)) + "," + cap2
    scores.update_scores(score)
    print("\n", name + ", " + "you guessed the capital after " + str(len(guesses)) + " letters. It took you " + str(end - start) + " seconds.")
    scores.main_w()
    main()


def looser(country):
    os.system("clear")
    print("\n", "The capital of " + country)
    print(" You lost all your life points!")
    scores.main_w()
    main()


def choice(cap_and_country):
    capital = list(cap_and_country[1].upper())
    country = cap_and_country[0]
    start = int(time.time())
    print(capital)
    while True:
        #os.system("clear")
        guesses = life_points(capital, country)
        if len(guesses) == 0:
            cap1 = len(capital) * "_"
            print(cap1)
            guess = get_input()
            guesses.append(guess)
            update_guesses(guesses)
        elif cap1 == capital:
            False
        elif len(guesses) > 0:
            cap1 = check_guess(capital, guesses, start)
            print(cap1)
            guess = get_input()
            guesses.append(guess)
            update_guesses(guesses)


def main():
    while True:
        title_text = "Would you like to play(1) or want to exit program(0)?"
        print(title_text)
        user_input = input("Enter one of the numbers: ")
        if user_input == "1":
            clear_guesses()
            cap_and_country = rand_capital()
            choice(cap_and_country)
        elif user_input == "0":
            sys.exit(0)
        else:
            print("Wrong input.")


if __name__ == "__main__":
        main()
