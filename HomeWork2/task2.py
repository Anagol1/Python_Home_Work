
# 2. Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

my_number = int(input('Input number: '))
mult = 1
for i in range(2, my_number+1):
    print(mult, end = ',')
    mult *= i
print(mult)