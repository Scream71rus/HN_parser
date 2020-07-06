
from tornado.httpclient import AsyncHTTPClient


class BaseParser:
    @property
    def application(self):
        return self._application

    def __init__(self, application=None):
        self._application = application

    async def get_html(self, url):
        httpclient = AsyncHTTPClient()
        response = await httpclient.fetch(url)

        return response.body.decode(errors="ignore")

