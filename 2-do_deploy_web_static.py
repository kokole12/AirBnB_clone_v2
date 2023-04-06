#!/usr/bin/python3
""" python fabric script to deploy the .tgz file from 1-pack_web_static"""
from fabric.api import *
from datetime import datetime
import os.path


env.host = ['52.91.124.43', '54.237.52.91']
env.user = 'ubuntu'
env.key_file = '~/.ssh/id_rsa'


def do_deploy(archive_path):
	""" This is afunction to deploy the .tgz file"""
	if (os.path.isfile(archive_path) is False):
		return False
	try:
		path = archive_path.split('/')[-1]
		folder = ("/data/web_static/releases/" + path.split('.')[0])

		""" upload file to /tmp/
		"""
		put(archive_path,'/tmp/')

		""" execute commands"""
		run("sudo mkdir -p {}".format(folder))
		run("sudo tar -xzf /tmp/{} -C {}".format(path, folder))

		""" delete archieve"""
		run("sudo rm /tmp/{}".formst(path))
		""" moving files to host web_static"""
		run("sudo mv {}/web_static/* {}/".format(folder, folder))

		""" remove other web_statuc dir"""
		run("sudo rm -rf {}/web_static".format(folder))

		""" deleting the symbolic link created before"""
		run('sudo rm -rf /data/web_static/current')

		"""creating the new symbolic link"""
		run("sudo ln -s {} /data/web_static/current".format(folder))

		return True

	except Exception as e:
		return False
