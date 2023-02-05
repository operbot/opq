# This file is placed in the Public Domain.


"persist"


import os
import unittest


from opq.obj import Object
from opq.pst import Persist, last, save
from opq.dbs import Wd


class TestPersist(unittest.TestCase):

    def test_constructor(self):
        obj = Persist()
        self.assertTrue(type(obj), Persist)

    def test__class(self):
        obj = Persist()
        clz = obj.__class__()
        self.assertTrue("Persist" in str(type(clz)))

    def test_save(self):
        Wd.workdir = ".test"
        obj = Persist()
        path = save(obj)
        self.assertTrue(os.path.exists(os.path.join(Wd.workdir, "store", path)))
