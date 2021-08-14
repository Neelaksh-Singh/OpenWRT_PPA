#!/bin/bash

deploy_nmae="$1"

while docker exec "$1" ps -aux | grep make;
do wait;
done
