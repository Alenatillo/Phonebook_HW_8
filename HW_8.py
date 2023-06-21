# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения. Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий. Также пользователь может добавлять новых людей в справочник в режиме экспорт.

def input_dataset():
    secondname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronym = input('Введите отчество: ')
    phonenum = input('Введите номер телефона: ')
    return secondname, name, patronym, phonenum

def controller():
    mode = int(input('Выберите пункт меню в спавочнике: (1 - найти контакт, 2 - добавить контакт): '))
    if mode == 1:
        secondname = input_secondname()
        find_person(secondname)
    elif mode == 2:
        dataset = input_dataset()
        write_person(dataset)
    else:
        print('Такого пункта в меню не существует!')
        controller()   

def write_person(dataset: tuple):
    with open('infobook.txt', 'a', encoding='utf-8') as file:
        file.write('\n'+'\n'.join(dataset))


def find_person(secondname: str):
    with open('infobook.txt', 'r', encoding='utf-8') as file:
        line_list = file.read().splitlines()
        found = False
        for ind in range(len(line_list)):
            if line_list[ind] == secondname.title():
                found = True
                print(line_list[ind])
                print(line_list[ind + 1])
                print(line_list[ind + 2])
                print(line_list[ind + 3])
        if not found:
            print('Контакт не найден!')


def input_secondname():
    secondname = input('Введите фамилию для поиска контакта: ')
    return secondname

controller()
