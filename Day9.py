#Learning Python Day9

#Short-hand If-Else
a = int(input('Enter A\n'))
b = int(input('Enter B\n'))
print('A is bigger.') if a>b else print('B is bigger.')
'''First the print statement and then the reason for it, then else and its print statement.'''

#Functions
#Built-In fn
a = 3
b = 4
c = sum((a , b))
print(c)
'''Here sum is an BuiltIn fn, and the reason behind two brackets is that, that fn only allows 
lists and alike and ints are not iterable, more on that word later, for now it means allowed. 
 Hence, not allowed.'''

#User-Defined fn
def fn():
    print('This is text.')
'''Functions generally have inputs but it doesn't mean they can't exist without them.
This one here is an example of creation of a fn, fns are created with help of keyword
def. There will be no result since i haven't executed the fn yet.'''
fn()
print(fn())
'''first we executed the fn alone, and it worked out well, but when we used print with it,
it also gave out none, coz the fn doesn't return a value to print.'''

def fn2(a, b):
    average = (a + b)/2
    return average
fn2(3, 5) #Executing this won't give anything since i haven't used print.
print(fn2(3,5)) #Now this is perfect.
'''In a file of code, the fns are firstly ignored and if any fn is used then the system goes back
and processes and uses its fns with the current given values and gives off result.'''

#Docstings
def fn3(a, b):
    """"First line after the def line is docstring."""
    v = a + b
    return v
print(fn3)
'''Docstrings are used for writing instructions about the fn that is being created.
Comments are not used coz you can't find them in need but you can find docstrings 
even if the fn is from somewhere else.'''

print(fn3.__doc__) #There are two underscores used on each side.