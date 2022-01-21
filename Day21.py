#Learning Python Day21

#Object Oriented Programming (OOPs)
'''
Object-oriented programming is a programming paradigm based on the concept of "objects",
which can contain data and code: data in the form of fields, and code, in the form of
procedures. A feature of objects is that an object's own procedures can access and
often modify the data fields of itself.(Copy pasted from the internet)
'''

#Decorators
def Alpha(Afn):
    def Beta():
        print('Starting!')
        Afn()
        print('Ending!')
    return Beta()

@Alpha
def Gama():
    print('Middle stuff!')

'''
Here, on line 11, @first is a decorator. It is like a coating for the fn 'third'.
It is used by adding an '@' along with the fn you want the second fn to be coated on,
above the def statement of that second fn.
'''

#Classes and Instances
'''
Think it this way, you have a form, and in that form are options like your name, age and
stuff like that, that you have to fill up. So, that form is a class, and just like there 
are multiple copies of that forms belonging to different people, there are multiple copies
of that class created whenever a new instance is created. And those options like name and age
and stuff that we have to fill in a form are called instance variables that have separate values
belonging to each instance.
'''

class student: #We just created a class.
    pass

aman = student() #These are the instaces.
priyanshu = student()

aman.name = 'Aman Kumar Singh' #This is an instace variable.
priyanshu.name = 'Priyanshu Kumar Singh'
aman.age = 16
priyanshu.age = 19

print(aman.name, priyanshu.age)
print(aman.__dict__)

'''
And we can check out all the values of the instance variables in the way that you can see
above.
'''


