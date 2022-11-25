from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logger
import pandas

value = str()
i = 1
lst = list()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    await update.message.reply_text(
        f'/hello - приветствие\n /help - FAQ\n /calc - запустить калькулятор\n /find - найти запись по индексу\n /add - добавить новую запись')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    await update.message.reply_text(
        f'/hello - приветствие\n /help - FAQ\n /calc - запустить калькулятор\n /find - найти запись по индексу\n /add - добавить новую запись')


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global value
    logger.log(update, context)
    value = 'calc'
    await update.message.reply_text('Введите вычисляемое выражение:')


async def find(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global value
    logger.log(update, context)
    value = 'find_id'
    await update.message.reply_text('Введите id записи:')


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global value
    logger.log(update, context)
    value = 'add'
    await update.message.reply_text('Введите данные:\nИмя:')


async def input_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    global value
    global i
    if value == 'calc':
        data = update.message.text
        await update.message.reply_text(f'{data} = {calculation(data)}')
        value = 'False'
    elif value == 'find_id':
        data = update.message.text
        await update.message.reply_text(find_id_row(data))
        value = 'False'
    elif value == 'add':
        data = update.message.text
        await update.message.reply_text(f'{add_row_in_file(data)}:')
        i += 1
    else:
        pass


def calculation(data):
    res = eval(data)
    return res


def find_id_row(data):
    file = pandas.read_csv('db.csv', index_col='id')
    if int(data) in file.index:
        text = str(file.loc[int(data)])
        return text
    else:
        return 'Запись не найдена!'


def add_row_in_file(data):
    global i, lst, value
    file = pandas.read_csv('db.csv')
    cols = file.columns
    lst.append(data)
    if i == 5:
        last_id = file['id'].loc[file.index[-1]] + 1
        lst.insert(0, last_id)
        file.loc[len(file)] = lst
        file.to_csv('db.csv', index=False)
        i = 0
        lst.clear()
        value = 'False'
        return f'Запись добавлена под индексом {int(last_id)}!\nДля ее просмотра используйте команду /find'
    return cols[i + 1]
