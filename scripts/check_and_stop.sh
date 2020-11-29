#!/bin/bash

id="$(docker ps | grep 'local/nesabot' | awk '{ print $1 }')"
if [[ -n "$id" ]]; then
    echo "One instance already running, stopping ..."
    docker stop $id > /dev/null
fi
