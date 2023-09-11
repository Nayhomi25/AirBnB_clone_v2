#!/usr/bin/python3
"""
Script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import *
import os.path
from datetime import datetime

env.hosts = ["18.233.62.178", "174.129.55.177"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

run_locally = True


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    result = local("tar -czvf {} web_static".format(archive_name))
    if result.succeeded:
        return archive_name
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    local("cp {} /tmp/{}".format(archive_path, file))
    local(
        "rm -rf /data/web_static/releases/{}/"
        .format(name))
    local(
        "mkdir -p /data/web_static/releases/{}/"
        .format(name))
    local(
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(file, name))
    local("rm /tmp/{}".format(file))
    local(
        "mv /data/web_static/releases/{}/web_static/*"
        " /data/web_static/releases/{}/"
        .format(name, name))
    local(
        "rm -rf /data/web_static/releases/{}/web_static"
        .format(name))
    local("rm -rf /data/web_static/current")
    local(
        "ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(name))

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/"
           .format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/"
           .format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
           .format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
           .format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
           .format(name)).failed is True:
        return False

    print("New version deployed!")
    return True


def deploy():
    """creates and distributes an archive to the web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
