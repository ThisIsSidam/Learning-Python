#Faulty Calculater

''' Design a faulty calculater, that will give correct results for all problems,
But for problems 45 * 3, 65 + 4 and 77/8 they will give 444, 554 and 543 respectively as results.
Just so you know, only fns learnt until Day6 are allowed.'''

print('Which operator do you want to use? Add/Subtract/Multiply/Divide')
op = input()
print('What are your two numbers? Press Enter after typing first number.')
fn, sn= int(input()), int(input())
if op == "Add":
    if fn == 65:
        if sn == 4:
            print(554)
        else:
            print(65 + sn)
    else:
        print(fn + sn)
elif op == "Subtract":
    print(fn - sn)
elif op == "Multiply":
    if fn == 45:
        if sn == 3:
            print(444)
        else:
            print(45 * sn)
    else:
        print(fn * sn)
elif op == 'Divide':
    if fn == 77:
        if sn == 8:
            print(543)
        else:
            print(77 / sn)
    else:
        print(fn / sn)
else:
    print('Type the operator name correctly!')
