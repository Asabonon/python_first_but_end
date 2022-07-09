### ИГРА УГАДАЙ ЧИСЛО
import random

number = random.randint(1, 100)
print(number)
user_number = None
count = 0

levels = {1: 10, 2: 5, 3: 3}
level = int(input('Введите сложность 1, 2, 3: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for user in range(user_count):
    user_name = input('Введите имя пользователя: ')
    users.append(user_name)
print(users)

is_winner = False
winner_name = ''

while not is_winner:
    count += 1
    if count > max_count:
        print("Вы проиграли! ")
        break
    print(f'Попытка № {count}')

    for user in users:
        print(f'Ход пользователя: {user}')

        user_number = int(input('Введите число! '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        if number > user_number:
            print('Больше')
        elif number < user_number:
            print('Меньше')
else:
    print(f'Победитель: {winner_name}')

