from csv import DictReader, DictWriter
from os.path import exists
file_name = 'phone.csv'

def get_info():
    flrst_name = "Иван"
    last_name = "Иванов"
    flag = False
    while not flag:
        try:
            phone_namber = int(input("Введите телефон:"))
            if len(str(phone_namber)) != 11:
                print('Неверная длина телефона!')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер!')

    return [flrst_name, last_name, phone_namber]

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
main()