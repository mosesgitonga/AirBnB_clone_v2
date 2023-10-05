#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from
 the contents of the web_static folder of my AirBnB 
 Clone repo, using the function do_pack"""

from fabric import Connection, task
#from collections.abc import Mapping
from datetime import datetime

@task
def do_pack(c):
    """do_pack func to pack files in web_static"""

    web_static_path = "/home/user/alx/AirBnB_clone_v2"

    archive_path = "/home/user/alx/AirBnB_clone_v2/versions"
    now = datetime.now()

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H") 
    minute =  now.strftime("%M")
    sec = now.strftime("%S")
    archive_name = (f"web_static_{year}{month}{day}{hour}{minute}{sec}.tgz")

    c.local(f"tar -czvf {archive_path}/{archive_name} -C {web_static_path} .")