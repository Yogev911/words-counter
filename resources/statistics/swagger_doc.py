from resources.common_modles import WordModel

statistic_post = {
    'tags': ['Statistics'],
    'description': 'null',
    'parameters': [
        {
            'name': 'word',
            'description': 'Word search',
            'in': 'body',
            'schema': WordModel,
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'Data received',
        },
        '501': {
            'description': 'Internal server error'
        }
    }
}
