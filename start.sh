#!/bin/bash

# Check if an instance is already running
if [[ -n "$(docker ps | grep 'local/nesabot')" ]]; then
    echo "Instance already running ..."
    exit 1
fi

if [[ "$(uname)" == "Darwin" ]]; then
    echo "Starting on local test machine ..."
    docker run -v "/mnt/hgfs$(pwd)/src":/nesabot/src local/nesabot
else
    echo "Starting on remote linux server ..."
    docker run -v "/var/www/nesabot/src":/nesabot/src local/nesabot
fi
