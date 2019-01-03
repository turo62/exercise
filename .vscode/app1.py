import random
from time import sleep

def valid_choice(choice):
    for character in choice:
        if character not in "HT":
            return False
        return True

comuter_start = random.choice([False, True])
player_choice = ""
if computer_start: