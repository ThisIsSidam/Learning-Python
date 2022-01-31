# Python Test6

# Text Searcher

'''
Get a piece of text, and do something so that we can search anything in that text,
tell how many results were found and how much time it took.
'''
import re
import time


text = input('Copy Paste the text you want to Search in.\n')

search = input('What do you want to search?\n')

atime = time.time()
iter = re.finditer(search, text, re.IGNORECASE)

n = 0

for i in iter:
    n += 1
    print(i)

else:
    if n == 0:
        print(f'\'{search}\' word not found!')
    else:
        print(f'{n} result(s) found in {format(time.time() - atime, ".4f")} seconds')



