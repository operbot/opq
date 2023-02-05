# This file is placed in the Public Domain.


"classes"


def __dir__():
    return (
            'Classes',
           )


__all__ = __dir__()
 

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
