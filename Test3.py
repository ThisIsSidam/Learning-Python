#Python Test3

#Lots of Calories

'''
You're in a restaurant, the food menu is given below, make a list out
of it, in the menu, price and calories are given. Get budget and
calories(user wants to consume) from the user as input and find all
the suitable items.

Menu-
Butter Chicken - 500rs - 600Cal
Haka Noodles - 150rs - 300Cal
Chicken Tikka Masala - 485rs - 500Cal
Dal Makhani + Bhuna Jeera Rice - 450rs - 500Cal
'''

hn = ['Haka Noodles', 150, 300]
bck = ['Butter Chicken', 500, 600]
ctm = ['Chicken Tikka Masala', 485, 500]
dm = ['Dal Makhani + Bhuna Jeera Rice', 450, 500]

bud = int(input('How much money do you want to use?\n'))
cal = int(input('How many calories do you want to consume at max.\n'))

class restr():
    def __init__(self, lst):
        self.name = lst[0]
        self.price = lst[1]
        self.cal = lst[2]

    def check(self):
        if self.price <= bud and self.cal <= cal:
            print(self.name)
        else:
            pass

bck = restr(bck)
hn = restr(hn)
ctm = restr(ctm)
dm = restr(dm)

inst = [bck, hn, ctm, dm]
for i in inst:
    i.check()



