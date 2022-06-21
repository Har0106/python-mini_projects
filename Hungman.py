lives = 6
words = 'instrument'
want = set(words)
used = set()

while lives != 0 and len(want) != 0:
    l = input().lower()
    if l in want:
        want.remove(l)
        used.add(l)
    else:
        lives -= 1
    print(''.join([i if i in used else '_' for i in words]))

if len(want) == 0:
    print('You Won!')
else:
    print('Sorry You Lost, Try Again.')