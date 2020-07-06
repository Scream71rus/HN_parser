
from models.base_model import BaseModel


class HackerNewsModel(BaseModel):

    @classmethod
    async def get_list(cls, order, order_type, limit=None, offset=None):
        sql = "select * from hn_parser.hacker_news order by {} {}".format(order, order_type)

        if offset:
            sql = sql + ' offset {}'.format(offset)
        if limit:
            sql = sql + ' limit {}'.format(limit)

        cursor = await cls.db.fetch(sql)
        return cursor

    @classmethod
    async def create(cls, data):
        sql = "insert into hn_parser.hacker_news(title, link) values($1, $2) returning id"
        cursor = await cls.db.fetchval(sql, data.get('title'), data.get('link'))
        data['id'] = cursor
        return data
