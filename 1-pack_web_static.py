#!/usr/bin/python3
# generates a .tgz to a dir
""" Fabric script to deploy """
import os
from fabric.api import local
from datetime import datetime


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
