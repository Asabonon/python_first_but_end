"""
Функции
О: Фрагиент программного кода (подпрограмма), 
к которому можно обратиться из другого места программы
print, type, range, len, input, int, float, str, ...

abs - модуль числа
min, max - мин. макс. значение последовательности
round - округление числа
print(round(10.9872, 2)) # 2 - до какого знака после запятой
sum - сумма элементов посл-ти
enumerate - пронумеровать посл-ть для цикла
###
some_list = ['1', '11', '111']
for number, some_string in enumerate(some_list, 1):
    print(number, some_string)
Вывод:
1 1
2 11
3 111
###

def some_name():
    ----
    ----
    # return можно, но не обязательно


some_name()

greeting ('Leo', 'Hi')
можно явно указывать аргумент при вызове функции
greeting (name = 'Leo', say = 'Hi')
можно при объявлении функции указывать параметр по умолчанию
def greeting (name, say = 'Hi')

для передачи любого количества аргументов:
args - передача любого количества по порядку (приходит кортеж)
def greeting (say, *args):
    print(say, args)

greeting ('Hi', '1', '2', '3')

kwargs - передача любого количества по имени (приходит словарь)
def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

get_person(name = 'Leo', age = 20, has_car = True)

локальные переменные - внутри функции
глобальные  - выше функции или через global my_var
внутри функции своя область видимости
функции в Python - тоже объект


def some_f():
    return 10


result = some_f()
print(result) # выведется 10

a = some_f
print(a) # выведется <function some_f at 0x0000015A7EB5D7E0>
print(type(a)) # выведется <class 'function'>
print(a()) # выведется 10

можно передавать функцию как параметр другой функции, 
например алгоритм проверки делимости на 2

lambda-функции
Применяются для создания анонимных функций по месту их использования
Синтаксис:
    lambda входные параметры: результат
Пример:
    lambda number: number % 2 == 0 # Делимость на 2
    lambda number: number > 4 # Больше 4 ?

Удобно, когда у нас есть некое выражение, 
 которое хочется записать в одну строчку,
 мы не хотим давать функции имя,
 хотим кратко передать функцию, в другую функцию

Функции sorted, filter, map
sorted:
    аргументы: последовательность, ключ для сортировки, порядок

numbers = [1, 5, 3, 5, 9, 7, 11]
# Сортировка по возрастанию, или алфавиту
print(sorted(numbers)) # Вывод: [1, 3, 5, 5, 7, 9, 11]
# Сортировка по убыванию
print(sorted(numbers, reverse=True)) # Вывод: [11, 9, 7, 5, 5, 3, 1]

cities = [('Москва', 1000), ("Лас-Вегас", 500), ("Антверпен", 2000)]
print(sorted(cities)) # Сортировка будет по алфавиту

def by_count(city):
    return city[1] #выделяем второй элемент у кортежей из списка

# Сортировка будет по второму элементу (числу по возрастанию)
print(sorted(cities,key=by_count))
print(sorted(cities,key=lambda city: city[1]))


filter(function, iterable)
    аргументы: функция фильтрации, последовательность

numbers = (1, 2, 3, 5, 6, 7, 11)
def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)
print(result) # Вывод: <filter object at 0x0000016B345B3DC0>
result = list(result)
print(result) # Вывод: [2, 6]

names = ['Max', 'Leo', 'Kate']

print(list(filter(lambda x: len(x) > 3, names)))

map
Применение функции к к аждому элементу последовательности
map(func, iterable, ...)

numbers = [1, 2, 3, 5, 6, 7, 11]
print(list(map(lambda x: x**2, numbers))) # Квадрат всех чисел
print(list(map(lambda x: str(x), numbers))) # Приведение к строке всех чисел

""" 
#### 1 ####
print('#### 1 ####')

from audioop import mul


def str_mod(name, age, city):
    return(print(f'{name}, {age} год(а), проживает в городе {city}'))

str_mod('Василий', '21', 'Москва')

#### 2 ####
print('#### 2 ####')

def str_mod(num_1, num_2, num_3):
    return max(num_1, num_2, num_3)

print(str_mod(55, 6, 7))


#### 3 ####
print('#### 3 ####')

player = {
    'name': 'player', 
    'health': 100, 
    'armor': 1.2,
    'damage': 50
}

enemy = {
    'name': 'enemy', 
    'health': 100, 
    'armor': 1.2,
    'damage': 50
}

def true_dmg(armor = 1.1, damage = 30):
    return damage // armor

def attack(defender, attacker):
    defender['health'] -= true_dmg(defender['armor'], attacker['damage'])
    defender['health'] = int(defender['health'])
    if (defender['health'] < 0):
        defender['health'] = 0
        defender['name'] = 'dead_' + defender['name']
        
attack(player, enemy)
print(player)
attack(enemy, player)
print(player)
print(enemy)
attack(enemy, player)
print(enemy)
attack(enemy, player)
print(enemy)

attack(player, enemy)
attack(player, enemy)
print(player)
