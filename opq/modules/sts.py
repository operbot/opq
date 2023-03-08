# This file is placed in the Public Domain.


"status"


from operbot.listens import Listens
from operbot.objects import tostr


def sts(event):
    for bot in Listens.objs:
        if "state" in dir(bot):
            event.reply(tostr(bot.state, skip="lastline"))
