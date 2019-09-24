from flask_cors import CORS
from flask import Flask
from flask_restful_swagger_2 import Api

from resources.words.words import Words
from resources.statistics.statistics import Statistics

from utilities.logger import Logger

# logger = Logger(__name__)

app = Flask(__name__)

CORS(app)
api = Api(app, api_version='0.1')

api.add_resource(Words, "/words")
api.add_resource(Statistics, "/statistics")

if __name__ == '__main__':
    # logger.info('Starting API')
    app.run(host="0.0.0.0", port=5000)
