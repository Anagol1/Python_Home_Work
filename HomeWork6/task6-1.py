# 3. Задайте список из n чисел последовательности (1+(1/n))^n и выведите
#  на экран их сумму.


N = int(input('Input number: '))
# # Было:
# my_list = []
# sum_nums = 0
# for i in range(1, N + 1):
#     num_of_list = int((i + (1 / i))** i)
#     my_list.append(num_of_list)
#     sum_nums += num_of_list
# print(my_list)
# print(sum_nums)

# # Стало:

list = [int((i + (1 / i))** i) for i in range(1, N + 1)]
print(list)
print(sum(list))

