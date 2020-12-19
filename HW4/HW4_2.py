from random import randint
my_list = [randint(0, 100) for i in range(10)]
new_list = []
for idx in range(1,len(my_list)):
    if my_list[idx] > my_list[idx-1]:
        new_list.append(my_list[idx])
print(my_list)
print(new_list)
