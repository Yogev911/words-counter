import os
from collections import Counter
import re

from conf import URL_RE, SPLIT_WORDS_RE



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
