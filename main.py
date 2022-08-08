# Создать информационную систему позволяющую работать с сотрудниками некой компании \ 
# студентами вуза \ учениками школы

database = {}
db = {'parents': 1, 'children': 2}

def reading_file_to_dict1():
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\1.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        # print(data)
        database[1] = []
        for i in data:
            database[1].append(tuple(i.split(';')))
        print(f'{database} \n ')

def reading_file_to_dict2():
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\2.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        # print(data)
        database[2] = []
        for i in data:
            database[2].append(tuple(i.split(';')))
        print(f'{database} \n ')

def print_childrens(second_name):
    id = [i[0] for i in database[db['parents']] if second_name in i][0]
    deti = [i for i in database[db['children']] if id == i[0]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])

def record_file_to_dict1():
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\1.txt', 'a', encoding='utf-8') as file_1:
        file_1.write('\n' + input('Введите данные через ; '))
      
def record_file_to_dict2():
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\2.txt', 'a', encoding='utf-8') as file_1:
        file_1.write('\n' + input('Введите данные через ; '))

def del_file_to_dict1():
    text = ''
    dell = str(input('Введите фамилию пользователя, которого необходимо удалить: '))
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\1.txt', 'r', encoding='utf-8') as d:
        for line in d.readlines():
            if dell in line:
                pass
            else:
                text += line
    print(text)
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\1.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        
def del_file_to_dict2():
    text = ''
    dell = str(input('Введите фамилию пользователя, которого необходимо удалить: '))
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\2.txt', 'r', encoding='utf-8') as d:
        for line in d.readlines():
            if dell in line:
                pass
            else:
                text += line
    print(text)
    with open(r'C:\Users\Начальник\Desktop\УЧЁБА\PYTHON\Seminar_8\2.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        


# reading_file_to_dict1()
# reading_file_to_dict2()
# print(database)
# record_file_to_dict1()
# record_file_to_dict2()
# print_childrens('Petrov')
# del_file_to_dict1()
# del_file_to_dict2()

