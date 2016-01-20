import dnf
import subprocess


class CacheUpdateinfoPlugin(dnf.Plugin):

    def transaction(self):
        output = subprocess.check_output(['/usr/bin/dnf', '-qC', 'updateinfo'])
        with open('/var/run/dnf-updateinfo.txt', 'w') as f:
            f.write(output)
