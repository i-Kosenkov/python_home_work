# Создайте программу для игры в ""Крестики-нолики"".

import random

a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = ' '
id_x = 'X'
id_o = '0'
count = 0


def board():
    print('   1   2   3 ')
    print('A ', a1, '|', a2, '|', a3)
    print('  ---|---|---')
    print('B ', b1, '|', b2, '|', b3)
    print('  ---|---|---')
    print('C ', c1, '|', c2, '|', c3)


def check_input(id_player):
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, count
    count += 1
    while True:
        # cell = random.choice(['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'])  # для игры c ботом
        cell = input('Укажите адрес ячейки (пример: a1, a2..): ')  # для игры человек vs человек
        if cell == 'a1' and a1 == ' ':
            a1 = id_player
            return
        elif cell == 'a2' and a2 == ' ':
            a2 = id_player
            return
        elif cell == 'a3' and a3 == ' ':
            a3 = id_player
            return
        elif cell == 'b1' and b1 == ' ':
            b1 = id_player
            return
        elif cell == 'b2' and b2 == ' ':
            b2 = id_player
            return
        elif cell == 'b3' and b3 == ' ':
            b3 = id_player
            return
        elif cell == 'c1' and c1 == ' ':
            c1 = id_player
            return
        elif cell == 'c2' and c2 == ' ':
            c2 = id_player
            return
        elif cell == 'c3' and c3 == ' ':
            c3 = id_player
            return
        else:
            print('Ошибочка! Повторите ввод.')


def check_win():
    if (a1 == a2 == a3 == 'X' or b1 == b2 == b3 == 'X'
            or c1 == c2 == c3 == 'X' or a1 == b1 == c1 == 'X'
            or a2 == b2 == c2 == 'X' or a3 == b3 == c3 == 'X'
            or a1 == b2 == c3 == 'X' or a3 == b2 == c1 == 'X'):
        print('Выиграли крестики!')
        exit()
    if (a1 == a2 == a3 == '0' or b1 == b2 == b3 == '0'
            or c1 == c2 == c3 == '0' or a1 == b1 == c1 == '0'
            or a2 == b2 == c2 == '0' or a3 == b3 == c3 == '0'
            or a1 == b2 == c3 == '0' or a3 == b2 == c1 == '0'):
        print('Выиграли нолики!')
        exit()
    if count == 9:
        print('Ничья!')
        exit()


board()
print('Первые играют:', ch := random.choice(['крестики', 'нолики']), end="\n")
if ch == 'нолики':
    check_input(id_o)
    board()
while True:
    check_input(id_x)
    board()
    if count > 4: check_win()

    check_input(id_o)
    board()
    if count > 4: check_win()
