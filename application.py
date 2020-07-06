
import asyncpg

import tornado.web
from tornado.options import options
from tornado.ioloop import IOLoop
from models.base_model import BaseModel
from workers.hacker_news_parser import HackerNewsParser


class Application(tornado.web.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        IOLoop.current().spawn_callback(self.connect_to_db)

        hacker_news_parser = HackerNewsParser(self)
        tornado.ioloop.IOLoop.current().spawn_callback(hacker_news_parser.run)

    async def connect_to_db(self):
        BaseModel.db = await asyncpg.connect(database=options.db_name,
                                             user=options.db_user,
                                             password=options.db_password,
                                             host=options.db_host)
