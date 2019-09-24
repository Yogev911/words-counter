from flask_restful_swagger_2 import Schema


class WordModel(Schema):
    type = 'object'
    properties = {
        'user': {
            'word': 'string'
        }
    }


class DataModel(Schema):
    type = 'object'
    properties = {
        'answer': {
            'data': 'string'
        }
    }
