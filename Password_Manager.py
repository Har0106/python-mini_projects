from cryptography.fernet import Fernet

# Don't use f string when encrypting or decrypting

print('Welcome to password manager!')
print('\nEnter view to view existing password.\nEnter add to add a new account and password.\nEnter quit to exit password manager.\n')

# with open('key.key', 'wb') as key_file:
#     key = Fernet.generate_key()
#     key_file.write(key)

with open('key.key', 'rb') as key_file:
    key = key_file.read()

fer = Fernet(key)

def add(account, password):
    with open('password.txt', 'a') as file:
        file.write(f'{account}: ' + fer.encrypt(password.encode()).decode() + '\n')

def view(account):
    with open('password.txt', 'r') as file:
        for i in file.readlines():
            if i.startswith(account):
                account, password = i.rstrip().split(': ')
                print('Password:', fer.decrypt(password.encode()).decode())
                break
        else:
            print('There is no such account')

while True:
    activity = input('What do you want to do? ').strip().lower()

    if activity not in ['view', 'add', 'quit']:
        print('Invalid input. Try again.')
        continue

    if activity == 'quit':
        break
    elif activity == 'view':
        account = input('Account: ').strip().capitalize()
        view(account)
    else:
        account = input('Account: ').strip().capitalize()
        password = input('Password: ')
        add(account, password)