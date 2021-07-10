import os
import subprocess

# CMD for getting all the running docker containers
dc = " docker ps -a --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}' "

# list containing all the url
url_list = []

def url_present(url):
    subprocess.getoutput("../my-test/present.sh")

def container():
    return subprocess.getoutput(dc)

def myfiles():
    return subprocess.getoutput("../my-test/x")
