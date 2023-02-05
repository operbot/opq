# This file is placed in the Public Domain.


import unittest


from opq.dft import Default


class TestEvent(unittest.TestCase):

    def testconstructor(self):
        dft = Default()
        self.assertEqual(type(dft), Default)
