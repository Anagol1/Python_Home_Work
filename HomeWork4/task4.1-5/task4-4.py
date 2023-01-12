# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random as rand

num_k = int(input('Введите степень k многочлена: '))
list_koeff = [rand.randint(0,100) for i in range(num_k+1)]
# print(list_koeff)

many_members = ''
for i in range(num_k, -1, -1):
    
    koeff = (list_koeff[i])
    if koeff !=0:
        many_members=str(koeff) + '*x' + '^' + str(num_k-i) + ' + ' + many_members
    else: continue

print(many_members.replace('*x^0 +', '').replace('^1 ', ' ').replace('1*x', 'x')+'= 0') 

