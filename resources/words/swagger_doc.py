from resources.common_modles import DataModel

words_post = {
    'tags': ['word'],
    'description': 'null',
    'parameters': [
        {
            'name': 'data',
            'description': 'Input data',
            'in': 'body',
            'schema': DataModel,
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
