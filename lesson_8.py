"""
Практикум. File Manager. Основные функции:
Шаг 1
    Создание файла.
    Создание папки.
Шаг 2
    Функция создания папки.
Шаг 3
    Расширение функционала.
    Просмотр списка файлов и папок.
Шаг 4
Цикл.
    Пользователь играет, пока не угадает число.
Шаг 5
    Удаление файла.
Шаг 6
    Копирование.
Шаг 7
    Запись информации о работе менеджера в файл.
Шаг 8
    Цикл.
    Пользователь играет, пока не угадает число.
Шаг 9
    Импорт функций.
Шаг 10
    Логика работы скрипта.
Шаг 11
    Параметры для каждой функции.
Шаг 12
    Проверка функционала.
Шаг 13
    Вызов функции информации о менеджере.
    Обработка возможных ошибок ввода пользователя.
"""
import os
import shutil
import datetime

def create_file(name, text = None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)

def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)

def copy_file (name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка уже есть')
    else:
        shutil.copy(name, new_name)

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    print(result)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

def change_dir(name):
    os.chdir(name)



if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_f')
    get_list()
    get_list(True)
    delete_file('text.dat')
    copy_file('new_f', 'newest_f')
    create_file('text.dat', 'some text2')
    copy_file('text.dat', 'text2.dat')
    save_info('123')
