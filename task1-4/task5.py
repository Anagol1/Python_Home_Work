# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве (AB = √(xb - xa)2 + (yb - ya)2).

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x_a = float(input('Input Xa: '))
y_a = float(input('Input Ya: '))
x_b = float(input('Input Xb: '))
y_b = float(input('Input Yb: '))
ab = (((x_b - x_a)**2) + ((y_b - y_a)**2))**0.5
print(ab)
