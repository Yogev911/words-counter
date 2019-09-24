from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.words import service
from resources.words.swagger_doc import puzzle_get, puzzle_put


class Words(Resource):
    @swagger.doc(puzzle_get)
    def post(self):
        return service.extract_words(request)
