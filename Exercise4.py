#The Shooting Stars

'''This time we have to write a code that enables us to take two numeral inputs from user
and then print no. of rows as the no. of first input. The second input will tell the code
whether the stars will be in ascending order or descending coz the first no. will also tell
us to print the many no. of stars in each row, like in ascending order the first row will have
one star, second row will have two stars and so on, and the descending order will be just
the opposite.
Also, fns only till Day11 are usable. '''

print('Hello there, Let\'s play the game The Shooting Stars')
n = int(input('Type a number from 1 to 50.\n'))
nn = int(input('Choose 0 or 1\n'))
nnn = bool(nn)

if nnn == True:
    for i in range(1, n + 1, 1):
        print(i * '*')
elif nnn == False:
    for i in range(n, 0, -1):
        print(i * '*')
else:
    print('Check your input please!')