#!/usr/bin/python3
# delete out of date archives
import os
from fabric.api import *

env.hosts = ['3.91.55.160', '54.147.16.57']


def do_clean(number=0):
    number = 1 if int(number) == 0 else int(number)
    arch = sorted(os.listdir("versions"))
    [arch.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arch]

    with cd("/data/web_static/releases"):
        arch = run("ls -tr").split()
        arch = [a for a in arch if "web_static_" in a]
        [arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arch]
