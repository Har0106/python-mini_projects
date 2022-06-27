print('Welcome to password manager!')
print('\nEnter view to view existing password.\nEnter add to add a new account and password.\nEnter quit to exit password manager.\n')

def view(account):
    with open('password.txt', 'r') as file:
        for i in file.readlines():
            if i.startswith(account):
                account, password = i.strip().split(':')
                print(f'Password: {password}')
            else:
                print('There is no such account.')

def add(account, password):
    with open('password.txt', 'a') as file:
        file.write(f'{account} : {password}\n')

while True:
    activity = input('What do you want to do? ').lower()

    if activity not in ['view', 'add', 'quit']:
        print('Invalid input. Try again.')
        continue

    if activity == 'quit':
        break
    elif activity == 'view':
        account = input('Account: ').capitalize()
        view(account)
    else:
        account = input('Account: ').capitalize()
        password = input('Password: ')
        add(account, password)