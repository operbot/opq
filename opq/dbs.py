# This file is placed in the Public Domain.


"database"


import os
import _thread


from .jsn import load
from .obj import Object, search
from .utl import fnclass, fntime
from .wdr import Wd


def __dir__():
    return (
            'Classes',
            'Db',
            'load',
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
    def all(otp, selector=None):
        names = Wd.types(otp)
        for nme in names:
            for obj in Db.find(nme, selector):
                yield obj

    @staticmethod
    def find(otp, selector=None):
        if selector is None:
            selector = {}
        for fnm in Db.fns(otp):
            obj = Db.hook(fnm)
            if "__deleted__" in obj and obj.__deleted__:
                continue
            if selector and not search(obj, selector):
                continue
            yield fnm, obj

    @staticmethod
    def fns(otp):
        assert Wd.workdir
        path = os.path.join(Wd.workdir, "store", otp) + os.sep
        dname = ""
        for rootdir, dirs, _files in os.walk(path, topdown=False):
            if dirs:
                dname = sorted(dirs)[-1]
                if dname.count("-") == 2:
                    ddd = os.path.join(rootdir, dname)
                    fls = sorted(os.listdir(ddd))
                    if fls:
                        path2 = os.path.join(ddd, fls[-1])
                        yield path2

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
    def last(otp, selector=None):
        res = sorted(
                     Db.find(otp, selector),
                     key=lambda x: fntime(x[0])
                    )
        if res:
            return res[-1]
        return None, None

    @staticmethod
    def match(otp, selector=None):
        names = Wd.types(otp)
        for nme in names:
            item = Db.last(nme, selector)
            if item:
                return item
        return None, None


Classes.add(Object)
