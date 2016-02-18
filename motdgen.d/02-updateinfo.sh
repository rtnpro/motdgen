path=/var/run/updateinfo.txt
if [ -f "$path" ]; then
    cat $path
else
    echo "Update info not available!"
fi
