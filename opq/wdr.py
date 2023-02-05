# This file is placed in the Public Domain.


"working directory"


import os


def __dir__():
    return (
            'Wd',
           )


__all__ = __dir__()


class Wd:

    workdir = ".opq"

    @staticmethod
    def get():
        assert Wd.workdir
        return Wd.workdir

    @staticmethod
    def getpath(path):
        return os.path.join(Wd.get(), "store", path)

    @staticmethod
    def set(path):
        Wd.workdir = path

    @staticmethod
    def storedir():
        return os.path.join(Wd.get(), "store")

    @staticmethod
    def types(oname=None):
        res = []
        path = Wd.storedir()
        if not os.path.exists(path):
            return res
        for fnm in os.listdir(path):
            if oname and oname.lower() not in fnm.split(".")[-1].lower():
                continue
            if fnm not in res:
                res.append(fnm)
        return res
