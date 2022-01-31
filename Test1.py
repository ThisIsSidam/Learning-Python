#Python Test1

#What's your age?

'''
Create a program, in which you have to ask for the user's age or birth year, you
have to check yourself if it is an age or year. After that you have to ask when's age do you wanna know,
and tell them what their age will be in that year.
Don't use modules!!
'''
print('With this program you can know your age in a future year.')

ayear = int(input('Type your BirthYear or Age.\n'))

if 100 < ayear < 1900 or ayear > 2022:
    raise Exception('Stop Lying!')
elif 1900 < ayear < 2022:
    pass
elif 0 < ayear <= 100:
    ayear = 2022 - ayear
else:
    print('Something Went Wrong.')

byear = int(input('What is the year you want to know your age of.\n'))

if byear > 2022:
    print(f'Your age in {byear} is {byear - ayear}')
if byear < 2022:
    print('You really wanna go back in your mama\'s womb')

