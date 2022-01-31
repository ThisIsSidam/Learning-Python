1# Python Test5

# Guess the number MP

'''
We have previously made the guess the number game, as I remember, or maybe not.
Still, this time we are going to make a multiplayer version. You are the user to
give it to ints, and you randomly generate a number between those to numbers.
The user has to  guess that random number. Make it as there are two players
playing the game, whoever guess in the least number of tries wins the game.
'''

import random

a = int(input('Give a number.\n'))
b = int(input('Give a second number greater than the first number.\n'))



achance = 10

print('Player One:')
c = random.randrange(a, b)

# Taking Guesses From Player One
for i in range(achance):
    guess = int(input(f'Make a guess.      Tries left- {achance}\n'))
    achance -= 1
    if guess == c:
        print(f'Player One has guessed the number in {10 - achance} tries.')
        break
else:
    print(f'Player One has used all his {10 - achance} tries.')


bchance = 10

print('Player Two:')
d = random.randrange(a, b)

# Taking Guesses From Player Two
for i in range(bchance):
    guess = int(input(f'Make a guess.      Tries left- {bchance}\n'))
    bchance -= 1
    if guess == d:
        print(f'Player Two has guessed the number in {10 - bchance} tries.')
        break
else:
    print(f'Player Two has used all his {10 - bchance} tries.')


# Checking Who Won
if achance > bchance:
    print('Player One has Won the game.')
elif achance < bchance:
    print('Player Two has Won the game.')
elif achance == bchance:
    print('It\'s a draw.')
else:
    print('Something Went Wrong.')