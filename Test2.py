#Python Test2

#Apple Divider

'''
There are twenty kids, you have to ask the user, how many total apples he wants to give.
And then, you have to divide it among the kids equally, no one should get half or one fourth.
If that happens, tell how many more apples from the perfect division you have.
'''

apples = int(input('How many apples do you want to give?\n'))
kids = 20
a = apples/kids

if a.is_integer() == True:
    print(f'{int(a)} apple(s) were given to each kid.')
elif a.is_integer() == False:
    b = a.__ceil__()
    c = (kids*b) - apples
    if c < 10:
        print(f'We need {c} more apple(s).')
    if c > 10:
        print(f'We have {kids-c} more apple(s).')
else:
    print('Something Went Wrong!')