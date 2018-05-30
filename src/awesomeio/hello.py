from flask import current_app as app
from flask import abort, Response
import pymongo
import simplejson as json


def hello_endpoint():
    try:
        helloCollection = app.data.driver.db['_hello']
        lookup = {'foo': 'bar'}
        find = helloCollection.find_one(lookup)
        if (find):
            helloCollection.delete_one(lookup)
        else:
            helloCollection.insert_one(lookup)
        return json.dumps({"status": "up & running"})
    except (pymongo.errors.AutoReconnect, pymongo.errors.ServerSelectionTimeoutError):
        abort(Response(json.dumps({"status": "database is not available!"}), 500))
