def input_int_number():
    while True:
        number = input('Enter the number: ')
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

def random_list(a, b, n):
    import random
    return random.sample(range(a, b), n)