# This file is placed in the Public Domain.


import unittest


from opq.storage import Wd


class TestWorkingDirectory(unittest.TestCase):

    def testconstructor(self):
        wdr = Wd()
        self.assertEqual(type(wdr), Wd)
