# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import time
import random


def people_choise():
    while True:
        quantity = input('Человек: ')
        if quantity.isdigit() and 0 < int(quantity) < 29:
            return int(quantity)
        else:
            print('Не больше 28 конфет в одни руки!')


def bot_choise():
    time.sleep(0.5)
    if 29 < amount <= 56:
        print('Андройд: ', amount - 29)
        return amount - 29
    elif amount < 29:
        print('Андройд: ', amount)
        return amount
    print('Андройд: ', x := random.randint(1, 29))
    return x


amount = 100

print('Первый ход начинает', ch := random.choice(['Человек', 'Андройд']))
time.sleep(0.5)
if ch == 'Андройд':
    amount -= bot_choise()
    print('Осталось: ', amount)

while True:
    amount -= people_choise()
    if amount <= 0:
        print('Победил человек ㋛')
        break
    print('Осталось: ', amount)

    amount -= bot_choise()
    if amount <= 0:
        print('Победил андройд! ¯\_(ツ)_/¯')
        break
    print('Осталось: ', amount)
