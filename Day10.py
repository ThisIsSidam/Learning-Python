#Learning Python Day10

#Try-Except Error Exception Handling
a = input('Enter a number.\n')
b = input('Enter another number.\n')
try:
    print('The sum of those two numbers is',
          int(a) + int(b))
except Exception as e:
    print(e)
print('You are a genius.')
'''Normally, two inputs are asked, and it add the two given numbers and gives off result.
But what if the inputs are not numbers, it will cause an error right there and the code 
after that won't be used(I know it's not the right word for it). But since we used try, if
the code under try causes an error, it will leave it out and go to the next code. And if 
I used except after that I did, it will save the error in a var which is e in this case and
as i used under except, it will print out the e which is the error, and move to the next code.'''

#File I/O(Input/Output)
'''Gonna type some words, just see, you'll know what it means later on.
---Attributes---
"r" - Open file for reading - Default
"w" - Open file for writing
"x" - Creates a file if doesn't exist, and causes error if exists.
"a" - Add something in the end

"t" - Text Mode - Default
"b" - Binary Mode
"+" - Update Mode
'''

f = open("ThorOdinson.txt", "rt")
print(f.read(5)) #Can also do slicing.
print(f.read()) #Next time read() is used, it'll just show the remaining.
print(f.read())
f.close()
'''Here, f is used as a 'File Pointer/File ', so after this to recall the opened file
we'll just need to type 'f', open() can have multiple attributes, in which a file name
is a must, second is all those attributes above, 'rt' is default so, it's ok if you 
don't type them. Once used read(), the file becomes usable, and in first read() above, 
we took 6 alphabets and after that we took all, and there is nothing for the third read(). 
And after using that file, it is a must to close it, just like you close your fridge door
after opening it.'''
f = open("ThorOdinson.txt") #r and t are defaults.
print(f.readline()) #For a line.
print(f.readlines()) #For all lines, but as a list.
f.close()

#Many more fns that you can search for online.