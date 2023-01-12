#5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def Parsing(multinomial):
    dict_multinomial = {}
    multinomial = multinomial.replace(' + ', ' +').replace('*x', 'x').replace('= 0','')
    multinomial = multinomial.split()
    for i in range(len(multinomial)):
        multinomial[i] = multinomial[i].replace('+','').split('x^')
        dict_multinomial[int(multinomial[i][1])] = int(multinomial[i][0])
    return dict_multinomial

def Sum_multinom(dict1, dict2):
    dict_res = {}
    len_dict_sum = (max(max(dict1),max(dict2)))
    for i in range(len_dict_sum, -1, -1):
        first_membr = dict1.get(i)
        second_membr = dict2.get(i)
        if first_membr != None or second_membr != None:
            dict_res[i] = (first_membr if first_membr != None else 0) + (second_membr if second_membr != None else 0)
    return dict_res

def Res_multinomial(dict):
    result = ''
    for i in dict.items():
        if result == '':
            result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
        result = result.replace('x^0','').replace('x^1','x')
    return result + ' = 0'    

with open('D:/Обучение/Python/HomeWork/HomeWork4/task4.1-5/file1.txt','r') as data:
    mult1 = data.readline()
with open('D:/Обучение/Python/HomeWork/HomeWork4/task4.1-5/file2.txt','r') as data:
    mult2 = data.readline()
print(mult1)
print(mult2)

dict_multinomial1 = Parsing(mult1)
dict_multinomial2 = Parsing(mult2)

print(dict_multinomial1)
print(dict_multinomial2)

dict_sum_res = Sum_multinom(dict_multinomial1,dict_multinomial2)

print(dict_sum_res)
mult_sum_res = Res_multinomial(dict_sum_res)
print(mult_sum_res)

with open('D:/Обучение/Python/HomeWork/HomeWork4/task4.1-5/file3.txt','w') as data:
    data.writelines(mult_sum_res)