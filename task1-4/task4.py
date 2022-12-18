# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

quarter_num = int(input('Input number of quarter from 1 to 4: '))

if quarter_num == 1:
        print ('Coordinates in 1st quarter: x > 0 and y > 0')
elif quarter_num == 2:
        print ('Coordinates in 2nd quarter: x < 0 and y < 0')
elif quarter_num == 3:
        print ('Coordinates in 3d quarter: x < 0 and y < 0')
elif quarter_num == 4: 
        print ('Coordinates in 4th quarter: x < 0 and y < 0')
else: print ('Quarter is not exist')
