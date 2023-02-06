# This file is placed in the Public Domain.


"persist"


import os
import unittest


from opq.obj import Object
from opq.pst import last, save
from opq.dbs import Wd


class TestPersist(unittest.TestCase):


    def test_save(self):
        Wd.workdir = ".test"
        obj = Persist()
        path = save(obj)
        self.assertTrue(os.path.exists(os.path.join(Wd.workdir, "store", path)))
