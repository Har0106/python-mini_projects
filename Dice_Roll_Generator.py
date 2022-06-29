import random

roll = input('Enter R to roll a dice, Q to quit: ')

if roll == 'Q':
    quit()
elif roll == 'R':
    while True:
        print(random.randrange(1,7))
        roll_again = input('Enter R to roll the dice again, Q to quit: ')
        if roll_again == 'Q':
            break
        elif roll_again == 'R':
            continue