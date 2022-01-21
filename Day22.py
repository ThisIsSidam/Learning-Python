#Learing Python Day22

#Class variable
'''
Last time we saw instance variable. Now there are class variable too, that have same value
for each instance.
'''

class worker:
    working_hours = 8

jack = worker()
mack = worker()

jack.age = 34
mack.age = 35
print(jack.working_hours, mack.working_hours)

jack.working_hours = 10
print(jack.working_hours, mack.working_hours)

worker.working_hours = 9
print(jack.working_hours, mack.working_hours)
print(jack.__dict__, mack.__dict__)
'''
Here, we first saw that the value for class variable was same for both instances. But when we changed
it on line19, it just changed for jack not for mack, hence we see that class variable can only be changed
by class not by instances, if tried using an instance, it will create a new instance variable of the same 
name as class variable that will work separately. 
'''

#Methods and Self
'''
Functions created under class statement/syntax are methods, normally they have self as their 
argument which is used for instances, and after that we have class methods that we'll learn about 
later.
'''
class model:
    def hot(self):
        return f'{self.name} is very hot!'
    def nhot(self):
        return f'{self.name} is not hot at all!'

jackey = model()
mia = model()

jackey.name = 'Jackey Saloni'
mia.name = 'Mia Lopez'

mia.hot()
jackey.nhot()

'''
Here, we created and used a fn, but we didn't use that 'self' argument while using the fn.
The thing is that, that self argument automatically picks up it's instance since we used it with an 
instance var. It picked mia and jackey as its value and according to the fn picked out their names
and showed it to us.
'''


