#!/bin/bash

root_path="/var/www/nesabot"

sudo rm -rf $root_path
sudo mkdir $root_path
sudo chown -R $USER:$USER $root_path
sudo chmod 755 $root_path
sudo chmod +s $root_path
