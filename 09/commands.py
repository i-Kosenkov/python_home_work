from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logger
import calculate


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    await update.message.reply_text(f'/hello - приветствие\n /help - FAQ\n /calc - запустить калькулятор\n')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    await update.message.reply_text(f'/hello - приветствие\n /help - FAQ\n /calc - запустить калькулятор\n')


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.log(update, context)
    await update.message.reply_text('Введите вычисляемое выражение:\n')


async def input_message(update, context) -> None:
    logger.log(update, context)
    data = update.message.text
    res = calculate.calculator(data)
    await update.message.reply_text(f'{data} = {res}')
