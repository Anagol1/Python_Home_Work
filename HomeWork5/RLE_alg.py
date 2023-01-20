# 4.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Сжатие данных

# with open('D:/Обучение/Python/HomeWork/HomeWork5/in_file.txt','r') as data:
#     s = data.readline()

# print(s)
# # s = 'vvvvffffgggmlllpou'
# rle_alg_s = "" 
# i = 0
# while i < len(s):
    
#     count = 1
#     while i + 1 < len(s) and s[i] == s[i + 1]:
#         count += 1
#         i += 1
#     rle_alg_s += str(count) + s[i]
#     i += 1

# with open('D:/Обучение/Python/HomeWork/HomeWork5/out_file.txt','w') as data:
#     data.writelines(rle_alg_s)
# print(rle_alg_s)   

# Восстановление данных

with open('D:/Обучение/Python/HomeWork/HomeWork5/out_file.txt','r') as data:
    rle_s = data.readline()

# rle_s = '4v4f3g1m3l1p1o1u'

s = ''
old_list = []
for i in range(0,len(rle_s),2):
    s = s + (int(rle_s[i]) * str(rle_s[i+1]))
            
print(s)