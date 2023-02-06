# This file is placed in the Public Domain.


"json"


import json
import _thread


from .obj import Object, update
from .utl import cdir, locked


def __dir__():
    return (
            'ObjectDecoder',
            'ObjectEncoder',
            'dump',
            'dumps',
            'load',
            'loads'
           )

__all__ = __dir__()


disklock = _thread.allocate_lock()


class ObjectDecoder(json.JSONDecoder):


    def decode(self, s, _w=None):
        value = json.loads(s)
        return Object(value)


class ObjectEncoder(json.JSONEncoder):


    def default(self, o):
        if isinstance(o, dict):
            return o.items()
        if isinstance(o, Object):
            return vars(o)
        if isinstance(o, list):
            return iter(o)
        if isinstance(o,
                      (type(str), type(True), type(False),
                       type(int), type(float))
                     ):
            return str(o)
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)


@locked(disklock)
def dump(obj, opath):
    cdir(opath)
    with open(opath, "w", encoding="utf-8") as ofile:
        json.dump(
            obj.__dict__, ofile, cls=ObjectEncoder, indent=4, sort_keys=True
        )
    return opath


def dumps(self):
    return json.dumps(self, cls=ObjectEncoder)


@locked(disklock)
def load(obj, opath):
    with open(opath, "r", encoding="utf-8") as ofile:
        res = json.load(ofile, cls=ObjectDecoder)
        update(obj, res)


def loads(jsonstr):
    return json.loads(jsonstr, cls=ObjectDecoder)
