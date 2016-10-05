import unittest
import subprocess
import sys
from threading import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x

ON_POSIX = 'posix' in sys.builtin_module_names


class TestFedoraMotdSSHLoginMessage(unittest.TestCase):

    def test_ssh_login_message(self):

        def enqueue_output(out, queue):
            for line in iter(out.readline, ''):
                queue.put(line)
            out.close()

        cmd = (
            'ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null '
            'fedora@localhost')
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                             stdin=None, close_fds=ON_POSIX)
        q = Queue()
        t = Thread(target=enqueue_output, args=(p.stdout, q))
        t.daemon = True
        t.start()

        output = []
        while len(output) < 2:
            try:
                line = q.get_nowait()
            except Empty:
                pass
            else:
                output.append(line.strip())
                print output

        p.kill()

        self.assertTrue('load average' in output[0].lower())
        self.assertTrue(
            'update' in output[1].lower() and 'available' in output[1].lower())
