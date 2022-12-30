# 3. Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму.

Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

N = int(input('Input number: '))
my_list = []
sum_nums = 0
for i in range(1, N + 1):
    num_of_list = int((i + (1 / i))** i)
    my_list.append(num_of_list)
    sum_nums += num_of_list
print(my_list)
print(sum_nums)
