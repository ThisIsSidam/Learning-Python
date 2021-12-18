#Health Management Program

'''In this exercise I am going to create a Health management program,
where I have three clients, namely Carry, Harry and Mary, you have to make 6
files three of exercise for the three and three diet plans of the three.
Now with the program you'll be able to update or get the data from the six files.
Also, you have to show time every time data is shown, which will be done by the
given code-
def getdate():
    import getdate()
    return getdate.getdate.now()

Also, fns only learnt until Day11 are usable.
'''
'''When you will run this program for the first time, you won't have any
existing data, hence first choose edit and enter data and do the 
retrieving after that.'''

print('What do you wanna do, edit data or retrieve data?')
da = int(input('Press 1 for edit and 2 for retrieving data.\n'))
cl = int(input('Select Client-\n 1 for Carry\n 2 for Harry\n 3 for Mary\n'))
dt = int(input('Which data-\n 1 for Exercise data\n 2 for Diet data\n'))

def datetime():
    import datetime
    return datetime.datetime.now()

if da == 1:
    if cl == 1:
        if dt == 1:
            with open('CarEx.txt', 'a') as f:
                CarEx = input('Enter Data\n')
                f.write(CarEx)
                print(datetime(), 'Done, Data edited!')
        if dt == 2:
            with open('CarDi.txt', 'a') as f:
                CarDi = input('Enter Data\n')
                f.write(CarDi)
                print(datetime(), 'Done, Data edited!')
    if cl == 2:
        if dt == 1:
            with open('HarEx.txt', 'a') as f:
                HarEx = input('Enter Data\n')
                f.write(HarEx)
                print(datetime(), 'Done, Data edited!')
        if dt == 2:
            with open('HarDi.txt', 'a') as f:
                HarDi = input('Enter Data\n')
                f.write(HarDi)
                print(datetime(), 'Done, Data edited!')
    if cl == 3:
        if dt == 1:
            with open('MarEx.txt', 'a') as f:
                MarEx = input('Enter Data\n')
                f.write(MarEx)
                print(datetime(), 'Done, Data edited!')
        if dt == 2:
            with open('MarDi.txt', 'a') as f:
                MarDi = input('Enter Data\n')
                f.write(MarDi)
                print(datetime(), 'Done, Data edited!')
if da == 2:
    if cl == 1:
        if dt == 1:
            with open('CarEx.txt') as f:
                print(datetime())
                print(f.readlines())
        if dt == 2:
            with open('CarDi.txt') as f:
                print(datetime())
                print(f.readlines())
    if cl == 2:
        if dt == 1:
            with open('HarEx.txt') as f:
                print(datetime())
                print(f.readlines())
        if dt == 2:
            with open('HarDi.txt') as f:
                print(datetime())
                print(f.readlines())
    if cl == 3:
        if dt == 1:
            with open('MarEx.txt') as f:
                print(datetime())
                print(f.readlines())
        if dt == 2:
            with open('MarDi.txt') as f:
                print(datetime())
                print(f.readlines())
