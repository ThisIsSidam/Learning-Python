#Learning Python Day32

#Else and Finally
'''
In Day10 we learnt try and except, else and finally are also there parts.
recalling try and except.
try is for trying if something works or not, if works then ok, if not it will
give an error, but there comes except.
except is if try doesn't work and to handle that error.
now, else is something that will only work if try works, so we can also
say that between except and else, only one will work.
Then, there is finally, it will work doesn't matter try works or not.
'''

#Case1- Try works.
try:
    f = open('ThorOdinson.txt') #A file that exists.
except Exception as e:
    print(e)
else:
    print('This is the else statement.')
finally:
    print('This is the finally statement.')
    f.close()

#Case2- Try doesn't work.
try:
    f = open('zigizagia') #A file that doesn't exist.
except Exception as e:
    print(e)
else:
    print('This is the else statement.')
finally:
    print('This is the finally statement.')

