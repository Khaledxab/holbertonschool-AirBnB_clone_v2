#!/usr/bin/python3
""" BASED on TASK1 / Fabric script deploy archive to web server"""
from fabric.api import env
from fabric.api import put
from fabric.api import run
from os import path


env.hosts = ['3.91.55.160', '54.147.16.57']
env.user = "ubuntu"


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
