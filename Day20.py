#Learning Python Day20

#Join
'''
Suppose, you have a list of items, or names or whatever and you want to
print it out but with a comma, or maybe an 'and' between each item.
'''

lst = ['Venusaur', 'Incineroar', 'Empolean', 'Mamoswine', 'Noivern']

print(' and '.join(lst), 'and sorry I don\'t have a sixth member yet.')

'''
We used join fn, I first chose the thing I wanted to insert between them
and used the join fn after that. 
'''

#Map
'''
Map is used to use a fn on every element of a list or tuple. For, example-
You have a list of numbers in str format but you wanna change it into ints.
'''

ls = ['3', '4', '76', '6']

for i in range(len(ls)): #Without Map
    ls[i] = int(ls[i])
print(ls)

ls = list(map(int, ls)) #With Map
print(ls)

ls = map(int, ls)
print(ls)

'''
We had to do all that without Map, but with map, it was a bit easier and 
will be even more helpfull with long stuff. The two mandatory arguments
in map are- first the function, which was int in this case which we used
to change elements into int and second was the list that we operated on.
Also, map needs the list fn before it, without it, it will print something
like <map object at 0zajfoien33>. Let's see one more example. 
'''

lst = [1, 2, 5, 66, 6444]
lst = list(map(lambda a:a*a, lst))
print(lst)

#Filter
lt = (1, 523, 45, 3, 64, 44, 12)
lt = list(filter(lambda a: a<50, lt))
print(lt)

'''
Very much similar functioning to the Map fn, same arguments. Just the work is
different, and it does exactly what it says, FILTER. 
'''

#Reduce
'''
Reduce is a fn from the 'functools' module.
'''

from functools import reduce

li = [3, 5, 6, 88]
li = reduce(lambda a, b: a + b, li)
print(li)

'''
Similar to the previous ones, and since it's result is not 
a list it doesn't need a list coating. And you can figure out
what else happened in that code.
'''