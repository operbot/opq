# This file is placed in the Public Domain.


from opq.dbs import Db
from opq.obj import format, keys
from opq.utl import elapsed, fntime
from opq.wdr import Wd


def __dir__():
    return (
            "fnd",
           )


__all__ = __dir__()


def fnd(event):
    if not event.args:
        res = ",".join(sorted([x.split(".")[-1].lower() for x in Wd.types()]))
        if res:
            event.reply(res)
        else:
            event.reply("no types yet.")
        return
    otype = event.args[0]
    nmr = 0
    keyz = None
    if event.gets:
        keyz = ",".join(keys(event.gets))
    if len(event.args) > 1:
        keyz += "," + ",".join(event.args[1:])
    for path, obj in Db.all(otype, event.gets):
        if not keyz:
            keyz = "," + ",".join(keys(obj))
        txt = "%s %s %s" % (
                         str(nmr),
                         format(obj, keyz),
                         elapsed(fntime(path))
                        )
        nmr += 1
        event.reply(txt)
    if not nmr:
        event.reply("no result (%s)" % event.txt)
