import sys
from lesson_8 import change_dir, copy_file, create_file, create_folder, get_list, delete_file, save_info

save_info('Старт')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести команду в терминал, напр. help')
else:
    if command == 'list':
        get_list()
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Необходимо ввести имя копируемого и нового файлов')
        else:
            copy_file(name, new_name)
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя нового файлов')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя новой папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя файла или папки')
        else:
            delete_file(name)
    elif command == 'save':
        try:
            name = sys.argv[2]
        except IndexError:
            name = 'No message'
        save_info(name)

    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя новой директории')
        else:
            change_dir(name)

    elif command == 'help':
        print('help - список команд консольного файлового менеджера')
        print('list - список файлов и папок')
        print('copy - копирование файла и папки')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файлов и папок')
        print('save - сохранение текущего вмерени и сообщения в файл')
        print('ch - смена директории')
    
    
    save_info('Конец')
    