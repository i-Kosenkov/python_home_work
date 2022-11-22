import controller
import interface
import pandas
import logger


def menu_choice(data):
    logger.logging.info("Вывод меню")
    if data == '1':
        view_file_csv()
    elif data == '2':
        add_row_in_file_csv()
    elif data == '3':
        change_row_in_file_csv()
    elif data == '4':
        delete_row_in_file_csv()
    elif data == '5':
        create_file_csv()
    elif data == 'x':
        exit()
    else:
        print('Выбрано не верное значения, повторите ввод!')
        controller.run()


def view_file_csv():
    logger.logging.info("Просмотр базы данных")
    data = pandas.read_csv('db.csv')
    interface.view_data(data)


def add_row_in_file_csv():
    data = pandas.read_csv('db.csv')
    last_id = data['id'].loc[data.index[-1]] + 1
    print('Добавьте новую запись:')
    data.loc[len(data.index)] = [last_id, input('Имя: '), input('Фамилия: '), input('Дата рождения: '),
                                 input('Группа: '), input('Телефон: ')]
    data.to_csv('db.csv', index=False)
    print('Данные добавлены!')
    logger.logging.info(f'Добавление новой записи в базу, id {last_id} ')


def change_row_in_file_csv():
    client_id = int(interface.get_id())
    data = pandas.read_csv('db.csv', index_col='id')
    if client_id in data.index:
        logger.logging.info(f'Изменение записи базы данных, id {client_id}')
        print('Найдена запись:')
        interface.view_data(data[data.index == client_id])
        print('Введите новые данные:')
        data.at[client_id, 'Имя'] = input('Имя: ')
        data.at[client_id, 'Фамилия'] = input('Фамилия: ')
        data.at[client_id, 'Дата рождения'] = input('Дата рождения: ')
        data.at[client_id, 'Группа'] = input('Группа: ')
        data.at[client_id, 'Телефон'] = input('Телефон: ')
        data.to_csv('db.csv')
        print('Данные изменены!')
    else:
        logger.logging.info(f'Изменение записи базы данных, id {client_id} не найден')
        print('Запись не найдена!')


def delete_row_in_file_csv():
    client_id = int(interface.get_id())
    data = pandas.read_csv('db.csv', index_col='id')
    if client_id in data.index:
        logger.logging.info(f'Удаление записи, id {client_id} ')
        print('Найдена запись:')
        interface.view_data(data[data.index == client_id])
        data.drop([client_id], inplace=True)
        data.to_csv('db.csv')
        print('Запись удалена!')
    else:
        logger.logging.info(f'Удаление записи, id {client_id} не найден')
        print('Запись не найдена!')


def create_file_csv():
    data = pandas.read_csv('db.csv')
    file_name = input('Введите название файла: ')
    data.to_csv(file_name, index=False)
    logger.logging.info(f'Запись в файл {file_name}')
