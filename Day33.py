#Learning Python Day33

#OS Module
'''
Os module is used to check, change and do lots of stuff with
directories and folders and stuff.
'''

import os

print(os.getcwd()) #Shows the current directory.

'''
As the name says, current directory is the directory 
you are currently working on, and if you try to open a 
file which is not in your current working directory, you'll get an error.
Let's try it, and for it we'll use a file which is present in you system,
but not on the working directory.
'''
# f= open('Hahahaha.txt')
# f.close()

'''
I commented it because it gives of an error.

Next, see some more functions we get with os module.
'''
print(dir(os))  #List of all functions os modules is composed of.

# os.chdir('/sdcard') #To change directory.
# print(os.getcwd())

print(os.listdir('/sdcard')) #List of all directories present at that given location.

'''
Reasons to comment that one, first I don't want my directory changed, 
not that I can't rechange it, but since it's not going to run on yours
because that directory is on my device not yours so, to try it out, you'll
have to edit it, so you can also uncomment it that time.

Also, everywhere where it asks for a path, give the path of your device coz, mine 
might not exist in your device.
'''

os.mkdir('Hello') #To make a directory.
os.rmdir('Hello') #To remove a directory.
os.makedirs('Hello/Hi') #To create a directory inside a directory.
os.removedirs('Hello/Hi') #To delete directories.

os.mkdir('Rename')
os.rename('Rename', 'Renaaaaaam')
os.rmdir('Renaaaaaam')

'''
Folders are simultaneously created and then, deleted so, comment out removing code lines
to test the folder creation, and comment out the creater lines to test out the deletion,
also, if you won't comment creation lines while testing the deletion, it will give you an error
because the folder will already exist from the last time you used the code while testing the
creation, and while testing the renaming, do the same thing, leave one and comment out others.

There are lots more fns, you can check it on the web, it's not like you have to memorize it all,
you just have to check it that it exist, so that whenever you need it, you know that it exists and
can search it again on the web for how to use it.
'''

