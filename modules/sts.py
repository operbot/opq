# This file is placed in the Public Domain.


"status"


from opq.listens import Listens
from opq.objects import tostr


def sts(event):
    for bot in Listens.objs:
        if "state" in dir(bot):
            event.reply(tostr(bot.state, skip="lastline"))
