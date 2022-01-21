#Leaning Python Day25

#Inheritence
'''
Just like kids inherit their parents' qualities and stuff. Classes also inherit other
classes.
'''

#Single Inheritence
class Science:
    def __init__(self, chapname, chapnum):
        self.chapname = chapname
        self.chapnum = chapnum

class Physics(Science):
    pass

light = Science('Light', 7)
lightnray = Physics('Light and Rays', 4)
print(light.chapnum, lightnray.chapnum)

'''
Just like here the class Physics, inherited the constructor from the its parent class 
Science, it can copy all other stuff like var, classmethods etc.
'''

#Multiple Inheritence

class animalvr:
    var = 40
    def __init__(self, animalsathome, totalbreeds):
        self.animalsathome = animalsathome
        self.totalbreeds = totalbreeds

class plantslvr:
    var = 86
    def __init__(self, plantsathome, kindsofplants, biggestreesize):
        self.plantsathome = plantsathome
        self.kindsofplants = kindsofplants
        self.biggestreesize = biggestreesize

class naturelvr(animalvr, plantslvr):
    var = 126

jimmy = animalvr(3, 2)
sam = plantslvr(35, 25, '40m')
sid = naturelvr(6,4)
print(sid.var)

'''
We just made a class that has inherited two other classes. Now, things to know are that
if it has to find a variable value, like var, it will first check itself, then the
class that this class inherited first, which is animalvr and after that the other, this
is the order of finding something. Wanna test it out, try removing the var from the naturelvr,
and see what happens.
     If we don't give it any constructer, it will try to find the constructer in animalvr
first, coz that is the first inherited class and after that the plantslvr. Try uncommenting the
line below, it will give an error because we didn't give naturelvr a constructer and it inherited
the constructor from its first parent which is animalvr and it had only 2 arguments (not including self),
and since the constructor of plantslvr has 3 arguments and is not inherited, it will give an error.  
'''

# mandeline = naturelvr(34, 4, '24m')

'''
Not next, but later on, we'll learn about taking a constructor from an inherited class and adding 
arguments to it by 'super' and 'overriding'.
'''

#MultiLevel Inheritence
class Science: #Parent Class
    var = 4

class Physics(Science): #Child Class
    var = 5

class Electrodynamics(Physics): #Grandchild Class
    var = 7

print(Electrodynamics.var)
'''
This is called a multilevel inheritence, a class is inherited by a class and then, the 
inherited class is also inherited by a third class and it may go on. In these cases, 
if you would try to find the value of that var from the grandchild class, it will try
to first find it in itseld, if not found, it will try to find it in the child class 
which is the grandchild class's parent classand then go to the real parent class which
is the grandchild class's grandparent class. Hope I'm not making it a mess with and 
those relations. And the value in the result will be the one it finds first.
'''

