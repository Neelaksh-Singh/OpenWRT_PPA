#!/bin/bash


cd $(dirname $0)

repo_link="$1"
deploy_name="$2"

git clone "${repo_link}" /tmp/ppa-dump/"$2"/



#docker push "${image_name}":"${version}" registry.localhost:5000/registry.localhost

docker run -dit  --name "$2" -v /tmp/ppa-dump/"$2":/home/build/openwrt/remote neelaksh1/custom-owrtppa:v3

#docker run -it --name testppa -v "${PWD}"/temp:/home/build/openwrt/remote neelaksh1/custom-owrtppa:v2
sleep 10
./build.sh "$2"

./htp.sh "$2"


