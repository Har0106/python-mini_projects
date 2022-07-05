while True:
    n = input('Enter S to use email slicer, Q to quit: ')
    if n == 'S':
        email = input('Enter the email address: ')
        username, domainame = email.split('@')
        print(f'User name: {username}\nDomain name: {domainame}')
        continue
    elif n == 'Q':
        break
    else:
        print('Invalid. Try again.')