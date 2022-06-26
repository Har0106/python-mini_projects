import random

print('Welcome to number guessing game')
print('You have to guess a number which is between 0 and 10')

number = random.randint(0, 10)
guesses = 0

while True:
    guess = input('Make a guess: ')

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
    else:
        print('Invalid number. Try Again.')
        continue

    if guess == number:
        print('You won!')
        break
    elif guess < number:
        print('Your guess is below the number')
    else:
        print('Your guess is above the number')

print(f'You got the number in {guesses} guesses')