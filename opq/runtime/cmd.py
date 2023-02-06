# This file is placed in the Public Domain.


"commands"


from opq.objects import Object


def __dir__():
    return (
            'Commands',
           )


__all__ = __dir__()
 

class Commands(Object):

    cmds = Object()
    errors = []

    @staticmethod
    def add(cmd):
        setattr(Commands.cmds, cmd.__name__, cmd)

    @staticmethod
    def dispatch(evt):
        if not evt.isparsed:
            evt.parse(evt.txt)
        func = getattr(Commands.cmds, evt.cmd, None)
        if func:
            try:
                func(evt)
            except Exception as ex:
                exc = ex.with_traceback(ex.__traceback__)
                Commands.errors.append(exc)
                evt.ready()
                return None
            evt.show()
        evt.ready()

    @staticmethod
    def remove(cmd):
        delattr(Commands.cmds, cmd)
