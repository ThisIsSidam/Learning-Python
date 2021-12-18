#Learning Python Day 1

'''Datatypes
String- Texts
Int- Integers
Float- Decimals
Bool(Boolean expressions)- True or False
Nonetype- None'''

#Print, End and Type
print("Hello World") #Prints out, needed to be in "" or '' for texts.
print(6)
print("6") #This is a string now not int,coz it's in "".

'''With end the print statement with end right there
and won't go to the next line.'''
print("Hello Sidam", end="")
'''We can add anything in end to be added 
in the end of the line.'''
print("Hello Miss", end="Bye")

print(type(6)) #Prints out the Datatype(Of 6 here).
print(type("Hello"))

#Python also works as a Calculater
2+4
2*7-4-3*5/4
'''These ones didn't print coz we ordered to do 
maths but didn't order it to print out the results.'''
print(2+4)
print(2*7-4-3*5/4)

#Comments
'''Texts starting with # or 3 * ' are used for comments, they
don't interere in the code they are just to be read by someone
who is reading the code. # is used for single line comments
 and 3 * ' are used for multi line comment.'''

#Escape Sequances
# \n is a new line sequance, starts a new line
print("Hello \n World")
''' What if you want to write \n in a print functon but can't coz it
will execute it. So, for this we have \.'''
print("This is how we write \\n")
# \ prevents the execution of the function.
'''You can't use "" inside "", coz it will cause errors. So, it's used like this'''
print("He said 'You are bad'") #Or ' in place of " and vice versa
#Now with the use of \
print("I said \"No\"")
