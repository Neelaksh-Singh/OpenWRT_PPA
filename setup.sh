#!/bin/bash 

pip3 install -r requirement.txt
chmod +x web/htp.sh web/run.sh web/build.sh

# kubectl configuration
#1 download
#curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

#2 checksum file for validation
#curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

# 3 validating kubectl
#echo "$(<kubectl.sha256) kubectl" | sha256sum --check

# install kubectl
#sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Install Docker-Compose

#sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

#sudo chmod +x /usr/local/bin/docker-compose

##############################################################################



# installation of k3d

#curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash

#sudo chmod +x /usr/local/bin/k3d


# configuration of k3d

#k3d cluster create  {{ users_cluster_name }}

# Listing clusters
#kubectl config get-clusters 

# current context
#kubectl config current-context


#deleting cluster

#k3d cluster delete {{ usercluster }}

#Stting up local repository

# A) Creating local repo

#sudo docker volume create local_registry
#sudo docker container run -d --name registry.localhost -v local_registry:/var/lib/registry --restart always -p 5000:5000 registry:2

# B) Copying registries.yaml to /home/${USER}/.k3d

#cp registries.yaml /home/${USER}/.k3d/

# C) Creating our very own cluster 

#k3d cluster create --agents 1 --k3s-server-arg --disable=traefik --volume $HOME/.k3d/registries.yaml:/etc/rancher/k3s/registries.yaml

# D) Setting context for our cluster

#kubectl config use-context k3d-k3s-default

# E) Putting registry inside same network as k3d

#docker network connect k3d-k3s-default registry.localhost

#echo "127.0.0.1 registry.localhost" >> /etc/hosts 

#------------------------------------------------------------------------------------------------

# creating dump data folder
mkdir -p /tmp/ppa-data
mkdir -p /tmp/ppa-dump
chmod o+x /tmp/ppa-data 
export FLASK_ENV=development

docker pull neelaksh1/custom-owrtppa:v3

docker run -d --name ppa-server -v /tmp/ppa-data:/usr/local/apache2/htdocs -p 8085:80 neelaksh1/ppa-httpd:v1
#--------------------------------------------------------------------------------
#setting flask environment
#export FLASK_ENV=development


