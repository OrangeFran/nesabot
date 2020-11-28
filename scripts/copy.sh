#!/bin/bash

root_path="/var/www/nesabot"

echo -n "Using the root_path $root_path, continue? (y/n) " && read REPLY
if [[ "$REPLY" =~ (y|Y|yes|Yes) ]]; then
    ssh server "bash -s" < "$(pwd)/scripts/set_permissions.sh"
    scp -r "$(pwd)/src" server:$root_path/src
    scp -r "$(pwd)/scripts" server:$root_path/scripts
    scp "$(pwd)/dockerfile" server:$root_path/dockerfile
    scp "$(pwd)/requirements.txt" server:$root_path/requirements.txt
    scp "$(pwd)/nesabot.service" server:$root_path/nesabot.service
    ssh server "$root_path/scripts/install.sh"
else
    echo "Aborting ..."
    exit 1
fi
