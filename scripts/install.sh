#!/bin/bash

root_path="/var/www/nesabot"
creds_file="$root_path/src/creds.py"

get() {
    echo -n "$1: "
    read $1
}

remote_work() {
    cd $root_path
    # Create the creds file (if needed)
    if [ -f "$creds_file" ]; then
        echo "Credentials found, continuing ..."
    else
        get username
        get password
        get bot_token
        get chat_id

        touch $creds_file

        echo "UNAME = \"$username\"" >> $creds_file
        echo "PASSWD = \"$password\"" >> $creds_file
        echo "TOKEN = \"$bot_token\"" >> $creds_file
        echo "MY_CHAT_ID = $chat_id" >> $creds_file
    fi

    echo "Building docker file with name 'local/nesabot' ..."
    scripts/build.sh

    echo "Starting systemctl service 'nesabot' ..."
    sudo cp "nesabot.service" /etc/systemd/system
    sudo systemctl daemon-reload
    sudo systemctl start nesabot.service
}

remote_work
