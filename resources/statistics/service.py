import json
import redis
from utilities.exceptions import *
from utilities.utils import get_logger
cache = redis.Redis(host='localhost', port=6379)
logger = get_logger()


def get_word_count(request):
    try:
        data = json.loads(request.data)
        word = data.get('word')
        if not isinstance(word,str):
            raise BadInput(f"Expected string, received {type(word)}")
        word = word.lower()
        logger.info(f"Search for word {word}")
        count = cache.get(word)
        if not count:
            raise WordNotFound(f"Word {word} not found")
        logger.info(f"word {word} returned {count} times")
        return f"word {word} returned {count} times", 200
    except WordNotFound as e:
        logger.info(f"Word {word} not found")
        return e.__str__(), 404
    except BadInput as e:
        logger.info(f"bad input, {e.__str__()}")
        return e.__str__(), 400
    except Exception as e:
        return f'Failed get word count {e.__str__()}', 501
