#Learning Python Day18

#Enumerate
lst = ['India', 'US', 'UK', 'Japan', 'Singapore']
i = 1
for item in lst:
    if i % 2 == 0:
        print(item)
    i += 1

'''
Suppose, you are working on a list, and you want to print elements at the place of two and
its multiple, so you build a program like that one above. But it kinda took six lines, ya
you can shorten it a bit, but what if you have to do something more complex and need all the 
list elements to kinda have an index no. That's when comes the Superhero named Enumerate, it
gives an index to all the list and tuple elements.
'''

lst2 = ['English', 'Hindi', 'Maths', 'Science', 'S.St.']
for index, item in enumerate(lst2, 1):
    if index % 2 == 0:
        print(item)
print(type(enumerate(lst2)))        
'''
Look, we did the same thing with a different list but just in four lines. Here, index refers
to the numbers assigned to the list elements, the items are.... items. And the second 
argument given to enumerate is the number where the indexing will start from, it has the 
value 0 as default but as you can see I changed it to 1. Also, as you can see, the data type
is tuple even though lst2 was a list. It means that enumerate changes data type to tuple, and
dont think it will change tuple into lists, tuples stay tuples.
'''
