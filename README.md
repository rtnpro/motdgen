# Fedora MOTD

Generate dynamic MOTD: Message of the day, for Fedora

## Usage

- ``sudo cp dnf/plugins/cache_updateinfo.py /usr/lib/python2.7/site-packages/dnf-plugins/``
- Run a dnf transaction: ``install``, ``update``, ``remove`` to trigger creating a cache of updateinfo
- `` python motdgen.py -s motdgen.d/``

