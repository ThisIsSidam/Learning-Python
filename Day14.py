#Learning Python Day14

#Lambda / Anonymous functions
def plus(a, b): #This is the general way of making fns.
    return a + b
print(plus(2, 3))

plus2 = lambda a, b: a + b
print(plus2(3, 4))
'''
Lambda is used for convenience, not that you can't live without it.
It is a one-liner for creating fns. Can even be used like this-
'''
a = [[2, 3], [62, 8], [8, 23]]
a.sort(key= lambda x:x[0])
print(a)
'''
Here, The 'Key' argument of sort fn demands a fn, and i made a lambda
fn right where it was demanding the fn, without lambda I would have 
had to create a fn separately, but lambda is there to help with that.
Also there are many fns that if you execute inside print, will give off
just 'none' hence, they are used separately.
'''

#Modules
'''
Some stuff about Modules and installing them is written in the start and
here I am just reminding you not to forget them, they are a very crucial
part of programming and also now you'll know some parts of a module named 
random. And just so you know, modules are always imported in the start of 
a file, but we'll do it here because it is possible and this is like the 
start of this module section. 
'''
import random

lst = ['uck', 'itch', 'cker', 'ole']
a = random.choice(lst)
print(a)
'''
Here, choice is a function inside random module, sometimes fns are inside 
a module's submodules like in the case of datetime module that we have used
earlier, remember we typed datetime.datetime.now it means now fn is inside
datetime module's submodule of the same name. Well, here choice fn demands 
a lst or else for action so we gave it one, and gives off a random choice
out of the various values of that lst.
'''

random_num = random.randint(1,5)
random_num2 = random.randint(0,1)
print(random_num, random_num2)
#Randint fn gives a random value between the gives numbers.

a = random.random()
print(a)
a = random.random() * 8
print(a)

'''Random fn gives off a random value between 0 and 1 and it can be even floats
coz they too are numbers, right.  Multiplying it meand changing min value
which is 0 to 0*8 which is still 0 and max value which is 1 to 1*8, which is 8.
So, the random value we'll get will be from 0 to 8.
Now, all this was just to show how awesome modules can be, although module can do
way awesome things. So, search the net for more modules, and study their fns.'''