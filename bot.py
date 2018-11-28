
import logging
import data

from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import secret_settings

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
    keyboard = [[InlineKeyboardButton("album", callback_data='album'),
                 InlineKeyboardButton("album", callback_data='2'),
                InlineKeyboardButton("album", callback_data='3')]]
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


def photo(bot, update):
    chat_id = update.message.chat_id
    file_id = update.message.photo[-1].file_id
    file_path = bot.getFile(file_id)['file_path']
    logger.info(f"= Got on chat #{chat_id}: add photo!")
    bot.sendMessage(chat_id=chat_id, text="added succesfull")
    data.save_image(file_path, chat_id)

photo_handler = MessageHandler(Filters.photo, photo)
dispatcher.add_handler(photo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()

updater.dispatcher.add_handler(CallbackQueryHandler(button))
