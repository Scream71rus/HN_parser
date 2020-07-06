
import datetime
import json
from asyncpg import Record

class ObjectEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Record):
            return dict(o)

        if isinstance(o, datetime.datetime):
            return datetime.datetime.strftime(o, "%Y-%m-%d %H:%M")

        if isinstance(o, datetime.date):
            return datetime.datetime.strftime(o, "%Y-%m-%d")

        return json.JSONEncoder.default(self, o)
