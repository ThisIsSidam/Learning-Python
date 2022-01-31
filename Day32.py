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

#Coroutine
import time

def routine():
    Book = 'This is a long book'
    time.sleep(4)

    while True:
        word = (yield)
        if word in Book:
            print('This word is present in the Book')
        else:
            print('This word is not present in the Book')

co = routine()
print('Started!')
next(co)
co.send('long')
co.send('Albama')
co.close()

'''
you'll mainly have large files that the system will take time to read and as a 
substitute for that we have used the sleep fn, just think that the 'Book' string 
is actually a large file and those 4 secs is the time system takes to read it.

Moving on from that, the function that we created is called the Coroutine, after we
used the next fn on line 52, it read the file or say accessed the code above while,
and after it gets the send fn on line 53 and 54, it accessed the code under while. 

The thing that happens is that, with next it read the whole file for kinda no reason and
with send it gets the thing that it has to do with the file that it read. Here, we sent a 
word, which got saved as yield and then as the var called word, and as told from the if
statement, it searched the word on Book string and since it had already read that file, it 
knew whether that word is in that syntax or not. 

It's very much like Generators, in this case it is capable of telling which word is in it or
not, but needs the send fn to get what to search, also it is crucial to close it since the while
loop is on True which means it won't end, and will keep taking on device space.
'''

