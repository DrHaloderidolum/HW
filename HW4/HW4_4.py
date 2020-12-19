from random import randint
my_list = [randint(0, 15) for i in range(20)]
print(my_list)

print([el for el in my_list if my_list.count(el) == 1])