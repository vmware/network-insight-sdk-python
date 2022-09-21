import traceback
from json import JSONEncoder

from mongoengine.base import BaseDocument

"""
This class is utlility class for mongo services.
"""


class MongoEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseDocument):
            data = o.to_mongo()
            # might not be present if EmbeddedDocument
            o_id = data.pop('_id', None)
            if o_id:
                data['id'] = str(o_id)
            data.pop('_cls', None)
            return data
        else:
            return JSONEncoder.default(self, o)


class MandatoryParameterMissing(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


