#Guess the Number

'''Have to make a program, that makes the user guess a hidden number
the program is a game with ten chances
you have to tell the user that the guessed number is larger or
smaller than the hidden number. and in the end you have to tell the number of guesses
the user took, and he ran out of limited guesses print game over.
Also, only fns learnt until Day7 are allowed.'''

HN = 69
guess = 0
print('Guess the Hidden Number')
while(10):
    gs = int(input())
    guess += 1
    if guess == 10:
        print('GAME OVER\n You have used all your 10 chances.')
        break
    elif gs < HN:
        print('Think bigger.')
    elif gs > HN:
        print('This smaller.')
        continue
    else:
        print('You Dirty Minded;) You Guessed The Right Number in', guess, 'tries')
        break

