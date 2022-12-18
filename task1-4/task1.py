# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Input day of week from 1 to 7: '))
if day > 0 and day < 6:
    print ('it is not a holiday') 
if day > 5 and day < 8:
    print ('it is a holiday')  
else:
    print ('its wrong number of day')