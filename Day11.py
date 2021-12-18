#Learning Python Day11

#Writing in a file.
'''
I don't want these to be executed, coz it will make changes to the file.
Remove commas and use one by one.
'''
'''
f = open("ThorOdinson.txt", "w") #2nd attribute t is default.
f.write("Keep Coding #Writing")
f.close()

The write() is used to enter data in a file, if used in 'w'(Write mode), it
 creates a file and then writes that data, but if the file
is already present, it will erase all its data and then enter all the new 
data and I don't want that to happen. But  'a'(Append mode)  enters data without 
deleting previous data.

f = open("ThorOdinson.txt", "a")
f.write("Keep Coding #Appending") #This is the same thing above, just in append mode.
a = f.write("Hello")
print(a) #Now this shows the numbers of characters printed on that file.
f.close()
'''

#Reading and writing at the same time
'''
f = open("ThorOdinson.txt", "r+")
print(f.read())
f.write('HEllo wOrLd')

Here we used the 'r' attribute for enabling reading, and the + means update mode.
That helps us in writing.
'''

#Tell and Seek
f = open('ThorOdinson.txt')
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())
f.close()
'''Everytime a file is read, its file handle, 'f' here changes location. like 
if one line is read by readline fn then, if used again the readline fn will read
print the next line. So, the 'tell()' fn tells us the location of the file handle
and 'seek()' changes the location of the file handle, like it jumped the file handle
to 0 in the upper example.'''

#With block
with open('ThorOdinson.txt') as f:
    print(f.readlines())

'''By using 'With' we don't have to close the file, and everything is the same.'''