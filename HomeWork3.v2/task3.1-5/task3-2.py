# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = list(map(int,(input('Input numbers with probel: ').split())))
new_list = []

for i in range(int(len(my_list)) // 2 + int(len(my_list)) % 2):
    new_list.append(int(my_list[i] * my_list[-i-1]))

print(new_list) 