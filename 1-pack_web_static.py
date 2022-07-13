#!/usr/bin/python3
"""generate .tgz archive"""
from fabric.api import local
from datetime import datetime
from os import path


def do_pack():
    """[generates a .tgz archive]
    """
    timeF = '%Y%m%d%H%M%S'
    time = datetime.utcnow().strftime(timeF)
    file = "versions/web_static_{}.tgz".format(time)
    """fab commands"""
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(filepath))
    """############"""
    if path.exists(file):
        return file
    else:
        return None
