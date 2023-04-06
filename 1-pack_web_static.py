#!/usr/bin/python3
<<<<<<< HEAD
""" setting up to generate a .tgz fiel"""
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
=======
""" python fabric script to generate a .tgz file"""


def do_pack():
    pass
>>>>>>> 23670310a5f51324f483d669bef0f1f6fa3bb7f2
