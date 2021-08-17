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
$ cd OpenWRT_PPA/
$ chmod +x setup.sh
$ ./setup.sh
```
Now once the setup is done do the following 

```console
$ cd web/
$ export FLASK_ENV=development
$ flask run
```
After this step Your Flask app will be running at **localhost:5000** and would look like this:-

![image](https://user-images.githubusercontent.com/56018436/129763880-3df70308-dd8d-43a9-8ec3-e1b5342df815.png)

Now you are good to go, just provide your repo-link and let the machine build it in the background.

After the build is completed, you will be able to view your built packages on **localhost:8085**.

These packages are stored inside `/tmp/ppa-data/` with the name you had provided your ***deployment***.


## ✍️ Blog

During the cource of this program Freifunk asked the students to write their journey in the form of blog.

These were:

1. [Blog 1](https://blog.freifunk.net/2021/06/05/openwrt-ppa-google-summer-of-code-2021/)
2. [Blog 2](https://blog.freifunk.net/2021/07/11/gsoc-2021-openwrt-ppa-update-for-first-evaluation/)



## 🚀 FUTURE PLANS

1. Improve Web-portal with added UI/UX.
2. Finding more ways to host packages.
3. Improving the build process by running it in Kubernetes Cluster.
4. Having provision for multiple-builds.
5. Possibly include a CI/CD pipeline.

## 📚 Reference and Resources
1. [OpenWRT SDK](https://openwrt.org/docs/guide-developer/using_the_sdk)
2. [Build System](https://openwrt.org/docs/guide-developer/build-system/use-buildsystem)
3. [Multiprocessing in Python-Flask](https://docs.python.org/3/library/multiprocessing.html)
4. [Popen in Subprocess](https://docs.python.org/3/library/subprocess.html?highlight=popen#subprocess.Popen)
5. [Docker Image](https://hub.docker.com/search?q=neelaksh1&type=image)
