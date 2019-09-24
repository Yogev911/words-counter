import json

from pymongo import MongoClient
import conf

from flask import Flask, escape, request

app = Flask(__name__)


class DbClient(object):
    def __init__(self):
        self.client = MongoClient("mongodb+srv://root:1234@cluster0-83gw4.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.get_database('Lemonade')
        self.words = self.db.get_collection('words')


# db = DbClient()


@app.route('/insert',methods=['POST'])
def insert():
    data = json.loads(request.data)
    print(data)
    # db.words.find()
    return 'ok', 200


def serve():
    app.run('0.0.0.0', 8081)
