from itertools import count
from itertools import cycle

n = int(input("Enter integer in range from 1 to 99: "))
for el in count(n):
    if el > 100:
        break
    else:
        print(el)

x = list(input("Enter some letters, or words, or numbers separated by spaces: "))
y = 0
for el in cycle(x):
    if y > 10:
        break
    else:
        print(el)
    y += 1
