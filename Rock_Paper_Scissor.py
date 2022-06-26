import random

print('Welcome to rock paper scissor game!')
print('\nType \nR for Rock \nP for Paper \nS for Scissor\n')
print('You will have to choose R, P or S ten times to see who wins')

user_score = 0
computer_score = 0
n = 0

while n < 10:
    computer_choice = random.choice(['R', 'P', 'S'])
    user_choice = input('R or P or S? ').capitalize()

    if user_choice not in ['R', 'P', 'S']:
        print('Invalid Selection. Try Again.')
        continue 

    if computer_choice == 'R' and user_choice == 'P':
        print(f'You won round {n+1}')
        user_score += 1
    elif computer_choice == 'S' and user_choice == 'R':
        print(f'You won round {n+1}')
        user_score += 1   
    elif computer_choice == 'P' and user_choice == 'S':
        print(f'You won round {n+1}')
        user_score += 1
    else:
        computer_score += 1
        print(f'Computer won round {n+1}')

    n += 1

if user_score > computer_score:
    print('You Won!')
elif user_score == computer_score:
    print('The Game Tied!')
else:
    print('Sorry, You Lost.')

print('Thank You For Playing!')
