#!/bin/bash

root_path="/var/www/nesabot"

scp -r . server:$root_path
