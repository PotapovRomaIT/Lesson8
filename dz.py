from csv import DictWriter
from os.path import exists
file_name = 'phone2.csv'

def get_info():
    flag = False
    while not flag:
        try:
            namber = int(input("Введите номер строки: "))
            flag = True
        except ValueError:
            print('Это не номер!')
    with open("phone.csv", 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i == namber:
                return line
        print("Такой строки нет!")
    return get_info()
    
def create_file(file_name): # создание файла.
    with open(file_name, 'a', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_w.writeheader()
    
def main():
    while True:
        print(namber_line, end='')
        command = input("Желаете копировать эту строку? 'Да'/'Нет': ")
        if command == "Нет":
            break
        elif command == "Да":
            if not exists(file_name):
                create_file(file_name)
            data = open(file_name, 'a', encoding='utf-8')
            data.writelines(namber_line)
            data.close()
            print("Строка копирована в фаил", file_name)
            break

namber_line = get_info()
main()
