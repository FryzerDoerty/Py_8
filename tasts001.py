# Создали файл и добавили в него записи
# with open('directory.txt', 'w') as data:
#     data.write('Ivanov Ivan Sergeevich 12358395389 \n')
#     data.write('Petrov Petr Anatolevich 12358395989 \n')
#     data.write('Samoylova Anastasia Dmitrievna 12328305989 \n')
#Добавили запись в текстовый файл
def WritePerson(second_name, first_name, patronymic, phone):
    with open('directory.txt', 'a') as f:
        f.write(f'\n{second_name} {first_name} {patronymic} {phone} ')
def write_data():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    WritePerson(second_name, first_name, patronymic, phone)
#write_data()

#Чтение всего файла
def read_file():
    file1 = open('directory.txt', 'r')
    lines = file1.readlines()
    for line in lines:
        print(line.strip())
    file1.close
#read_file()   

#Поиск по одной харатеристике
def search_charact():
    charact = input('Введите одну из характеристик (номер телфона, имя, фимилия, отчетсво): ')
    file1 = open('directory.txt', 'r')
    while True:
        line = file1.readline()
        if not line:
            break
        if charact in line:
            print(line.strip())
    file1.close

#Замена строки
def replacement_line():
    s = input('Введите одну из характеристик (номер телфона, имя, фимилия, отчетсво): ')   
    ch = input('Введите то, на что меняем: ')
    f = open('directory.txt', 'r')
    L = f.readlines()
    c=0
    for line in L:
        if s in line:
            L[c] = line.replace(s, ch)
        c+=1

    f.close()

    f = open('directory.txt', 'w')

    for line in L:
        f.write(line)

    f.close()

#Удаление строки или элемента
def delite_line():
    s = input('Введите характеристику или строку, которую хотите удалить (номер телфона, имя, фимилия, отчетсво): ')   
    f = open('directory.txt', 'r')
    L = f.readlines()
    c=0
    for line in L:
        if s in line:
            L[c] = line.replace(s, '')

        c+=1
    d=0
    for line in L:
        if line == '\n':
            L[d] = L[d+1]

        d+=1

    f.close()

    f = open('directory.txt', 'w')

    for line in L:
        f.write(line)
    f.close()
   
def res():
    a = input('Выберите, какое действие вы хотите совершить(Напиите строчную букву): а)прочитать файл; б) добавить запись; в)удалить запись или элемент; г) заменить; д) найти: ')
    if(a=='а'):
        read_file()  
    elif(a=='б'):
        write_data()
    elif(a=='в'):
        delite_line()
    elif(a=='г'):
        replacement_line()
    elif(a=='д'):    
        search_charact()

    f = open('directory.txt', 'r')
    L = f.readlines()
    d=0
    for line in L:
        if line == '\n':
            L[d] = L[d+1]
        d+=1

    f.close()
res()
