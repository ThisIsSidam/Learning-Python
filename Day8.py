#Learning Python Day8

#Operators
'''The symbol or whatever is used to operate is called operator.
the numbers or whatever being operated are called operands.'''

#Arithmetic Operators
print('5 + 2 is', 5+2) #Addition- Adds two operands.
print('5 - 2 is', 5-2) #Subtraction- Subtracts two operands.
print('5 / 2 is', 5/2) #Division(float)- Divides two operands.
print('5 * 2 is', 5*2) #Multiplication- Multiplies two operands.
print('5 ** 2 is', 5**2) #Power- Returns first raised to power second.
print('15 // 2 is', 15//2) #Division(floor)- Divides two operands, gives off just integer with quotient.
print('15 % 2 is', 15%2) #Modulus- Divides two operands, gives off just the quotient.

#Assignment Operators
a = 7 #Assigned the value 7 to variable a.
print(a)
a += 7 #Same for a = a + 7, addes the RHS value to var and assigns result value to LHS.
print(a)
a -= 7 #Same for a = a - 7, subtracts the RHS value from var and assigns result value to LHS.
print(a)
#*=, /=, and many more that work similarily, search the internet to know more.

#Comparison Operators
print(5 == 6) #Equality- Compares value and gives boolean result.
print(5 != 6) #Inequality- Compares value and gives boolean result.
#<, >, <= and more that work similarily, search the internet to know more.

#Logical Operators
a = True
b = False
print(a and b) #and- True if both the operands are true.
print(a or b) #or- True if either of the operands is true.
print(not a) #not- True if the operand is false, and vice versa.

#Identity Operators
print(5 is 7) #is- True if the operands are same.
print(5 is not 7) #is not- True if the operands are not same.

#Membership Operators
lst = [4, 45, 3443, 343, 2]
print(2 in lst) #in- True if value is found in the sequence.
print(3 not in lst) #not in- True if value isn't found in the sequence.

#Bitwise Operators
a = 4
b = 7
print(a & b) #Bitwise AND
print(a | b) #Bitwise OR
'''Bitwise AND and OR are operations done in binary form, the values 4 and 7
of a and b will first be changed into binary and then Bitwise operations 
will be done, there are more such as ^(XOR), ~(NOT), etc.
Search the internet for more information.'''