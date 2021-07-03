import os
import subprocess

# CMD for getting all the running docker containers
dc = " docker ps -a --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}' "

def container():
    return subprocess.getoutput(dc)

def myfiles():
    return subprocess.getoutput("../my-test/x")
