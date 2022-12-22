#!/usr/bin/python3
""" Fabric script that distributes an archive to 2 web servers """

from fabric.api import env, put, run
import os.path


env.hosts = ['18.234.106.217', '100.25.30.148']


def do_deploy(archive_path):
    """
    Deploy archive to web server
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        file_name = archive_path.split("/")[-1]
        rmv_ext = file_name.split(".")[0]
        path_rmv_ext = "/data/web_static/releases/{}/".format(rmv_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_rmv_ext))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path_rmv_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_rmv_ext, path_rmv_ext))
        run("rm -rf {}web_static".format(path_rmv_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_rmv_ext, symlink))
        return True
    except:
        return False
