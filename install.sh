#!/bin/bash

root_path="/var/www"
creds_file="$root_path/nesabot/src/creds.py"

echo -n "Using the root_path $root_path, continue? (y/n) "
read REPLY
if [ $REPLY != [Yy] ]; then
    echo "Aborting ..."
    exit 1
fi

get() {
    echo -n "$1: "
    read $1
}

sudo cp -r . $root_path

# Create the creds file and the cache dir
get username
get password
get bot_token
get chat_id

touch $creds_file
echo "UNAME = \"$username\"" >> $creds_file
echo "PASSWD = \"$password\"" >> $creds_file
echo "TOKEN = \"$bot_token\"" >> $creds_file
echo "MY_CHAT_ID = $chat_id" >> $creds_file 

sudo chown -R web:www-data $root_path/nesabot
sudo cp $root_path/nesabot/nesabot.service /etc/systemd/system

docker build -t local/nesabot -f $root_path/dockerfile $root_path

sudo systemctl daemon-reload
sudo systemctl start nesabot.service
