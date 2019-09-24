import json
from random import randint
import requests
from collections import Counter
from multiprocessing import Pool, Manager
import os

import conf
from utilities.dal import DbClient
from utilities.logger import Logger
from utilities.utils import is_url, is_path, preprocess_data
from utilities.exceptions import *


# db = DbClient()
# logger = Logger(__name__)


def extract_words(request):
    """
    Post new words
    :param request:
    :return:
    """
    try:
        data = json.loads(request.data)
        raw_text = data.get('data')
        if is_path(raw_text):
            get_text_from_path(raw_text)
        elif is_url(raw_text):
            get_text_from_url(raw_text)
        else:
            get_text_from_body(raw_text)

        return 'ok', 200
    except Exception as e:
        # logger.exception(f'Failed blah blah Error: {e.__str__()}')
        return f'Failed blah blah Error: {e.__str__()}', 501


def get_text_from_url(url):
    res = requests.get(url)
    processed_data = preprocess_data(res.json().get('st'))
    insert_words_to_db(processed_data)


def get_text_from_body(raw_text):
    processed_data = preprocess_data(raw_text)
    insert_words_to_db(processed_data)


def get_text_from_path(path):
    try:
        words = Counter()
        pool = Pool(os.cpu_count())
        lines = list(range(get_line_count(path)))
        line_to_parse = 5
        liners = [[path] + lines[i:i + line_to_parse] for i in range(0, len(lines), line_to_parse)]

        for bulk in pool.map(parse_chunk, liners):
            words += bulk
        insert_words_to_db(words)
    except Exception as e:
        print(e.__str__())
    finally:
        pool.close()
        pool.join()


def parse_chunk(data):
    try:
        path = data[0]
        line_start = data[1]
        line_end = data[-1]
        words = Counter()
        with open(path) as fp:
            for i, line in enumerate(fp):
                if i > line_end:
                    break
                if line_start <= i <= line_end:
                    pass
                    words += preprocess_data(line)
            return words
    except Exception as e:
        print(e.__str__())
        return None


def get_line_count(path):
    """
    return the number of lines in text
    :param path:
    :return:
    """
    def blocks(files, size=65536):
        while True:
            b = files.read(size)
            if not b: break
            yield b

    with open(path, "r", encoding="utf-8", errors='ignore') as f:
        return sum(bl.count("\n") for bl in blocks(f))


def insert_words_to_db(word_counts):
    print(word_counts)
