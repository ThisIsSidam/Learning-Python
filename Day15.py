#Learning Python Day15

#String Formatting
'''
Thick, you want to add multiple variables into a print statement, what
will you do, use '+' or commas. Best way is to use Fstrings. But before
that we have to know about some other methods.
'''

a = "study"
b = 'Sidam'

hl = ('%s wants to %s')%(b, a) #Method1
print(hl)

ht = ('{} is going to {}') #Method2
print(ht.format(b, a))

'''
We saw two methods, one using %s, which comes in as a placeholder which 
is replaced by the varibles names written in after the % outside the print
brackets, also that the placeholders will be replaced in the same order your
var names are written in.
Then is the format fn, you leave curly braces in print statement which are
by the vars given in the format fn and in the same order as you give the var
names in.
Now comes the Fstrings.
'''

print(f'{b} will {a}')
'''
Here we just do stuff as a normal print statement, just add a 'f' before commas
and add vars in the statement which is to be printed just with curly braces.
This is faster than using %s or format fn or using + again and again. After all
fstrings means, Fast Strings.
'''

#*args and *kwargs

def first(a, b, c, d):
    print(a, b, c, d)
first('Ram', 'Shyam', 'Mohan', 'Sohan')
'''
As in this situation, if I want to add another name for the fn 'first', I'll have
to edit the fn. But,
'''

def second(*args):
    print(args)
lst = ['Ram', 'Shyam', 'Mohan', 'Sohan']
second(*lst)

'''
Now, we can add as many names as we want and since the argument is an arg, it will 
handle it. The same thing is kwarg, just with double asterisks, and for dictionaries.
'''

def third(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} is {value}')
dic = {'First':'Ramesh', 'Second':'Suresh', 'Third':'Jagesh'}
third(**dic)

'''
Same goes for this one too, we can add as many names as we want and since the argument 
is an kwarg, it will handle it. And just so you know, it is not compulsory for args 
to be named args, whatever you name it just put an asterisk before it and the same goes
for kwargs just with an extra asterisk. And it is compulsary for normal argument to be
befor args and for args to be before kwargs, you can't put it like, (**jack, *ash, n)
it is the complete opposite. Also, args and kwargs are optional so it depends on you to
give that argument a value or not.
'''