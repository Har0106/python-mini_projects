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
        print(f'Points: {u_points}', f'\nRemainig Chances: {n-i-1}')

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

n = 0
while True:
    n = input('How many chances do you want? ')
    if n.isdigit() and n != '0':
        n = int(n)
        break
    else:
        print('Invalid number. Try Again.')

if n != 0:
    rps(n)