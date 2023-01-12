# 2. Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

num_n = int(input('Input natural number: '))
prim_nums_list = []
for i in range(1, num_n+1):
    if(num_n % i==0):
        prim_nums_list.append(i)
        num_n /= i

print(prim_nums_list) 