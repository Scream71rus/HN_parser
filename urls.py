
from handlers.hacker_news_handler import HackerNewsHandler

urls = [
    (r'/posts?', HackerNewsHandler,),
]
