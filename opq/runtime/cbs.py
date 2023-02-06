# This file is placed in the Public Domain.


"callbacks"


from opq.objects import Object


from .thr import launch


def __dir__():
    return (
            'Callbacks',
           ) 


__all__ = __dir__()


class Callbacks(Object):

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
