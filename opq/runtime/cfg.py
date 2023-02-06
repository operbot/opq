# This file is placed in Public Domain.


"config"


from .prs import Parsed


def __dir__():
    return (
            'Config',
           ) 


__all__ = __dir__()


class Config(Parsed):

    pass
