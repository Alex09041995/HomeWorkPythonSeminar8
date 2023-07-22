import Base1  

def menu():
    data = Base1.read_file()
    while True:
        print('Выберите действие: ')
        print('1 - вывести инфо на экран')
        print('0 - выход из программы')
        n = int(input('ваш выбор: '))
        if n == 0:
            break
        elif n == 1:
            print(Base1.print_info(data))
        elif n == 2:
            print(Base1.edit_data(data))
        elif n == 3:
            data = Base1.append(data)

if __name__ == '__main__':
    menu()
