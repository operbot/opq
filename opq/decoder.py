# This file is placed in the Public Domain.


'decoder'


import json


from .objects import Object, olock
from .utility import locked


def __dir__():
    return (
            'ObjectDecoder',
            'diskloader',
            'loads'
           )


class ObjectDecoder(json.JSONDecoder):


    def decode(self, s, _w=None):
        value = json.loads(s)
        return Object(value)



def loads(s, *args, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    return json.loads(
                      s,
                      *args,
                      cls=cls or ObjectDecoder,
                      parse_float=parse_float,
                      parse_int=parse_int,
                      parse_constant=parse_constant,
                      object_pairs_hook=object_pairs_hook,
                      **kw
                     )
