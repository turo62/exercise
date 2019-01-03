import random
import string
import sys
import os
import time


def menu():
    answer = ""
    while answer != "N":
        print("Do you want to play (Y or N?")
        answer = input("Enter your choice: ")
        os.system("clear")
        if answer == "Y":
            cap, length = rand_capital()
            print_dash(cap, length)


def rand_capital():
    capitals = ["Tirana", "Vienna", "Minsk", "Brussels", "Sarajevo", "Sofia", "Zagreb", "Nicosia", "Prague",
                "Copenhagen", "Tallinn", "Tórshavn", "Helsinki", "Paris", "Berlin", "Gibraltar", "Athens",
                "Budapest", "Reykjavik", "Dublin", "Douglas", "Rome", "Pristina", "Riga", "Vaduz", "Vilnius",
                "Luxembourg", "Skopje", "Valletta", "Monaco", "Podgorica", "Amsterdam", "Oslo", "Warsaw",
                "Lisbon", "Bucharest", "Moscow", "Belgrade", "Bratislava", "Ljubljana", "Madrid", "Stockholm",
                "Bern", "Kiev", "London"]
    capital = random.choice(capitals)
    cap = capital.upper()
    length = len(cap)
    return cap, length


def print_dash(guess = input("Enter a letter or the word: ")
        guess = guess.upper()
    print(cap)
    cap = list(guess = input("Enter a letter or the word: ")
        guess = guess.upper()
    guess = ""
    life_points guess = input("Enter a letter or the word: ")
        guess = guess.upper()
    guesses = []
    guess = input("Enter a letter or the word: ")
        guess = guess.upper()
    not_in_word = []
    cap1 = length * "_"
    print(cap1)
    cap1 = list(cap1)
    print("You have " + str(life_points) + " life points.")
    start = int(time.time())
    while cap1 != cap or life_points != 0:
        if len(not_in_word) > 0:
            print("\n", "Guesses you missed were: " + str(not_in_word))
        guess = input("Enter a letter or the word: ")
        guess = guess.upper()
        if len(guess) > 1:
            guess = list(guess)
            if guess == cap:
                print("You guessed the capital after " + str(len(guesses)))
                print("\n", "Congratulations! You won!")
                menu()
            elif guess != cap:
                print("\n", "Sorry. You lost.")
                menu()
        elif len(guess) == 1:
            guesses.append(guess)
        os.system("clear")
        for i in range(length):
            for guess in guesses:
                if cap[i] == guess:
                    cap1[i] = guess
        for i in range(length):
            print(cap1[i], end="")
        if guess[-1] not in cap:
            print("\n", "Your guess is not in the word.")
            not_in_word.append(guess[-1])
            life_points -= 1
        print("\n", "You have " + str(life_points) + " life points.")
        if cap1 == cap:
            end = int(time.time())
            print("\n", "Congratulations! You won!")
            print("\n", "You guessed the capital after " + str(len(guesses)) + " letters. It took you " + 
            str(end - start) + " seconds.")
            menu()
        if life_points == 0:
            print("Sorry. You lost.")
            menu()
    return life_points


def main():
    menu()


if __name__ == "__main__":
        main()
