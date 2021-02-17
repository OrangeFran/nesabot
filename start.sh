#!/bin/bash

# Check if an instance is already running
if [[ -n "$(docker ps | grep 'local/nesabot')" ]]; then
    echo "Instance already running, kill manually."
    exit 1
fi

if [[ "$(uname)" == "Darwin" ]]; then
    # Volume mounts because this is my developer machine
    # and with this I don't have to rebuild the image every time
    echo "Starting on local test machine ..."
    docker run -v "$(pwd)/src":/nesabot/src nesabot
else
    echo "Starting on remote linux server ..."
    docker run nesabot
fi
