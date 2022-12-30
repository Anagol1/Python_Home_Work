# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на 
# указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random 
file = open("file.txt", "r")
for line in file:
    find_max = int(max(file.read())) # находим максимальнй индекс в файле
num_N = int (input ("Input number: "))
if num_N <= find_max: # чтобы количество элементов не было меньше максимального индекса 
    print("Input number >", find_max)
else:
    my_list = []
    for _ in range(num_N):
        my_list.append(random.randrange(-num_N,num_N+1))
    print(my_list)
    mult = 1
    file = open("file.txt", "r")
    for line in file:
        mult *= my_list[int(line)]
    file.close()
    print(mult)