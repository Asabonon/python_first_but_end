
""" 
my_str_1[:4] - срез от начала до 4го элемента ; my_str_1[4:] - срез от 4го элемента до конца my_str_1[-1] - последний
len(my_str_1) - длина строки (кол-во символов)
my_str_1.find('1') - найти символ 1 (выведет индекс или -1) ; my_str_1.split() - разделить строку по пробелам  '1 23'.split() = '1','23'
my_str_1.isdigit() - состоит только из чисел ; names.upper() или .lower() - приводит строку к верхнему или нижнему регистру
print("Вы ввели: {} {} {}".format(day_dict[dd], month_dict[mm], yyyy))
строка - str 'sdsd 213'; список - list  my_list_1 = [2, 2, 5, 12, 8, 2, 12], если по индексу, то строка, если срезом, то  список; 
my_list_1.append(14) - добавить в конец списка 14 ; my_list_1.pop() - удалить и вернуть последний элемент списка
my_list_1.clear() - очистить весь список ; 
my_list_1.remove(14) - удалить элемент из списка по значению ; del my_list_1[0] - удалить элемент по индексу
my_list_1.reverse() - перевернуть

оператор in 
if '1' in my_list_1:
    print('ок')

кортеж (turple) - список, который нельзя менять ; служит для защиты от изменений
my_turple_1 = (2, 5, 8, 2, 12, 12, 4, 2)
  
sorted(my_list_1) - отсортировать по алфавиту


for friend in friends:
    print(friend)

range()
<class 'range'> 
range()
range(6) == range(0, 6) == 0, 1, 2, 3, 4, 5
range(1, 6) ==  1, 2, 3, 4, 5
range(1, 6, 2) == 1, 3, 5

for - перебор последовательности. Индекс не нужен
for range - перебор последовательности. Нужен индекс
for range - необходимо пропустить некоторые элементы 
или идти с конца в начало
while - цикл связан с условием, но не с последовательностью

Словарь dict 
Неупорядоченные коллекции произвольных объектов с доступом по ключу

my_dict = {key1: val1, key2: val2, ...}

Множество set
Неупорядоченные коллекции, содержащий не повторяющиеся элементы
Во множестве не может быть 2-х оддинаковых элементов
cities_a = {'Las Vegas', 'Paris', 'Moscow'}
cities.add() .remove() len, in, for, итд 
cities_b = {'Las Vegas', 'Omsk', 'Tomsk'}

cities_a | cities_b - объединение set
cities_a & cities_b - пересечение set
cities_a - cities_b - есть в a, но нет в b
cities_b - cities_a - есть в b, но нет в a

"""

""" 
rng_a = range(1, 6)
print(type(rng_a))
print(list(rng_a))
 """

""" 
list_a = [1, 2, 3, 4]
if 1 in list_a:
    print('ok')
 """

## ПЕРЕБОР
""" 
friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам
for key in friend.keys():
    print(key) # выведет все ключи
    print(friend[key]) # выведет все значения
# или
for key in friend:
    print(key) # выведет все ключи
    print(friend[key]) # выведет все значения
 

# по значениям
for val in friend.values():
    print(val) # выведет все значения

# пары ключ значение
for item in friend.items():
    print(item) # выведет пары ключ значение в виде кортежей
for key, val in friend.items():
    print(key) # выведет все ключи
    print(val) # выведет все значения
"""




while True:
    example_number = input('Введите номер задания: ')
    if example_number == '1':
        my_list_1 = [2, 5, 8, 2, 12, 12, 4, 2]
        my_list_2 = [2, 7, 12, 3]

        for i in my_list_1[:]: #работа с копией списка
            if i in my_list_2:
                my_list_1.remove(i)
        print(my_list_1)
        
    elif example_number == '2':
        date = input("введите дату в формате: dd.mm.yyyy: ")
        dd, mm, yyyy = date.split('.') 
        day_dict = {
            '01': 'первое',
            '02': 'второе',
            '03': 'третье',
            '04': 'четвертое',
            '05': 'пятое',
            '06': 'шестое',
            '07': 'седьмое',
            '08': 'восьмое',
            '09': 'девятое',
            '10': 'десятое',
            '11': 'одиннадцатое',
            '12': 'двенадцатае',
            '13': 'тринадцатое',
            '14': 'четырнадцатое',
            '15': 'пятнадцатое',
            '16': 'шестнадцатое',
            '17': 'семнадцатое',
            '18': 'восемнадцатое',
            '19': 'девятнадцатое',
            '20': 'двадцатое',
            '21': 'двадцать первое',
            '22': 'двадцать второе',
            '23': 'двадцать третье',
            '24': 'двадцать четвертое',
            '25': 'двадцать пятое',
            '26': 'двадцать шестое',
            '27': 'двадцать седьмое',
            '28': 'двадцать восьмое',
            '29': 'двадцать девятое',
            '30': 'тридцатое',
            '31': 'тридцать первое'
        }
        month_dict = {
            '01': 'января',
            '02': 'февраля',
            '03': 'марта',
            '04': 'апреля',
            '05': 'мая',
            '06': 'июня',
            '07': 'июля',
            '08': 'августа',
            '09': 'сентября',
            '10': 'октября',
            '11': 'ноября',
            '12': 'декабря'
        }

        print("Вы ввели: {} {} {} года".format(day_dict[dd], month_dict[mm], yyyy))
        result = f'Вы ввели: {day_dict[dd]} {month_dict[mm]} {yyyy} года'
        print(result)


    elif example_number == '3':
        my_list_1 = [2, 2, 5, 12, 8, 2, 12]
        result = []
        for number in my_list_1:
            if my_list_1.count(number) == 1:
                result.append(number)
        print(result)
        
    else:
        print('Введи нормальный номер задания!')
        continue
    break 
print("Программа завершена!")

