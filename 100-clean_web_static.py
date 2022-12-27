#!/usr/bin/python3
""" distributes an archive to 2 web servers """
from fabric.api import *
import os


env.hosts = ['18.234.106.217', '100.25.30.148']


def do_clean(number=0):
    """
        Deletes out of date archives
            
    """
    if int(number) == 0:
        number = 1
    else:
        int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for num in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for num in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
