# 3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.


import random as rand

list_len = int(input('Введите длину списка: '))
my_list = [rand.randint(10,20) for _ in range(list_len)]
print(my_list)

# Было
# i=0
# my_new_list = []
# while i < len(my_list):
#     del_num = my_list[i]
#     my_list.remove(my_list[i])
#     if del_num not in my_list:
#         my_new_list.append(del_num)
#         my_list.insert(i, del_num)
#     i+=1

# print(my_new_list)

# Стало

my_new_list = list(filter(lambda x: my_list.count(x) == 1, my_list))
print(my_new_list)

