# Learning Python Day13

#Recursions
'''There are two types of recursions, iterative and recursive.
Recursions occur when a function calls itself. So,
The example will be a code to calculate factorials.
 n! = n * (n-1) * (n-2) * ... * 1
 n! = n * (n-1)!
 5! = 5 * 4 * 3 * 2 *1
 5! = 5 * 4!
 All of that was incase you don't remember factorials.'''

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))

'''In the case of recursive method, what's happening back stage is 
that, let's say the value of n is 4, then,
4 * factorial_recursive(3)
4 * 3 * factorial_recursive(2)
4 * 3 * 2 * factorial_recursive(1)
4 * 3 * 2 * 1
24

so, the fn is being used in itself again and again and again,
until it no longer needs to use itself.'''

#Mini-Excersize - Create a fn related to fabonacci sequence.
'''What really have to do is create a fn that will take input
and give off the fabonacci no. at that input's place.
What's a fabonacci sequence?
0 1 1 2 3 5 8 13
Just the two previous numbers get added to create the next one.'''

def fabo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabo(n-1) + fabo(n-2)

print(fabo(15))