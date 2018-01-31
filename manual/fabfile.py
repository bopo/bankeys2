# -*- coding: utf-8 -*-

import os
import re
import datetime

# import django
# from django.core.exceptions import AppRegistryNotReady
from fabric.api import local, env, lcd, put, run, cd, task
from fabric.contrib import project
# from fabvenv import virtualenv

HERE = os.path.abspath(os.path.dirname(__file__))
env.hosts = ['root@10.7.7.22']
env.port = '22'
env.local_dir = './_book/'
env.remote_dir = '/home/apps/manual/'


@task
def clean(migrate=None):
    local('find . -name "*.pyc" | xargs rm -rf')
    local('find . -name "*.bak" | xargs rm -rf')
    local('find . -name "*.log" | xargs rm -rf')
    local('rm -rf _book')


@task
def gen():
    s = open('SUMMARY.md').read()
    m = re.findall(r'\((.*?)\)', s, re.M)

    for x in m:
        if '/' in x[-1]:
            print(x)
            if not os.path.isdir(x):
                os.mkdir(x)
        else:
            if not os.path.exists(x):
                print '[+] %s' % x
                open(x, 'w').write('#' + x)


@task
def setup():
    local('gitbook install')


@task
def run():
    local('gitbook serve')


@task
def build():
    local('gitbook build .')


@task
def sync():
    build()

    project.rsync_project(
        remote_dir=env.remote_dir,
        local_dir=env.local_dir,
        delete=True)
