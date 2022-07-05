import sqlite3

print('Welcome to contact book!')
print('\nEnter view to view existing contact.\nEnter add to add a new contact.\nEnter delete to delete a contact.\nEnter quit to exit contact book.\n')

def add():
    connect = sqlite3.connect('contact_book.sqlite')
    cursor = connect.cursor()
    # cursor.execute('CREATE TABLE Contacts (name TEXT, phone_no TEXT, address TEXT, email TEXT)')
    
    name = input('Name: ').title().strip()

    cursor.execute('SELECT * FROM Contacts WHERE name = ?', (name,))
    row = cursor.fetchone()

    if row is None:
        phone_no = input('Phone Number: ')
        address = input('Address: ')
        email = input('Email: ')
        cursor.execute('INSERT INTO Contacts (name, phone_no, address, email) VALUES (?, ?, ?, ?)',(name, phone_no, address, email))
        print('Contact Added Successfully')
    else:
        print('Contact Already Exists')
    connect.commit()
    connect.close()

def view():
    name = input('Name: ').title().strip()
    
    connect = sqlite3.connect('contact_book.sqlite')
    cursor = connect.cursor()

    cursor.execute('SELECT phone_no, address, email FROM Contacts WHERE name = ?', (name,))
    row = cursor.fetchone()

    if row is not None:
        print(f'Phone Number: {row[0]}\nAddress: {row[1]}\nEmail: {row[2]}')
    else:
        print('Contact Does Not Exist')
    
    connect.commit()
    connect.close()

def delete_contact():
    connect = sqlite3.connect('contact_book.sqlite')
    cursor = connect.cursor()

    name = input('Name: ').title().strip()

    cursor.execute('SELECT * FROM Contacts WHERE name = ?', (name,))
    row = cursor.fetchone()

    if row is not None:
        cursor.execute('DELETE FROM contacts WHERE name = ?', (name,))
        print('Contact Deleted Successfully')
    else:
        print('Contact Does Not Exist')

    connect.commit()
    connect.close()

while True:
    m = input('What do you want to do? ').strip().lower()
    if m == 'view':
        view()
    elif m == 'add':
        add()
    elif m == 'delete':
        delete_contact()
    elif m == 'quit':
        break
    else:
        print('Invalid. Try again.')