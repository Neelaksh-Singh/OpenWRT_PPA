<p align="center">
  <img width="556" height="112" src="https://github.com/Neelaksh-Singh/OpenWRT_PPA/blob/main/src/logo.png">
</p>

#### Organisation: [Freifunk](https://github.com/freifunk)

#### Project: OpenWRT-PPA

#### Mentor: [Benjamin Henrion](https://github.com/zoobab)


## 🚩 ABSTRACT

OpenWrt is a Linux distribution for off the shelf WiFi routers. People who
want to make and distribute their personal packages, often for
development purposes, so far have the option to build the whole firmware
from zero, but very few people use the OpenWrt SDKs.

## 🌏 GOAL

The idea behind this project is to provide the user with an interface where
they can simply put in their GitHub repo URL, which can be then compiled
and built onto an executable Docker container fit for Launch in k3d cluster,
and also available locally.

<p align="center">
  <img width="500" height="300" src="https://github.com/Neelaksh-Singh/OpenWRT_PPA/blob/main/src/owrt.png">
</p>

## 💻 Installation

`!!! A running Docker daemon is a must. !!!` <br>

<b>Port 5000 and 8085 must be reserverd</b> <br>

Python 3.6+ is required to run code from this repo. 

```console
$ git clone https://github.com/Neelaksh-Singh/OpenWRT_PPA.git
$ chmod +x setup.sh
$ ./setup.sh
```
Now once the setup is done do the following 

```console
$ cd web/
$ flask run
```
After this step Your Flask app will be running at **localhost:5000** and would look like this 

## 🚀 FUTURE PLANS

1. Improve Web-portal with added UI/UX.
2. Finding more ways to host packages.
3. Improving the build process by running it in Kubernetes Cluster.
4. Possibly include a CI/CD pipeline.
