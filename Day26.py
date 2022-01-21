#Learning Python Day26

#Access Specifiers
'''
There are three access types, Public, Protected and Private. They are for variables. If
you use them it won't be like you can't you them, you'll still be able to use them and those
specifiers will be there just to notify/specify you that this var is private or protecte


Public- Create vars just the way you have until now, without any underscores in the front.
    They specify public access to the vars. You wanna use them in your inherited classes,
    use them, wanna use them in other files, no restrictions.

Protected- An underscore in the start of the name of a variable is used as the protected
    access specifier. To tell to not to use it anywhere other than that class or it's
    inherited class.

Private- Two underscores in the start of the name of a variable is used as the private
    access specifier, to tell you not to use it outside this class. It also has a special
    feature called Name Mangling with which it won't let you use that variable normally,
    you'll have to include an underscore and the name of its origin class before it.
    It is all to remind you of its private access.
'''
class access:
    public = 7
    _protected = 77
    __private = 777

print(access.public, access._protected, access._access__private)
# print(access.__private)
#Uncomment the above line if you wanna see it create an error.


#Polimorphism
'''
The word polymorphism means having many forms. In programming, polymorphism means the same function
name (but different signatures) being used for different types.
'''
print(33 +77)
print('44' + '34')

'''
Here, the '+' sign shows Polimorphism, when used with ints it adds them, but when used with strings
it sticks them together.
'''

#Super() and Overriding
'''
Suppose, you have a method in a class and then you create an inherited class of that class, and you want
to create a fn with the same name as the previous class, so you do that. Now, this is called Method
Overriding, and because of this the previous method is now unusable. 

Now, if you want to use that previous method, 'super()' will come in handy. It will make that previous 
method reusable.
'''

class A:
    def __init__(self):
        self.var = 'variable in class A.'
        self.special = 'special variable in class A.'
class B(A):
    def __init__(self):
        self.var = 'variable in class B'

shirts = A()
sleevless = B()

# print(sleevless.special)    This one will create an error becuase of overriding.

class C(A):
    def __init__(self):
        super().__init__()
        self.var = 'variable in class C.'

halfshirt = C()

print(halfshirt.special)

'''
So, this way we can reuse the overriden methods. The positioning of the super() also can cause trouble.
'''

class D(A):
    def __init__(self):
        self.var = 'variable in class D.'
        super().__init__()

jeans = D()

print(halfshirt.var)
print(jeans.var)

'''
In line 90, we asked for value of 'var' variable, the search started in class C, and since super() is called
before self.var in line 72, it went in constructer of class A and found value of 'var' variable which was,
'variable in class A' in class A, and went back to class C, and got a different value of 'var' variable which 
was,'variable in class C' in class C, and gave the value. But in line 91, we asked for value of 'var' variable,
the search started in class D, and since value of 'var' variable is given in line 85, it got it, which was, 
'variable in class D', But then it went in super class, and got a different value of 'var' variable which was,
'variable in class A' and so, the system returned that value. Opposite positioning of super() caused this.
'''