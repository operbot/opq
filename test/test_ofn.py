# This file is placed in the Public Domain.


"object functions"


import unittest
import opq.ofn


class TestOfn(unittest.TestCase):

    def testdir(self):
        self.assertEqual(dir(opq.ofn), ["last", "save"])
