
# Урок 2. Знакомство с Python. Продолжение
# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def Sum_Of_Digit(any_number):

    sum_of_digits = 0
    for symbol in any_number:
        if symbol.isdigit():
            sum_of_digits += int(symbol)
    return sum_of_digits

my_number = input('Input any number: ')
print(Sum_Of_Digit(my_number))

