#!/bin/bash

docker build -v "$(pwd)/src":/nesabot/src local/nesabot
