from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from commands import *

app = ApplicationBuilder().token("telegram-key").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(MessageHandler(filters.TEXT, input_message))

app.run_polling()
