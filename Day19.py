#Learning Python Day19

#How import works
'''
How import works? Just type import and the module name after that and whoosh, its done.
No. When you use import, it searches for that module name everywhere, you can see the
paths that the fn will search, by doing this-
'''

import sys
print(sys.path)

'''
As you can see, it also contains the directory you currently create your files in.
So, if you use the name of a module in a file, and import that same module in that
file, the import fn will import that file itself. It will cause no errors, but if
try to use a fn from that module, it will cause errors, since the import fn will be 
finding that fn inside the very file you will be writing. So, never name a fn on 
the name of a module.
Also if you think the name of a module is a problem for you to use again and agian,
you can use 'as' this way-
'''

import random as ran
s = ['a', 'b']
print(ran.choice(s))

'''
I kinda gave that module a nickname for this file.
You can also, check the version of a module this way-

print(ran.__version__)
'''

'''
Just like from modules, you can take out fns from your previoulsy made files.
you just have to use a normal import keyword. Also, lemme tell you about 'from' 
keyword.

from random import choice

This way you can just write choice, instead of random.choice, and it'll work just fine.
And it works for every module not just random ;) . 
But using from keyword has a problem, if you are using a fn taken out from your own file.
Suppose, you made a fn named 'an' in a file, then you imported that file into another
file. So, if in the current file, if there is a var or something else already named 'an'
the values from the current file and the imported file may collide and cause problems.
Hence, it is preferred to not use the from keywork while importing your own previous file.
You should just use import and the file_name.function_name method, so that whenever you use
a fn it's name is not mismatched with current file's values because this way everytime you will
use that function, you would have addressed that this function_name comes from that file_name. 
'''

#if __name__ == '__main__':
'''
Now, one more problem that comes with using your own files for taking out fns. So, you make files
not just to create fns right. You must have some other stuff like print and for loops and stuff.
So, whenever you import other files, not just their fns but their other stuff also gets executed.
To stop that from happening we have if name == main. 
I have a supporting file for this, named Extradef19, in it there is a fn, also a print is used 
but inside name == main. Check out that file before reading ahead.
'''
import Extradef19

print(Extradef19.add44(4, 5))

'''
It is just like a normal if fn. If '__name__' which is a variable, is equal to '__main__' which 
it will only be inside the original file, execute the code inside it, and if outside that file, 
meaning in the files where it has been imported to, '__name__' becomes the name of the imported file, 
and the code inside it is not executed.
I wrote a print fn outside name == main, just to show that the value of __name__ actually changes. 
'''