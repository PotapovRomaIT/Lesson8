from csv import DictReader, DictWriter
from os.path import exists
file_name = 'phone.csv'
file_name2 = 'phone2.csv'

def get_info():
    flrst_name = "Иван"
    last_name = "Иванов"
    flag = False
    while not flag:
        try:
            phone_number = int(input("Введите телефон:"))
            if len(str(phone_number)) != 11:
                print('Неверная длина телефона!')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер!')
    return [flrst_name, last_name, phone_number]

def get_info2():
    flag = False
    while not flag:
        try:
            number = int(input("Введите номер строки: ")) # Ввод номера строки
            flag = True
        except ValueError: # Проверка на ввод числа
            print('Это не номер!')
    with open("phone.csv", 'r', encoding='utf-8') as f: # Копирование указанной строки. см. строку 25
        for i, line in enumerate(f):
            if i == number:
                return line
    line = "Такой строки нет!" # Проверка на наличие строки в файле 'phone.csv'
    return line # Замена рекурсии как было указанно

def create_file(file_name): # создание файла.
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя' : lst[0], 'Фамилия' : lst[1], 'Телефон' : lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def row_search(file_name):
    last_name = input("Введите фамилию: ")
    res = read_file(file_name)
    for elem in res:
        print(elem["Фамилия"], last_name)
        if elem["Фамилия"] == last_name:
            print(elem)
            break
    else:
        print("Фамилии нет")

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "w":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == "r":
            if not exists(file_name):
                print('Фаил отсутствует, создайте его!')
                continue
            print(*read_file(file_name))
        elif command == "f":
            if not exists(file_name):
                print('Фаил отсутствует, создайте его!')     
                continue
            row_search(file_name)   
        elif command == "c": # меню копирования
            number_line = get_info2() # вызов функции проверки на ввод числа и проверки на наличия строки в файле 'phone.csv'. Без рекурсии.
            print('Выбранная строка: ', number_line, end='')
            if number_line == "Такой строки нет!": # Остановка меню в случаи отсутствие строки. По примеру из семинара. строка 71.
                break
            command = input("Желаете копировать эту строку? 'Да'/'Нет': ") # Выбор копировать или не копировать.
            if command == "Нет": # Остановка работы меню по примеру из семинара. строка 71.
                break
            elif command == "Да":
                if not exists(file_name2):
                    create_file(file_name2)
                data = open(file_name2, 'a', encoding='utf-8')
                data.writelines(number_line)
                data.close()
                print("Строка копирована в файл: ", file_name2)
main()