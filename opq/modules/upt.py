# This file is placed in the Public Domain.


import time


from opq.handler import starttime


def __dir__():
    return (
            'upt'
           )


__all__ = __dir__()


def upt(event):
    event.reply(elapsed(time.time()-starttime))
