#Learning Python Day30

#Comprehensions
Numbers = []

for i in range(10):
    if i%2==0:
        Numbers.append(i)

print(Numbers)

Numbers2 = [i for i in range(10) if i%2==0]
print(Numbers2)

'''
From line 4 to 8, we did a thing with a method we knew, but on line 12,
we did all that of line 4 to 8 in a single line. That is called 
List Comprehension, there are more like, Dictionary Comprehension, 
Set Comprehension and Generator Comprehension. 

Let's see what we did on line 12, we first wrote what was going to be 
the element of that list, and then we wrote the for statement of it, and 
since we needed that if statement we also added it, List Comprehensions 
are not needed to have if statements. 
'''

Dict = {i:f'Book {i}' for i in range(5)}
print(Dict)

Dict2 = {value:key for key,value in Dict.items()}
print(Dict2)

'''
First, on line 27, we saw the dict comprehension, we first wrote what 
was going to be the element of the dict and then added the rules as we wanted.

Then, on line 30, we saw how to switche place of key to the place of the values.
It was not needed to creating a new dict and could have also done with that same dict.
'''

Sett = {book for book in ['Book 1', 'Book 2', 'Book 1', 'Book 2', 'Book 3']}
print(Sett)

'''
I don't think i need to repeat myseld, only thing to notice is that the element were five,
but the number of elements printed is three, that's because two were duplicates and sets
don't allow duplicates.

This might also concern you that which one uses which braces. List comprehensions use square
braces, both Set and Dict comprehensions use curly braces, but the kind of element substitute 
or say variable they have makes them different and in the end, Generator comprehensions use 
normal braces.  
'''

gen = (i for i in range(10))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

'''
I think, i don't need to explain anything here. 
'''

#Use of Else with For
Books = ['Math', 'English', 'Scince', 'S.St.', 'Hindi']
for i in Books:
    print(i)
else:
    print('All Done')

'''
Here, else will only run if the for fn ends normally.

There are two ways a for fn ends, one after completing what it was asked to do, 
and second with a break. 

So, if it ended after work completion, the else statement will run and if it breaks,
else statement won't run.
'''

for i in Books:
    if i == 'Economics':
        break
else:
    print('Book not found!')