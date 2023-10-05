#!/usr/bin/env python3
#a Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack

from fabric,api import Connection, task, local
#from collections.abc import Mapping
from datetime import datetime

@task
def do_pack(c):
    """do_pack func to pack files in web_static"""

    local("mkdir -p versions")
    now = datetime.now()

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H") 
    minute =  now.strftime("%M")
    sec = now.strftime("%S")
    archive_name = (f"web_static_{year}{month}{day}{hour}{minute}{sec}.tgz")

    local(f"tar -czvf versions/{archive_name} web_static .")
    return f"versions/{archive_name}"
