
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части 
# элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
list_len = int(input('Введите длину списка: '))
float_list=[round(random.uniform(0.99, 100), 2) for float_list in range(list_len)]
print(float_list)

new_float_list = []
for i in range(list_len):
    new_num = float_list[i] % 1 
    new_float_list.append(round(new_num, 2))
print(new_float_list)
print(f"Difference between max = {max(new_float_list)} and min = {min(new_float_list)} is {max(new_float_list) - min(new_float_list)}")

