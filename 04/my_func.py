import random


def input_int_number(n):
    while True:
        number = input(n)
        if number.isdigit():
            return int(number)
        else:
            print('Error! Enter a NUMBER!!!')


def input_float_number(n):
    while True:
        number = input(n)
        try:
            float(number)
            return float(number)
        except ValueError:
            print('Error! Enter a NUMBER!!!')


def random_list_with_variables(a, b, n):
    return random.sample(range(a, b), n)


def random_list(a, b, n):
    from random import randint
    list = [randint(a, b) for i in range(n)]
    return list


def random_list_float_numbers(n, a, b, rnd):
    list = [random.uniform(a, b) for i in range(n)]
    list = [round(i, rnd) for i in list]
    return list
