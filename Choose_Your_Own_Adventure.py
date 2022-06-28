print('Welcome to Exit the dangerous house!')
print('Now you are in the 13th room')
print('The door to exit the house can be seen in two rooms')
print('You have to enter the number of the room\n')

room =  input('Room 10/12: ')
if room == '10':
    print('You explored a science lab with bottled animals and picked a fire extinguisher.')
    room = input('Room 6/8: ')
    if room == '6':
        print('You were let into a room with fire, but you managed to escape with the use of fire extinguisher')
        room = input('Room 2/4: ')
        if room == '2':
            print('You were let into a room of checmical rain and died')
        else:
            print('You won! You exited the dangerous house!')
    else:
        print('You died in the room of growing jelly moster.')
else:
    print('You went into a garden with flowers and butterflies.')
    room = input('Room 9/11: ')
    if room == '9':
        print('You were eaten by a Titanoboa.')
    else:
        print('You went into a museum of extinct and picked 5 lives.')
        room = input('Room 5/7: ')
        if room == '7':
            print('You were bitten by a Arthropleura but you used 5 lives to save yourself.')
            room = input('Room 1/3: ')
            if room == '1':
                print('You won! You exited the dangerous house!')
            else:
                print('You died in a room full of sand')
        else:
            print('You died in a room with 2000 celsius heat.')
