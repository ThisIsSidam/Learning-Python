#Learning Python Day24

#Static methods.
'''
In classes, all functions normally become instance methods, and like we have to use
classmethod decorator to create a class method, we have to use a staticmethod
decorator to create a normal method.
'''

class Books:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    @staticmethod
    def great(str):
        print('This is a', str, 'book.')

jungleb = Books('Jungle Book', 256)
mboat = Books('Three Men In A Boat', 224)

Books.great('great')

'''Ta Da! I don't think of muck uses of it, but there's nothing wrong in knowing about it.'''

#Abstractions and Encapsulation
'''
Data abstraction in python and data encapsulation in python programming are related to each other.
The main point that is necessary here to note is that data abstraction is only possible to achieve
through encapsulation.
                     Encapsulation means storing or placing data in a single place to make it 
easily readable and compact in one place. Whereas data abstraction in python programming means to 
hide internal functionalities that are performing on the application using codes and to show only 
essential information (class attributes).

I get what it means, but not actually get it. I'll get it with an example that we may get in future.f
'''