# Python Test8

# Funny Names

'''
Everyone is sad at school, so you try making a program that switches
the name and title of your school's teachers, and make everyone laugh.
'''

import random

num = int(input('How many names do you want to add?\n'))

full_names = []

for i in range(num):
    name = input('Write a name.\n')
    full_names.append(name)

first = []
last = []
def name_splitter(ls):
    for i in range(len(full_names)):
        a = full_names[i].split()[0]
        b = full_names[i].split()[1]
        first.append(a), last.append(b)
    return

def name_jumbler(ls, ls2):
    a = random.randrange(0, 6)
    b = random.randrange(0, 5)
    print(ls[a], ls2[b])
    return

if __name__ == '__main__':
    name_splitter(full_names)
    name_jumbler(first, last)




