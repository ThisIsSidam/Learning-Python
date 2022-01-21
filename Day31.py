#Learning Python Day31

#Function Caching
'''
Currently, you run functions, and they get finished in a fraction of a second,
but this won't last long, in near future, the functions will start taking time,
the slower the cpu, more the time it takes, so, are you gonna run same function
again and agian if you have to, with caching, you can save their results and when
the function is run again, caching will bring back the result from the previous time
it ran and copypaste it.
'''

import time #Just for explanation
from functools import lru_cache

@lru_cache(maxsize= 2)
def some_work(n):
    time.sleep(n)
    return

print('Work Started.')
some_work(4)
print('Done, starting again.')
some_work(4)
print('Done, starting agian.')

'''
That 3sec time sleep is just there as a substitute for a thing that 
the system might take time to complete.
You'll see that it takes time in the first time the some work fn is
executed but after line 23, line 25 is executed without timelapse. 
That is because the result of line 22 was saved as cache by the 
lru cache and the second time the fn is executed, it was not needed
to run the whole fn again. 
Now, What's that maxsize, it is the limit of how many times it can save.
Currently, it can save 2 times, meaning, if the somework is ran with 4
different argument, it will save them. Not the first 2, the last 2, 
you can kinda say the newest 2.
'''
@lru_cache(maxsize= 2)
def taketime(n):
    time.sleep(n)
    return


print("A")
taketime(2)
print('B')
taketime(4)
print('C')
taketime(6)
print('D')
taketime(4) #This won't take time.
print('E')
taketime(2) #This will take time.
print('F')

'''
It first saved the fn with 2sec then the one with 4sec, then the one
with 6sec but removed the one with 2sec because the limit is 2. Then,
used the cached 4sec one but after that 2sec one was not in the cache
so, the fn ran again, and got saved again. 

It is also possible not to have any limit but its better to have a 
limit because it needs space for saving the cache which is the deviceand
the device may get loaded up with cache.
'''

