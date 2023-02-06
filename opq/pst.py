# This file is placed in the Public Domain.


"persist"


import datetime
import os
import uuid
import _thread


from .dbs import Db
from .jsn import dump
from .obj import Object, kind, oid, update
from .utl import cdir, locked
from .wdr import Wd


def __dir__():
    return (
            'last',
            'save'
           ) 


__all__ = __dir__()


def last(obj, selector=None):
    if selector is None:
        selector = {}
    fn, ooo = Db.last(kind(obj), selector)
    if ooo:
        update(obj, ooo)


def save(obj):
    opath = Wd.getpath(oid(obj))
    dump(obj, opath)
    return opath
