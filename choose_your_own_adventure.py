import random

class ExitHouse():
    def __init__(self):
        self.lives = 0
        self.weapon = False
        self.qanda = [['What disease commonly spread on pirate ships? ', 'Scurvy'], ['What is the most common surname in the United States? ', 'Smith'], ['Who has won the most total Academy Awards? ', 'Walt Disney'], ['How many elements are in the periodic table? ', '118'], ['Which planet in the Milky Way is the hottest? ', 'Venus']] 

    def eigth_room(self):
        print('Welome to Exit The Dangerous House!\nNow you are in room 8. Where do you want to go next?')
        room = input('\nRoom 6/7: ').strip()
        if room == '6':
            self.sixth_room()
        elif room == '7':
            self.seventh_room()
    
    def seventh_room(self):
        print('You entered a into stone age and explored extinct animals.\nAnd also you recieved a weapon from a caveman.')
        self.weapon = True
        room = input('\nRoom 1/4: ')
        if room == '1':
            self.quiz_room()
        elif room == '4':
            self.forth_room()

    def sixth_room(self):
        print('You entered into the space and explored the galaxy.\nAnd also you recieved 10 lives form the alien.')
        self.lives += 10
        room = input('\nRoom 2/5: ')
        if room == '2':
            self.luck_room()
        elif room == '5':
            self.fifth_room()

    def fifth_room(self):
        print('You were burnt in the chemical rain.')
        if self.lives >= 3:
            print('But you survived using 3 lives')
            self.lives -= 3
        else:
            print('Sorry. You died.')
            return
        room = input('\nRoom 0/3: ')
        if room == '0':
            self.win_room()
        elif room == '3':
            self.third_room()

    def forth_room(self):
        if self.weapon:
            print('You were in the room of Titanoboa.\nBut you it with the weapon.')
            self.weapon = False
        else:
            print('You were eaten by a Titanoboa.')
            return
        room = input('\nRoom 0/3: ')
        if room == '0':
            self.win_room()
        elif room == '3':
            self.third_room()

    def third_room(self):
        print('You entered the pyramid. But it started to sink.')
        if self.lives >= 3:
            print('But you survived using 3 lives.')
            self.lives -= 3
        else:
            print('Sorry. You died.')
            return
        room = input('\nRoom 1/2: ')
        if room == '1':
            self.quiz_room()
        elif room == '2':
            self.luck_room()

    def luck_room(self):
        print('Welcome to the room of luck.\nWe are going to toss a coin. What do you choose?')
        if random.choice(['Head', 'Tail']) == input('Head/Tail: ').strip().capitalize():
            print('You won the game! Congratulations!')
        else:
            print('Sorry. You lost.')

    def quiz_room(self):
        print('Welcome to the quiz room.')
        quiz = random.choice(self.qanda)
        if input(quiz[0]).strip().capitalize() == quiz[1]:
            print('You won the game! Congratulations!')
        else:
            print('Sorry. You lost.')

    def win_room(self):
        print('You entered the with the door.\nYou won the game! Congratulations!')
    
ExitHouse().eigth_room()