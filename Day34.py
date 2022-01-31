#Learning Python Day34

#requests Module
import requests

jack = requests.get('https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-82/')
print(jack.text)
print(jack.status_code)

'''
Requests module is used to get data and lots of other stuff from websites.
Get is used to get data from the site we requested.
We can see that data with .text and status_code gives us the status code of that request.
I don't know much yet but status code 200 means O.k. or like the request was completed 
without any problems.

This is a very imported module for people who wanna go into web dev. industory. 
You can get more info on the web. 
'''

#json Module
'''
It's full form is Javascript Object Notation.
This is used to connect with the internet, if you want your code to connect with the internet, 
you must learn and use json module. 
'''

import json

a = {'Name':'CrackJack', 'Crackiness':'Ultimate lvl', 'Taste':'Salty'}
b = json.dumps(a)
print(b)

'''
This is called parsing.
load(): This method is used to load data from a JSON file into a python dictionary.
Loads( ): This method is used to load data from a JSON variable into a python dictionary.
dump(): This method is used to load data from the python dictionary to the JSON file.
dumps(): This method is used to load data from the python dictionary to the JSON variable.
Since, python syntax is different from javascript syntax, parsing is used to change the little 
things that may cause an error in a different language on the basis of that different language. 

Currently, I don't get it that much but I will in the near future.
And I always say, look up more functions on the internet, you don't have to memorize them, just have 
to be aware of their existence so when you really need them you can search them on the web.
'''


