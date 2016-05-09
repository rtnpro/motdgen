if [ "${SSH_CONNECTION}" != "" ]; then
    test -e /var/run/motdgen/motd && cat /var/run/motdgen/motd
fi
