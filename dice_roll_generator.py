import random

roll = input('Enter R to roll a dice, Q to quit: ').capitalize()

if roll == 'Q':
    quit()
elif roll == 'R':
    while True:
        print(random.randrange(1,7))
        roll_again = input('Enter R to roll the dice again, Q to quit: ').capitalize()
        if roll_again == 'Q':
            break
        elif roll_again == 'R':
            continue
        else:
            print('Invalid. Try next time.')
            break
else:
    print('Invalid. Try next time.')