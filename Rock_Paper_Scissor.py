import random

def rps(n):
    u_points = 0
    c_points = 0

    for i in range(n):
        c = random.choice(['R', 'P', 'S'])
        u = input('R or P or S? ').capitalize()

        if u != 'R' and u != 'P' and u != 'S':
            print('Invalid Selection')
            c_points += 1
        elif who_wins(c,u) == 'u' or c == u:
            u_points += 1
        else:
            c_points += 1
        print(f'Points: {u_points}')

    if u_points > c_points:
        print('You Won!')
    elif u_points == c_points:
        print('The Game Tied!')
    else:
        print('Sorry, You Lost.')

    print('Thank You For Playing!')

def who_wins(c,u):
    if (c == 'R' and u == 'P') or (c == 'S' and u == 'R') or (c == 'P' and u == 'S'):
        return 'u'
    return 'c'

try:
    n = int(input('How many chances do you want? '))
    rps(n)
except:
    print('Invalid Number')