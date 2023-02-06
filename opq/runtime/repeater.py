# This file is placed in the Public Domain.


"repeater"


from .thread import launch
from .timer import Timer


def __dir__():
    return (
            'Repeater',
           )


__all__ = __dir__()


class Repeater(Timer):

    def run(self):
        thr = launch(self.start)
        super().run()
        return thr
