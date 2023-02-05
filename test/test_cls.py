# This file is placed in the Public Domain.


"classes"


import unittest


from opq.cls import Classes


class TestClasses(unittest.TestCase):

    def testconstructor(self):
        cls = Classes()
        self.assertEqual(type(cls), Classes)
