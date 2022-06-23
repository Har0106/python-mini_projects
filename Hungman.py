import random

def hungman():
    lives = 6
    words = ['algorithm', 'argument', 'program', 'conditional', 'declaration', 'framework', 'iteration', 'autonomous', 'statements', 'compiling', 'latency', 'asynchronous', 'backpropagation', 'centroid', 'clustering', 'denoising', 'generalization', 'lambda', 'authentication', 'decryption', 'encryption', 'scareware', 'bootstrap', 'debugging', 'deployment', 'microsoft', 'oracle', 'adobe', 'console']
    word = random.choice(words)
    want = set(word)
    used = set()

    while lives != 0 and len(want) != 0:
        l = input('Enter Alphabet Letter: ').lower()
        if l in want:
            want.remove(l)
            used.add(l)
        else:
            lives -= 1
        print(''.join([i if i in used else '_' for i in word]), f"\nRemaining Lives: {lives}")

    if len(want) == 0:
        print('You Won!')
    else:
        print(f'The Word Was {word.capitalize()}')
        print('Sorry You Lost, Try Again.')

hungman()