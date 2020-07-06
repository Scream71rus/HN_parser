
from handlers.base_handler import BaseHandler
from models.hacker_news import HackerNewsModel


class HackerNewsHandler(BaseHandler):

    async def get(self):
        default_order = ['title', 'created']

        limit = self.get_query_argument('limit', '')
        offset = self.get_query_argument('offset', '')
        order = self.get_query_argument('order', '')
        order_type = self.get_query_argument('order_type', '')

        queries = {
            'limit': limit if limit.isdigit() else 5,
            'offset': offset if offset.isdigit() else None,
            'order': order if order in default_order else 'created',
            'order_type': order_type if order_type == 'asc' else 'desc'
        }

        post_list = await HackerNewsModel.get_list(**queries)
        self.response(post_list)
