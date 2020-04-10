#!/usr/bin/python3
# deploy a file into the web servers Airbnb clone
""" Fabric script to deploy """
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['104.196.193.253', '54.221.57.153']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"
env.warn_only = True


def do_deploy(archive_path):
    """ deploy servers """
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
