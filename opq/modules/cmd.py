# This file is placed in the Public Domain.


from opq.handler import Handler


def __dir__():
    return (
            'cmd',
           )


__all__ = __dir__()


def cmd(event):
    event.reply(",".join(sorted(Handler.cmds)))
