#Rock, Paper and Scissors

'''
In this exercise, we're gonna give the choice to user of selecting one from the three options
Rock, Paper and Scissors, and the system will also choose one randomly, after that it will be
seen who won most times in the 10 times of the game. Also, only stuff learnt until Day15 is
applicable.
'''

import random

print('We are playing Rock, Paper and Scissors.')
lst = ['Rock', 'Paper', 'Scissors']
pp, sp = 0, 0
tms = 0
s = random.choice(lst)
while tms != 10:
    p = input('Choose One:\nR for Rock\nP for Paper\nS for Scissors\n')
    if p == 'r' and s == 'Rock':
        print('It is a draw')
        tms +=1
    elif p == 'r' and s == 'Paper':
        print('You Lost!')
        tms += 1
        sp += 1
    elif p == 'r' and s == 'Scissors':
        print('You Won!')
        tms +=1
        pp += 1
    elif p == 'p' and s == 'Paper':
        print('It is a draw')
        tms +=1
    elif p == 'p' and s == 'Rock':
        print('You Won!')
        pp += 1
    elif p == 'p' and s == 'Scissors':
        print('You Lost!')
        tms +=1
        sp += 1
    elif p == 's' and s == 'Scissors':
        print('It is a draw')
        tms +=1
    elif p == 's' and s == 'Rock':
        print('You Lost!')
        tms += 1
        sp += 1
    elif p == 's' and s == 'Paper':
        print('You Won!')
        tms +=1
        pp += 1
    else:
        break

if pp < sp:
    print(f'The Computer Won the game with {sp} wins!')
elif pp > sp:
    print(f'You Won the game with {pp} wins!')
elif pp == 0 and sp == 0:
    print('Check Your Input!')
else:
    print('It is a draw!')