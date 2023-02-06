# This file is placed in the Public Domain.


"scan"


import inspect


from opq.dbs import Classes
from opq.obj import Object


from .cmd import Commands


def __dir__():
    return (
            'scan',
            'scancls',
            'scancmd'
           )

__all__ = __dir__()


def scan(mod):
    scancls(mod)
    scancmd(mod)


def scancls(mod):
    for key, cls in inspect.getmembers(mod, inspect.isclass):
        if key.startswith("cb"):
            continue
        if issubclass(cls, Object):
            Classes.add(cls)


def scancmd(mod):
    for key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith("cb"):
            continue
        names = cmd.__code__.co_varnames
        if "event" in names:
            Commands.add(cmd)
