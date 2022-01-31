# Python Test7

# Fraud Joe

'''
There is a guy named Joe, he made a program that gives the multiplication
table of the number you give to the program, but to treak his friends he
made it so that any one number of that multiplication table is wrong.

So, you have to create Joe's faulty program and then a program to check
which number in the table is wrong.
'''

import random

n = int(input('Which number\'s multiplication table do you want?\n'))

fault_index = random.randrange(1, 9)
table = [n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10,]
table[fault_index] = table[fault_index] + fault_index

print(f'Joe\'s table - {table}')

table2 = [n * 1, n * 2, n * 3, n * 4, n * 5, n * 6, n * 7, n * 8, n * 9, n * 10,]



for i in range(1, 10):
    if table[i] == table2[i]:
        pass
    else:
        print(f'Joe\'s table is incorrect at place {i + 1}.\n'
              f'The Correct multiplication at place {i + 1} is {table2[i]}.')

