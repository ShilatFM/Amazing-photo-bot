
import logging
import data
import mergeimage

from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import secret_settings

logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(token=secret_settings.BOT_TOKEN)
dispatcher = updater.dispatcher


dicargs={}
def start(bot, update, args):
    chat_id = update.message.chat_id
    if args:
        dicargs[chat_id] = args
    print(args)
    logger.info(f"> Start chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="Welcome !!!")
    keyboard = [[InlineKeyboardButton("Collage", callback_data='Collage'),
                 InlineKeyboardButton("Calendar", callback_data='Calendar'),
                InlineKeyboardButton("Greeting Card", callback_data='Greeting Card')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose what you want to do:', reply_markup=reply_markup)


def respond(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"> Respond chat #{chat_id}")


def button(bot, update):
    logger.info(f"> Button chat #{chat_id}")

    query = update.callback_query

    bot.edit_message_text(text="ok. Ill do a {} for you".format(query.data),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    if query.data == 'Collage':
        bot.send_message(chat_id=update.message.chat_id, text=f"ok. Ill do a {text} for you")

    if query.data == 'Calender':
        bot.send_message(chat_id=update.message.chat_id, text=f"ok. Ill do a {text} for you")

    if query.data == 'Greeting Card':
        bot.send_message(chat_id=update.message.chat_id, text=f"ok. Ill do a {text} for you")


def share(bot, update):
    logger.info(f"> Share chat #{chat_id}")

    chat_id = update.message.chat_id

    bot.send_message(chat_id=chat_id, text="Send this link to your friends")
    bot.send_message(chat_id=chat_id, text=f" https://telegram.me/{secret_settings.BOT_NAME}?start={chat_id}")


def photo(bot, update):
    logger.info(f"> Photo chat #{chat_id}")

    chat_id = update.message.chat_id
    file_id = update.message.photo[-1].file_id
    file_path = bot.getFile(file_id)['file_path']
    logger.info(f"= Got on chat #{chat_id}: add photo!")
    bot.sendMessage(chat_id=chat_id, text="added succesfull")
    if dicargs[chat_id]:
        data.save_image(file_path, dicargs[chat_id])
    else:
        data.save_image(file_path, chat_id)


def finish(bot, update):
    chat_id = update.message.chat_id
    logger.info(f"> end chat #{chat_id}")
    bot.send_message(chat_id=chat_id, text="ok, I will send your collage in few seconds")
    lst = data.load_image(chat_id)
    mergeimage.create_collage(lst).save(f"{chat_id}_collage.jpg")


photo_handler = MessageHandler(Filters.photo, photo)
dispatcher.add_handler(photo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

finish_handler = CommandHandler('finish', finish)
dispatcher.add_handler(finish_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

logger.info("Start polling")
updater.start_polling()

share_handler = CommandHandler('share', share)
dispatcher.add_handler(share_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(button))
