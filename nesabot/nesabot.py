#!/usr/bin/env python3

'''
A simple bot that queries the site for grades
and displays them in a nice way to me.
'''

import logging

def setup_logger() -> logging.Logger:
    f = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format = f, level = logging.INFO)
    return logging.getLogger(__name__)

import threading, time, logging, sys
from telegram import Bot
from telegram.ext import Updater, CommandHandler

from scraper import fetch
from const import INTERVAL
from creds import TOKEN, MY_CHAT_ID
from commands import cmd_help, cmd_grades, cmd_fetch

logger = setup_logger()

# Background thread to fetch grades every x minutes
def bg_fetching(bot, wait):
    logger.log(msg = "Fetching every {} seconds!".format(wait), level = logging.INFO)
    while True:
        _ = fetch(False, bot)
        logger.log(msg = "Fetched grades!", level = logging.INFO)
        time.sleep(wait)

def main():
    # Start the bot
    bot = Bot(TOKEN)
    updater = Updater(TOKEN, use_context = True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", cmd_help))
    dp.add_handler(CommandHandler("start", cmd_help))
    dp.add_handler(CommandHandler("grades", cmd_grades))
    dp.add_handler(CommandHandler("fetch", cmd_fetch))
    updater.start_polling()

    # Start fetching grades in the background
    thread = threading.Thread(target = bg_fetching, args = (bot, INTERVAL * 60, ))
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()
