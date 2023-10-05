def do_deploy(archive_path):
    """
    Distributing archive to the web server.
    """
    if os.path.isfile(archive_path) is False:
        return False

    archive = archive_path.split("/")[-1]
    extensionLess = archive.split(".")[0]

    if put(archive_path, "/tmp/{}".format(archive)).failed is True:
        return False

    if run("mkdir /data/web_static/releases/{}/".
           format(extensionLess)).failed is True:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(archive, extensionLess)).failed is True:
        return False

    if run("rm /tmp/{}".format(archive)).failed is True:
        return False

    if run("rm -rf /data/web_static/current/").failed is True:
        return False

    if run("mkdir /data/web_static/current/").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current/"
           .format(extensionLess)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".
           format(extensionLess)).failed is True:
        return False
    return True
