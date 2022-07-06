# int float bool str None

# name = 'Me'
# age = 4
# print(name, age, sep="/", end='!

while True:
    example_number = input('Введите номер задания: ')
    if example_number == '1':
        entered_int = int(input('Введите число: '))
        print(entered_int + 2)

    elif example_number == '2':
        entered_int = 11
        while 0 >= entered_int or entered_int >= 10:
            entered_int = int(input('Введите число больше 0, но меньше 10: '))
        else:
            entered_int = entered_int ** 2
            print(entered_int)

    elif example_number == '3':
        # Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
        # Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
        # Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

        patient_age = int(input('Введите возраст: '))
        patient_weight = int(input('Введите вес: '))

        if patient_age <= 30 and 50 <= patient_weight <= 120:
            print("Пациент в хорошем состоянии")

        if 40 >= patient_age > 30 and (patient_weight < 50 or patient_weight > 120):
            print("Пациенту требуется заняться собой")

        if patient_age > 40 and (patient_weight < 50 or patient_weight > 120):
            print("Пациенту требуется врачебный осмотр")

    else:
        print('Введи нормальный номер задания!')
        continue
    break
print("Программа завершена!")
