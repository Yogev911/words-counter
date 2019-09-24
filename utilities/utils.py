import os
from collections import Counter

import re

url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

words_splitter_regex = r'\b(\w*)\b'


def is_url(st):
    """
    Check if a string is a valid url format
    :param st: string
    :return: bool
    """
    return re.match(url_regex, st) is not None


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
        row_text = row_text.lower()
        return Counter(map(lambda x: x.lower(), re.findall(words_splitter_regex, row_text)))
    except:
        return None
