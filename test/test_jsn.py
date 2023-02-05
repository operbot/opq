# This file is placed in the Public Domain.


import unittest


from opq.obj import Object
from opq.jsn import dumps, loads


VALIDJSON = '{"test": "bla"}'


class TestJSON(unittest.TestCase):

    def test_json(self):
        obj = Object()
        obj.test = "bla"
        res = loads(dumps(obj))
        self.assertEqual(res.test, "bla")

    def test_jsondump(self):
        obj = Object()
        obj.test = "bla"
        self.assertEqual(dumps(obj), VALIDJSON)
