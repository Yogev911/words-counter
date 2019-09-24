import json

from pymongo import MongoClient
import conf
from threading import Lock, Thread
from flask import Flask, request
from time import sleep

app = Flask(__name__)
lock = Lock()
cache = {}


class DbClient(object):
    def __init__(self):
        self.client = MongoClient("mongodb+srv://root:1234@cluster0-83gw4.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.get_database('Lemonade')
        self.words = self.db.get_collection('words')


# db = DbClient()


@app.route('/insert', methods=['POST'])
def insert():
    global cache
    data = json.loads(request.data)
    lock.acquire()
    for k, v in data.items():
        if k in cache:
            cache[k] += v
        else:
            cache[k] = v
    lock.release()
    # db.words.find()
    return 'ok', 200


def words_aggregator(lock):
    global cache
    while True:
        try:
            lock.acquire()  # will block if lock is already held
            # TODO
            print(cache)
            cache = {}
            lock.release()

        except Exception as e:
            print(e.__str__())
            lock.release()
        finally:
            sleep(20)


def serve():
    try:
        aggregator = Thread(target=words_aggregator, args=(lock,))
        aggregator.start()
        app.run('0.0.0.0', 8081)
    except Exception as e:
        print(e.__str__())
        aggregator.join()
    finally:
        if aggregator.is_alive():
            aggregator.join()
