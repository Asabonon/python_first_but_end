while True:
    example_number = input('Введите номер задания: ')
    if example_number == '1':
        my_list_1 = [2, 5, 8, 2, 12, 12, 4, 2]
        my_list_2 = [2, 7, 12, 3]
        for i in my_list_2:
            while i in my_list_1:
                my_list_1.remove(i)
        print(my_list_1)
    elif example_number == '2':
        date = input("введите дату в формате: dd.mm.yyyy")
        print(date)
        print(type(date))
        dd = date[0:2]
        mm = date[3:5]
        yyyy = date[6:10]
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
        print("Вы ввели: {} {} {}".format(day_dict[dd], month_dict[mm], yyyy))
        break
    elif example_number == '3':
        my_list_1 = [2, 2, 5, 12, 8, 2, 12]
        break
    else:
        print('Введи нормальный номер задания!')
        continue


