print('Welcome to contact book!')
print('\nEnter view to view existing contact.\nEnter add to add a new contact.\nEnter quit to exit contact book.\n')

def add():
    name = input('Name: ').title()
    phone = input('Phone Number: ')
    address = input('Address: ')
    email = input('Email: ')

    with open('contacts.txt', 'w') as file:
        file.write(f'{name} : {phone} : {address} : {email}')

def view():
    name = input('Name: ').title()
    
    with open('contacts.txt', 'r') as file:
        for i in file.readlines():
            if i.startswith(name):
                name, phone, address, email = i.split(' : ')
                print(f'Phone Number: {phone}\nAddress: {address}\nEmail: {email}')
                break
        else:
            print('Contact not found.')

while True:
    m = input('What do you want to do? ')
    if m == 'view':
        view()
    elif m == 'add':
        add()
    elif m == 'quit':
        break
    else:
        print('Invalid. Try again.')