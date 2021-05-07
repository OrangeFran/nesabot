#!/usr/bin/env python3

'''
A simple bot that queries the site for grades
and displays them in a nice way to me.
'''

import logging
from log import setup_logger
logger = setup_logger()

import threading, time, os, dotenv
from scraper import fetch

# Constants from env variables
dotenv.load_dotenv('.env.local')
INTERVAL = int(os.environ['CHECK_INTERVAL'])

# Background thread to fetch grades every x minutes
def main():
    wait = INTERVAL * 60
    logger.log(msg='[=] Fetching every {} seconds!'.format(wait), level=logging.INFO)
    while True:
        # Check if the process failed
        if fetch():
            logger.log(msg='[+] Fetched grades!', level=logging.INFO)
        else: 
            logger.log(msg='[x] Something went wrong, retrying ...', level=logging.WARNING)
            continue
        time.sleep(wait)

if __name__ == '__main__':
    main()
