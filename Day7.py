#Learning Python Day7

#For loops
lst = ['red', 'blue', 'green', 'yellow']
for item in lst:
    print(item)
'''Here, we made a list, and in the for fn we called every element of 
the list item, and so for every item we used the print fn.
Also, if we wanna print those items without changing lines, just remove the commas.'''

ltt = [['red', 3], ['blue', 4], ['green', 34], ['yellow', 6656]]
for item, number in ltt:
    print(item, number) #We can also do it this way.
    print(item, 2*number) #Or this way, there are infinite methods to explore.

#Mini-Exercise3 - Creating a list and then printing all items that are numbers and are bigger than 5.
jack = [4, 45, 'cabbage', 78, 45, 3, 'Potato', 'Burger', 777, 979]
for item in jack:
    if str(item).isnumeric() and item>5:
            print(item)

#While Loop
i = 0

while( i < 34):
    print(i)
    i = i + 1
'''Here, I made a var i, gave it a value 0, and for the time its value is <34, the while loop
will keep printing the var i. So, added another line, by which the value of i will keep increasing.
Also, i = i +1 can also be written as, i += i.'''
#For loops work till the list or whatever hasn't finished, and while loops works till the condition is true.

#Continue and Break
i = 0

while(True): #while(True) or while(1) are same they mean, that the loop will run forever.
    if i + 1< 5:
        i += 1
        continue
    print(i + 1)
    i += 1
    if i == 45:
        break
''' Made a program that will just print no. above 5 and below 45. 
Continue means skip the below code and start the loop again.
break means stop the whole loop.'''

#Mini-Exercise4 - Making a program that takes input until the input isn't greater than 100.
while(1):
    tito = int(input('Enter a number.'))
    if tito<100:
        print('Try Again.')
        continue
    else:
        print('You have broken the loop by typing a no. bigger than 100.\n''Congratulations')
        break