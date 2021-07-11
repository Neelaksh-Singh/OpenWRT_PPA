#!/bin/bash

repo_link="$1"
folder_name="$2"

git clone "${repo_link}" "${folder_name}"/

#docker push "${image_name}":"${version}" registry.localhost:5000/registry.localhost

docker run  --name qwe -v "${PWD}"/"${folder_name}"/:/home/build/openwrt/remote neelaksh1/custom-owrtppa:v1

#./htp.sh


