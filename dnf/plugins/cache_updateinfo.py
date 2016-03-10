import dnf
import os


class CacheUpdateinfoPlugin(dnf.Plugin):

    def transaction(self):
        os.spawnl(os.P_NOWAIT,
                  'motdgen-cache-updateinfo',
                  'motdgen-cache-updateinfo')
