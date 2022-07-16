""" 2: Создайте модуль. В нем создайте функцию, 
которая принимает список и возвращает из него случайный элемент. 
Если список пустой функция должна вернуть None. 
Проверьте работу функций в этом же модуле. """

import random

def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result
    else: # бесполезно, ибо это в Python по умолчанию
        return None

print(get_random([1, 2, 3, 4]))