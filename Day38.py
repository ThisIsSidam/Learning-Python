#Learning Python Day38

#Converting .py into .exe
'''
To convert a python file into an exe, we first have to install pyinstaller through pip.
After that, open the terminal at the folder location you have your python file,
run
-pyinstaller file_name.py
It'll take its time, also may give lots of warnings, but will be completed,
if it doesn't, you'll have to search the internet regarding your issue.
If completed, you'll get multiple folders created at that location, in which there will
be a dist or something file which will have your exe file, you can run it, try it.

Now, if you're thinking that, why all these files? They are their to help it run and lots
more, some are details about that file. But if you want just a sinlge file. Then,
run
-pyinstaller --onefile file_name.py

and you'll get a file you want.

Also, a thing you should know.
In terminal, you can also run .txt files as .py, it just needs to contain python code, and
you can even convert it into .exe just like you converted .py.
'''

#Raising Exceptions.
'''
Think your program asks for the user's name, and in response the user gives off a number, but
you don't allow numbers, and there is a ton of code that will run before the program tells the
user that numbers aren't allowed, so what will you do? 
'''

# name = input('What is your name?\n')
# if name.isnumeric():
#     raise Exception('Numbers are not allowed.')
# else:
#       print(f'Hello {name}')

'''
This way it will cause an error and stop the following code from executing.
There are multiple types of exceptions, you can look them up by searching built-in exceptions. 
'''

#The ZeroDivision Error
a = int(input('Give the nominator.\n'))
b = int(input('Give the denominator.\n'))
if b == 0:
    raise ZeroDivisionError('The denominator can\'t be 0.')
else:
    print(f'The division is {a/b}')


#NameError- When a var is not definedd

#SyntaxError- When the syntax is not right.

#IndexError- When you give an index number which is out of range or not even a number.



#Is vs ==
'''
The term 'is' and the operator '==' seems like they might have the same meaning, but 
they don't, ya you can call it similar, but not same.

== - Two objects have the same value.
is - Two references refer to the same object.
'''

a = [3, 4, 5]
b = [3, 4, 5]
print(a == b)
print(a is b)

'''
'==' shows that the the value of the two vars are two different objects that look same, meaning they have 
different memory location.
'is' shows that the the value of the two vars is the same object, and even their memory location is same. 
'''

#The End
'''
This is the last file. 
After this, there was module creation, command utility creation and differences between python 2.x and 3.x.
But, I'm not making files for them, because I don't think I will have to do those in the near future and 
when I'll have to, I'll watch a tutorial, I have seen the videos once already and know about it. Also, there
is nothing in 2.x and 3.x, it's just a thing to know. 
Sayonara!!
'''