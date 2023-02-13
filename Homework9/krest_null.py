# 3.Создайте программу для игры в ""Крестики-нолики"".

import emoji

import random
steps_table = [1,2,3,
        4,5,6,
        7,8,9]

def Print_steps_table():
    print(steps_table[0], end = ' ') 
    print(steps_table[1], end = ' ') 
    print(steps_table[2]) 
    print(steps_table[3], end = ' ') 
    print(steps_table[4], end = ' ') 
    print(steps_table[5]) 
    print(steps_table[6], end = ' ') 
    print(steps_table[7], end = ' ') 
    print(steps_table[8])   

victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]] 

def step_maps(step,symbol):
    while step not in steps_table:
        print('Некорректный ввод, попробуйте еще')
        print(emoji.emojize(':downcast_face_with_sweat:'))
        step = int(input("Ваш ход: "))
    else:
        ind = steps_table.index(step)  
        steps_table[ind] = symbol

def get_result():
    win = ""
    for i in victories:
        if steps_table[i[0]] == 'X' and steps_table[i[1]] == 'X' and steps_table[i[2]] == 'X':
            win = "X"
        if steps_table[i[0]] == '0' and steps_table[i[1]] == '0' and steps_table[i[2]] == '0':
            win = "0"
    return win

game_over = False

print(emoji.emojize("Кто ходит первым :megaphone:"))
first_player = random.choice([True, False])
if first_player == 1:
    print(emoji.emojize('X, ваш ход :penguin:'))
    first_player == True
else: 
    print(emoji.emojize('0 ходит первым :paw_prints:'))
    first_player == False
  
while game_over == False :
 
    Print_steps_table()
 
    if first_player == True:
        symbol = "X"
        step = int(input("X, введите номер ячейки: "))

    else:
        symbol = "0"
        step = int(input("0, введите номер ячейки: "))
 
    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
 
    first_player = not(first_player) 
Print_steps_table()

print("Победил", win)     