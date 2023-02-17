# This file is placed in the Public Domain.


import unittest


from opq.decoder import loads
from opq.encoder import dumps
from opq.objects import Object


class TestDecoder(unittest.TestCase):

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")

