# This file is placed in the Public Domain.


"callbacks"


from ..objects import Object


from .thread import launch


def __dir__():
    return (
            'Callback',
           ) 


__all__ = __dir__()


class Callback(Object):

    def __init__(self):
        Object.__init__(self)
        self.cbs = Object()
        self.errors = []

    def register(self, typ, cbs):
        if typ not in self.cbs:
            setattr(self.cbs, typ, cbs)

    def dispatch(self, event):
        func = getattr(self.cbs, event.type, None)
        if not func:
            event.ready()
            return
        event.__thr__ = launch(func, event)

    def get(self, typ):
        return getattr(self.cbs.get, typ, None)
