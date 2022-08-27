#!/usr/bin/env python
import logging

from telegram import __version__ as TG_VER

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

#groupname:superduper2379
updater = Updater("5662021609:AAG0cqF1ZFhDpGo80GJn8yPO4sYMYyIlweE",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello Welcome to Swapnil's Bot")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Help TODO""")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" %
                              update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" %
                              update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

# updater.dispatcher.add_handler(CommandHandler(Filters.command, unknown))
# updater.dispatcher.add_handler(MessageHandler(
#     Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
