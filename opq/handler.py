# This file is placed in the Public Domain.


import inspect
import queue
import threading


from .listens import Listens
from .objects import Object, register, update
from .message import Message
from .threads import launch


def __dir__():
    return (
            "Handler",
            'clone',
            'command',
            'dispatch',
            'parse_cli',
            'scan'
           ) 


__all__ = __dir__()


class Handler(Object):

    cmds = Object()
    errors = []

    def __init__(self):
        Object.__init__(self)
        self.cbs = Object()
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.register("command", dispatch)
        Listens.add(self)

    def handle(self, event):
        func = getattr(self.cbs, event.type, None)
        if not func:
            event.ready()
            return
        event.__thr__ = launch(func, event)

    def loop(self):
        while not self.stopped.set():
            self.handle(self.poll())

    def poll(self):
        return self.queue.get()

    def put(self,event):
        if not event.orig:
            event.orig = repr(self)
        self.queue.put_nowait(event)

    def register(self, typ, cbs):
        setattr(self.cbs, typ, cbs)

    def restart(self):
        self.stop()
        self.start()

    def stop(self):
        self.stopped.set()

    def start(self):
        self.stopped.clear()
        launch(self.loop)


def clone(obj, other):
    update(obj.cmds, other.cmds)


def command(cli, txt):
    e = Message()
    e.parse(txt)
    e.orig = repr(cli)
    dispatch(e)
    return e


def dispatch(event):
    if not event.isparsed:
        event.parse(event.txt)
    func = getattr(Handler.cmds, event.cmd, None)
    if func:
        try:
            func(event)
        except Exception as ex:
            exc = ex.with_traceback(ex.__traceback__)
            Handler.errors.append(exc)
            event.ready()
            return None
        event.show()
    event.ready()


def parse_cli(txt):
    e = Message()
    e.type = "command"
    e.parse(txt)
    return e


def scan(mod):
    for key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith("cb"):
            continue
        names = cmd.__code__.co_varnames
        if "event" in names:
            register(Handler.cmds, key, cmd)
