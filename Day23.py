#Learning Python Day23

#Constructer- __init__
'''
Constructer, which is '__init__', is used so that we don't have to add instance variables one by one.
'''

class bulbs:
    def __init__(self, aname, abrightness, aquality):
        self.name = aname
        self.brightness = abrightness
        self.quality = aquality

syska = bulbs('Syska', 95, 'high')
philips = bulbs('Philips', 90, 'high')
bajaj = bulbs('Bajaj', 85, 'high')
local = bulbs('Local', 60, 'low')
print(syska.quality)

'''
You can understand everything just by looking above, only confusing thing can
be, name and aname. name is the instance variable, and aname is variable used 
by fn to explain itself.
'''

#Classmethods
'''
Just like normal methods have selfs in it, there are cls in classmethods which are for classes. Think 
of a time when you want to change a class var not normally, but by a method. Also, for creating class 
methods, we have to use the classmethod decorator above the method.
'''

class brothers:
    total_bro = 17

    def __init__(self, age, e_l):
        self.age= age
        self.bs= e_l

    @classmethod
    def total_changer(cls, bbro):
        brothers.total_bro= bbro

kanhai = brothers(18, 'elder')
priyanshu = brothers(19, 'elder')

brothers.total_changer(18)
print(brothers.total_bro)
kanhai.total_changer(29)
print(brothers.total_bro)
'''
Here, we used a classmethod, and we tried it with both, using the class and an instance, if we would
have tried to change a class var with an instance we would have ended up not changing the class var but
creating a separate instance var, but here, since we are using a classmethod, with both the class or an 
instance, we changed the class var successfully.
'''

#Classmethod as a constructer
class Date:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    @classmethod
    def slashes(cls, string):
        return cls(*string.split('/'))
        #Longer way
        #def slashes(cls, string):
        #sthing = string.split('/')
        #return cls(sthing[0], sthing[1], sthing[2])

kanhai = Date.slashes('20/08/2003')
priyanshu = Date.slashes('18/08/2002')
print(kanhai.date)

