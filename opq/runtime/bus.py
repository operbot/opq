# This file is placed in the Public Domain.


"bus"


from ..objects import Object


def __dir__():
    return (
            'Bus',
           ) 


__all__ = __dir__()


class Bus(Object):

    objs = []

    @staticmethod
    def add(obj):
        if repr(obj) not in [repr(x) for x in Bus.objs]:
            Bus.objs.append(obj)

    @staticmethod
    def announce(txt):
        for obj in Bus.objs:
            obj.announce(txt)

    @staticmethod
    def byorig(orig):
        res = None
        for obj in Bus.objs:
            if repr(obj) == orig:
                res = obj
                break
        return res

    @staticmethod
    def say(orig, txt, channel=None):
        bot = Bus.byorig(orig)
        if bot:
            if channel:
                bot.say(channel, txt)
            else:
                bot.raw(txt)
