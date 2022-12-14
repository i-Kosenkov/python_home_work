from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from commands import *

app = ApplicationBuilder().token("5916296344:AAHaewqB0FGRaMVqqdyqrttMc88Tea1RqMU").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("find", find))
app.add_handler(CommandHandler("add", add))
app.add_handler(MessageHandler(filters.TEXT, input_message))

app.run_polling()
