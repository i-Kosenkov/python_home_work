def input_int_number(n):
    while True:
        number = input(n)
        if number.isdigit():
            return int(number)
        else:
            print('Error! Enter a NUMBER!!!')


def input_float_number():
    while True:
        number = input('Enter the number: ')
        try:
            float(number)
            return float(number)
        except ValueError:
            print('Error! Enter a NUMBER!!!')


def random_list_with_variables(a, b, n):
    import random
    return random.sample(range(a, b), n)

def random_list(n, a):
    from random import randint
    list = [randint(-a, a) for i in range(n)]
    return list
