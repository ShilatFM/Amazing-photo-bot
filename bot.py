import secret_settings
import logging

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token=secret_settings.BOT_TOKEN)
dispatcher = updater.dispatcher


def start(bot, update):
    chat_id = update.message.chat_id
    logger.info(f"> Start chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="Welcome !!!")
    keyboard = [[InlineKeyboardButton("Album", callback_data='Album'),
                 InlineKeyboardButton("Greeting Card", callback_data='Greeting Card'),
                InlineKeyboardButton("Collage", callback_data='Collage')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def respond(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    response = text.replace("7", "💣")
    bot.send_message(chat_id=update.message.chat_id, text=response)

def button(bot, update):
    query = update.callback_query

    bot.edit_message_text(text="ok. Ill do a {} for you".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def photo_handler(bot, update):
    file = bot.getFile(update.message.photo.file_id)
    # print("file_id: " + str(update.message.photo.file_id))
    file.download('photo.jpg')
    bot.send_message("photo send successfully")

# updater = Updater(token='my token')
# dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))



start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(button))

logger.info("Start polling")
updater.start_polling()

