# This file is placed in the Public Domain.


from opq.objects import keys, tostr
from opq.utility import elapsed, fntime


from modules.storage import Storage, find


def __dir__():
    return (
            'fnd',
           )


__all__ = __dir__()


def fnd(event):
    if not event.args:
        res = ','.join(sorted([x.split('.')[-1].lower() for x in Storage.files()]))
        if res:
            event.reply(res)
        else:
            event.reply('no types yet.')
        return
    otype = event.args[0]
    nmr = 0
    keyz = None
    if event.gets:
        keyz = ','.join(keys(event.gets))
    if len(event.args) > 1:
        keyz += ',' + ','.join(event.args[1:])
    for path, obj in find(otype, event.gets):
        if not keyz:
            keyz = ',' + ','.join(keys(obj))
        txt = '%s %s %s' % (
                         str(nmr),
                         tostr(obj, keyz),
                         elapsed(fntime(path))
                        )
        nmr += 1
        event.reply(txt)
    if not nmr:
        event.reply('no result (%s)' % event.txt)
