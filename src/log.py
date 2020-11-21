'''
Log every command with a simple format: time - name - level - message.
'''

import logging

def setup_logger() -> logging.Logger:
    f = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format = f, level = logging.INFO)
    return logging.getLogger(__name__)
