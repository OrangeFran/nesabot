#!/bin/bash

if [ "$1" =~ "(l|local)" ]; then
    echo "Starting on local test machine ..."
    docker run -v "/mnt/hgfs$(pwd)/src":/nesabot/src local/nesabot
else
    echo "Starting on remote linux server ..."
    docer run -v "/var/www/nesabot/src":/nesabot/src local/nesabot
fi
