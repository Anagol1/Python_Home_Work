# 1. Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
num_Pi = math.pi
print(num_Pi)

def Digits_after_point(digits_after_point):
    count = 0
    num_Pi = math.pi
    while digits_after_point % 1 != 0:
        digits_after_point *= 10
        count += 1
 
    print(count)
    acc_of_num = int((num_Pi)*(10**count))/(10**count)
    
    return acc_of_num

digits_after_point = float(input('Введите число в формате d = 0.000..1, с количеством знаков после запятой, которое нужно показать в числе пи: '))
print(Digits_after_point(digits_after_point)) 

