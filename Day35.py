#Learning Python Day35

#pickle Module

'''
What is a pickel, it is a thing we eat, but is preserved for long usage, same way,
pickle module converts normal data into pkl format for later use, this is called
pickling.
'''

import pickle

#Saving data
# Anime = ['MHA', 'AOT', 'Naruto', 'Boruto', 'Jujutsu Kaisen', 'Naruto: Shippuden', 'Dragon Ball', 'One Punch Man']
# file = 'FevAnime.pkl'
# fileobj = open(file, 'wb')
# pickle.dump(Anime, fileobj)
# fileobj.close()

#Retrieving data
# file = 'FevAnime.pkl'
# fileobj = open(file, 'rb')
# Alist = pickle.load(fileobj)
# print(Alist)
# print(type(Alist))

'''
Do things one by one, first comment out the retrieving code and save the data and uncomment
retrieving data and comment out saving data so that it doesn't cause any error. 

Also, pickle modules is hated because when you make a pickle file with a python version, let it 
be 3.2 and try to retrieve that data with another python version, let it be 3.7, it causes errors.
'''