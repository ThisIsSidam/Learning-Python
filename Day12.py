#Learning Python Day12

#Local and Global Variables
N = 4 #This is a Global Var
def printify(n):
    N = 5 #This is a Local Var
    print(N, n)
printify('df')
'''Variables that are present outside of any function like that 'N' var above.
are known as Global var. And the 'N' var inside the printify fn is a Local var.
Think locals like house money and global like government money, and that fn or 
anything else like it are the house. If you have money then the house will use 
house money meaning local var and if you don't it will take govrnmnt money as 
charity or something and use it, meaning use the global var, and if there is no 
money meaning no var then it will give error. So, as seen above, even if globally
there is a var, the used var is local coz if you already have money in house, then 
why go to govrnmnt for help.
'''

#Global Keyword
j = 4
def print34():
    global j
    j = 34
    print(j)
print34()
'''Now if you want to change the value of a global var in a local place as in a fn,
you can't do it, think it as you can't change things about the govrnmnt's money.
But with 'global' keyword you get a permission to do that. Also, if there is no existing 
global var of that name, it will create one.'''

b = 55
def print344():
    b = 34
    def print44():
        global b
        b = 4
        print(b)
print344()
'''Here, the global keyword is used at sublocal level, and it changed the value of the b at
 global level not the local level, hence the value at local level was used. Also, after the fn 
 is being used the value of the var b has been changed permanently. But if it wasn't used it won't
 have been changed since the block of code under def is used only when the function created is 
 being used/called.'''
