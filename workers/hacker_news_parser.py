
from bs4 import BeautifulSoup
from tornado.gen import sleep
from tornado.options import options
from asyncpg.exceptions import UniqueViolationError

from models.hacker_news import HackerNewsModel
from workers.base_parser_worker import BaseParser


class HackerNewsParser(BaseParser):

    async def parse_hacker_news(self, url, page_count=1):

        for page_number in range(page_count):
            url_with_pagination = url + 'p={}'.format(page_number + 1)

            html = await self.get_html(url_with_pagination)
            html = BeautifulSoup(html, 'html.parser')

            for tr in html.select('.athing'):
                try:
                    await HackerNewsModel.create({
                        'title': tr.select('.storylink')[0].text,
                        'link': tr.select('.storylink')[0].get('href')
                    })

                except UniqueViolationError:
                    pass

                except Exception as ex:
                    print(ex)

    async def run(self):
        while True:
            await self.parse_hacker_news(options.hacker_news_url)

            await sleep(60 * 30)
