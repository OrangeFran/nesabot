#!/bin/bash

root_path="/var/www/nesabot"

echo -n "Using the root_path $root_path, continue? (y/n) "
read REPLY
if [ "$REPLY" =~ "(y|Y|yes|Yes)" ]; then
    sudo rm -rf $root_path 
    scp -r . server:$root_path
    ssh server "$root_path/scripts/install.sh"
else
    echo "Aborting ..."
    exit 1
fi
