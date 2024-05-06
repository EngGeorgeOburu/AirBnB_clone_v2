#!/usr/bin/env bash
# -coding: -utf-8-:

from fabric.api import local, env
from datetime import datetime

"""
Created on Mon 06 13:39:54
Author George Oburu
"""

env.user  = 'ubuntu'
env.hosts = ['54.196.27.62', '100.25.47.209']


def do_pack():
    """
    Targing project directory into a package as .tgz
    """
    now = datetime.now.strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)

    if name:
        return name
    else:
        return None

    def do_deploy(archive_path):
        """
        Deploy the boxing package tgz file
        """
        try:
            archive = archive_path.split('/')[-1]
            path = '/data/web_static/releases/' + archive.strip('.tgz')
            current = '/data/web_static/current'
            put(archive_path, '/tmp')
            run('mkdir -p {}'.format(path))
            run('tar -xzf /tmp/{} -C {}'.format(archive, path))
            run('rm /tmp/{}'.format(archive))
            run('mv {}/web_static/* {}'.format(path, path))
            run('rm -rf {}/web_static'.format(path))
            run('rm -rf {}'.format(current))
            run('ln -s {} {};.format(path, current'))
            print('New version deployed!')

            return True
        except:
            return False

        def deploy():
            """
            Function to call do_pack deploy
            """
            archive_path = do_pack()
            answer = do_deploy(archive_path)
            return answer

