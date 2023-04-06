#!/usr/bin/python3
""" setting up to generate a .tgz fiel"""
from fabric.api import local
from time import strftime


def do_pack():
    """setting up the local directory """
    try:
        local('mkdir -p versions')
        date = strftime("%Y%m%d%H%M%S")
        """ creating the file"""
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
        return ('versions/web_static_{}.tgz'.format(date))
    except Exception as e:
        return None
