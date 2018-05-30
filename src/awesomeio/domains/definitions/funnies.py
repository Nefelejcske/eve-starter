from awesomeio.domains import domain


@domain()
class Funnies(object):
    name = "funnies"
    domain = {
        'item_title': 'solution',
        'cache_control': '',
        'cache_expires': 0,
        'public_methods': ['POST'],
        'public_item_methods': ['PUT'],
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PATCH', 'DELETE', 'PUT'],
        'auth_field': 'author',
        'schema':
            {
                'author':
                    {
                        'type': 'objectid',
                        'data_relation': {
                            'resource': 'users',
                            'field': '_id',
                            'embeddable': True
                        },
                        'required': True,
                        'empty': False
                    },
                'funny': {
                    'type': 'string',
                    'required': True,
                    'empty': False
                }
            }
    }
