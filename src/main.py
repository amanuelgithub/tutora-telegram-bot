'''
Initializes and runs the bot 24/7
'''

import sys

sys.path.append('.')

import logging

from dotenv import load_dotenv
import os

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from src.menu import *

# load .env file form the directory structure(by using the dotenv library)
load_dotenv()

# accessing the api token generated for the bot
API_KEY = os.getenv('API_KEY')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_KEY)

    # Get dispather to register handler
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    dispatcher.add_handler(
        CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
    updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))
    updater.dispatcher.add_error_handler(error)

    # Start tte Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
