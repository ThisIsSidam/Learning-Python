#Learning Python Day 3

#Indexing
Var1 = "Just Chill Guys"
print(len(Var1))
'''len fn tells us the length of the string.
Also, indexing(Numbering) starts from 0 in python.
So, index numbers are from 0 to 14 in this case.'''
print(Var1[2])
'''Single num inside Square brackets will show character at that num,
Here, J is 0, u is 1 and so s is 2. '''

#String slicing
print(Var1[0:2])
'''This will slice out the characters inside those numbers.
Note- Character at left num will be included but on right num will be
exluded from the result so output will be Ju.
0 is default value of left index and total num of characters is default 
of right, so if you don't right it, it will be ok.'''
print(Var1[:10])
print(Var1[:])
print(Var1[:30])
'''The result won't have an error even if the 2nd index is larger than 
existing characters, it will just include the maximum number of
 characters there are.'''

#Advance/Extended string slicing
print(Var1[0:15:3])
#The result will consist of evey other 3rd character, coz of third index num.
print(Var1[::2])
print(Var1[-1:15:3])
'''Because of 1st index being -1 it goes to the back of the string, where s is -1
from there 15 characters just include s, and there are no character to jump.'''
print(Var1[::-1]) #Default value of 3rd index is 1, and putting -1 inverts the str.
'''In short, 1st index shows where to start from, 2nd index shows the final point 
and the 3rd index shows how many characters to jump.'''

#More Functions
print(Var1.isalnum()) #Tells us that the variable is alphanumeric or not.
print(Var1.count("l")) #Tells the number of 'l' in variable.
print(Var1.capitalize()) #Capitalizes the first letter of variable.
print(Var1.upper()) #Turns the whole string in capital and fn 'lower' is opposite of this.
print(Var1.endswith("fun")) #Tells if the variable ends with the given argument.
print(Var1.find("chill")) #Tells the starting index of the argument.
print(Var1.replace("chill", "fun")) #Replaces the first argument with the second.

'''If the results of this fns used in the end are different from what you expected, then
look again, they are affected by the fns used previously.'''