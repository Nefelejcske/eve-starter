from awesomeio.domains import domain


@domain()
class Users(object):
    name = "users"
    domain = {
        'item_title': 'users',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
                'empty': False
            }
        }
    }
