#!/bin/bash

docker build -t local/nesabot -f "$(pwd)/dockerfile" "$(pwd)" 
