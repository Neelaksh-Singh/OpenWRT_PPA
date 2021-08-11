import os
import subprocess

# CMD for getting all the running docker containers
dc = " docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}' "

def url_present(url, deploy_name):
    subprocess.getoutput("./run.sh " + str(url) + "  " + str(deploy_name) )

def container():
    return subprocess.getoutput(dc)

#def myfiles():
#    return subprocess.getoutput("../my-test/x")
