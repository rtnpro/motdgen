if [ "${SSH_CONNECTION}" != "" ]; then
    test -e /var/run/motd && cat /var/run/motd
fi
