""" Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). 
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. 
Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле. """

import os

def create_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)

def delete_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)
        
#create_folders()
#delete_folders()