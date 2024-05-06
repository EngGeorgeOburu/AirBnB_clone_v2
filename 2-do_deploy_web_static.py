#!/usr/bin/env bash
# -*- coding: utf-8 -*-
"""
Created on Mon March 06 13:30:45 2024
Author: George Oburu
"""

from fabric.api import local, env
from datetime import datetime

env.user  = 'ubuntu'
env.hosts = ['54.196.27.62', '100.25.47.209']

def d0_pack():
    """
    Targing proj directory as a.tgz file
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local = ('sudo mkdir -p ./versions')
    path = ('./versions/web_static_{}'.format(now))
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)

    if name:
        return name
    else:
        return None


