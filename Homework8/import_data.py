all_classes = {}
all_students = {}
id_student = 1

def create_student():
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    otch = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = input("Введите номер класса ученика: ")
    global all_classes
    if class_name not in all_classes:
        create_cl(class_name) # вызов функции create_class, если нет такого класса
    all_classes[class_name].append(id_student) # добавляем id студента в класс
    st_data = [surname, name, otch, birth, tel, adress, class_name] # из 12 строки
    global all_students
    all_students[id_student] = st_data
    global id_student
    id_student += 1

def create_cl(name_class=False): # если класс есть, функция не вызывается 
    if not name_class: # если класс есть
        name_class = input("Введите номер класса: ")
    all_classes[name_class] = [] # добавляется пустой список(класс будет создан)

def edit_student():
    student_id = input("Введите id ученика: ")
    surname = input("Введите фамилию ученика: ")
    name = input("Введите имя ученика: ")
    otch = input("Введите отчество ученика: ")
    birth = input("Введите дату рождения ученика: ")
    tel = input("Введите телефон ученика: ")
    adress = input("Введите адрес ученика: ")
    class_name = all_students[student_id][-1]
    new_st_data = [surname, name, otch, birth, tel, adress, class_name]
    all_students[student_id] = new_st_data

def delete_student():
    student_id = int(input("Введите id студента."))
    global all_classes
    global all_students
    all_classes[all_students[student_id][-1]].remove(student_id) # обращаемся по ключу student_id к словарю all_students и удаляем список-значение
    del all_students[student_id] # удаление из словаря all_students студента по id (del удаляет по индексу)

def change_class():
    student_id = int(input("Введите id студента."))
    old_class_number = all_students[student_id][-1] # находим имя класса студента
    new_class_number = input("Введите номер нового класса.")
    global all_classes
    global all_students
    all_classes[old_class_number].remove(student_id)
    all_classes[new_class_number].append(student_id)