#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on March 5 22:11:43 2024
@author: George Oburu
"""
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.196.27.62', '100.25.47.209']


def do_pack():
    """
    Targging project directoy into a package as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_sstatic'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
