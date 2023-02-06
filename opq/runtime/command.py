# This file is placed in the Public Domain.


"commands"


from ..objects import Object


def __dir__():
    return (
            'Command',
           )


__all__ = __dir__()
 

class Command(Object):

    cmds = Object()
    errors = []

    @staticmethod
    def add(cmd):
        setattr(Command.cmds, cmd.__name__, cmd)

    @staticmethod
    def dispatch(evt):
        if not evt.isparsed:
            evt.parse(evt.txt)
        func = getattr(Command.cmds, evt.cmd, None)
        if func:
            try:
                func(evt)
            except Exception as ex:
                exc = ex.with_traceback(ex.__traceback__)
                Command.errors.append(exc)
                evt.ready()
                return None
            evt.show()
        evt.ready()

    @staticmethod
    def remove(cmd):
        delattr(Command.cmds, cmd)
