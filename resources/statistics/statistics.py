from flask_restful_swagger_2 import Resource, swagger
from flask import request
from resources.statistics import service
from resources.statistics.swagger_doc import statistic_post


class Statistics(Resource):
    @swagger.doc(statistic_post)
    def post(self):
        return service.get_word_count(request)
