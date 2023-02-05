# This file is placed in the Public Domain.


"functions"


from .dbs import Db
from .jsn import dump
from .obj import kind, update
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
    ooo = Db.last(kind(obj), selector)
    if ooo:
        update(obj, ooo)
        obj.__oid__ = ooo.__oid__


def save(obj):
    opath = Wd.getpath(obj.__oid__)
    dump(obj, opath)
    return obj.__oid__
