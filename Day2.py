#Learning Python Day 2

import random
#Modules
''' Modules are premade function available for us, preinstalled in python 
or to be installed from the internet using pip, for example write in terminal 
"pip install flask" and are imported using fn(function) import, above I have imported a 
premade fn called random already installed via python'''

#Concatinating lines
print("Hello")
print("World")
print("Hello", " World") #Hence written two print statements at once.
'''You can also concatinate two str with +'''

#Variables
'''Variables carry values, and change as the code goes'''
var = 5 #Here value of variable var is 5
print(var)
var = var + 5 #Now value of var has changed to 10
print(var)
#Note- Equal sign is used for assigning values and sign of equality is ==

#Typecasting- Changing datatypes
num1 = 45 #Here, value 45 is int.
str(num1) #Now the value of num1 has changed into str.
'''Same goes for int(), and float(). Just don't try to
 convert str into int or float.'''

#Input
number = input()
#Here input fn will ask for input and save in variable 'number'
print(number)
'''Note- Inputs are taken usually as str, before doing operations
you might have to change the type.'''
nm = input('Hello there.')
print(nm)
#Can also write text in input fn like this.

#Multiplying strings
print(10 * "Hi")
'''Now I will get 10 Hi, and if I put a \n, I will get those 10 Hi vertically.
Note- Don't do this with ints or floats, it will just multiply them, first convert
them into strings.'''
print(10 * "Hello, there\n")
print(10 * str(10))

#Mini-Exercise - Creating a code that asks for two numbers and gives off their addition.
print("Enter your first number.")
num1 = input()
print("Enter your second number.")
num2 = input()
print("The sum of the two numbers is", int(num1) + int(num2))
