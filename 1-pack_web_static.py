#!/usr/bin/python3
""" setting up to generate a .tgz fiel"""
from fabric.api import local
from time import strftime
import time


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    try:
	local('mkdir -p versions')
	local('tar -cvzf versions/web_static_{}.tgz web_static/'.format(
	      time.strftime("%Y%m%d%H%M%S")))
	return ('versions/web_static_{}.tgz'.format(time.strftime('%Y%m%d%H%M%S')))
    except:
	return None
