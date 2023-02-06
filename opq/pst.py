# This file is placed in the Public Domain.


"persist"



from .dbs import Db
from .jsn import dump
from .obj import kind, oid, update
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
    _fn, ooo = Db.last(kind(obj), selector)
    if ooo:
        update(obj, ooo)


def save(obj):
    opath = Wd.getpath(oid(obj))
    dump(obj, opath)
    return opath
