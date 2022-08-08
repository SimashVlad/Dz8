from main import *

def Start():
    print('Выберите желаемое действие: \n 1. Отобразить всю базу. \n 2. Поиск по базе. \n 3. Добаить пользователя. \n 4. Удалить пользователя. ')
    n = int(input('Ваш выбор: '))
    if n == 1:
        print('База родителей: \n')
        reading_file_to_dict1()
        print('База детей: \n')
        reading_file_to_dict2()
    elif n == 2:
        second_name = input('Введите фамилию родителя для поиска детей: ')
        reading_file_to_dict1()
        reading_file_to_dict2()
        print_childrens(second_name)
    elif n == 3:
        num = int(input('В какую базу добавить? 1 - Родители, 2 - Дети. Вводите число 1 или 2: '))
        if num == 1:
            record_file_to_dict1()
        elif num == 2:
            record_file_to_dict2()
        else:
            print('Введено некоректное значение! ')
    elif n == 4:
        num1 = int(input('Из какой базы удалить? 1 - Родители, 2 - Дети. Вводите число 1 или 2: '))
        if num1 == 1:
            del_file_to_dict1()
        elif num1 == 2:
            del_file_to_dict2()
        else:
            print('Введено некоректное значение! ')
    else:
        print('Ошибка, пожалуйста вводите число от 1 до 4')

