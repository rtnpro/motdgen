path=/var/run/updateinfo.txt
if [ -f "$path" ]; then
    cat $path
else
    echo "Update info not available yet! Run 'dnf updateinfo' for info."
fi
