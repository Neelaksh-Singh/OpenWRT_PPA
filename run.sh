#!/bin/bash

cd $(dirname $0)

repo_link="$1"
folder_name="$2"
deploy_name="$3"

git clone "${repo_link}" "${deploy__name}"/

#docker push "${image_name}":"${version}" registry.localhost:5000/registry.localhost

docker run -d  --name "${deploy__name}" -v "${PWD}"/"${deploy__name}":/home/build/openwrt/remote neelaksh1/custom-owrtppa:v2

#docker run -it --name testppa -v "${PWD}"/temp:/home/build/openwrt/remote neelaksh1/custom-owrtppa:v2


./htp.sh "${deploy_name}"


