"""
Модули и библиотеки
 Python позволяет поместить классы, функции, данные, 
а также скрипты в отдельный файл 
и использовать их в других программах.

О: Модулем в Python называется любой файл с программой.

Зачем нужны модули:
    Повторное использование кода.
    Управление пространством  имен.
    Деление большого проекта на мелкие части.

Разновидности модулей:
    встроенные (math, random, ...)
    сторонние (django, PyQt5, ...)
    свои (любой .py файл)
    между своими и сторонними модулями нет принципиальной разницы, 
отличие только в авторе

Варианты подключения:
    модуль целиком 
        import math
    псевдоним для модуля 
        import math as mt
    импорт всего содержания 
        from math import * (не рекомендуется)
    импорт конкретных функций, классов, … 
        from math import sin, cos

Использование math:
    Математические функции.
    Работа с числами.

Основные функции math:
    factorial - факториал числа
    exp - экспонента
    log, log2, log10 - логарифмы
    sqrt - квадратный корень
    sin, cos, asin, asoc, ...
    и многие другие

Использование random:
    Генерация случайных чисел.
    Букв.
    Элементов последовательности.

Основные функции random:
    randint - целое случайное число от A до B
    choice - случайный элемент последовательности
    shuffle - перемешивает последовательность
    random - случайное число от 0 до 1
    sample - список длиной k из последовательности (неск. из послед-ти)
    и многие другие

Импорт из своих модулей:
    Совершается так же, как и из стандартных модулей
    При импорте нужно учитывать путь до модуля
    import firstmodule
    import folder.secondmodule

Модули со скриптами:
    При любом варианте импорта скрипты будут выполняться
    Если не указано никаких условий (if __name__ == ‘__main__’)
    Это обязательно нужно учитывать при импорте


if __name__ == ‘__main__’:
    Ограничивает выполнение скриптов
    При импорте код не будет выполняться
    Он будет выполняться при запуске модуля


Определение пакета:
    Пакет - каталог, включающий в себя другие пакеты и модули
    Пакет содержит файл __init__.py

Назначение пакета:
    Формирование пространства имен.
    Работа с модулями с указанием уровня вложенности.
    пакет1.пакет2.модуль.
    Уровни отделяются точкой.

Варианты импортов:
    import .модуль - внутри пакета из одного модуля в другой
    import пакет.модуль - стандартно
    import, from, as ...
    вложенность пакетов может быть любой (пакет в пакете ...)

Модуль os:
    Функции для работы с операционной системой
    Не зависит от конкретной ОС

Функции и переменные os:
    name - имя операционной системы
    chdir - смена текущей директории 
    getcwd() - текущая рабочая директория
    mkdir() - создание директории (папки)
    os.path - модуль для работы с путями 
    и многие другие

Модуль sys:
    Взаимодействие с интерпретатором Python

Функции и переменные sys:
    executable - путь к интерпретатору Python
    exit() - выход из Python
    platform - информация об ОС
    path - список путей поиска модулей
    argv - список аргументов командной строки
    и многие другие

sys.path:
очень важная переменная
    она хранит пути, по которым Python ищет модули
    она имеет изменяемый тип данных list
    таким образом мы можем изменять эту переменную

Пример для тренировки:
    В папке с модулем создать 5 подпапок, 
    названия которых состоят из платформы, 
    на которой запущен интерпретатор и порядкового номера, 
    начиная с 1: win32_1, win_32_2, … Платформа может быть другой.

sys.argv:
    список аргументов командной строки при запуске скрипта Python
    sys.argv[0] - путь до скрипта
    остальные параметры передаются при вызове скрипта через пробел
    python my_script.py par1 par2 par3 ...

Практический пример:
    В зависимости от параметра вызывать различные функции скрипта
    Параметр ping -> функция выводит pong
    2 параметра name <Имя> -> функция приветствия пользователя
    параметр list: показать содержимое текущей директории
"""

# ### создаст 5 папок в этом каталоге ###
# import sys, os

# name = sys.platform

# for i in range(1, 6):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
#     os.mkdir(new_path)
    
# ### /создаст 5 папок в этом каталоге ###

# import sys

# print('Работа с командной строкой ввести: python 5_fifth.py') 
# print(sys.argv[0])  #если из терминала, то выведет 5_fifth.py, 
#                     #А если f5, то c:\Users\asabi\Desktop\summer2022\python_first_but_end\5_fifth.py
# print('ж'*50)

# for arg in sys.argv: # после вызова модуля, передаем аргументы
#     print(arg) # вывод введенных аргументов построчно
#     print(type(arg)) # вывод типов введеных аргументов (все строки)



""" import sys, os

def ping():
    print ('pong')

def hello(name):
    print('Hello ', name)

def get_info():
    print(os.listdir())

command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name) """

# cls - очистить / стереть историю терминала

""" Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. 
Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле. """

""" import os

def create_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)

def delete_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)
        
#create_folders()
#delete_folders() """

""" 2: Создайте модуль. В нем создайте функцию, 
которая принимает список и возвращает из него случайный элемент. 
Если список пустой функция должна вернуть None. 
Проверьте работу функций в этом же модуле. """

""" import random

def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result
    else: # бесполезно, ибо это в Python по умолчанию
        return None

print(get_random([1, 2, 3, 4])) """

""" 3: Создайте модуль main.py. 
Из модулей реализованных в заданиях 1 и 2 
сделайте импорт в main.py всех функций. 
Вызовите каждую функцию в main.py 
и проверьте что все работает как надо. """

""" from 5_
import 5.1_fifth.py """