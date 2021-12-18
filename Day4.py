#Learning Python Day 4

#Lists
vegies = ["Spinach", "Potato", "Tomato", "Chillies", "Cauliflower"]
#We just made a list
print(vegies)
print(type(vegies))
#We can also have ints in the list but it will make it a mixed list.
#Can also use index accessing and slicing normally with lists.
print(vegies[4])
print(vegies[:3])
print(vegies[::2])
print(vegies[::-1])

numb = [3, 4. ,23 ,233, 2, 12]
'''fns like sort and reverse are used without print and they
change the original value of variable.'''
numb.sort() #sorted the original var
print(numb)
numb.reverse() #reverses the list
print(numb)
numb.append(7) #adds the argument in the end
print(numb)
numb.insert(2, 67) #adds the second argument in the 2nd argument which is the index number
print(numb)
numb.pop #removes the last element of list
numb[2] = 45 #changed the original value at index 2 to 45
#empty lists can also be created just by leaving the brackets empty.

numm = (3, 4, 23, 65)
'''lists use square brackets whereas tuples use parenthesis.
Values in tuples can't be changed'''
print(numm)
print(type(numm))
#numm[3] = 5  because this is a tuple, running this will cause an error hence commented.

#creating a single element tuple
numt = (33, ) #a comma is needed or the system will ignore the parenthesis.
nums = [3]
print(nums)
#creating an empty tuple is useless since you can't add values.


#interchanging variable values
a = 5
b = 7
#traditional way
temp = a #making a temperory variable to hold a's value
a = b
b = temp #hence values interchanged
print(a, b)
#python's easy way
a, b = b, a
print(a, b) #don't match the values with the originals, they were already changed by traditional method

#Also search for more lists, strings and else's functions on the internet.