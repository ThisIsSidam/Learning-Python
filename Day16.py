#Learning Python Day16

#Time module
import time

time1 = time.time()

for i in range(40):
    print('Hello, there!')

print(f'Time is', time.time() - time1)

'''
Here, we got to know the time that was taken to complete that for fn.
But what does the time.time actually does. Out computers know the time 
as a number which increases over time, obsiouly cause time is always 
passing, so, that number actually started increasing from a date and 
time called Epoch, usually its a time from where the calender era has 
thought to have started. In computing Epoch is the time from which our 
computer measure time, so the number given to us with time.time is the
numerical version of time passed from the time Epoch. So, our computer
subtracted the time when line6 was in action from the time line11 was in
action giving us the time taken by the comp. to complete that fn.
'''

print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

'''
Now, time.time gives of the current time, but not in a manner that we can 
understand, localtime converts it into a tuple that we can understand but
asctime maked it even simpler. Hence, we get the current time.
'''

for i in range(10):
    print('Isn\'t it nice')
    time.sleep(1)

'''Now, you can just see what is happening, the sleep fn makes the code sleep for
the given amount of time, in this case 1sec.'''
