# This file is placed in the Public Domain.


from opq.listens import Listens
from opq.objects import kind


def __dir__():
    return (
            'flt',
           )


__all__ = __dir__()


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(Listens.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(' | '.join([kind(o, True) for o in Listens.objs]))
