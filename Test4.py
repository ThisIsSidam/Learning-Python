#Python Test4

#Palindrome

'''
Something that when reversed returns itself is called a Palindrome.
Some of it's examples are- 434, mom, 100001
Here, you have to get a list of numbers as input from the user and
give back a list of all next palindromes of all elements of that list.
'''

size = int(input('What will be the number of input?\n'))
ls = []

# Adding inputs in list ls
for i in range(size):
    n = int(input('Give a number.\n'))
    ls.append(n)


def reverse_num(num):
    """Creates a reverse number of the attribute."""
    if len(str(num)) == 1:
        return num
    else:
        num += 1
        while not check_reverse(num):
            num += 1
        return num


def check_reverse(num):
    """Checks if the numbers and its reverse are equal or not."""
    return str(num) == str(num)[::-1]


print(list(map(reverse_num, ls)))

