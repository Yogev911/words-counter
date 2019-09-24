from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.words import service
from resources.words.swagger_doc import words_post


class Words(Resource):
    @swagger.doc(words_post)
    def post(self):
        return service.extract_words(request)
