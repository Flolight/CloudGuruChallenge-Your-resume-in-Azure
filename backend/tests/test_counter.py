import unittest

import azure.functions as func
from GetCounter import main

class TestCounter(unittest.TestCase):
    def test_counter(self):
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/getcounter')
        resp = main(req)

        self.assertEqual(resp.get_body(), 2)