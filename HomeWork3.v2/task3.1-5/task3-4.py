
# 4. Напишите программу, которая будет преобразовывать десятичное число в 
# двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Input any number: '))
bin_num = ''
while num != 0:
    bin_num = str(num % 2) + bin_num
    num //= 2
print(bin_num)