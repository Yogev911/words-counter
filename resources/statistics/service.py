import json
import redis

cache = redis.Redis(host='localhost', port=6379)


def get_word_count(request):
    try:
        data = json.loads(request.data)
        word = data.get('word')
        count = cache.get(word)
        if count:
            return count, 200
        else:
            return "word not found", 404
    except Exception as e:
        print(f'Failed get word count {e.__str__()}')
        return f'Failed login {e.__str__()}', 501
