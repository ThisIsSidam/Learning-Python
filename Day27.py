#Learning Python Day27

#Diamond Shaped Problem in Multiple Inheritence.
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

'''
Now, if we make a graph of inheritence for these four classes, we'll get a square shaped graph, 
which is called diamond in this case. According to pros, this causes a lot of problem so it's 
prefferred to use single and multilevel inheritence and not preferred to use multiple inheritence
and to  keep things simple.
'''

#Dunder/Special/Magic methods
'''
Dunder methods are names that are preceded and succeeded by double underscores, hence the name 
dunder (Double Under). They are also called magic methods and can help override functionality for
built-in functions for custom classes.

An example of such method is the __init__ constructer, it has double underscores around it and has
a special functionality of adding instance variable easily that it performs without being called.
'''

# class Books:
#     def __int__(self, price): #Also called Dunder Init
#         self.price = price
#     # def __add__(self, other):    #This is called Dunder Add
#     #     """I will tell you when to uncomment it."""
#     #     return self.price + other.price
#
# maths = Books(150)
# science = Books(200)

# print(maths + science)

'''
Just like we add an instance var, it uses the init constructer in background, when we use +, it uses
dunder add in background, if you try using that print syntax in line 41, you'll get an error because 
currently, it doesn't know what to do, whether to add the prices or the names, but with dunder add,
we've told it to add the prices, so try uncommenting the method on line 34 and print syntax on line 41. 

Also, there are lots more dunder methods that you can know about on the internet.
'''

#Operator Overloading
'''
Operator overloading is the ability of a single operator to perform more than one operation based on the
type of operands(The things that the operator is being used on). For example, the + operator can be used 
to add two numbers, concatenate two strings or merge two lists.

We also saw operator overloading above with the dunder add, the given operands were maths and science but 
the + operator went to dunder add method, found the prices and then added them and gave the result. We
overloaded the work on the + operator.
'''

#repr and str
'''
repr and str are two brother like dunder methods, in which repr is the elder brother, like, when someone's 
on the door, your elder brother says you to open the door but when someone's specifically asking for the elder
bro, he himself goes to check out. It works just like that. 
'''

class switches:
    def __init__(self, role):
        self.role = role
        self.used = 1000
    def __repr__(self):
        return f'It switches on the \'{self.role}\' and was used \'{self.used}\' times.'
    def __str__(self):
        return f'It switches on the {self.role} and was used {self.used} times.'

left = switches('lights')
print(left)
print(repr(left))
print(str(left))

'''
Try commenting both repr and str fns, and also the line 80 and 81, you'll see the result of line 79 as a kind
of address, but with repr and str you get a readable meaningful line, not that the previous line was meaningless, 
It's just me who doesn't understand it yet. So, repr's goal is to be clear that the things that go through it have
direct and clear meaning, it doesn't leave space for ambigous thoughts, like, in the result of line 81, which is
of str, you can have thoughts that the 1000 comes from a variable or not, but in repr, it makes it clear by covering
it with commas, on the other hand, str's goal is to be as readable as it can be.  

Also, if both exist, str is the first to come, as we can see in the result of line 79. 

And it is not just used in OOPS's classes, it is also used without those as you can see below.
'''

import datetime

print(repr(datetime.datetime.now()))
print(str(datetime.datetime.now()))

'''
You can see the difference in results.
'''