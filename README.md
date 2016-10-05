# motdgen

Generate dynamic MOTD: Message of the day

## Setup

```
sudo python setup.py install
sudo echo "session    include      motdgen" >> /etc/pam.d/sshd
sudo motdgen-cache-dnfupdateinfo
```

or, just

``[sudo] dnf install fedora-motd``

## Usage

On ssh login to the machine, you should see something like:

```
Last login: Thu Feb  4 22:39:21 2016 from 127.0.0.1
 22:39:58 up 17 days, 13:52,  6 users,  load average: 0.88, 0.68, 0.46
Updates Information Summary: available
    34 Security notice(s)
    66 Bugfix notice(s)
    26 Enhancement notice(s)
     1 other notice(s)
```

## Tests

- Install tunir as mentioned at https://tunir.readthedocs.io/en/latest/installation.html
- Download fedora atomic image as ``fedora-atomic.qcow2`` in the current directory
- Run the tests: ``sudo tunir --job tunirtests/tunir``
