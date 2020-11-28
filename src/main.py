#!/usr/bin/env python3

'''
A simple bot that queries the site ksbg.nesa-sg.ch for grades
and displays them in a nice way to me.
'''

import threading, time, logging, sys
from telegram import Bot
from telegram.ext import Updater, CommandHandler

from log import setup_logger
from scraper import fetch
from const import HELP_MSG
from creds import TOKEN, MY_CHAT_ID

logger = setup_logger()

# Background thread to fetch grades every hour
def bg_fetching(bot, wait):
    logger.log(msg = "Fetching every {}mins!".format(wait), level = logging.INFO)
    while True:
        _ = fetch(False, bot)
        logger.log(msg = "Fetched grades!", level = logging.INFO)
        time.sleep(60 * wait)

# Check if it's actually me that issued the command
def wrong_user(update) -> bool:
    chat_id = update.effective_chat.id
    logger.info("{} tried to access the bot => {}!".format(
        chat_id, chat_id == MY_CHAT_ID and "allowed" or "denied"
    ))
    return chat_id != MY_CHAT_ID

def cmd_help(update, context):
    if wrong_user(update): return
    update.message.reply_text(text = HELP_MSG)
def cmd_grades(update, context):
    if wrong_user(update): return
    update.message.reply_text(text = fetch(True))
def cmd_fetch(update, context):
    if wrong_user(update): return
    update.message.reply_text(text = fetch(False))

if __name__ == "__main__":
    # Start the bot
    bot = Bot(TOKEN)
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("help", cmd_help))
    dp.add_handler(CommandHandler("start", cmd_help))
    dp.add_handler(CommandHandler("grades", cmd_grades))
    dp.add_handler(CommandHandler("fetch", cmd_fetch))
    updater.start_polling()
    # Start background fetching every x minutes
    if len(sys.argv) == 1:
        timeout = 30
    else:
        timeout = int(sys.argv[1])  
    thread = threading.Thread(target = bg_fetching, args = (bot, timeout, ))
    thread.start()
    thread.join()

