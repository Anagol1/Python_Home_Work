
# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Человек против человека

# from random import randint as ri

# def Start_game():
#     print(f"На столе лежит {total_num_of_sweets} конфета. Первый ход определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход.")
#     Who_is_First()
    
# def Who_is_First():
#     first_player = ri(1,2)
#     if first_player == 1:
#         player_1_turn()
#     else: player_2_turn()

# def player_1_turn():
#     global total_num_of_sweets
#     global taking_sweets
#     global player_1_sweets
    
#     print(f'На столе {total_num_of_sweets} конфет: ')
#     taking_sweets = int(input('Игрок_1, возьмите не более 28 конфет: '))
#     while taking_sweets > 28 or taking_sweets > total_num_of_sweets:
#         taking_sweets = int(input('Неверное колическтво конфет. Возьмите меньше конфет: '))
#     total_num_of_sweets -= taking_sweets
#     player_1_sweets += taking_sweets
#     if total_num_of_sweets > 0:
#         player_2_turn()
#     else: 
#         return print('Игрок_1 Вы выиграли!')
    
# def player_2_turn():
#     global total_num_of_sweets
#     global taking_sweets
#     global player_2_sweets

#     print(f'На столе {total_num_of_sweets} конфет: ')
#     taking_sweets = int(input('Игрок_2, возьмите не более 28 конфет: '))
#     while taking_sweets > 28 or taking_sweets > total_num_of_sweets:
#         taking_sweets = int(input('Неверное количество конфет. Возьмите меньше конфет: '))
#     total_num_of_sweets -= taking_sweets
#     player_2_sweets += taking_sweets
#     if total_num_of_sweets > 0:
#         player_1_turn()
#     else: 
#         return print('Игрок_2 Вы выиграли!')
    
#     # taking_sweets = total_num_of_sweets % 29 != 0 else ri(1,28)
# total_num_of_sweets = 150
# taking_sweets = 0
# player_1_sweets = 0
# player_2_sweets = 0
# Start_game()

# Вариант бот против человека

from random import randint as ri

def Start_game():
    print(f"На столе лежит {total_num_of_sweets} конфета. Первый ход определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. \nВсе конфеты оппонента достаются сделавшему последний ход.")
    Who_is_First()
    
def Who_is_First():
    first_player = ri(1,2)
    if first_player == 1:
        print('Игрок_1, ваш ход')
        player_1_turn()
    else: 
        print('Бот ходит первым')
        bot_turn()

def player_1_turn():
    global total_num_of_sweets
    global taking_sweets
    global player_1_sweets
    
    print(f'На столе {total_num_of_sweets} конфет: ')
    taking_sweets = int(input('Игрок_1, возьмите не более 28 конфет: '))
    while taking_sweets > 28 or taking_sweets > total_num_of_sweets:
        taking_sweets = int(input('Неверное колическтво конфет. Возьмите меньше конфет: '))
    total_num_of_sweets -= taking_sweets
    player_1_sweets += taking_sweets
    if total_num_of_sweets > 0:
        bot_turn()
    else: 
        return print('Игрок_1 Вы выиграли!')
    
def bot_turn():
    global total_num_of_sweets
    global taking_sweets
    global bot_sweets

    # taking_sweets = ri(1,28)  # если бот не наделен интеллектом
    
    if total_num_of_sweets % 29 !=0: 
        taking_sweets = total_num_of_sweets % 29
    else: taking_sweets = ri(1,28)
    total_num_of_sweets -= taking_sweets
    bot_sweets += taking_sweets
    print(f'Бот взял {taking_sweets} конфет')
    if total_num_of_sweets > 0:
        player_1_turn()
    else: 
        return print('Бот выиграл!')
    
    # taking_sweets = total_num_of_sweets % 29 != 0 else ri(1,28)
total_num_of_sweets = 2021
taking_sweets = 0
player_1_sweets = 0
bot_sweets = 0
Start_game()




# 3.Создайте программу для игры в ""Крестики-нолики"".

# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.