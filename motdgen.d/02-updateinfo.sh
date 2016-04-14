path=/var/run/updateinfo.txt
firstrun=/var/run/motd-updateinfo.run

if [ ! -f "$firstrun" ]; then
    touch $firstrun
    nohup /usr/bin/motdgen-cache-updateinfo &
fi

if [ -f "$path" ]; then
    cat $path
else
    echo "Update info not available yet! Run 'dnf updateinfo' for info."
fi
