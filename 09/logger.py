from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    time = datetime.now().strftime('%D %H:%M')
    file = open('log.csv', 'a')
    file.write(f'{time},{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()
