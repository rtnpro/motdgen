import subprocess


class BaseMotdPlugin(object):
    CMD = None

    @property
    def message(self):
        output = self.run_cmd()
        return self.format(output)

    def run_cmd(self):
        ret = subprocess.Popen(
            self.CMD, shell=True, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        out, err = ret.communicate()
        return out

    def format(self, message):
        raise NotImplementedError


class UpdateInfoPlugin(BaseMotdPlugin):

    CMD = 'dnf updateinfo -q'

    def format(self, msg):
        msg = msg.decode()
        lines = msg.strip().splitlines()
        formatted_msg = "No update available"
        if lines:
            formatted_msg = (
                "Updates available: {}".format(
                    ", ".join([_.strip() for _ in lines[1:]]))
            )
        return formatted_msg


class LoggedinUsersPlugin(BaseMotdPlugin):

    CMD = 'users'

    def format(self, msg):
        msg = msg.decode().strip()
        return "Logged in users: {}".format(
            ', '.join(set(msg.split())))


def run():
    plugins = [_() for _ in [UpdateInfoPlugin, LoggedinUsersPlugin]]

    for plugin in plugins:
        print(plugin.message)


if __name__ == '__main__':
    run()
