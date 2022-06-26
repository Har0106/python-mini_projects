print('Welcome to Python quiz game!')

score = 0

answer = input('What is the extension of a Python file? ').lower()
if answer == '.py':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is .py')

answer = input('Which character is used to give single-line comments? ')
if answer == '#':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is #')

answer = input('What does pip stand for python? ').lower()
if answer == 'preferred installer program':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is preferred installer program')

answer = input('Who developed Python Programming Language? ').lower()
if answer == 'Guido van Rossum':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is Guido van Rossum')

answer = input('Is Python case sensitive when dealing with variables? ').lower()
if answer == 'no':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is no')

answer = input('Which keyword is used for function? ').lower()
if answer == 'def':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is def')

answer = input('Which module in the python standard library parses options received from the command line? ').lower()
if answer == 'getopt':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is getopt')

answer = input('How is a code block indicated in Python? ').lower()
if answer == 'indentation':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is indentation')

answer = input('Which module in Python supports regular expressions? ').lower()
if answer == 're':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is re')

answer = input('In which year was the Python language developed? ').lower()
if answer == '1989':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    print('The answer is 1989')

print(f'You have got {score} points')
print(f'Your Accuracy is {(score/10)*100}')