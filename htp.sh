#!/bin/bash

cd $(dirname $0)

deploy_name="$1"

#rm -rf /root/bin/*

docker cp "${deploy_name}":/home/build/openwrt/bin /tmp/ppa-data/

#docker run -d --name ftptest -p 20-21:20-21 -p 65500-65515:65500-65515 -v /root/bin/:/var/ftp:ro neelaksh1/custom-ftp:v1

#docker cp serene_napier:/home/build/openwrt/bin remote/

