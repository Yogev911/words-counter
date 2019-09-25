import json
import requests
import time
from collections import Counter
from multiprocessing import Pool
import redis
from conf import MAX_LINES_TO_PARSE, MAX_PROCESS, BLOCK_SIZE, DB_HOST, DB_PORT
from utilities.utils import is_url, is_path, preprocess_data, get_logger
from utilities.exceptions import *
import traceback
cache = redis.Redis(host=DB_HOST, port=DB_PORT)
logger = get_logger()

def extract_words(request):
    """
    Post new words and parse them
    :param request:
    :return:
    """
    try:
        data = json.loads(request.data)
        raw_text = data.get('data')
        logger.info("start process data")
        if is_path(raw_text):
            get_text_from_path(raw_text)
        elif is_url(raw_text):
            get_text_from_url(raw_text)
        else:
            get_text_from_body(raw_text)
        logger.info("done")
        return 'data received', 201
    except Exception as e:
        logger.info(f'Failed parse words: {e.__str__()}')
        return f'Failed parse words: {e.__str__()}', 501


def get_text_from_url(url):
    res = requests.get(url)
    processed_data = preprocess_data(res.json().get('data'))
    insert_words_to_db(processed_data)


def get_text_from_body(raw_text):
    processed_data = preprocess_data(raw_text)
    insert_words_to_db(processed_data)


def get_text_from_path(path):
    try:
        start_time = time.time()
        pool = Pool(MAX_PROCESS)
        lines = list(range(get_line_count(path)))
        line_to_parse = MAX_LINES_TO_PARSE
        liners = [[path] + lines[i:i + line_to_parse] for i in range(0, len(lines), line_to_parse)]
        pool.map_async(parse_chunk, liners)
        pool.close()
        pool.join()
        end_time = time.time()
        logger.info(f"total time : {end_time - start_time}")
    except Exception as e:
        logger.info(e.__str__())
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
            insert_words_to_db(words)
    except Exception as e:
        print(e.__str__())
        print(traceback.format_exc())


def get_line_count(path):
    """
    return the number of lines in text
    :param path:
    :return:
    """

    def blocks(files):
        while True:
            b = files.read(BLOCK_SIZE)
            if not b: break
            yield b

    with open(path, "r", encoding="utf-8", errors='ignore') as f:
        return sum(bl.count("\n") for bl in blocks(f))


def insert_words_to_db(word_counts):
    for k, v in word_counts.items():
        cache.incr(k, v)
