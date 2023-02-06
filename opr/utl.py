# This file is placed in the Public Domain.


"utilitites"


import getpass
import os
import pwd
import time


def __dir__():
    return (
            'privileges',
            'spl',
            'wait'
           )


__all__ = __dir__()


def privileges(username):
    if os.getuid() != 0:
        return
    try:
        pwnam = pwd.getpwnam(username)
    except KeyError:
        username = getpass.getuser()
        pwnam = pwd.getpwnam(username)
    os.setgroups([])
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)


def spl(txt):
    try:
        res = txt.split(",")
    except (TypeError, ValueError):
        res = txt
    return [x for x in res if x]


def wait(func=None):
    while 1:
        time.sleep(1.0)
        if func:
            func()
