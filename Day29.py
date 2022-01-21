#Learning Python Day29

#Object Introspection
#It just means getting data or say information on objects

print(type(6))

#We just got the info that, that object '6' in an int.

print(id('Hello World'))

#Everything has an id in python, and that's the way to get it.

class parts:
    def __init__(self, name):
        self.name = name

hand = parts('Hand')
print(dir(hand))

'''
dir() is a powerful inbuilt function which returns list of the attributes and 
methods of any object (say functions , modules, strings, lists, dictionaries etc.)
'''

import inspect
print(inspect.getmembers(hand))

'''
The inspect module helps in checking the objects present in the code that we 
have written. As Python is an OOP language and all the code that is written 
is basically an interaction between these objects, hence the inspect module 
dbecomes very useful in inspecting certain modules or certain objects.
'''

#Iteration and Generators
'''
There are three terms, iterable, iterators and iteration. Iterating something is 
 called iteration, the thing can be iterated if it is iterable, and the thing that
 it is iterated with is called the iterator. Think of the range 
fn, it is something called a generator which is nothing but an iterator. 
When you use it in a for fn, give it an input 5, it writes 1,2,3,4, and 5.
How does it actually happen, are those numbers stored somewhere, no, they are 
generated, how?, because range is a generator, it generates it one by one,
you run it, it will give you 1, run it again, it will give you 2 and same way
it will reach 5, and that is what the for fn is used, to run it again and agian.
 
So, moving on from that, iterable are stuff that can be used by iterators, they 
include strings, lists, tuples and dictionaries. Data types like, int and floats
are not iterables.
Now, the question may arise that how can range which is a generator use ints which 
are not iterables. We'll talk about it, after we see some things. 
'''

h = iter('hello world')
print(h.__next__())
print(h.__next__())

'''
By using the fn iter, I made it usable by the iterators, which was that __next__ fn.
If I keep doing it, it'll print the whole thing, including the space, cause that is also 
a character for it, and in the end cause an error when nothing else is there to print. 
'''

def gen():
    for i in range(4):
        yield i

four = gen()
print(four.__next__())
print(four.__next__())
print(four.__next__())

'''
We just created a generator, it is literally same as creating a fn, we just have to use the
keyword 'yield' instead of 'return', it's use is also similar to return, return just returns 
the value it gets, but yield also saves that value and the next time it is used, it resumes from 
the saved state. 

Now, the question we had previously, so, I searched the net but didn't get anything, it's not like
I googled the shit out of google, I just did a single search and I didn't get the thing I was asking 
for on top, so, this is what I think, with strings and lists, they have a limit, there are a limited 
amount of characters in them, like, we did that hello world thing on line 55, it started from h and
will end on d, but in ints and floats there aren't any boundaries, they just go on and on and on, 
the thing called infinity exists because of them. Now, if you are thinking something like why with
ints like 53454 it doesn't print like 5 then, 3 then, 4 and so on, then tell me what difference will
there be between ints and strings, if you just wanna do that, then type that number as a string.

Also, with this we end our story of Object Oriented Programming.
'''
