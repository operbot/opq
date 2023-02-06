# This file is placed in the Public Domain.


"event"


import threading
import time


from ..default import Default
from ..objects import update


from .bus import Bus
from .parser import Parsed


def __dir__():
    return (
            'Event',
           ) 


__all__ = __dir__()


class Event(Default):

    __slots__ = ("__createtime__", "__parsed__", "__ready__", "__thr__")

    def __init__(self):
        Default.__init__(self)
        self.__createtime__ = time.time()
        self.__parsed__ = Parsed()
        self.__ready__ = threading.Event()
        self.__thr__ = None
        self.channel = ""
        self.orig = ""
        self.result = []
        self.txt = ""
        self.type = "event"

    def bot(self):
        return Bus.byorig(self.orig)

    def done(self, txt=None):
        text = "ok " + (txt or "")
        text = text.rstrip()
        Bus.say(self.orig, text, self.channel)

    def error(self):
        pass

    def parse(self, txt):
        self.__parsed__.parse(txt)
        update(self, self.__parsed__)

    def ready(self):
        self.__ready__.set()

    def reply(self, txt):
        self.result.append(txt)

    def show(self):
        for txt in self.result:
            Bus.say(self.orig, txt, self.channel)

    def wait(self):
        if self.__thr__:
            self.__thr__.join()
        self.__ready__.wait()
