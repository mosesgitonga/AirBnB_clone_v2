#!/usr/bin/python3
# a Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import local
from datetime import datetime


def do_pack():
    """do_pack func to pack files in web_static"""
    try:
        local("mkdir -p versions")
        now = datetime.now()
        
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
                now.year, now.month, now.day, now.hour, now.minute, now.second)

        local("tar -czvf versions/{} web_static").format(archive_name)

        return "versions/{}".format(archive_name)
    except Exception:
        return None
