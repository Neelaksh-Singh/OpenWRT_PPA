#!/usr/bin/bash

repo_link="$1"
image_name="$2"
version="$3"

docker build --rm -t "${image_name}":"${version}" .

docker push "${image_name}":"${version}" registry.localhost:5000/registry.localhost