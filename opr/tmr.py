# This file is placed in the Public Domain.


"timer"


import threading
import time


from opq.objects import Object
from opq.utility import name


from .thr import launch


def __dir__():
    return (
            'Timer',
           )


__all__ = __dir__()


class Timer:

    def __init__(self, sleep, func, *args, thrname=None):
        super().__init__()
        self.args = args
        self.func = func
        self.sleep = sleep
        self.name = thrname or name(self.func)
        self.state = Object
        self.timer = None

    def run(self):
        self.state.latest = time.time()
        launch(self.func, *self.args)

    def start(self):
        timer = threading.Timer(self.sleep, self.run)
        timer.name = self.name
        timer.daemon = True
        timer.sleep = self.sleep
        timer.state = self.state
        timer.state.starttime = time.time()
        timer.state.latest = time.time()
        timer.func = self.func
        timer.start()
        self.timer = timer
        return timer

    def stop(self):
        if self.timer:
            self.timer.cancel()
