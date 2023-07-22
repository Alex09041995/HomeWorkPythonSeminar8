def print_info(temp):
    print(temp)


def read_file():
    with open('my_file.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()
    return temp

def write_file():
    pass

def export_data():
    with open('my_file.txt', 'r', encoding = 'utf-8') as file:
        temp = file.readlines()
    num = len(file.readlines)
    with open('my_file.txt', 'r', encoding = 'utf-8') as data:
        fio = input('Введите ФИО: ')
    phone_number = input('Введите номер телефона: ')
    data.write('Base1'{num} | {fio} | {phone_number}\)
        print('Добавлена запись' : {num} | {fio} | {phone_number}\)

def edit_data(filename):
    print('Изменение информации')
    with open(filename, «r», encoding=’utf-8′) as data:
    tel_book = data.read()
    print(tel_book)
    index_delete_data = int(input(«Введите номер строки для редактирования: «)) — 1
