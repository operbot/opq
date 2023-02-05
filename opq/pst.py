# This file is placed in the Public Domain.


"persist"


import datetime
import os
import uuid
import _thread


from .jsn import dump
from .obj import Object, kind
from .utl import cdir, locked
from .wdr import Wd


def __dir__():
    return (
            'Persist',
            'last',
            'save'
           ) 


__all__ = __dir__()


class Persist(Object):

    __slots__ = ('__oid__')

    def __init__(self, *args, **kwargs):
        Object.__init__(self, *args, **kwargs)
        self. __oid__ = os.path.join(
                                    kind(self),
                                    str(uuid.uuid4().hex),
                                    os.sep.join(str(datetime.datetime.now()).split()),
                                   )


def last(obj, selector=None):
    if selector is None:
        selector = {}
    ooo = Db.last(kind(obj), selector)
    if ooo:
        update(obj, ooo)
        obj.__oid__ = ooo.__oid__


def save(obj):
    opath = Wd.getpath(obj.__oid__)
    dump(obj, opath)
    return obj.__oid__
