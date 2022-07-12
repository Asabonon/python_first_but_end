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
""" 




