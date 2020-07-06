
from tornado.options import define, options, parse_config_file
import tornado.web

from application import Application
import urls


define("port", type=int)
define("db_name", type=str)
define("db_user", type=str)
define("db_password", type=str)
define("db_host", type=str)
define("db_port", type=str)
define("size_db_connection_pool", type=int)

define("hacker_news_url", type=str)

define("debug", type=str)

parse_config_file("application.conf")
tornado.options.parse_command_line()


if __name__ == "__main__":
    application = Application(
        urls.urls,
        debug=options.debug == "yes")

    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
