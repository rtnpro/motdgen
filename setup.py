#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='motdgen',
    version='0.1.2',
    description='A utility to generate dynamic Message Of The Day.',
    author='Ratnadeep Debnath',
    author_email='rtnpro@gmail.com',
    url='https://github.com/rtnpro/motdgen',
    license="GPLv2",
    scripts=["motdgen", "motdgen-cache-updateinfo"],
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('/etc/profile.d', ['motdgen.sh']),
        ('/etc/pam.d', ['pam.d/motdgen']),
        ('/usr/lib/python2.7/site-packages/dnf-plugins',
         ['dnf/plugins/cache_updateinfo.py']),
        ('/etc/motdgen.d', [
            'motdgen.d/01-uptime.sh',
            'motdgen.d/02-updateinfo.sh']),
        ('/etc/cron.daily', ['motdgen-cache-updateinfo']),
        ('/etc/systemd/system', ['motdgen.service']),
        ('/var/run', ['motd'])
    ]
)
