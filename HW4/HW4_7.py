from math import factorial

x = int(input("Enter integer: "))


def fact(x):
    for el in range(1, x+1):
        y = factorial(el)
        yield y


print(fact)
for i in fact(x):
    print(i)
