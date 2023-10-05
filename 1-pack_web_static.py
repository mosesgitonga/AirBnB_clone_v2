#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from the contents of the
 web_static folder of your AirBnB Clone repo, using the function do_pack"""

from fabric.api import local
# from collections.abc import Mapping
from datetime import datetime


def do_pack():
    """do_pack func to pack files in web_static"""
    try:
        local("mkdir -p versions")
        now = datetime.now()

        year = now.year
        month = now.month
        day = now.strftime("%d")
        hour = now.hour
        minute = now.day
        sec = now.second
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
                year, month, day, hour, minute, sec
                )
        local("tar -czvf versions/{} web_static").format(archive_name)
        return "versions/{}".format(archive_name)
    except Exception as e:
        print(f"{}".format(e))
        