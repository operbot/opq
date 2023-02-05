# This file is placed in the Public Domain.


"utilities"


import unittest
import opq.utl


ATTRIBUTES = [
              'cdir',
              'elapsed',
              'fnclass',
              'fntime',
              'locked',
              'name',
              'spl',
             ]


class TestUtilities(unittest.TestCase):

    def testdir(self):
        self.assertEqual(dir(opq.utl), ATTRIBUTES)
