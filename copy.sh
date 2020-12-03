#!/bin/bash

ssh_server="linode"
root_path="/var/www/nesabot"

echo -n "Using the root_path $root_path, continue? (y/n) " && read REPLY
if [[ "$REPLY" =~ (y|Y|yes|Yes) ]]; then
    ssh $ssh_server "bash -s" < "$(pwd)/scripts/check_and_stop.sh"
    ssh $ssh_server "bash -s" < "$(pwd)/scripts/set_permissions.sh"

    scp -r "$(pwd)/src" $ssh_server:$root_path/src
    scp -r "$(pwd)/scripts" $ssh_server:$root_path/scripts
    scp -r "$(pwd)/start.sh" $ssh_server:$root_path/start.sh
    scp "$(pwd)/dockerfile" $ssh_server:$root_path/dockerfile
    scp "$(pwd)/requirements.txt" $ssh_server:$root_path/requirements.txt
    scp "$(pwd)/nesabot.service" $ssh_server:$root_path/nesabot.service

    ssh $ssh_server "$root_path/scripts/install.sh"
else
    echo "Aborting ..."
    exit 1
fi
