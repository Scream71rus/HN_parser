
import json

from tornado.testing import AsyncTestCase
from tornado.testing import AsyncHTTPClient
import tornado.testing


class HackerNewsTest(AsyncTestCase):

    def get_body(self, body):
        return json.loads(body.decode())

    @tornado.testing.gen_test
    def test_get_without_query(self):
        client = AsyncHTTPClient()
        response = yield client.fetch("http://localhost:9090/post")
        self.assertIn(response.code, (200, 201))

    @tornado.testing.gen_test
    def test_get_with_query(self):
        client = AsyncHTTPClient()

        query = "limit=7&offset=1&order=title&order_by=desc"

        response = yield client.fetch("http://localhost:9090/post?{}".format(query))
        self.assertIn(response.code, (200, 201))
        self.assertIn(len(self.get_body(response.body)), (7,), msg='response len != set limit in query')

    @tornado.testing.gen_test
    def test_get_with_bad_query(self):
        client = AsyncHTTPClient()

        query = "limit=-5&offset=qwe&order=1&order_by=1"

        response = yield client.fetch("http://localhost:9090/post?{}".format(query))
        self.assertIn(response.code, (200, 201))


if __name__ == '__main__':

    tornado.testing.main()
