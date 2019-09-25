from flask_restful_swagger_2 import Schema


class WordModel(Schema):
    type = 'object'
    properties = {
        'word': {
            'type': 'string'
        }
    }


class DataModel(Schema):
    type = 'object'
    properties = {
        'data': {
            'type': 'string'
        }
    }
