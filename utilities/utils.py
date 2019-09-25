import os
from collections import Counter
import re

from conf import URL_RE, SPLIT_WORDS_RE

import logging


def get_logger():
    # Gets or creates a logger
    logger = logging.getLogger(__name__)
    # set log level
    logger.setLevel(logging.DEBUG)
    # define file handler and set formatter
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)
    # add file handler to logger
    logger.addHandler(file_handler)
    return logger


def is_url(st):
    """
    Check if a string is a valid url format
    :param st: string
    :return: bool
    """
    return re.match(URL_RE, st) is not None


def is_path(st):
    """
    Check if a string is a valid path
    :param st: string
    :return: bool
    """
    return os.path.exists(os.path.dirname(st))


def preprocess_data(row_text):
    # strip and lower
    try:
        # row_text = row_text.lower()
        return Counter(map(lambda x: x.lower(), re.findall(SPLIT_WORDS_RE, row_text)))
    except:
        return None
