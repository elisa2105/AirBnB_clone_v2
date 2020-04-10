#!/usr/bin/python3
# full deploy
""" Fabric script to deploy """
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['104.196.193.253', '54.221.57.153']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"
env.warn_only = True


def deploy():
    """ full deploy """
    pathF = do_pack()
    if os.path.exists(pathF):
        deployed = do_deploy(pathF)
        return deployed
    else:
        return False


def do_pack():
    timeF = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_" + timeF + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + path + " web_static")
    if os.path.exists(path):
        size = os.path.getsize(path)
        return path
    else:
        return None


def do_deploy(archive_path):
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
    try:
        filename = os.path.splitext(os.path.basename(archive_path))[0]
        put(local_path=archive_path, remote_path="/tmp")
        run("mkdir -p /data/web_static/releases/" + filename + "/")
        run("sudo tar -xzf /tmp/" + filename + ".tgz" +
            " -C /data/web_static/releases/" + filename + "/")
        run("rm /tmp/" + filename + ".tgz")
        run("mv /data/web_static/releases/" + filename +
            "/web_static/* /data/web_static/releases/" + filename + "/")
        run("rm -rf /data/web_static/releases/" + filename +
            "/web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/" + filename +
            "/ /data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False
