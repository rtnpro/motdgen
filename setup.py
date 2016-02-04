#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='motdgen',
    version='0.1',
    description='A utility to generate dynamic Message Of The Day.',
    author='Ratnadeep Debnath',
    author_email='rtnpro@gmail.com',
    url='https://github.com/rtnpro/fedora-motd',
    license="GPLv2",
    entry_points={
        'console_scripts': ['motdgen=motdgen:cli'],
    },
    scripts=["motdgen-cache-dnfupdateinfo"],
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('/etc/profile.d', ['motdgen.sh']),
        ('/etc/pam.d', ['pam.d/motdgen']),
        ('/usr/lib/python2.7/site-packages/dnf-plugins',
         ['dnf/plugins/cache_updateinfo.py'])
    ]
)
