# This file is placed in Public Domain.


"config"


from .parser import Parsed


def __dir__():
    return (
            'Config',
           ) 


__all__ = __dir__()


class Config(Parsed):

    pass
