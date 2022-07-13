#!/usr/bin/python3
"""[Fabric script]
"""
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import local
from datetime import datetime
from os import path

env.hosts = ['3.91.55.160', '54.147.16.57']
env.user = "ubuntu"


def do_pack():
    """.tgz archive do"""
    timeF = '%Y%m%d%H%M%S'
    time = datetime.utcnow().strftime(timeF)
    file = "versions/web_static_{}.tgz".format(time)
    """fab commands"""
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(file))
    """############"""
    if path.exists(file):
        return file
    else:
        return None


def do_deploy(archive_path):
    """deploy archive to web serve"""
    if not path.exists(archive_path) and path.isfile(archive_path):
        return False
    file = archive_path.split("/")[-1].split(".")[0]
    path1 = "/data/web_static/releases/{}/web_static/*".format(file)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(file))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
            format(file, file))
        run("sudo rm /tmp/{}.tgz".format(file))
        run("sudo mv {} /data/web_static/releases/{}/".format(path1, file))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".
            format(file))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(file))
        return True
    except BaseException:
        return False


def deploy():
    """full deploy"""
    filepath = do_pack()
    if filepath is None:
        return False
    else:
        return do_deploy(filepath)
