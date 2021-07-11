import os
import subprocess

# CMD for getting all the running docker containers
dc = " docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}' "

# list containing all the url
url_list = []

def url_present(url, image):
    subprocess.getoutput("../run.sh " + str(url) + " " + str(image) )

def container():
    return subprocess.getoutput(dc)

def myfiles():
    return subprocess.getoutput("../my-test/x")
