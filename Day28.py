#Learning Python Day28

#Abstract Base Class
from abc import ABC, abstractmethod

class pillows(ABC):

    @abstractmethod
    def softness(self, softy):
        pass

class soft(pillows):
    def softness(self, softy):
        return f'{softy} Very, very soft.'

pillow24 = soft()
print(pillow24.softness(24))

'''
Doing the things we did above, like importing ABC and absractmethod from abc, and using it, 
it makes that class, Abstract Base Class. It doesn't accept any instanceand is used as a blueprint 
for the classes that inherit it. Every method created in it which has the abstractmethod decorator 
on it becomes a must for the classes that inherit it. If you make a class and try using it without
creating a method which is in the base class, it will give you an error. Try changing the name of 
that softness method in the soft class and using it.
'''

#Property decorator, setter,getter and deleter.

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)

del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)

'''
Property dec is for using methods as instance var, coz like, when you use a method you have to 
add braces in the end but after using property dec, you don't hav to do that. After that, setter
is used to set stuff, deleter is to delete stuff but in python, stuff isn't actually deleted, it's
just changed to nonetype. 
I know, I'm not explaining it nicely but you got the whole internet, search a bit.
'''