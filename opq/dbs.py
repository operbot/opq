# This file is placed in the Public Domain.


"database"


import json
import os
import _thread


from .jsn import ObjectDecoder, ObjectEncoder
from .obj import kind, search, update
from .utl import cdir, fnclass, fntime, locked
from .wdr import Wd



def __dir__():
    return (
            'Classes',
            'Db',
            'dump',
            'last',
            'load',
            'save'
           )


__all__ = __dir__()



disklock = _thread.allocate_lock()


class Classes:

    cls = {}

    @staticmethod
    def add(clz):
        Classes.cls["%s.%s" % (clz.__module__, clz.__name__)] =  clz

    @staticmethod
    def all(oname=None):
        res = []
        for key, value in Classes.cls.items():
            if oname is not None and oname not in key:
                continue
            res.append(value)
        return res

    @staticmethod
    def get(oname):
        return Classes.cls.get(oname, None)


    @staticmethod
    def remove(oname):
        del Classes.cls[oname]


class Db:

    @staticmethod
    def all(otp, selector=None, index=None, timed=None, deleted=True):
        names = Wd.types(otp)
        result = []
        for nme in names:
            res = Db.find(nme, selector, index, timed, deleted)
            result.extend(res)
        return sorted(result, key=lambda x: fntime(x.__oid__))

    @staticmethod
    def find(otp, selector=None, index=None, timed=None, deleted=True):
        if selector is None:
            selector = {}
        nmr = -1
        res = []
        for fnm in Db.fns(otp, timed):
            obj = Db.hook(fnm)
            if deleted and "__deleted__" in obj and obj.__deleted__:
                continue
            if selector and not search(obj, selector):
                continue
            nmr += 1
            if index is not None and nmr != index:
                continue
            res.append(obj)
        return res

    @staticmethod
    def fns(otp, timed=None):
        if not otp:
            return []
        assert Wd.workdir
        path = os.path.join(Wd.workdir, "store", otp) + os.sep
        res = []
        dname = ""
        for rootdir, dirs, _files in os.walk(path, topdown=False):
            if dirs:
                dname = sorted(dirs)[-1]
                if dname.count("-") == 2:
                    ddd = os.path.join(rootdir, dname)
                    fls = sorted(os.listdir(ddd))
                    if fls:
                        path2 = os.path.join(ddd, fls[-1])
                        if (
                            timed
                            and "from" in timed
                            and timed["from"]
                            and fntime(path2) < timed["from"]
                        ):
                            continue
                        if timed and timed.to and fntime(path2) > timed.to:
                            continue
                        res.append(path2)
        return sorted(res)

    @staticmethod
    def hook(otp):
        fqn = fnclass(otp)
        cls = Classes.get(fqn)
        if not cls:
            cls = Classes.all("Object")[-1]
        obj = cls()
        load(obj, otp)
        return obj

    @staticmethod
    def last(otp, selector=None, index=None, timed=None):
        res = sorted(
                     Db.find(otp, selector, index, timed),
                     key=lambda x: fntime(x.__oid__)
                    )
        if res:
            return res[-1]
        return None

    @staticmethod
    def match(otp, selector=None):
        names = Wd.types(otp)
        for nme in names:
            item = Db.last(nme, selector)
            if item:
                return item
        return None
