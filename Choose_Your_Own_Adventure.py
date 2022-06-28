import random

class ExitHouse():
    def __init__(self):
        self.lives = 0
        self.weapon = False
        self.qanda = [['What country has the highest life expectancy? ', 'Hong Kong'], 
                        ['What is the most common surname in the United States? ', 'Smith'],
                        ['Who has won the most total Academy Awards? ', 'Walt Disney'],
                        ['How many elements are in the periodic table? ', '118'],
                        ['Which planet in the Milky Way is the hottest? ', 'Venus']] 

    def tenth_room(self):
        print('Welome to Exit The Dangerous House!')
        print('Now you are in room 10. Where do you want to go next?')

        room = input('\nRoom 8/9: ').strip()
        if room == '8':
            self.eigth_room()
        elif room == '9':
            self.ninth_room()
    
    def ninth_room(self):
        print('You entered into stone age and explored extinct animals.')
        print('And also you recieved a weapon from caveman.')
        self.weapon = True

        room = input('\nRoom 6/7: ').strip()
        if room == '6':
            self.sixth_room()
        elif room == '7':
            self.seventh_room()

    def eigth_room(self):
        print('You entered the space and explored the galaxy.')
        print('And also you got 2 lives from kind aliens.')
        self. lives += 2

        room = input('\nRoom 6/7: ')
        if room == '6':
            self.sixth_room()
        elif room == '7':
            self.seventh_room()

    def seventh_room(self):
        print('You entered a circus and played a lots of games.')
        print('And also you got 5 lives from the games you won.')
        self.lives += 5

        room = input('\nRoom 2/3: ')
        if room == '2':
            self.quiz_room()
        elif room == '3':
            self.third_room()

    def sixth_room(self):
        print('You entered into a palace and met the princess.')
        print('And also you got 3 lives form her.')
        self.lives += 3

        room = input('\nRoom 4/5: ')
        if room == '4':
            self.fourth_room()
        elif room == '5':
            self.fifth_room()

    def fifth_room(self):
        print('You were burnt in the chemical rain.')
        if self.lives >= 3:
            print('But you survived using 4 lives')
            self.lives -= 3
        else:
            print('Sorry. You died.')
            return

        room = input('\nRoom 0/1: ')
        if room == '0':
            self.win_room()
        elif room == '1':
            self.luck_room()

    def fourth_room(self):
        print('You were eaten by a Titanoboa.')
        if self.weapon:
            print('You killed the Titanoboa with the weapon.')
            self.weapon = False
        else:
            print('Sorry. You died.')
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

        room = input('\nRoom 4/5: ')
        if room == '4':
            self.fourth_room()
        elif room == '5':
            self.fifth_room()

    def luck_room(self):
        print('Welcome to the room of luck.')
        print('We are going to toss a coin. What do you choose?')

        toss = random.choice(['Head', 'Tail'])
        choice = input('Head/Tail: ').strip().capitalize()
        if toss == choice:
            print('You won the game! Congratulations!')
        else:
            print(toss, 'on the coin.')
            print('Sorry. You lost.')

    def quiz_room(self):
        print('Welcome to the quiz room.')
        
        quiz = random.choice(self.qanda)
        answer = input(quiz[0]).strip().capitalize()
        if answer == quiz[1]:
            print('You won the game! Congratulations!')
        else:
            print('Sorry. You lost.')

    def win_room(self):
        print('You entered the with the door.')
        print('You won the game! Congratulations!')
    
ExitHouse().tenth_room()