# This file is placed in the Public Domain.


"handler"


import queue
import threading


from .bus import Bus
from .cbs import Callbacks
from .cmd import Commands
from .thr import launch


def __dir__():
    return (
            'Handler',
           )


__all__ = __dir__()


class Handler(Callbacks):

    def __init__(self):
        Callbacks.__init__(self)
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.stopped.clear()
        self.register("event", Commands.dispatch)
        self.register("command", Commands.dispatch)
        Bus.add(self)

    def handle(self, event):
        if not event.orig:
            event.orig = repr(self)
        Callbacks.dispatch(self, event)

    def loop(self):
        while not self.stopped.set():
            self.handle(self.poll())

    def poll(self):
        return self.queue.get()

    def put(self, event):
        if not event.orig:
            event.orig = repr(self)
        self.queue.put_nowait(event)

    def stop(self):
        self.stopped.set()

    def start(self):
        self.stopped.clear()
        launch(self.loop)
