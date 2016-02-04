# Fedora MOTD

Generate dynamic MOTD: Message of the day, for Fedora

## Setup

```
sudo python setup.py install
sudo echo "session    include      motdgen" >> /etc/pam.d/sshd
sudo motdgen-cache-dnfupdateinfo
```

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

