path=/var/run/motdgen/updateinfo.txt
firstrun=/var/run/motdgen/motd-updateinfo.run

if [ ! -f "$firstrun" ]; then
    touch $firstrun
    nohup /usr/bin/motdgen-cache-updateinfo </dev/null >/dev/null 2>&1 &
fi

if [ -f "$path" ]; then
    cat $path
else
    echo "Update info not available yet!"
fi
