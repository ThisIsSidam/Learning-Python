#Learning Python Day36

#Regular Expressions.
'''
Regular expressions are a way to kinda filter something from a piece of text,
or a file. I know there are ways you may already know to do that stuff but
Regular expr. are better and special because with them you can search for
stuff you can't search for normally.

Also, for using them we use Raw strings, like fstrings have a f in start, raw
strings have an r in start. In Raw strings, escape sequences and there brothers
don't have any effect, they are just used as normal characters,

Also, don't think what the hell is that string you're gonna see, it's just for explaining stuff.
'''

import re

#Triple quotes are used for multiline string.
str = '''Hello my name is Sidam, and I hope that at the time you are reading
this, I have become a very successfull man.'''

'''Searches for the occurence of what you searched from left to right. Don't
think it's useless,you'll get to know the real meaning of searching in re after
you get to know and learn to use the meta characters and special sequences.'''
print('Result of line 23')
print(re.findall(r'Phone', str))

'''This one finds the first match but also tells its location as index number.'''
print('\n\n\n\nResult of line 31')
print(re.search(r'Phone', str))

'''This one splits, you can use these fns amazingly after you get to know about
the meta characters and special sequences.'''
print('\n\n\n\nResult of line 36')
print(re.split(r'-', str)[0])

'''The thing that we give as 1st argument, that raw string is called the pattern,
the pattern for the search or whatever you want to do, compile fn is used when 
you have to use a single pattern on multiple strings.'''
print('\n\n\n\nResult of line 42')
hllo = re.compile(r'-')
print(hllo.search(str))

'''finditer gives the location of all matches of the given pattern from the given
string. Just that, it returns an iterator object, and if you try to print it, 
you'll just get a location that won't be understandable for you, so, we use for 
statement.'''
print('\n\n\n\nResult of line 50')
hllo = re.finditer(r'-', str)
for match in hllo:
    print(match)
print(hllo)

'''
We'll see Meta characters and Special sequences in Day37.
'''