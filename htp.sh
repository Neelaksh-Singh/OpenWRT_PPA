#!/bin/bash

rm -rf /root/bin/*

docker cp otest:/home/build/openwrt/bin /root/bin/

docker run -d --name ftptest -p 20-21:20-21 -p 65500-65515:65500-65515 -v /root/bin/:/var/ftp:ro neelaksh1/custom-ftp:v1
