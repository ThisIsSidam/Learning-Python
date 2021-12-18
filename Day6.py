#Learning Python Day 6

#Sets
s = set() #Creates a set
print(type(s))
'''Remember studying chapter set in maths, it is same here
whatever we used to do in sets, can be done here also.'''
s.add(2) #We just added an element in set
'''We can also make sets to have a list of elements or make list add it separately.'''
st = set([1, 4, 7])
print(st)
st.add(4)
print(st) #and since its not a list, no same element can exist twice, remember thats a rule in sets.
st.remove(4) #to remove elements.

#other fns like union, intersection and all from set chapters also exist here.
print(st.union(s)) #union- adds two sets
print(st.intersection(s)) #Intersection- keeps only the common stuff of both the sets

#other fns of sets- mostly may also work in lists and else.
print(st.isdisjoint(s)) #checks if the two sets are disjoint
#see more fns on the internet

#If-else
v = 4
t = int(input()) #Directly coverting the defualt str type of input to int.
if t > v:
    print("Greater")
else:
    print("Smaller")
'''It is all simple, if this is true do this or do that. Things to know, ':', called indentation, a colon gives 
a tab/4 spaces, it indicates that the next fn, print in this case is inside or under if fn
and the second print is under else. In our above code, we didn't say that if t<v then do the 
other thing we just said if first line is incorrect do that. so now,'''
if t > v:
    print("Big")
elif t == v: #== is sign of equality and = is sign of value assignment
    print("equal")
else:
    print("small")
'''First thing, i didn't ask for value of t again so giving value once will give two results.
elif is used for in case there are more possibilities, we can also just use if again instead of
elif, but in case there are hundreds of possibilities it is useful to use elif, if used just 'if'
 then the program will check all hundreds of possibilities and then give results, whereas, when used elif,
 and if the second elif line is true, it will break out right there. still multiple ifs are also usable 
 in some cases.'''

lst = [4, 3, 7, 8]
#Using keywords in and not, they mean the same as they mean in english.
print(4 in lst) #result will be a bool.
print(3 not in lst)
if 7 in lst:
    print("YEs")
else:
    print("No")
if 8 not in lst:
    print("Yes")
else:
    print("No")


#Mini-Exercise2 - Creating a code to know a person can drive or not.
print("What is your age?")
age = int(input())
if age < 18:
    print("No, you can't drive.")
elif age == 18:
    print("Can't say, Physical checkup required.")
else:
    print("Yes, you can drive.")







