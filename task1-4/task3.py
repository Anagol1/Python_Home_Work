# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Input X '))
y = int(input('Input Y '))

if x > 0 and y > 0:
    print ('Its 1st quarter')
elif x < 0 and y > 0:
    print ('Its 2nd quarter')
elif x < 0 and y < 0:
    print ('Its 3d quarter')
elif x < 0 and y < 0: 
    print ('Its 4th quarter')
else: print ('Point is not in any quarter')
    