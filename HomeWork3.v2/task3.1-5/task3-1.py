
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = list(map(int,(input('Input numbers with probel: ').split())))
sum_odd_nums = 0
for i in range(1,(len(my_list)), 2):
    sum_odd_nums += my_list[i]
print(sum_odd_nums)
