#Learning Python Day37

#Meta Characters and special sequances
'''
Meta Characters
[] A set of characters.
\ Signals a special sequence (can also be used to escape special characters).
. Any character (except newline character).
^ Starts with.
$ Ends with.
* Zero or more occurrences.
+ One or more occurrences.
{} Exactly the specified number of occurrences.
| Either or.
() Capture and group.

Special Sequences
-  \A Returns a match if the specified characters are at the beginning of the string.
-  \b Returns a match where the specified characters are at the beginning or at the
end of a word.
-  \B Returns a match where the specified characters are present, but NOT at the
beginning (or at the end) of a word.
-  \d Returns a match where the string contains digits (numbers from 0-9)
-  \D Returns a match where the string DOES NOT contain digits
-  \s Returns a match where the string contains a white space character
-  \S Returns a match where the string DOES NOT contain a white space character
-  \w Returns a match where the string contains any word characters (characters
from a to Z, digits from 0-9, and the underscore _ character).
-  \W Returns a match where the string DOES NOT contain any word characters.
-  \Z Returns a match if the specified characters are at the end of the string.

'''

#This is a text I copied for explanation.
str = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Tata Sonseeeee, North America
1700 North Moore St, Suite 1520

Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
This is Sidam
'''

import re

'''We got lots of explanations, so we'll be making multiple compile lines
which will be used for one finditer line that is at the bottom, uncomment
compiler lines one by one and see their results.'''

'''(Dot) means everything, literally everything, even the spaces, only 
exception is the new line characteres.'''
# str2 = re.compile(r'.')

'''You can use the caret symbol (^) at the start of a regular expression 
to indicate that a match must occur at the beginning of the searched text.'''
# str2 = re.compile(r'^Tata')

'''You can use the dollar symbol ($) at the start of a regular expression 
to indicate that a match must occur at the end of the searched text.'''
# str2 = re.compile(r'Sidam$')

'''With an asterisk (*) you can search for a text that has that letter 0 
to n times, it's not about the whole word you give as argument, it's only
about the word the asterisk is next to, i in this example, it will give all
a with or without i'''
# str2 = re.compile(r'ai*')

'''Same as asterisk, just the miminal number of occurence is 1.'''
# str2 = re.compile(r'vi+')

'''Same as the past two just the occurence doesn't have a range, it has a fixed number.'''
# str2 = re.compile(r'se{5}')


'''I guess the description given above is enough and by above I mean at the start.'''
# str2 = re.compile(r'\bTa')

'''I guess the description given above is enough.'''
# str2 = re.compile(r'\d5')


#This is the finditer line.
str3 = str2.finditer(str)
for match in str3:
    print(match)

'''
It's not like I'm gonna show you all, search and practice.
'''
