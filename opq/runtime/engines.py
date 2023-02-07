# This file is placed in the Public Domain


"engine"


from multiprocessing import Pool, Process


def __dir__():
    return (
            "Engine".
            "launch"
           ) 


class Engine(Pool):

    pass


def __dir__():
    return (
            "launch",
           ) 


def launch(func, *args):
    p = Process(target=f, args=args)
    p.start()
    return p
