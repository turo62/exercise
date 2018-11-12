import random

o_die1 = random.randint(1, 6)
o_die2 = random.randint(1, 6)
o_die3 = random.randint(1, 6)

d_die1 = random.randint(1, 6)
d_die2 = random.randint(1, 6)

print("The offense has rolled a %s, %s and a %s" % (o_die1, o_die2, o_die3))

print("The defense has rolled a %s and a %s" % (d_die1, d_die2))

def winner():
    if o_die1 > d_die1 or d_die2:
        print("The offense has won")
    elif o_die2 > d_die1 or d_die2:
        print("The offense has won")
    elif o_die3 > d_die1 or d_die2:
        print("The offense has won")
    else:
        print("The defense has won")
           
winner()