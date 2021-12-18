#Learning Python Day 5

#Dictionary- nothing but key-value pairs.
di = {} #Dictionaries use curved brackets.
print(type(di)) #Here the type is dict which means dictionary
dc = {"Mom":"Momos", "Me":"Chhole Bhature"}
#First str is key and second is the value. We use keys to search for values.
print(dc)
print(dc["Mom"]) #This way we can get the value of a certain key.
dd = {"Me":"Chhole Bhature", "Bro":{"BF":"Samosa", "LN":"Eggroll", "DN":"Chat"}}
#This way we can also add a dict to a value of a key.
print(dd["Bro"]["LN"])
#This way we can extract value from inside of a dict's dict.
#It is preffered to use ints and str as keys. you can use both in same dict as well.
#You can have dicts, tuples or even lists as values in dicts.

#Adding and removing
dd["Mom"] = "Tedhe Medhe" # This is how we add keys along with their values.
dd[45] = "Roti"
print(dd)
del dd[45] #This is how we remove or delete keys.
print(dd)

#Some fns of Dicts
print(dd.copy()) #It just creates a copy of that dict
#Used actually to copy the whole dict to a different dict
df = dd.copy()
print(df)
'''If i will use df=dd, it won't create a new dict, it will just take dd as 
its value and while editing one of them another one will be edited automatically.'''

print(dd.get("Mom")) #Accessing value of a key without a square bracket.
dd.update({"34":"Dal Chawal"}) #Another way of adding elements
print(dd)

print(dd.keys()) #shows all keys in the dict.
print(dd.items()) #shows all items in the dict, items include both keys and their values

#Know about more fns on the internet.

#Keywords.
'''There are lots of keywords in python, 
like, and, or, is, they mean the same as they 
mean in english. THey are actually called operators
that you will know more about later on.'''